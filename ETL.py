import pandas as pd
import numpy as np
import os

#Read the Airbnb dataset
try:
    Airbnb_df = pd.read_excel(os.path.join("Datasource", "airbnb.xlsx"))
    print(f"{'='*5} Retrieve original dataset successfully {'='*5}")
except Exception as e:
    print(f"Error reading dataset: {str(e)}")
    print(f"Please check if the 'Datasource' directory exists and you have read permissions.")
    exit(1)

# Display the shape of the dataset
print(f"Dataset Overview: {Airbnb_df.shape[0]:,} x {Airbnb_df.shape[1]}")

# Print all column names
print("\nAll Column Names:")
for i, col in enumerate(Airbnb_df.columns, 1):
    print(f"{i:2d}. {col}")

Airbnb_df = Airbnb_df.sort_values(by='Host Id', ascending=True)

print(f"Reviews per Price: {Airbnb_df['Price'].describe()}")
print(Airbnb_df.head(10))

##Clean Dataset
print(f"{'='*5} Clean Dataset {'='*5}")

# Remove leading and trailing spaces from column names
for col in Airbnb_df.columns:
    clean_col = col.strip()
    if col != clean_col:
        Airbnb_df.rename(columns={col: clean_col}, inplace=True)

#Remove duplicate rows based on 'Host Id' and 'Host Since'
Airbnb_df = Airbnb_df.drop_duplicates(subset=['Host Id', 'Host Since'])

# Reset "Host Since" column to datetime format and convert to date only
Airbnb_df["Host Since"] = pd.to_datetime(Airbnb_df["Host Since"], format= "%d/%m/%Y").dt.date

#Delete "Review Scores Rating (bin)" column
Airbnb_df = Airbnb_df.drop(columns=['Review Scores Rating (bin)'])

#Ensure numeric columns are in the correct format
Airbnb_df['Price'] = pd.to_numeric(Airbnb_df['Price'], errors='coerce')
Airbnb_df['Number of Records'] = pd.to_numeric(Airbnb_df['Number of Records'], errors='coerce')
Airbnb_df['Number Of Reviews'] = pd.to_numeric(Airbnb_df['Number Of Reviews'], errors='coerce')
Airbnb_df['Review Scores Rating'] = pd.to_numeric(Airbnb_df['Review Scores Rating'], errors='coerce')

# Fill empty/NaN values with consistent value for specific columns
# More sophisticated approach "def hierarchical_price_imputation"
Airbnb_df['Price'] = Airbnb_df['Price'].fillna(Airbnb_df.groupby('Zipcode')['Price'].transform('median'))
Airbnb_df['Price'] = Airbnb_df['Price'].fillna(Airbnb_df.groupby('Neighbourhood')['Price'].transform('median'))
Airbnb_df = Airbnb_df.dropna(subset=['Price'])

#Check rating values between 0 and 100
# Option 1: Clip outliers (keeps all rows, fixes bad values)
# Airbnb_df['Review Scores Rating'] = Airbnb_df['Review Scores Rating'].clip(lower=0, upper=100)

# Option 2: Remove outliers (removes rows with bad values) - REDUNDANT with clip
Airbnb_df = Airbnb_df[(Airbnb_df['Review Scores Rating'] >= 1) & (Airbnb_df['Review Scores Rating'] <= 100)]

# Remove rows with no records
Airbnb_df = Airbnb_df[(Airbnb_df['Number of Records'] >= 1)]

# Cleaning the dataset
Airbnb_df = Airbnb_df.dropna(
    subset=['Host Id', 'Review Scores Rating', 'Zipcode', 'Neighbourhood'])

#Catelog Neighbourhood, Room type, Beds and Property Type
Airbnb_df['Neighbourhood'] = Airbnb_df['Neighbourhood'].astype('category')
Airbnb_df['Room Type'] = Airbnb_df['Room Type'].astype('category')
Airbnb_df['Beds'] = Airbnb_df['Beds'].astype('category')
Airbnb_df['Property Type'] = Airbnb_df['Property Type'].astype('category')

