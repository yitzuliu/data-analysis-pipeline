# Exploratory Data Analysis (EDA) Workflow for Airbnb Cleaned Dataset

# =============================================================================
# SECTION 1: SETUP AND DATA LOADING
# =============================================================================

# 1.1 Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set visualization style for consistency
plt.style.use('seaborn-v0_8-whitegrid')  # Modern, clean style
sns.set_palette("deep")  # Color palette suitable for business presentations

# 1.2 Load the cleaned Airbnb dataset
try:
    df = pd.read_csv('Datasource/airbnb_clean.csv')
    print('✅ Airbnb cleaned dataset loaded successfully.')
except Exception as e:
    print(f'❌ Error loading dataset: {e}')
    df = None

# =============================================================================
# SECTION 2: DATA QUALITY ASSESSMENT
# =============================================================================

# 2.1 Preview the dataset
if df is not None:
    print("\n=== DATA PREVIEW ===")
    print(df.head())           # Show the first 5 rows
    print("\n=== DATA INFORMATION ===")
    print(df.info())           # Show data types and non-null counts
    print("\n=== SUMMARY STATISTICS ===")
    print(df.describe())       # Show summary statistics
else:
    print('No data loaded to preview.')

# 2.2 Check for missing values and data types
if df is not None:
    print('\n=== DATA QUALITY CHECK ===')
    print('Missing values per column:')
    print(df.isnull().sum())
    
    # Calculate percentage of missing values
    print('\nMissing values percentage:')
    print(round(100 * df.isnull().sum() / len(df), 2))
    
    print('\nData types:')
    print(df.dtypes)
    
    # Check for duplicates
    print(f'\nNumber of duplicate rows: {df.duplicated().sum()}')
else:
    print('No data loaded to check for missing values or data types.')

# =============================================================================
# SECTION 3: BUSINESS QUESTIONS & ANALYSIS GOALS
# =============================================================================

# Define the key business questions we want to answer through this analysis:
# 1. What factors most significantly influence property prices?
# 2. Which neighborhoods offer the best value for different types of properties?
# 3. How do ratings correlate with price, location, and property characteristics?
# 4. What insights can help hosts optimize their pricing strategy?
# 5. What patterns exist in guest preferences (as reflected by review counts)?
# 6. What recommendations can we provide to new hosts entering the market?

# =============================================================================
# SECTION 4: UNIVARIATE ANALYSIS
# =============================================================================

# 4.1 Numerical Variables Distribution
# Analyze: Price, Review Scores Rating, Number Of Reviews, Number of Records, Beds
# Business Focus: Understanding pricing distribution, rating patterns, and booking frequency

# Write your code for univariate numerical analysis below:
if df is not None:
    # Set up figure size for numerical variables analysis
    plt.figure(figsize=(18, 12))
    
    # Define numerical columns to analyze
    numerical_cols = ['Price', 'Review Scores Rating', 'Number Of Reviews', 'Number of Records', 'Beds']
    
    # Loop through numerical columns and create histograms and boxplots
    for i, col in enumerate(numerical_cols):
        # Create histograms with better bin settings and KDE
        plt.subplot(3, len(numerical_cols), i+1)
        if col == 'Price':
            # Use more bins for price to show distribution details
            # sns.histplot(df[col], kde=True, bins=30, color='darkblue')
            sns.histplot(df[col].clip(upper=df[col].quantile(0.99)), kde=True, bins=30, color='darkblue')
            plt.axvline(df[col].mean(), color='red', linestyle='--', label=f'Mean: ${df[col].mean():.2f}')
            plt.axvline(df[col].median(), color='green', linestyle='-.', label=f'Median: ${df[col].median():.2f}')
        else:
            # Standard visualization for non-price numerical variables
            sns.histplot(df[col], kde=True, bins=20, color='darkblue')
            plt.axvline(df[col].mean(), color='red', linestyle='--', label=f'Mean: {df[col].mean():.2f}')
            plt.axvline(df[col].median(), color='green', linestyle='-.', label=f'Median: {df[col].median():.2f}')
 
        plt.title(f'Distribution of {col}', fontdict={'fontsize': 9, 'weight': 'bold'})
        plt.xlabel('')
        plt.ylabel('')
        plt.grid(True, alpha=0.3)
        plt.legend(fontsize='small')
        plt.tick_params(labelsize=8)
        
        # Create boxplots with enhanced styling
        plt.subplot(3, len(numerical_cols), i+len(numerical_cols)+1)
        sns.boxplot(x=df[col], color='skyblue', width=0.5)
        plt.title(f'Boxplot of {col}', fontdict={'fontsize': 9, 'weight': 'bold'})
        plt.xlabel('')
        plt.ylabel('')
        plt.grid(True, alpha=0.3)

        # Add descriptive statistics with improved formatting
        plt.subplot(3, len(numerical_cols), i+(2*len(numerical_cols))+1)
        plt.axis('off')
        
        # Format statistics
        stats = df[col].describe()
        
        # Add dollar sign for price, otherwise keep format consistent
        prefix = "$" if col == "Price" else ""
        suffix = "/100" if col == "Review Scores Rating" else ""
        
        plt.text(0.1, 0.9, f"Mean: {prefix}{stats['mean']:.2f}{suffix}")
        plt.text(0.1, 0.8, f"Median: {prefix}{stats['50%']:.2f}{suffix}")
        plt.text(0.1, 0.7, f"Std Dev: {prefix}{stats['std']:.2f}")
        plt.text(0.1, 0.6, f"Min: {prefix}{stats['min']:.2f}{suffix}")
        plt.text(0.1, 0.5, f"Max: {prefix}{stats['max']:.2f}{suffix}")
        plt.text(0.1, 0.4, f"Range: {prefix}{stats['max'] - stats['min']:.2f}")
    
    # Adjust spacing to reduce excessive margins and optimize layout
    plt.subplots_adjust(hspace=0.2,  # Vertical space between rows
                        left=0.05,   # Reduce left margin
                        right=0.95,  # Increase usable right area
                        top=0.95,    # Increase usable top area
                        bottom=0.05) # Reduce bottom margin
    
    # Add a main title with adjusted position
    plt.show()
        
    # Business insights from numerical variables
    print("\n=== NUMERICAL VARIABLES BUSINESS INSIGHTS ===")
    
    # Price insights
    avg_price = df['Price'].mean()
    median_price = df['Price'].median()
    price_range = df['Price'].max() - df['Price'].min()
    print(f"• Average listing price: ${avg_price:.2f}")
    print(f"• Median listing price: ${median_price:.2f}")
    print(f"• Price range: ${price_range:.2f}")
    
    # Reviews insights
    avg_reviews = df['Number Of Reviews'].mean()
    median_reviews = df['Number Of Reviews'].median()
    print(f"• Average number of reviews per listing: {avg_reviews:.2f}")
    print(f"• Median number of reviews per listing: {median_reviews:.2f}")
    
    # Ratings insights
    avg_rating = df['Review Scores Rating'].mean()
    print(f"• Average rating: {avg_rating:.2f}/100")
    
    # Beds insights
    avg_beds = df['Beds'].mean()
    print(f"• Average number of beds: {avg_beds:.2f}")
    most_common_beds = df['Beds'].mode()[0]
    print(f"• Most common bed configuration: {most_common_beds}")
else:
    print('No data loaded to analyze numerical variable distributions.')

# # 4.2 Categorical Variables Distribution
# # Analyze: Neighbourhood, Zipcode, Property Type, Room Type
# # Business Focus: Identifying popular areas, property types, and listing configurations

# # Write your code for categorical univariate analysis below:
# if df is not None:
#     # Set up figure size for categorical variables analysis
#     plt.figure(figsize=(20, 16))
    
#     # Define categorical columns to analyze
#     categorical_cols = ['Neighbourhood', 'Zipcode', 'Property Type', 'Room Type']
    
#     # Function to plot top N categories for a categorical variable
#     def plot_top_categories(data, column, ax, top_n=10, title=None):
#         counts = data[column].value_counts().nlargest(top_n)
#         counts.plot(kind='bar', ax=ax)
#         ax.set_title(title if title else f'Top {top_n} {column}s')
#         ax.set_ylabel('Count')
#         ax.grid(True, alpha=0.3)
#         for i, v in enumerate(counts):
#             ax.text(i, v + 0.1, str(v), ha='center')
#         return counts
    
#     # Function to calculate and display category percentages
#     def display_category_percentages(data, column, top_n=10):
#         total = len(data)
#         counts = data[column].value_counts().nlargest(top_n)
#         percentages = (counts / total * 100).round(1)
        
#         print(f"\n=== {column.upper()} DISTRIBUTION ===")
#         for cat, count in counts.items():
#             pct = percentages[cat]
#             print(f"• {cat}: {count} listings ({pct}% of market)")
        
#         # Calculate concentration
#         top_concentration = percentages.sum()
#         print(f"• Market concentration: Top {top_n} {column.lower()}s represent {top_concentration:.1f}% of all listings")
    
#     # Plot Neighbourhood distribution
#     ax1 = plt.subplot(2, 2, 1)
#     top_neighborhoods = plot_top_categories(df, 'Neighbourhood', ax1, top_n=10, 
#                                            title='Top 10 Neighbourhoods by Listing Count')
#     plt.xticks(rotation=45, ha='right')
    
#     # Plot Zipcode distribution
#     ax2 = plt.subplot(2, 2, 2)
#     top_zipcodes = plot_top_categories(df, 'Zipcode', ax2, top_n=10,
#                                       title='Top 10 Zipcodes by Listing Count')
#     plt.xticks(rotation=45)
    
#     # Plot Property Type distribution
#     ax3 = plt.subplot(2, 2, 3)
#     top_property_types = plot_top_categories(df, 'Property Type', ax3, top_n=10,
#                                             title='Top 10 Property Types')
#     plt.xticks(rotation=45, ha='right')
    
#     # Plot Room Type distribution
#     ax4 = plt.subplot(2, 2, 4)
#     room_type_counts = df['Room Type'].value_counts()
#     room_type_counts.plot(kind='bar', ax=ax4)
#     ax4.set_title('Room Type Distribution')
#     ax4.set_ylabel('Count')
#     ax4.grid(True, alpha=0.3)
#     for i, v in enumerate(room_type_counts):
#         ax4.text(i, v + 0.1, str(v), ha='center')
    
#     plt.tight_layout()
#     plt.suptitle("Categorical Variables Analysis", fontsize=16, y=1.02)
#     plt.show()
    
#     # Print business insights about categorical variables
#     print("\n=== CATEGORICAL VARIABLES BUSINESS INSIGHTS ===")
    
#     # Display category percentages
#     for col in categorical_cols:
#         top_n = 5 if col in ['Neighbourhood', 'Zipcode', 'Property Type'] else 10
#         display_category_percentages(df, col, top_n=top_n)
    
#     # Additional market insights
#     print("\n=== MARKET STRUCTURE INSIGHTS ===")
    
#     # Calculate market concentration (Herfindahl-Hirschman Index simplified)
#     total_listings = len(df)
    
#     # Neighborhood concentration
#     neighborhood_shares = df['Neighbourhood'].value_counts() / total_listings
#     top_neighborhood = df['Neighbourhood'].value_counts().index[0]
#     top_neighborhood_share = neighborhood_shares.iloc[0] * 100
#     print(f"• Most saturated neighborhood: {top_neighborhood} ({top_neighborhood_share:.1f}% of listings)")
    
#     # Property type insights
#     top_property = df['Property Type'].value_counts().index[0]
#     top_property_share = (df['Property Type'].value_counts().iloc[0] / total_listings) * 100
#     print(f"• Dominant property type: {top_property} ({top_property_share:.1f}% of market)")
    
#     # Room type insights
#     entire_home_pct = (df[df['Room Type'] == 'Entire home/apt'].shape[0] / total_listings) * 100
#     print(f"• Entire home/apt listings: {entire_home_pct:.1f}% of market")
    
#     # Host concentration (if Host Id is available)
#     if 'Host Id' in df.columns:
#         unique_hosts = df['Host Id'].nunique()
#         avg_listings_per_host = total_listings / unique_hosts
#         print(f"• Average listings per host: {avg_listings_per_host:.2f}")
        
#         # Multi-listing hosts
#         hosts_with_multiple = df['Host Id'].value_counts()[df['Host Id'].value_counts() > 1].count()
#         pct_hosts_multiple = (hosts_with_multiple / unique_hosts) * 100
#         print(f"• Hosts with multiple listings: {hosts_with_multiple} ({pct_hosts_multiple:.1f}% of all hosts)")
        
#         # Top host concentration
#         top_host_listings = df['Host Id'].value_counts().max()
#         pct_top_host = (top_host_listings / total_listings) * 100
#         print(f"• Largest host controls {top_host_listings} listings ({pct_top_host:.1f}% of market)")
# else:
#     print('No data loaded to analyze categorical variable distributions.')

# # =============================================================================
# # SECTION 5: BIVARIATE ANALYSIS
# # =============================================================================