## Reorder columns for better readability
Airbnb_df = Airbnb_df[['Host Id', 'Host Since', 'Neighbourhood', 'Zipcode', 'Property Type', 'Room Type', 'Beds', 'Price', 'Number of Records', 'Number Of Reviews', 'Review Scores Rating']]

print(f"\n {"=" *5} Result after clean data {"=" *5}")
print(f"Cleaned dataset shape: {Airbnb_df.shape[0]:,} rows × {Airbnb_df.shape[1]} columns")
print(f"Data shape after cleaning: {Airbnb_df.shape}")
print(f"Missing values: {Airbnb_df.isnull().sum().sum()}")
print(Airbnb_df.head(10))
print(f"Empty prices after imputation: {Airbnb_df['Price'].isnull().sum()}")

# Save the cleaned dataset with error handling
try:
    output_path = os.path.join("Datasource", "airbnb_clean.csv")
    Airbnb_df.to_csv(output_path, index=False)
    print(f"✅ Dataset saved successfully to: {output_path}")
    print(f"📊 Cleaned dataset: {Airbnb_df.shape[0]:,} rows × {Airbnb_df.shape[1]} columns")
except Exception as e:
    print(f"❌ Error saving dataset: {str(e)}")
    print(f"⚠️  Please check if the 'Datasource' directory exists and you have write permissions.")

#region advanced price imputation
# Hierarchical price imputation using median values

# def hierarchical_price_imputation(df):
#     """
#     Fill missing prices using hierarchical median imputation:
#     1. Zipcode -> 2. Neighbourhood -> 3. Room Type -> 4. Property Type -> 5. Overall median
#     """
#     df_copy = df.copy()
#     empty_price_mask = df_copy['Price'].isnull()
    
#     for idx in df_copy[empty_price_mask].index:
#         if pd.isnull(df_copy.loc[idx, 'Price']):
#             zipcode = df_copy.loc[idx, 'Zipcode']
#             neighbourhood = df_copy.loc[idx, 'Neighbourhood']
#             room_type = df_copy.loc[idx, 'Room Type']
#             property_type = df_copy.loc[idx, 'Property Type']
            
#             # Strategy 1: Try Zipcode median
#             if pd.notna(zipcode):
#                 zipcode_median = df_copy[df_copy['Zipcode'] == zipcode]['Price'].median()
#                 if pd.notna(zipcode_median):
#                     df_copy.loc[idx, 'Price'] = zipcode_median
#                     continue
            
#             # Strategy 2: Try Neighbourhood median
#             if pd.notna(neighbourhood):
#                 neighbourhood_median = df_copy[df_copy['Neighbourhood'] == neighbourhood]['Price'].median()
#                 if pd.notna(neighbourhood_median):
#                     df_copy.loc[idx, 'Price'] = neighbourhood_median
#                     continue
            
#             # Strategy 3: Try Room Type median
#             if pd.notna(room_type):
#                 room_type_median = df_copy[df_copy['Room Type'] == room_type]['Price'].median()
#                 if pd.notna(room_type_median):
#                     df_copy.loc[idx, 'Price'] = room_type_median
#                     continue
            
#             # Strategy 4: Try Property Type median
#             if pd.notna(property_type):
#                 property_type_median = df_copy[df_copy['Property Type'] == property_type]['Price'].median()
#                 if pd.notna(property_type_median):
#                     df_copy.loc[idx, 'Price'] = property_type_median
#                     continue
            
#             # Strategy 5: Use overall median as last resort
#             overall_median = df_copy['Price'].median()
#             df_copy.loc[idx, 'Price'] = overall_median
    
#     return df_copy

# Apply hierarchical imputation
# Airbnb_df = hierarchical_price_imputation(Airbnb_df)
#endregion advanced price imputation