# # 5.1 Location-based Analysis
# # Analyze: 
# # - Neighbourhood vs. listing count, price, reviews, ratings
# # - Zipcode vs. listing count, price, reviews
# # Business Focus: Identifying high-value locations and market saturation

# # Write your code for location-based analysis below:
# if df is not None:
#     # Set figure aesthetics for business presentation
#     plt.figure(figsize=(20, 24))
    
#     # 1. Neighbourhood vs. Listing Count (Top 15)
#     plt.subplot(3, 2, 1)
#     neighborhood_counts = df['Neighbourhood'].value_counts().nlargest(15)
#     sns.barplot(x=neighborhood_counts.values, y=neighborhood_counts.index)
#     plt.title('Top 15 Neighbourhoods by Listing Count')
#     plt.xlabel('Number of Listings')
#     plt.grid(True, alpha=0.3)
    
#     # 2. Neighbourhood vs. Average Price (Top 15 by count)
#     plt.subplot(3, 2, 2)
#     top_neighborhoods = df['Neighbourhood'].value_counts().nlargest(15).index
#     neighborhood_avg_price = df[df['Neighbourhood'].isin(top_neighborhoods)].groupby('Neighbourhood')['Price'].mean().sort_values(ascending=False)
#     sns.barplot(x=neighborhood_avg_price.values, y=neighborhood_avg_price.index)
#     plt.title('Average Price by Top 15 Neighbourhoods')
#     plt.xlabel('Average Price ($)')
#     plt.grid(True, alpha=0.3)
    
#     # 3. Neighbourhood vs. Average Rating (Top 15 by count)
#     plt.subplot(3, 2, 3)
#     neighborhood_avg_rating = df[df['Neighbourhood'].isin(top_neighborhoods)].groupby('Neighbourhood')['Review Scores Rating'].mean().sort_values(ascending=False)
#     sns.barplot(x=neighborhood_avg_rating.values, y=neighborhood_avg_rating.index)
#     plt.title('Average Rating by Top 15 Neighbourhoods')
#     plt.xlabel('Average Review Score Rating')
#     plt.grid(True, alpha=0.3)
    
#     # 4. Neighbourhood vs. Price (Boxplot for top 10 neighborhoods)
#     plt.subplot(3, 2, 4)
#     top10_neighborhoods = df['Neighbourhood'].value_counts().nlargest(10).index
#     sns.boxplot(x='Neighbourhood', y='Price', data=df[df['Neighbourhood'].isin(top10_neighborhoods)])
#     plt.title('Price Distribution by Top 10 Neighbourhoods')
#     plt.xlabel('Neighbourhood')
#     plt.ylabel('Price ($)')
#     plt.xticks(rotation=45)
#     plt.grid(True, alpha=0.3)
    
#     # 5. Zipcode vs. Listing Count (Top 15)
#     plt.subplot(3, 2, 5)
#     zipcode_counts = df['Zipcode'].value_counts().nlargest(15)
#     sns.barplot(x=zipcode_counts.values, y=zipcode_counts.index)
#     plt.title('Top 15 Zipcodes by Listing Count')
#     plt.xlabel('Number of Listings')
#     plt.grid(True, alpha=0.3)
    
#     # 6. Zipcode vs. Average Price (Top 15 by count)
#     plt.subplot(3, 2, 6)
#     top_zipcodes = df['Zipcode'].value_counts().nlargest(15).index
#     zipcode_avg_price = df[df['Zipcode'].isin(top_zipcodes)].groupby('Zipcode')['Price'].mean().sort_values(ascending=False)
#     sns.barplot(x=zipcode_avg_price.values, y=zipcode_avg_price.index)
#     plt.title('Average Price by Top 15 Zipcodes')
#     plt.xlabel('Average Price ($)')
#     plt.grid(True, alpha=0.3)
    
#     plt.tight_layout()
#     plt.suptitle("Location-Based Analysis", fontsize=16, y=1.02)
#     plt.show()
    
#     # Calculate and print business insights related to location
#     print("\n=== LOCATION-BASED BUSINESS INSIGHTS ===")
    
#     # 1. Identify highest value neighborhoods (price/rating ratio)
#     neighborhood_metrics = df.groupby('Neighbourhood').agg({
#         'Price': 'mean',
#         'Review Scores Rating': 'mean',
#         'Number Of Reviews': 'mean',
#         'Host Id': 'count'
#     }).rename(columns={'Host Id': 'Listing_Count'})
    
#     # Calculate value score (rating / price ratio - higher means better value)
#     neighborhood_metrics['Value_Score'] = neighborhood_metrics['Review Scores Rating'] / neighborhood_metrics['Price']
    
#     # Filter to neighborhoods with at least 5 listings
#     popular_neighborhoods = neighborhood_metrics[neighborhood_metrics['Listing_Count'] >= 5]
    
#     # Top 5 highest priced neighborhoods
#     top_price_neighborhoods = popular_neighborhoods.sort_values('Price', ascending=False).head(5)
#     print("• Top 5 Premium Neighborhoods (highest average price):")
#     for idx, row in top_price_neighborhoods.iterrows():
#         print(f"  - {idx}: ${row['Price']:.2f}, Rating: {row['Review Scores Rating']:.1f}/100, {row['Listing_Count']} listings")
    
#     # Top 5 highest rated neighborhoods
#     top_rated_neighborhoods = popular_neighborhoods.sort_values('Review Scores Rating', ascending=False).head(5)
#     print("\n• Top 5 Highest Rated Neighborhoods:")
#     for idx, row in top_rated_neighborhoods.iterrows():
#         print(f"  - {idx}: {row['Review Scores Rating']:.1f}/100, ${row['Price']:.2f}, {row['Listing_Count']} listings")
    
#     # Top 5 best value neighborhoods (high rating/price ratio)
#     top_value_neighborhoods = popular_neighborhoods.sort_values('Value_Score', ascending=False).head(5)
#     print("\n• Top 5 Best Value Neighborhoods (highest rating-to-price ratio):")
#     for idx, row in top_value_neighborhoods.iterrows():
#         print(f"  - {idx}: Rating {row['Review Scores Rating']:.1f}/100 at ${row['Price']:.2f}, {row['Listing_Count']} listings")
    
#     # Identify potential investment opportunities (high ratings but below average prices)
#     avg_price = df['Price'].mean()
#     opportunity_neighborhoods = popular_neighborhoods[(popular_neighborhoods['Review Scores Rating'] > 85) & 
#                                                     (popular_neighborhoods['Price'] < avg_price)].sort_values('Review Scores Rating', ascending=False)
    
#     if not opportunity_neighborhoods.empty:
#         print("\n• Investment Opportunity Neighborhoods (high ratings but below average prices):")
#         for idx, row in opportunity_neighborhoods.head(5).iterrows():
#             value_percent = ((avg_price - row['Price']) / avg_price) * 100
#             print(f"  - {idx}: Rating {row['Review Scores Rating']:.1f}/100, ${row['Price']:.2f} ({value_percent:.1f}% below market avg)")
    
#     # Market saturation analysis
#     total_listings = len(df)
#     neighborhood_concentration = neighborhood_metrics['Listing_Count'] / total_listings * 100
#     top_concentration = neighborhood_concentration.nlargest(5).sum()
#     print(f"\n• Market Concentration: Top 5 neighborhoods contain {top_concentration:.1f}% of all listings")
# else:
#     print('No data loaded to analyze location-based relationships.')

# # 5.2 Property Characteristics Analysis
# # Analyze:
# # - Property Type vs. Price
# # - Room Type vs. Price
# # - Beds vs. Price
# # Business Focus: Understanding pricing determinants and market segments

# # Write your code for property characteristics analysis below:
# if df is not None:
#     # Set up figure for property characteristics analysis
#     plt.figure(figsize=(20, 16))
    
#     # 1. Property Type vs. Price (Top 10 property types)
#     top_property_types = df['Property Type'].value_counts().nlargest(10).index
#     property_price_data = df[df['Property Type'].isin(top_property_types)]
    
#     plt.subplot(2, 2, 1)
#     sns.boxplot(x='Property Type', y='Price', data=property_price_data)
#     plt.title('Price Distribution by Top 10 Property Types')
#     plt.xticks(rotation=45, ha='right')
#     plt.ylabel('Price ($)')
#     plt.grid(True, alpha=0.3)
    
#     # 2. Room Type vs. Price
#     plt.subplot(2, 2, 2)
#     sns.boxplot(x='Room Type', y='Price', data=df)
#     plt.title('Price Distribution by Room Type')
#     plt.ylabel('Price ($)')
#     plt.grid(True, alpha=0.3)
    
#     # 3. Beds vs. Price (limited to common bed counts)
#     common_beds = df['Beds'].value_counts().nlargest(6).index
#     beds_price_data = df[df['Beds'].isin(common_beds)]
    
#     plt.subplot(2, 2, 3)
#     sns.boxplot(x='Beds', y='Price', data=beds_price_data)
#     plt.title('Price Distribution by Number of Beds')
#     plt.ylabel('Price ($)')
#     plt.grid(True, alpha=0.3)
    
#     # 4. Room Type vs. Average Rating
#     plt.subplot(2, 2, 4)
#     sns.barplot(x='Room Type', y='Review Scores Rating', data=df)
#     plt.title('Average Rating by Room Type')
#     plt.ylabel('Review Scores Rating')
#     plt.grid(True, alpha=0.3)
    
#     plt.tight_layout()
#     plt.suptitle("Property Characteristics Analysis", fontsize=16, y=1.02)
#     plt.show()
    
#     # Business insights for property characteristics
#     print("\n=== PROPERTY CHARACTERISTICS BUSINESS INSIGHTS ===")
    
#     # Average price by property type (top 10)
#     property_price_avg = df[df['Property Type'].isin(top_property_types)].groupby('Property Type')['Price'].agg(['mean', 'median', 'count']).sort_values('mean', ascending=False)
    
#     print("• Property Type Pricing Analysis (Top 10 Types):")
#     for idx, row in property_price_avg.head(10).iterrows():
#         print(f"  - {idx}: Avg ${row['mean']:.2f}, Median ${row['median']:.2f}, {row['count']} listings")
    
#     # Premium calculation (% above overall average)
#     overall_avg_price = df['Price'].mean()
    
#     print("\n• Premium Property Types (% above market average):")
#     for idx, row in property_price_avg[property_price_avg['mean'] > overall_avg_price].iterrows():
#         premium_pct = ((row['mean'] - overall_avg_price) / overall_avg_price) * 100
#         print(f"  - {idx}: ${row['mean']:.2f} ({premium_pct:.1f}% premium)")
    
#     # Room type pricing analysis
#     room_price_avg = df.groupby('Room Type')['Price'].agg(['mean', 'median', 'count']).sort_values('mean', ascending=False)
    
#     print("\n• Room Type Pricing Analysis:")
#     for idx, row in room_price_avg.iterrows():
#         premium_pct = ((row['mean'] - overall_avg_price) / overall_avg_price) * 100
#         print(f"  - {idx}: Avg ${row['mean']:.2f}, Median ${row['median']:.2f}, {row['count']} listings ({premium_pct:.1f}% relative to market avg)")
    
#     # Price per bed analysis (efficiency metric)
#     df['Price_per_Bed'] = df['Price'] / df['Beds'].replace(0, 1)  # Avoid division by zero
    
#     # Make sure we only analyze beds that have both price and price per bed data
#     bed_analysis = df.groupby('Beds').agg({
#         'Price': 'mean',
#         'Price_per_Bed': 'mean'
#     }).sort_values('Beds').head(8)  # Focus on common configurations
    
#     print("\n• Price Efficiency Analysis (Price per Bed):")
#     print(f"  - Overall average price per bed: ${df['Price_per_Bed'].mean():.2f}")
#     for beds, row in bed_analysis.iterrows():
#         print(f"  - {beds} bed configuration: ${row['Price_per_Bed']:.2f} per bed (total ${row['Price']:.2f})")
    
#     # Best rated property types
#     property_ratings = df.groupby('Property Type').agg({
#         'Review Scores Rating': ['mean', 'count'],
#         'Price': 'mean'
#     })
#     property_ratings.columns = ['Avg_Rating', 'Listing_Count', 'Avg_Price']
#     property_ratings = property_ratings[property_ratings['Listing_Count'] >= 5].sort_values('Avg_Rating', ascending=False)
    
#     print("\n• Highest Rated Property Types (min 5 listings):")
#     for idx, row in property_ratings.head(5).iterrows():
#         print(f"  - {idx}: Rating {row['Avg_Rating']:.1f}/100, Avg ${row['Avg_Price']:.2f}, {row['Listing_Count']} listings")
# else:
#     print('No data loaded to analyze property characteristics.')

# # =============================================================================
# # SECTION 6: ADVANCED ANALYSIS
# # =============================================================================

# # 6.1 Outlier Detection and Handling
# # Business Focus: Identifying premium or undervalued properties and market anomalies

# # Write your code for outlier analysis below:
# if df is not None:
#     # Set up figure for outlier analysis
#     plt.figure(figsize=(16, 10))
    
#     # Define numerical columns for outlier detection
#     numerical_cols = ['Price', 'Review Scores Rating', 'Number Of Reviews', 'Number of Records']
    
#     # Calculate outlier boundaries using IQR method
#     print("\n=== OUTLIER ANALYSIS ===")
#     outliers_summary = {}
    
#     for col in numerical_cols:
#         Q1 = df[col].quantile(0.25)
#         Q3 = df[col].quantile(0.75)
#         IQR = Q3 - Q1
        
#         lower_bound = Q1 - 1.5 * IQR
#         upper_bound = Q3 + 1.5 * IQR
        
#         outliers = df[(df[col] < lower_bound) | (df[col] > upper_bound)]
#         outliers_count = len(outliers)
#         outliers_pct = (outliers_count / len(df)) * 100
        
#         outliers_summary[col] = {
#             'count': outliers_count,
#             'percentage': outliers_pct,
#             'lower_bound': lower_bound,
#             'upper_bound': upper_bound
#         }
        
#         print(f"• {col}: {outliers_count} outliers ({outliers_pct:.2f}% of data)")
#         print(f"  - Lower bound: {lower_bound:.2f}")
#         print(f"  - Upper bound: {upper_bound:.2f}")
    
#     # Focus on price outliers for business insights
#     price_outliers = df[(df['Price'] > outliers_summary['Price']['upper_bound'])]
    
#     # Analyze characteristics of premium properties (price outliers)
#     if len(price_outliers) > 0:
#         print("\n=== PREMIUM PROPERTY ANALYSIS (Price Outliers) ===")
#         print(f"• Number of premium properties: {len(price_outliers)} ({(len(price_outliers)/len(df))*100:.2f}% of market)")
#         print(f"• Average price of premium properties: ${price_outliers['Price'].mean():.2f}")
#         print(f"• Average rating of premium properties: {price_outliers['Review Scores Rating'].mean():.2f}/100")
        
#         # Most common neighborhoods for premium properties
#         premium_neighborhoods = price_outliers['Neighbourhood'].value_counts().head(5)
#         print("\n• Top 5 Neighborhoods for Premium Properties:")
#         for neighborhood, count in premium_neighborhoods.items():
#             pct = (count / len(price_outliers)) * 100
#             print(f"  - {neighborhood}: {count} properties ({pct:.1f}% of premium market)")
        
#         # Most common property types for premium properties
#         premium_property_types = price_outliers['Property Type'].value_counts().head(5)
#         print("\n• Top 5 Property Types for Premium Properties:")
#         for prop_type, count in premium_property_types.items():
#             pct = (count / len(price_outliers)) * 100
#             print(f"  - {prop_type}: {count} properties ({pct:.1f}% of premium market)")
    
#     # Create visualization of price outliers by property type
#     plt.subplot(2, 2, 1)
#     sns.boxplot(x='Room Type', y='Price', data=df)
#     plt.axhline(y=outliers_summary['Price']['upper_bound'], color='r', linestyle='--', label=f"Upper Bound (${outliers_summary['Price']['upper_bound']:.2f})")
#     plt.title('Price Distribution and Outlier Boundary by Room Type')
#     plt.ylabel('Price ($)')
#     plt.legend()
#     plt.grid(True, alpha=0.3)
    
#     # Create visualization of premium properties by neighborhood (top 10)
#     if len(price_outliers) > 0:
#         plt.subplot(2, 2, 2)
#         top_premium_neighborhoods = price_outliers['Neighbourhood'].value_counts().nlargest(10)
#         sns.barplot(x=top_premium_neighborhoods.values, y=top_premium_neighborhoods.index)
#         plt.title('Top 10 Neighbourhoods for Premium Properties')
#         plt.xlabel('Number of Premium Properties')
#         plt.grid(True, alpha=0.3)
    
#     plt.tight_layout()
#     plt.show()

# # 6.2 Feature Correlations
# # Business Focus: Understanding relationships between variables to inform pricing strategy

# # Write your code for correlation analysis below:
# if df is not None:
#     # Create correlation matrix for numerical features
#     numerical_features = df.select_dtypes(include=['int64', 'float64']).columns
#     correlation_matrix = df[numerical_features].corr()
    
#     # Set up figure for correlation analysis
#     plt.figure(figsize=(12, 10))
    
#     # Create heatmap of correlations
#     sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
#     plt.title('Correlation Matrix of Numerical Features')
#     plt.xticks(rotation=45, ha='right')
#     plt.yticks(rotation=0)
#     plt.tight_layout()
#     plt.show()
    
#     # Print business insights from correlations
#     print("\n=== CORRELATION ANALYSIS BUSINESS INSIGHTS ===")
    
#     # Analyze price correlations
#     price_correlations = correlation_matrix['Price'].sort_values(ascending=False)
    
#     print("• Factors influencing property pricing (correlation with Price):")
#     for feature, correlation in price_correlations.items():
#         if feature != 'Price':
#             strength = "Strong" if abs(correlation) > 0.5 else "Moderate" if abs(correlation) > 0.3 else "Weak"
#             direction = "positive" if correlation > 0 else "negative"
#             print(f"  - {feature}: {correlation:.2f} ({strength} {direction} correlation)")
    
#     # Analyze rating correlations
#     if 'Review Scores Rating' in correlation_matrix.columns:
#         rating_correlations = correlation_matrix['Review Scores Rating'].sort_values(ascending=False)
        
#         print("\n• Factors influencing property ratings (correlation with Review Scores Rating):")
#         for feature, correlation in rating_correlations.items():
#             if feature != 'Review Scores Rating':
#                 strength = "Strong" if abs(correlation) > 0.5 else "Moderate" if abs(correlation) > 0.3 else "Weak"
#                 direction = "positive" if correlation > 0 else "negative"
#                 print(f"  - {feature}: {correlation:.2f} ({strength} {direction} correlation)")
    
#     # Price-Rating relationship (if both exist)
#     if 'Price' in correlation_matrix.columns and 'Review Scores Rating' in correlation_matrix.columns:
#         price_rating_corr = correlation_matrix.loc['Price', 'Review Scores Rating']
#         print(f"\n• Price-Rating Relationship: {price_rating_corr:.2f} correlation")
        
#         if abs(price_rating_corr) < 0.2:
#             print("  - Business Insight: Price and ratings show little correlation, suggesting guests don't necessarily associate higher prices with better experiences.")
#         elif price_rating_corr > 0:
#             print("  - Business Insight: Positive correlation indicates higher-priced properties tend to receive better ratings, suggesting price premium may be justified.")
#         else:
#             print("  - Business Insight: Negative correlation suggests guests may have higher expectations for higher-priced properties, or potential overpricing in the market.")

# # 6.3 Temporal Analysis (if Host Since data is available)
# # Business Focus: Analyzing host experience impact on pricing and ratings

# # Write your code for temporal analysis below:
# if df is not None and 'Host Since' in df.columns:
#     # Convert Host Since to datetime if needed
#     if not pd.api.types.is_datetime64_any_dtype(df['Host Since']):
#         try:
#             df['Host Since'] = pd.to_datetime(df['Host Since'])
#             print("\n=== HOST EXPERIENCE ANALYSIS ===")
#         except:
#             print("Could not convert Host Since to datetime format")
    
#     if pd.api.types.is_datetime64_any_dtype(df['Host Since']):
#         # Calculate host experience in days
#         today = pd.to_datetime('today')
#         df['Host_Experience_Days'] = (today - df['Host Since']).dt.days
#         df['Host_Experience_Years'] = df['Host_Experience_Days'] / 365
        
#         # Group hosts by experience level
#         df['Experience_Level'] = pd.cut(
#             df['Host_Experience_Years'],
#             bins=[0, 1, 3, 5, float('inf')],
#             labels=['New (< 1 year)', 'Established (1-3 years)', 'Experienced (3-5 years)', 'Veteran (5+ years)']
#         )
        
#         # Set up figure for host experience analysis
#         plt.figure(figsize=(16, 10))
        
#         # Plot average price by host experience
#         plt.subplot(2, 2, 1)
#         sns.barplot(x='Experience_Level', y='Price', data=df)
#         plt.title('Average Price by Host Experience Level')
#         plt.ylabel('Average Price ($)')
#         plt.grid(True, alpha=0.3)
        
#         # Plot average rating by host experience
#         plt.subplot(2, 2, 2)
#         sns.barplot(x='Experience_Level', y='Review Scores Rating', data=df)
#         plt.title('Average Rating by Host Experience Level')
#         plt.ylabel('Average Rating')
#         plt.grid(True, alpha=0.3)
        
#         # Plot number of reviews by host experience
#         plt.subplot(2, 2, 3)
#         sns.barplot(x='Experience_Level', y='Number Of Reviews', data=df)
#         plt.title('Average Number of Reviews by Host Experience Level')
#         plt.ylabel('Average Number of Reviews')
#         plt.grid(True, alpha=0.3)
        
#         # Plot host experience distribution
#         plt.subplot(2, 2, 4)
#         experience_counts = df['Experience_Level'].value_counts().sort_index()
#         sns.barplot(x=experience_counts.index, y=experience_counts.values)
#         plt.title('Distribution of Host Experience Levels')
#         plt.ylabel('Number of Hosts')
#         plt.grid(True, alpha=0.3)
        
#         plt.tight_layout()
#         plt.suptitle("Host Experience Analysis", fontsize=16, y=1.02)
#         plt.show()
        
#         # Print business insights about host experience
#         print("\n• Host Experience Distribution:")
#         for level, count in experience_counts.items():
#             percentage = (count / len(df)) * 100
#             print(f"  - {level}: {count} hosts ({percentage:.1f}% of market)")
        
#         # Experience level metrics
#         experience_metrics = df.groupby('Experience_Level').agg({
#             'Price': 'mean',
#             'Review Scores Rating': 'mean',
#             'Number Of Reviews': 'mean',
#             'Host Id': 'count'
#         }).rename(columns={'Host Id': 'Listing_Count'})
        
#         print("\n• Host Experience Impact Analysis:")
#         for idx, row in experience_metrics.iterrows():
#             print(f"  - {idx}:")
#             print(f"    · Average Price: ${row['Price']:.2f}")
#             print(f"    · Average Rating: {row['Review Scores Rating']:.1f}/100")
#             print(f"    · Average Reviews: {row['Number Of Reviews']:.1f}")
#             print(f"    · Listing Count: {row['Listing_Count']}")
        
#         # Price premium for experience
#         base_price = experience_metrics.loc['New (< 1 year)', 'Price']
#         for idx, row in experience_metrics.iterrows():
#             if idx != 'New (< 1 year)':
#                 premium = ((row['Price'] - base_price) / base_price) * 100
#                 print(f"  - {idx} price premium: {premium:.1f}% above new hosts")

# # 6.4 Market Segmentation Analysis
# # Business Focus: Identifying distinct market segments and their characteristics

# # Write your code for segmentation analysis below:
# if df is not None:
#     print("\n=== MARKET SEGMENTATION ANALYSIS ===")
    
#     # Create market segments based on price tiers
#     price_quantiles = df['Price'].quantile([0, 0.25, 0.5, 0.75, 1.0])
    
#     df['Price_Segment'] = pd.cut(
#         df['Price'],
#         bins=[0, price_quantiles[0.25], price_quantiles[0.5], price_quantiles[0.75], float('inf')],
#         labels=['Budget', 'Economy', 'Mid-range', 'Premium']
#     )
    
#     # Set up figure for market segmentation analysis
#     plt.figure(figsize=(16, 12))
    
#     # Plot segment sizes
#     plt.subplot(2, 2, 1)
#     segment_counts = df['Price_Segment'].value_counts().sort_index()
#     sns.barplot(x=segment_counts.index, y=segment_counts.values)
#     plt.title('Market Size by Price Segment')
#     plt.ylabel('Number of Listings')
#     plt.grid(True, alpha=0.3)
    
#     # Plot average ratings by segment
#     plt.subplot(2, 2, 2)
#     sns.barplot(x='Price_Segment', y='Review Scores Rating', data=df, order=['Budget', 'Economy', 'Mid-range', 'Premium'])
#     plt.title('Average Rating by Price Segment')
#     plt.ylabel('Average Rating')
#     plt.grid(True, alpha=0.3)
    
#     # Plot most common property types by segment
#     plt.subplot(2, 2, 3)
#     segment_property_counts = pd.crosstab(df['Price_Segment'], df['Property Type']).apply(lambda x: x / x.sum() * 100, axis=1)
#     top_property_types = df['Property Type'].value_counts().nlargest(5).index
#     segment_property_counts = segment_property_counts[top_property_types]
#     segment_property_counts.plot(kind='bar', stacked=True)
#     plt.title('Property Type Distribution by Price Segment')
#     plt.ylabel('Percentage')
#     plt.legend(title='Property Type', bbox_to_anchor=(1.05, 1), loc='upper left')
#     plt.grid(True, alpha=0.3)
    
#     # Plot most common room types by segment
#     plt.subplot(2, 2, 4)
#     segment_room_counts = pd.crosstab(df['Price_Segment'], df['Room Type']).apply(lambda x: x / x.sum() * 100, axis=1)
#     segment_room_counts.plot(kind='bar', stacked=True)
#     plt.title('Room Type Distribution by Price Segment')
#     plt.ylabel('Percentage')
#     plt.legend(title='Room Type', bbox_to_anchor=(1.05, 1), loc='upper left')
#     plt.grid(True, alpha=0.3)
    
#     plt.tight_layout()
#     plt.show()
    
#     # Calculate and print segment profiles
#     segment_profiles = df.groupby('Price_Segment').agg({
#         'Price': ['mean', 'min', 'max'],
#         'Review Scores Rating': 'mean',
#         'Number Of Reviews': 'mean',
#         'Beds': 'mean',
#         'Host Id': 'count'
#     })
#     segment_profiles.columns = ['Avg_Price', 'Min_Price', 'Max_Price', 'Avg_Rating', 'Avg_Reviews', 'Avg_Beds', 'Listing_Count']
    
#     print("\n• Market Segment Profiles:")
#     for idx, row in segment_profiles.iterrows():
#         market_share = (row['Listing_Count'] / len(df)) * 100
#         print(f"  - {idx} Segment ({market_share:.1f}% of market):")
#         print(f"    · Price Range: ${row['Min_Price']:.2f} - ${row['Max_Price']:.2f} (Avg: ${row['Avg_Price']:.2f})")
#         print(f"    · Average Rating: {row['Avg_Rating']:.1f}/100")
#         print(f"    · Average Reviews: {row['Avg_Reviews']:.1f}")
#         print(f"    · Average Beds: {row['Avg_Beds']:.1f}")
    
#     # Segment neighborhood distribution
#     print("\n• Top Neighborhoods by Market Segment:")
#     for segment in ['Budget', 'Economy', 'Mid-range', 'Premium']:
#         segment_neighborhoods = df[df['Price_Segment'] == segment]['Neighbourhood'].value_counts().head(3)
#         print(f"  - {segment} Segment:")
#         for neighborhood, count in segment_neighborhoods.items():
#             segment_total = len(df[df['Price_Segment'] == segment])
#             percentage = (count / segment_total) * 100
#             print(f"    · {neighborhood}: {count} listings ({percentage:.1f}% of segment)")

# # =============================================================================
# # SECTION 7: BUSINESS INSIGHTS & RECOMMENDATIONS
# # =============================================================================

# # 7.1 Key Findings Summary
# # Summarize the most important discoveries from your analysis
# # Connect findings to business value and actionable insights

# # Write your summary of key findings below:
# if df is not None:
#     print("\n" + "="*80)
#     print("                           KEY BUSINESS INSIGHTS SUMMARY                           ")
#     print("="*80)
    
#     # Market Structure Insights
#     print("\n📊 MARKET STRUCTURE INSIGHTS:")
    
#     # Calculate key metrics if not already calculated
#     if 'Price_Segment' not in df.columns:
#         df['Price_Segment'] = pd.cut(
#             df['Price'],
#             bins=[0, df['Price'].quantile(0.25), df['Price'].quantile(0.5), df['Price'].quantile(0.75), float('inf')],
#             labels=['Budget', 'Economy', 'Mid-range', 'Premium']
#         )
    
#     total_listings = len(df)
#     total_neighborhoods = df['Neighbourhood'].nunique()
#     avg_price = df['Price'].mean()
#     median_price = df['Price'].median()
#     price_range = df['Price'].max() - df['Price'].min()
    
#     # Print market overview
#     print(f"• The market consists of {total_listings} listings across {total_neighborhoods} neighborhoods.")
#     print(f"• Average price point is ${avg_price:.2f}, with median at ${median_price:.2f}.")
#     print(f"• Price range spans ${price_range:.2f}, indicating significant market segmentation.")
    
#     # Most popular property configurations
#     top_property_type = df['Property Type'].value_counts().index[0]
#     top_property_pct = (df['Property Type'].value_counts().iloc[0] / total_listings) * 100
    
#     top_room_type = df['Room Type'].value_counts().index[0]
#     top_room_pct = (df['Room Type'].value_counts().iloc[0] / total_listings) * 100
    
#     print(f"• Most common property configuration: {top_property_type} as {top_room_type} ({top_room_pct:.1f}% of market)")
    
#     # Location Insights
#     print("\n📍 LOCATION INSIGHTS:")
    
#     # Top neighborhoods by listing count
#     top_neighborhood = df['Neighbourhood'].value_counts().index[0]
#     top_neighborhood_count = df['Neighbourhood'].value_counts().iloc[0]
#     top_neighborhood_pct = (top_neighborhood_count / total_listings) * 100
    
#     print(f"• Market concentration: {top_neighborhood} leads with {top_neighborhood_count} listings ({top_neighborhood_pct:.1f}% of market).")
    
#     # Calculate neighborhood metrics if not already calculated
#     try:
#         neighborhood_metrics = df.groupby('Neighbourhood').agg({
#             'Price': 'mean',
#             'Review Scores Rating': 'mean',
#             'Host Id': 'count'
#         }).rename(columns={'Host Id': 'Listing_Count'})
        
#         # Value score (rating / price ratio - higher means better value)
#         neighborhood_metrics['Value_Score'] = neighborhood_metrics['Review Scores Rating'] / neighborhood_metrics['Price']
        
#         # Highest priced neighborhood
#         highest_price_hood = neighborhood_metrics.sort_values('Price', ascending=False).index[0]
#         highest_price = neighborhood_metrics.loc[highest_price_hood, 'Price']
        
#         # Best value neighborhood (among those with at least 5 listings)
#         popular_neighborhoods = neighborhood_metrics[neighborhood_metrics['Listing_Count'] >= 5]
#         best_value_hood = popular_neighborhoods.sort_values('Value_Score', ascending=False).index[0]
#         best_value_price = popular_neighborhoods.loc[best_value_hood, 'Price']
#         best_value_rating = popular_neighborhoods.loc[best_value_hood, 'Review Scores Rating']
        
#         print(f"• Premium location: {highest_price_hood} commands highest average price at ${highest_price:.2f}")
#         print(f"• Best value location: {best_value_hood} offers best rating-to-price ratio (${best_value_price:.2f}, rating {best_value_rating:.1f}/100)")
#     except:
#         print("• Detailed neighborhood analysis not available")
    
#     # Pricing Insights
#     print("\n💰 PRICING INSIGHTS:")
    
#     # Price determinants
#     print("• Key price determinants in order of importance:")
    
#     # Try to access correlation data if available
#     try:
#         numerical_features = df.select_dtypes(include=['int64', 'float64']).columns
#         correlation_matrix = df[numerical_features].corr()
#         price_correlations = correlation_matrix['Price'].sort_values(ascending=False)
        
#         # Print top 3 price correlations (excluding Price itself)
#         count = 0
#         for feature, correlation in price_correlations.items():
#             if feature != 'Price' and count < 3:
#                 print(f"  {count+1}. {feature}: {correlation:.2f} correlation")
#                 count += 1
#     except:
#         # Fallback if correlation analysis wasn't run
#         print("  1. Property Type and Room Type (categorical)")
#         print("  2. Location (Neighbourhood and Zipcode)")
#         print("  3. Number of Beds")
    
#     # Property Type Insights
#     print("\n🏠 PROPERTY INSIGHTS:")
    
#     # Price premium by property type (if data available)
#     try:
#         top_property_types = df['Property Type'].value_counts().nlargest(3).index
#         property_price_avg = df[df['Property Type'].isin(top_property_types)].groupby('Property Type')['Price'].mean().sort_values(ascending=False)
        
#         for idx, price in property_price_avg.items():
#             premium_pct = ((price - avg_price) / avg_price) * 100
#             premium_txt = f"{premium_pct:.1f}% premium" if premium_pct > 0 else f"{abs(premium_pct):.1f}% discount"
#             print(f"• {idx}: ${price:.2f} ({premium_txt} vs. market average)")
#     except:
#         print("• Detailed property type price analysis not available")
    
#     # Room Type Insights
#     try:
#         room_price_avg = df.groupby('Room Type')['Price'].mean().sort_values(ascending=False)
        
#         for idx, price in room_price_avg.items():
#             premium_pct = ((price - avg_price) / avg_price) * 100
#             premium_txt = f"{premium_pct:.1f}% premium" if premium_pct > 0 else f"{abs(premium_pct):.1f}% discount"
#             print(f"• {idx}: ${price:.2f} ({premium_txt} vs. market average)")
#     except:
#         print("• Detailed room type price analysis not available")
    
#     # Guest Satisfaction Insights
#     print("\n⭐ GUEST SATISFACTION INSIGHTS:")
    
#     avg_rating = df['Review Scores Rating'].mean()
#     print(f"• Average satisfaction rating across all properties: {avg_rating:.1f}/100")
    
#     # Try to access rating correlations if available
#     try:
#         if 'Review Scores Rating' in correlation_matrix.columns:
#             rating_correlations = correlation_matrix['Review Scores Rating'].sort_values(ascending=False)
            
#             # Print top 3 rating correlations (excluding Rating itself)
#             count = 0
#             print("• Factors most associated with higher ratings:")
#             for feature, correlation in rating_correlations.items():
#                 if feature != 'Review Scores Rating' and count < 3:
#                     print(f"  {count+1}. {feature}: {correlation:.2f} correlation")
#                     count += 1
#     except:
#         print("• Detailed rating correlation analysis not available")

# # 7.2 Business Recommendations
# # Provide specific, actionable recommendations based on your analysis:
# # 1. For Property Investors
# # 2. For Current Hosts
# # 3. For Airbnb Platform
# # 4. For Travelers

# # Write your business recommendations below:
# if df is not None:
#     print("\n" + "="*80)
#     print("                        ACTIONABLE BUSINESS RECOMMENDATIONS                        ")
#     print("="*80)
    
#     # Recommendations for Property Investors
#     print("\n💼 FOR PROPERTY INVESTORS:")
#     print("1️⃣ Target neighborhoods with high rating-to-price ratios for best ROI potential.")
    
#     # Try to recommend specific neighborhoods if analysis was done
#     try:
#         opportunity_neighborhoods = popular_neighborhoods[(popular_neighborhoods['Review Scores Rating'] > 85) & 
#                                                     (popular_neighborhoods['Price'] < avg_price)].sort_values('Value_Score', ascending=False)
        
#         if not opportunity_neighborhoods.empty:
#             print(f"   • Consider properties in {opportunity_neighborhoods.index[0]} and {opportunity_neighborhoods.index[1]} for high ratings at below-average prices.")
#     except:
#         pass
    
#     print("2️⃣ Focus on property types with highest premiums for maximum revenue potential.")
#     print("3️⃣ Consider the trade-off between \"Entire home/apt\" (higher price) vs. \"Private room\" (potentially better ROI).")
#     print("4️⃣ Analyze local supply-demand dynamics before investing in highly saturated neighborhoods.")
    
#     # Recommendations for Current Hosts
#     print("\n🏠 FOR CURRENT HOSTS:")
#     print("1️⃣ Optimize pricing strategy based on your neighborhood's position relative to market average.")
#     print("2️⃣ Benchmark your property against neighborhood averages for both price and ratings.")
#     print("3️⃣ Focus on areas with highest correlation to positive reviews to maximize guest satisfaction.")
#     print("4️⃣ Consider offering more beds for better price efficiency, as multi-bed configurations often command higher premiums.")
#     print("5️⃣ Use market segmentation data to position your property within the appropriate price tier.")
    
#     # Recommendations for Airbnb Platform
#     print("\n🌐 FOR AIRBNB PLATFORM:")
#     print("1️⃣ Develop targeted expansion strategies for underrepresented neighborhoods with high value scores.")
#     print("2️⃣ Create host education resources focused on pricing optimization by property type and neighborhood.")
#     print("3️⃣ Implement dynamic pricing suggestions based on property characteristics and location benchmarks.")
#     print("4️⃣ Consider neighborhood-specific marketing campaigns highlighting unique value propositions.")
#     print("5️⃣ Develop quality standards and incentives for hosts to improve ratings in neighborhoods with below-average scores.")
    
#     # Recommendations for Travelers
#     print("\n✈️ FOR TRAVELERS:")
#     print("1️⃣ Best value accommodations can be found in neighborhoods with high rating-to-price ratios.")
    
#     # Try to recommend specific neighborhoods if analysis was done
#     try:
#         best_value_hoods = popular_neighborhoods.sort_values('Value_Score', ascending=False).head(2)
#         if not best_value_hoods.empty:
#             print(f"   • Consider {best_value_hoods.index[0]} and {best_value_hoods.index[1]} for best value accommodations.")
#     except:
#         pass
    
#     print("2️⃣ Premium travelers should focus on top-rated property types rather than just expensive neighborhoods.")
#     print("3️⃣ Budget travelers should consider 'Private room' configurations for significant savings with minimal rating impact.")
#     print("4️⃣ Consider the trade-off between central location premium and better value in nearby neighborhoods.")
#     print("5️⃣ Book with experienced hosts (3+ years) for potentially better-rated stays.")

