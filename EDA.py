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

# # region 4.1 Numerical Variables Distribution
# # Analyze: Price, Review Scores Rating, Number Of Reviews, Number of Records, Beds
# # Business Focus: Understanding pricing distribution, rating patterns, and booking frequency

# if df is not None:
#     # Set up figure size for numerical variables analysis
#     plt.figure(figsize=(18, 12))
    
#     # Define numerical columns to analyze
#     numerical_cols = ['Price', 'Review Scores Rating', 'Number Of Reviews', 'Number of Records', 'Beds']
    
#     # Loop through numerical columns and create histograms and boxplots
#     for i, col in enumerate(numerical_cols):
#         # Create histograms with better bin settings and KDE
#         plt.subplot(3, len(numerical_cols), i+1)
#         if col == 'Price':
#             # Use more bins for price to show distribution details
#             # sns.histplot(df[col], kde=True, bins=30, color='darkblue')
#             sns.histplot(df[col].clip(upper=df[col].quantile(0.99)), kde=True, bins=30, color='darkblue')
#             plt.axvline(df[col].mean(), color='red', linestyle='--', label=f'Mean: ${df[col].mean():.2f}')
#             plt.axvline(df[col].median(), color='green', linestyle='-.', label=f'Median: ${df[col].median():.2f}')
#         else:
#             # Standard visualization for non-price numerical variables
#             sns.histplot(df[col], kde=True, bins=20, color='darkblue')
#             plt.axvline(df[col].mean(), color='red', linestyle='--', label=f'Mean: {df[col].mean():.2f}')
#             plt.axvline(df[col].median(), color='green', linestyle='-.', label=f'Median: {df[col].median():.2f}')
 
#         plt.title(f'Distribution of {col}', fontdict={'fontsize': 9, 'weight': 'bold'})
#         plt.xlabel('')
#         plt.ylabel('')
#         plt.grid(True, alpha=0.3)
#         plt.legend(fontsize='small')
#         plt.tick_params(labelsize=8)
        
#         # Create boxplots with enhanced styling
#         plt.subplot(3, len(numerical_cols), i+len(numerical_cols)+1)
#         sns.boxplot(x=df[col], color='skyblue', width=0.5)
#         plt.title(f'Boxplot of {col}', fontdict={'fontsize': 9, 'weight': 'bold'})
#         plt.xlabel('')
#         plt.ylabel('')
#         plt.grid(True, alpha=0.3)

#         # Add descriptive statistics with improved formatting
#         plt.subplot(3, len(numerical_cols), i+(2*len(numerical_cols))+1)
#         plt.axis('off')
        
#         # Format statistics
#         stats = df[col].describe()
        
#         # Add dollar sign for price, otherwise keep format consistent
#         prefix = "$" if col == "Price" else ""
#         suffix = "/100" if col == "Review Scores Rating" else ""
        
#         plt.text(0.1, 0.9, f"Mean: {prefix}{stats['mean']:.2f}{suffix}")
#         plt.text(0.1, 0.8, f"Median: {prefix}{stats['50%']:.2f}{suffix}")
#         plt.text(0.1, 0.7, f"Std Dev: {prefix}{stats['std']:.2f}")
#         plt.text(0.1, 0.6, f"Min: {prefix}{stats['min']:.2f}{suffix}")
#         plt.text(0.1, 0.5, f"Max: {prefix}{stats['max']:.2f}{suffix}")
#         plt.text(0.1, 0.4, f"Range: {prefix}{stats['max'] - stats['min']:.2f}")
    
#     # Adjust spacing to reduce excessive margins and optimize layout
#     plt.subplots_adjust(hspace=0.2,  # Vertical space between rows
#                         left=0.05,   # Reduce left margin
#                         right=0.95,  # Increase usable right area
#                         top=0.95,    # Increase usable top area
#                         bottom=0.05) # Reduce bottom margin
    
#     # Add a main title with adjusted position
#     plt.show()
        
#     # Business insights from numerical variables
#     print("\n=== NUMERICAL VARIABLES BUSINESS INSIGHTS ===")
    
#     # Price insights
#     avg_price = df['Price'].mean()
#     median_price = df['Price'].median()
#     price_range = df['Price'].max() - df['Price'].min()
#     print(f"• Average listing price: ${avg_price:.2f}")
#     print(f"• Median listing price: ${median_price:.2f}")
#     print(f"• Price range: ${price_range:.2f}")
    
#     # Reviews insights
#     avg_reviews = df['Number Of Reviews'].mean()
#     median_reviews = df['Number Of Reviews'].median()
#     print(f"• Average number of reviews per listing: {avg_reviews:.2f}")
#     print(f"• Median number of reviews per listing: {median_reviews:.2f}")
    
#     # Ratings insights
#     avg_rating = df['Review Scores Rating'].mean()
#     print(f"• Average rating: {avg_rating:.2f}/100")
    
#     # Beds insights
#     avg_beds = df['Beds'].mean()
#     print(f"• Average number of beds: {avg_beds:.2f}")
#     most_common_beds = df['Beds'].mode()[0]
#     print(f"• Most common bed configuration: {most_common_beds}")
# else:
#     print('No data loaded to analyze numerical variable distributions.')
# #endregion

# # region 4.2 Categorical Variables Distribution
# # Analyze: Neighbourhood, Zipcode, Property Type, Room Type
# # Business Focus: Identifying popular areas, property types, and pricing strategies by segment

# if df is not None:
#     # Set up figure size for categorical variables analysis
#     plt.figure(figsize=(20, 18))
    
#     # Define categorical columns to analyze
#     categorical_cols = ['Neighbourhood', 'Zipcode', 'Property Type', 'Room Type']
    
#     # Color palette for consistent visuals
#     colors = plt.cm.tab10.colors
    
#     # Function to plot top N categories for a categorical variable
#     def plot_top_categories(data, column, axis, top_n=10, title=None, color=None):
#         counts = data[column].value_counts().nlargest(top_n)
#         bars = counts.plot(kind='bar', ax=axis, color=color)
#         axis.set_title(title if title else f'Top {top_n} {column}s', fontdict={'fontsize': 9, 'weight': 'bold'})
#         axis.grid(True, axis='y', alpha=0.3, linestyle='--')
        
#         # Add percentage labels to bars
#         total = len(data)
#         for i, v in enumerate(counts):
#             percentage = (v / total) * 100
#             axis.text(i, v + 0.1, f"{v}\n({percentage:.1f}%)", ha='center', fontsize= 8)
        
#         # Improve x-axis labels and y-axis labels
#         plt.setp(axis.xaxis.get_majorticklabels(), rotation=45, ha='right', rotation_mode='anchor', fontsize=8)
#         plt.setp(axis.yaxis.get_majorticklabels(), fontsize=8)
        
#         return counts
    
#     # Function to calculate and display category percentages with business insights
#     def display_category_percentages(data, column, top_n=10):
#         total = len(data)
#         counts = data[column].value_counts().nlargest(top_n)
#         percentages = (counts / total * 100).round(1)
        
#         # Calculate average price by category
#         category_prices = data.groupby(column)['Price'].agg(['mean', 'median', 'count'])
#         category_prices = category_prices.loc[counts.index]
        
#         print(f"\n=== {column.upper()} DISTRIBUTION ===")
#         for cat, count in counts.items():
#             pct = percentages[cat]
#             avg_price = category_prices.loc[cat, 'mean']
#             median_price = category_prices.loc[cat, 'median']
#             print(f"• {cat}: {count} listings ({pct}% of market) | Avg Price: ${avg_price:.0f} | Median: ${median_price:.0f}")
        
#         # Calculate concentration
#         top_concentration = percentages.sum()
#         print(f"• Market concentration: Top {top_n} {column.lower()}s represent {top_concentration:.1f}% of all listings")
        
#         # Price comparison
#         overall_avg = data['Price'].mean()
#         highest_price_cat = category_prices['mean'].idxmax()
#         highest_price = category_prices.loc[highest_price_cat, 'mean']
#         print(f"• Pricing insights: {highest_price_cat} has the highest average price (${highest_price:.0f} vs. overall ${overall_avg:.0f})")
    
#     # Plot Neighbourhood distribution (first column, first row)
#     ax1 = plt.subplot(3, 2, 1)
#     top_neighborhoods = plot_top_categories(df, 'Neighbourhood', ax1, top_n=10,title='Top Neighbourhoods by Listing Count', color=colors[0])
    
#     # Plot Zipcode distribution (first column, second row)
#     ax3 = plt.subplot(3, 2, 3)
#     top_zipcodes = plot_top_categories(df, 'Zipcode', ax3, top_n=10,title='Top 10 Zipcodes by Listing Count', color=colors[1])
    
#     # Plot Property Type distribution (first column, third row)
#     ax5 = plt.subplot(3, 2, 5)
#     top_property_types = plot_top_categories(df, 'Property Type', ax5, top_n=10, title='Top 10 Property Types', color=colors[2])
    
#     # Plot Room Type distribution with pie chart for better proportion visualization (second column, first row)
#     ax2 = plt.subplot(3, 2, 2)
#     room_type_counts = df['Room Type'].value_counts()
    
#     # Create pie chart for Room Type with no labels beside the slices, only percentages inside
#     wedges, _, autotexts = ax2.pie(
#         room_type_counts, 
#         labels=None,
#         autopct='%1.1f%%',
#         shadow=False, 
#         startangle=90,
#         colors=colors[3:6],
#     )

#     # Create a legend with room type information
#     ax2.legend(wedges, room_type_counts.index, title="Room Types", loc="center left", bbox_to_anchor=(0.85, 0.5))
    
#     # Style the percentage text inside slices
#     plt.setp(autotexts, size=9, weight="bold", color="white")
        
#     ax2.set_title('Room Type Distribution', fontdict={'fontsize': 9, 'weight': 'bold'})
#     ax2.axis('equal')  
    
#     # Add price comparison by Room Type (second column, second row)
#     ax4 = plt.subplot(3, 2, 4)
#     room_price_data = df.groupby('Room Type')['Price'].agg(['mean', 'median']).reset_index()
    
#     # Create a grouped bar chart for price comparison
#     x = range(len(room_price_data))
#     width = 0.35
#     ax4.bar([i - width/2 for i in x], room_price_data['mean'], width, label='Average', color=colors[6])
#     ax4.bar([i + width/2 for i in x], room_price_data['median'], width, label='Median', color=colors[7])
    
#     # Add data labels to bars
#     for i in x:
#         ax4.text(i - width/2, room_price_data['mean'][i] + 5, f"${room_price_data['mean'][i]:.0f}", ha='center', fontsize=8)
#         ax4.text(i + width/2, room_price_data['median'][i] + 5, f"${room_price_data['median'][i]:.0f}", ha='center', fontsize=8)
    
#     ax4.set_title('Price by Room Type', fontdict={'fontsize': 10, 'weight': 'bold'})
#     ax4.set_ylabel('Price ($)', fontdict={'fontsize': 10})
#     ax4.set_xticks(x)
#     ax4.set_xticklabels(room_price_data['Room Type'])
#     ax4.grid(True, axis='y', alpha=0.3, linestyle='--')
#     ax4.legend()
    
#     # Set font size for X and Y axis tick labels
#     plt.setp(ax4.xaxis.get_majorticklabels(), fontsize= 8)
#     plt.setp(ax4.yaxis.get_majorticklabels(), fontsize= 8)
    
#     # Add price comparison by Neighbourhood (second column, third row)
#     ax6 = plt.subplot(3, 2, 6)
#     neighbourhood_price = df.groupby('Neighbourhood')['Price'].agg(['mean', 'median', 'count']).sort_values('mean', ascending= True)
    
#     # Create horizontal bar chart for neighborhood prices
#     bars = ax6.barh(neighbourhood_price.index, neighbourhood_price['mean'], color=colors[8])
#     ax6.set_title('Average Price by Neighbourhood', fontdict={'fontsize': 10, 'weight': 'bold'})
#     ax6.set_xlabel('Price ($)', fontdict={'fontsize': 9})
#     ax6.grid(True, axis='x', alpha=0.3, linestyle='--')
    
#     # Add count and price labels
#     for i, bar in enumerate(bars):
#         neighborhood = neighbourhood_price.index[i]
#         count = neighbourhood_price.loc[neighborhood, 'count']
#         price = neighbourhood_price.loc[neighborhood, 'mean']
#         ax6.text(price + 5, i, f"${price:.0f} | {count} listings", va='center', fontsize= 8)
    
#     plt.tight_layout(pad=3.0)
#     plt.subplots_adjust(hspace=0.35, wspace=0.25, top=0.92)
#     plt.suptitle("Categorical Variables Analysis - Market Segments and Pricing", fontsize=18, y=0.98)
#     plt.show()
    
#     # Print business insights about categorical variables
#     print("\n=== CATEGORICAL VARIABLES BUSINESS INSIGHTS ===")
    
#     # Display category percentages with enhanced business metrics
#     for col in categorical_cols:
#         top_n = 5 if col in ['Neighbourhood', 'Zipcode'] else 8 if col == 'Property Type' else len(df[col].unique())
#         display_category_percentages(df, col, top_n=top_n)
    
#     # Additional market insights with business focus
#     print("\n=== MARKET STRUCTURE & PRICING INSIGHTS ===")
    
#     # Calculate market concentration metrics
#     total_listings = len(df)
    
#     # Neighborhood concentration and pricing premium
#     neighborhood_data = df.groupby('Neighbourhood').agg({
#         'Host Id': 'count',
#         'Price': ['mean', 'median', 'std']
#     })
#     neighborhood_data.columns = ['Listings', 'Avg_Price', 'Median_Price', 'Price_Std']
#     neighborhood_data['Market_Share'] = (neighborhood_data['Listings'] / total_listings * 100).round(1)
#     neighborhood_data['Price_Premium'] = ((neighborhood_data['Avg_Price'] / df['Price'].mean() - 1) * 100).round(1)
    
#     # Most expensive neighborhood
#     most_expensive = neighborhood_data.sort_values('Avg_Price', ascending=False).index[0]
#     premium_pct = neighborhood_data.loc[most_expensive, 'Price_Premium']
#     print(f"• Premium neighborhood: {most_expensive} commands {premium_pct:+.1f}% price premium vs. market average")
    
#     # Most popular neighborhood
#     most_popular = neighborhood_data.sort_values('Listings', ascending=False).index[0]
#     market_share = neighborhood_data.loc[most_popular, 'Market_Share']
#     print(f"• Market leader: {most_popular} holds {market_share:.1f}% market share with {int(neighborhood_data.loc[most_popular, 'Listings'])} listings")
    
#     # Property type insights
#     property_data = df.groupby('Property Type').agg({'Host Id': 'count','Price': ['mean', 'median']
#     }).iloc[:, :3]
#     property_data.columns = ['Listings', 'Avg_Price', 'Median_Price']
#     property_data['Market_Share'] = (property_data['Listings'] / total_listings * 100).round(1)
    
#     # Most profitable property type
#     most_profitable = property_data.sort_values('Avg_Price', ascending=False).index[0]
#     profit_premium = ((property_data.loc[most_profitable, 'Avg_Price'] / df['Price'].mean() - 1) * 100).round(1)
#     print(f"• Highest revenue opportunity: {most_profitable} listings average ${property_data.loc[most_profitable, 'Avg_Price']:.0f}/night ({profit_premium:+.1f}% vs. market)")
    
#     # Room type insights with price premium calculation
#     room_data = df.groupby('Room Type').agg({'Host Id': 'count','Price': ['mean', 'median']}).iloc[:, :3]
#     room_data.columns = ['Listings', 'Avg_Price', 'Median_Price']
#     room_data['Market_Share'] = (room_data['Listings'] / total_listings * 100).round(1)
    
#     # Entire home premium calculation
#     if 'Entire home/apt' in room_data.index and 'Private room' in room_data.index:
#         entire_home_premium = ((room_data.loc['Entire home/apt', 'Avg_Price'] / room_data.loc['Private room', 'Avg_Price'] - 1) * 100).round(1)
#         print(f"• Entire home premium: {entire_home_premium:+.1f}% price premium over private rooms")
    
#     # Price-to-bed ratio analysis
#     df['Price_per_Bed'] = df['Price'] / df['Beds']
#     best_value_type = df.groupby('Property Type')['Price_per_Bed'].median().nsmallest(1).index[0]
#     print(f"• Best value proposition: {best_value_type} offers lowest price-to-bed ratio")
    
#     # Most common property configuration
#     most_common_config = df.groupby(['Property Type', 'Room Type']).size().nlargest(1)
#     config_index = most_common_config.index[0]
#     config_share = (most_common_config.iloc[0] / total_listings * 100).round(1)
#     print(f"• Most common offering: {config_index[0]} with {config_index[1]} ({config_share:.1f}% of market)")
# else:
#     print('No data loaded to analyze categorical variable distributions.')
# #endregion

# =============================================================================
# SECTION 5: BIVARIATE ANALYSIS
# =============================================================================

# =============================================================================
# 5.1 Location-based Analysis
# =============================================================================
# Analyze: 
# - Neighbourhood vs. listing count, price, reviews, ratings
# - Zipcode vs. listing count, price, reviews
# Business Focus: Identifying high-value locations and market saturation

# Write your code for location-based analysis below:
if df is not None:
    # Set figure aesthetics for business presentation with consistent style
    plt.figure(figsize=(20, 24))
    
    # Color palette for consistent visuals (matching Section 4.2)
    colors = plt.cm.tab10.colors
    
    # 1. Neighbourhood vs. Listing Count (Top 15)
    ax1 = plt.subplot(3, 2, 1)
    neighborhood_counts = df['Neighbourhood'].value_counts().nlargest(15)
    bars = neighborhood_counts.plot(kind='barh', color=colors[0], ax=ax1)
    ax1.set_title('Top 15 Neighbourhoods by Listing Count', fontdict={'fontsize': 10, 'weight': 'bold'})
    ax1.set_xlabel('Number of Listings', fontdict={'fontsize': 9})
    ax1.set_ylabel('')
    ax1.grid(True, axis='x', alpha=0.3, linestyle='--')
    
    # Add count and percentage labels with consistent formatting
    total = len(df)
    for i, v in enumerate(neighborhood_counts):
        percentage = (v / total) * 100
        ax1.text(v + 1, i, f"{v} ({percentage:.1f}%)", va='center', fontsize=8)
    
    # Set font size for axis labels
    plt.setp(ax1.yaxis.get_majorticklabels(), fontsize=8)
    plt.setp(ax1.xaxis.get_majorticklabels(), fontsize=8)
    
    # 2. Neighbourhood vs. Average Price (Top 15 by count)
    ax2 = plt.subplot(3, 2, 2)
    top_neighborhoods = df['Neighbourhood'].value_counts().nlargest(15).index
    neighborhood_avg_price = df[df['Neighbourhood'].isin(top_neighborhoods)].groupby('Neighbourhood')['Price'].mean().sort_values(ascending=True)
    bars = neighborhood_avg_price.plot(kind='barh', color=colors[1], ax=ax2)
    ax2.set_title('Average Price by Top 15 Neighbourhoods', fontdict={'fontsize': 10, 'weight': 'bold'})
    ax2.set_xlabel('Average Price ($)', fontdict={'fontsize': 9})
    ax2.set_ylabel('', fontdict={'fontsize': 9})
    ax2.grid(True, axis='x', alpha=0.3, linestyle='--')
    
    # Add price labels with dollar sign formatting
    for i, v in enumerate(neighborhood_avg_price):
        ax2.text(v + 1, i, f"${v:.0f}", va='center', fontsize=8)
    
    # Set font size for axis labels
    plt.setp(ax2.yaxis.get_majorticklabels(), fontsize=8)
    plt.setp(ax2.xaxis.get_majorticklabels(), fontsize=8)
    
    # 3. Neighbourhood vs. Average Rating (Top 15 by count)
    ax3 = plt.subplot(3, 2, 3)
    neighborhood_avg_rating = df[df['Neighbourhood'].isin(top_neighborhoods)].groupby('Neighbourhood')['Review Scores Rating'].mean().sort_values(ascending=True)
    bars = neighborhood_avg_rating.plot(kind='barh', color=colors[2], ax=ax3)
    ax3.set_title('Average Rating by Top 15 Neighbourhoods', fontdict={'fontsize': 10, 'weight': 'bold'})
    ax3.set_xlabel('Average Review Score Rating (out of 100)', fontdict={'fontsize': 9})
    ax3.set_ylabel('', fontdict={'fontsize': 9})
    ax3.grid(True, axis='x', alpha=0.3, linestyle='--')
    
    # Add rating labels with consistent formatting
    for i, v in enumerate(neighborhood_avg_rating):
        ax3.text(v + 0.5, i, f"{v:.1f}/100", va='center', fontsize=8)
    
    # Set font size for axis labels
    plt.setp(ax3.yaxis.get_majorticklabels(), fontsize=8)
    plt.setp(ax3.xaxis.get_majorticklabels(), fontsize=8)
    
    # 4. Neighbourhood vs. Price (Boxplot for top 10 neighborhoods, clipped at 95th percentile)
    ax4 = plt.subplot(3, 2, 4)
    top10_neighborhoods = df['Neighbourhood'].value_counts().nlargest(10).index
    
    # Create filtered dataframe for cleaner visualization (removing extreme outliers)
    filtered_df_for_boxplot = df[df['Neighbourhood'].isin(top10_neighborhoods)].copy()
    
    # Calculate 95th percentile of prices for better visualization
    price_95th_percentile = filtered_df_for_boxplot['Price'].quantile(0.95)
    
    # Clip prices at 95th percentile for visualization purposes only
    filtered_df_for_boxplot['Price_Clipped'] = filtered_df_for_boxplot['Price'].clip(upper=price_95th_percentile)
    
    # Create boxplot with clipped prices - using consistent color without warnings
    sns.boxplot(x='Neighbourhood', y='Price_Clipped', data=filtered_df_for_boxplot, color=colors[3], ax=ax4)
    ax4.set_title('Price Distribution by Top 10 Neighbourhoods (95th Percentile)', fontdict={'fontsize': 10, 'weight': 'bold'})
    ax4.set_xlabel('', fontdict={'fontsize': 9})
    ax4.set_ylabel('Price ($, clipped at 95th percentile)', fontdict={'fontsize': 9})
    plt.setp(ax4.xaxis.get_majorticklabels(), rotation=45, ha='right', rotation_mode='anchor', fontsize=8)
    ax4.grid(True, axis='y', alpha=0.3, linestyle='--')
    
    # Add median price annotations with dollar sign formatting
    for i, neighborhood in enumerate(top10_neighborhoods):
        median_price = df[df['Neighbourhood'] == neighborhood]['Price'].median()
        p95_price = df[df['Neighbourhood'] == neighborhood]['Price'].quantile(0.95)
        ax4.text(i, median_price + 5, f"${median_price:.0f}", ha='center', fontsize=8, rotation=0)
        
    # Add note about clipping
    ax4.text(0.5, 0.97, f"Note: Prices clipped at ${price_95th_percentile:.0f} (95th percentile)", 
             transform=ax4.transAxes, ha='center', fontsize=7, style='italic')
    
    # Set font size for axis labels
    plt.setp(ax4.yaxis.get_majorticklabels(), fontsize=8)
    
    # 5. Zipcode vs. Listing Count (Top 15)
    ax5 = plt.subplot(3, 2, 5)
    zipcode_counts = df['Zipcode'].value_counts().nlargest(15)
    bars = zipcode_counts.plot(kind='barh', color=colors[4], ax=ax5)
    ax5.set_title('Top 15 Zipcodes by Listing Count', fontdict={'fontsize': 10, 'weight': 'bold'})
    ax5.set_xlabel('Number of Listings', fontdict={'fontsize': 9})
    ax5.set_ylabel('', fontdict={'fontsize': 9})
    ax5.grid(True, axis='x', alpha=0.3, linestyle='--')
    
    # Add count and percentage labels with consistent formatting
    for i, v in enumerate(zipcode_counts):
        percentage = (v / total) * 100
        ax5.text(v + 1, i, f"{v} ({percentage:.1f}%)", va='center', fontsize=8)
    
    # Set font size for axis labels
    plt.setp(ax5.yaxis.get_majorticklabels(), fontsize=8)
    plt.setp(ax5.xaxis.get_majorticklabels(), fontsize=8)
    
    # 6. Zipcode vs. Average Price (Top 15 by count)
    ax6 = plt.subplot(3, 2, 6)
    top_zipcodes = df['Zipcode'].value_counts().nlargest(15).index
    zipcode_avg_price = df[df['Zipcode'].isin(top_zipcodes)].groupby('Zipcode')['Price'].mean().sort_values(ascending=False)
    bars = zipcode_avg_price.plot(kind='barh', color=colors[5], ax=ax6)
    ax6.set_title('Average Price by Top 15 Zipcodes', fontdict={'fontsize': 10, 'weight': 'bold'})
    ax6.set_xlabel('Average Price ($)', fontdict={'fontsize': 9})
    ax6.set_ylabel('', fontdict={'fontsize': 9})
    ax6.grid(True, axis='x', alpha=0.3, linestyle='--')
    
    # Add price labels with dollar sign formatting
    for i, v in enumerate(zipcode_avg_price):
        ax6.text(v + 1, i, f"${v:.0f}", va='center', fontsize=8)
    
    # Set font size for axis labels
    plt.setp(ax6.yaxis.get_majorticklabels(), fontsize=8)
    plt.setp(ax6.xaxis.get_majorticklabels(), fontsize=8)
    
    # Adjust spacing to optimize layout (matching Section 4.2)
    plt.tight_layout(pad=3.0)
    plt.subplots_adjust(hspace=0.35, wspace=0.25, top=0.92, left=0.1, right=0.95, bottom=0.05)
    plt.suptitle("Location-Based Analysis - Market Distribution and Pricing", fontsize=18, y=0.98)
    plt.show()
    
    # Calculate and print business insights related to location
    print("\n=== LOCATION-BASED BUSINESS INSIGHTS ===")
    
    # 1. Identify highest value neighborhoods (price/rating ratio)
    neighborhood_metrics = df.groupby('Neighbourhood').agg({
        'Price': ['mean', 'median', 'std'],
        'Review Scores Rating': 'mean',
        'Number Of Reviews': 'mean',
        'Host Id': 'count'
    })
    
    # Flatten multi-level column index
    neighborhood_metrics.columns = ['Avg_Price', 'Median_Price', 'Price_Std', 'Avg_Rating', 'Avg_Reviews', 'Listing_Count']
    
    # Calculate market share for each neighborhood
    total_listings = len(df)
    
    # Calculate market share percentages
    # First calculate exact values, then round for display
    exact_market_shares = (neighborhood_metrics['Listing_Count'] / total_listings * 100)
    neighborhood_metrics['Market_Share'] = exact_market_shares.round(1)
    
    # Calculate price premium vs market average
    neighborhood_metrics['Price_Premium'] = ((neighborhood_metrics['Avg_Price'] / df['Price'].mean() - 1) * 100).round(1)
    
    # Calculate value score (rating / price ratio - higher means better value)
    neighborhood_metrics['Value_Score'] = neighborhood_metrics['Avg_Rating'] / neighborhood_metrics['Avg_Price']
    
    # Filter to neighborhoods with at least 5 listings
    popular_neighborhoods = neighborhood_metrics[neighborhood_metrics['Listing_Count'] >= 5]
    
    # Top 5 highest priced neighborhoods
    top_price_neighborhoods = popular_neighborhoods.sort_values('Avg_Price', ascending=False).head(5)
    print("• Top 5 Premium Neighborhoods (highest average price):")
    for idx, row in top_price_neighborhoods.iterrows():
        print(f"  - {idx}: ${row['Avg_Price']:.0f}/night ({row['Price_Premium']:+.1f}% vs. market), Rating: {row['Avg_Rating']:.1f}/100, {row['Market_Share']}% market share")
    
    # Top 5 highest rated neighborhoods
    top_rated_neighborhoods = popular_neighborhoods.sort_values('Avg_Rating', ascending=False).head(5)
    print("\n• Top 5 Highest Rated Neighborhoods:")
    for idx, row in top_rated_neighborhoods.iterrows():
        print(f"  - {idx}: {row['Avg_Rating']:.1f}/100, ${row['Avg_Price']:.0f}/night ({row['Price_Premium']:+.1f}% vs. market), {row['Market_Share']}% market share")
    
    # Top 5 best value neighborhoods (high rating/price ratio)
    top_value_neighborhoods = popular_neighborhoods.sort_values('Value_Score', ascending=False).head(5)
    print("\n• Top 5 Best Value Neighborhoods (highest rating-to-price ratio):")
    for idx, row in top_value_neighborhoods.iterrows():
        print(f"  - {idx}: Rating {row['Avg_Rating']:.1f}/100 at ${row['Avg_Price']:.0f}/night, {row['Market_Share']}% market share")
    
    # Most popular neighborhoods by listing count
    top_market_neighborhoods = popular_neighborhoods.sort_values('Listing_Count', ascending=False).head(5)
    print("\n• Top 5 Market Leaders (highest listing count):")
    for idx, row in top_market_neighborhoods.iterrows():
        print(f"  - {idx}: {int(row['Listing_Count'])} listings ({row['Market_Share']}% market share), ${row['Avg_Price']:.0f}/night, Rating: {row['Avg_Rating']:.1f}/100")
    
    # Identify potential investment opportunities (high ratings but below average prices)
    avg_price = df['Price'].mean()
    opportunity_neighborhoods = popular_neighborhoods[(popular_neighborhoods['Avg_Rating'] > 85) & (popular_neighborhoods['Avg_Price'] < avg_price)].sort_values('Avg_Rating', ascending=False)
    
    if not opportunity_neighborhoods.empty:
        print("\n• Investment Opportunity Neighborhoods (high ratings but below average prices):")
        for idx, row in opportunity_neighborhoods.head(5).iterrows():
            value_percent = ((avg_price - row['Avg_Price']) / avg_price) * 100
            print(f"  - {idx}: Rating {row['Avg_Rating']:.1f}/100, ${row['Avg_Price']:.0f}/night ({value_percent:.1f}% below market avg), {row['Listing_Count']} listings")
    
    # Market saturation analysis
    # Use the sorted values to get exact top 5 neighborhoods
    top_neighborhoods = neighborhood_metrics.sort_values('Listing_Count', ascending=False).head(5)
    
    # Calculate the exact concentration using the raw listing counts for accuracy
    top_concentration = (top_neighborhoods['Listing_Count'].sum() / total_listings * 100)
    print(f"\n• Market Concentration: Top 5 neighborhoods contain {top_concentration:.1f}% of all listings")
    
    # Price volatility by neighborhood
    top_price_volatility = neighborhood_metrics.sort_values('Price_Std', ascending=False).head(5)
    print("\n• Price Volatility by Neighborhood (highest standard deviation):")
    for idx, row in top_price_volatility.iterrows():
        cv = (row['Price_Std'] / row['Avg_Price'] * 100).round(1)  # coefficient of variation
        print(f"  - {idx}: Std Dev ${row['Price_Std']:.0f} (±{cv}% variation), Avg ${row['Avg_Price']:.0f}/night, {row['Listing_Count']} listings")
        
    # Create a Zipcode-Neighborhood mapping for better geographical understanding
    print("\n=== ZIPCODE TO NEIGHBORHOOD MAPPING ===")
    
    # Create a mapping between zipcodes and neighborhoods
    zipcode_neighborhood_map = df.groupby(['Zipcode', 'Neighbourhood']).size().reset_index()
    zipcode_neighborhood_map.columns = ['Zipcode', 'Neighbourhood', 'Count']
    
    # For each zipcode, show which neighborhoods it contains
    zipcode_groups = zipcode_neighborhood_map.groupby('Zipcode')
    
    # Show the top zipcodes and their neighborhoods
    top_zipcodes_to_display = df['Zipcode'].value_counts().nlargest(10).index
    
    for zipcode in top_zipcodes_to_display:
        neighborhoods_in_zipcode = zipcode_neighborhood_map[zipcode_neighborhood_map['Zipcode'] == zipcode].sort_values('Count', ascending=False)
        
        total_listings = neighborhoods_in_zipcode['Count'].sum()
        print(f"\n• Zipcode {zipcode} ({total_listings} total listings):")
        
        for _, row in neighborhoods_in_zipcode.iterrows():
            percentage = (row['Count'] / total_listings) * 100
            print(f"  - {row['Neighbourhood']}: {row['Count']} listings ({percentage:.1f}% of zipcode)")
    
    
else:
    print('No data loaded to analyze location-based relationships.')

# =============================================================================
# 5.2 Property Characteristics Analysis
# =============================================================================
# 
# NOTE: After analysis in Section 4, we found that Property Type, Room Type, and Beds variables
# don't have enough variety for meaningful bivariate analysis (one category represents >60% of the data).
# Therefore, we're excluding them from this section and will focus on more diverse variables in future analyses.
#
# Business Focus: Understanding pricing determinants and market segments

# # Write your code for property characteristics analysis below:
# if df is not None:
#     # Set up figure for property characteristics analysis
#     plt.figure(figsize=(15, 7))
    
#     # Alternative analysis: Review Score by Superhost Status
#     plt.subplot(1, 2, 1)
#     sns.boxplot(x='Host Is Superhost', y='Review Scores Rating', data=df)
#     plt.title('Rating Distribution by Superhost Status')
#     plt.xlabel('Superhost Status')
#     plt.ylabel('Review Scores Rating')
#     plt.grid(True, alpha=0.3)
    
#     # Alternative analysis: Price by Superhost Status
#     plt.subplot(1, 2, 2)
#     sns.boxplot(x='Host Is Superhost', y='Price', data=df)
#     plt.title('Price Distribution by Superhost Status')
#     plt.xlabel('Superhost Status')
#     plt.ylabel('Price ($)')
#     plt.grid(True, alpha=0.3)
    
#     plt.tight_layout()
#     plt.suptitle("Superhost Analysis", fontsize=16, y=1.02)
#     plt.show()
    
#     # Additional interesting relationship: Accommodates vs Price
#     plt.subplot(2, 2, 4)
#     sns.barplot(x='Room Type', y='Review Scores Rating', data=df)
#     plt.title('Average Rating by Room Type')
#     plt.ylabel('Review Scores Rating')
#     plt.grid(True, alpha=0.3)
    
#     plt.tight_layout()
#     plt.suptitle("Superhost Analysis", fontsize=16, y=1.02)
#     plt.show()
    
#     # Figure for Accommodates vs Price
#     plt.figure(figsize=(12, 6))
#     sns.boxplot(x='Accommodates', y='Price', data=df[df['Accommodates'] <= 8])
#     plt.title('Price by Accommodation Capacity (up to 8 guests)')
#     plt.xlabel('Number of Guests Accommodated')
#     plt.ylabel('Price ($)')
#     plt.grid(True, alpha=0.3)
#     plt.tight_layout()
#     plt.show()
    
#     # Business insights for alternative characteristics
#     print("\n=== SUPERHOST & ACCOMMODATION BUSINESS INSIGHTS ===")
    
#     # Superhost analysis
#     overall_avg_price = df['Price'].mean()
#     superhost_analysis = df.groupby('Host Is Superhost').agg({
#         'Price': ['mean', 'median', 'count'],
#         'Review Scores Rating': 'mean'
#     })
#     superhost_analysis.columns = ['Avg_Price', 'Median_Price', 'Listing_Count', 'Avg_Rating']
    
#     print("• Superhost Impact Analysis:")
#     for status, row in superhost_analysis.iterrows():
#         price_diff = ((row['Avg_Price'] - overall_avg_price) / overall_avg_price) * 100
#         print(f"  - {'Superhosts' if status else 'Regular hosts'}: ${row['Avg_Price']:.2f} avg price ({price_diff:.1f}% {'premium' if price_diff > 0 else 'discount'})")
#         print(f"    Rating: {row['Avg_Rating']:.1f}/100, Listings: {row['Listing_Count']} ({row['Listing_Count']/len(df)*100:.1f}% of market)")
    
#     # Price by accommodation capacity
#     accom_analysis = df.groupby('Accommodates').agg({
#         'Price': ['mean', 'median', 'count'],
#         'Review Scores Rating': 'mean'
#     }).sort_values('Accommodates')
#     accom_analysis.columns = ['Avg_Price', 'Median_Price', 'Listing_Count', 'Avg_Rating']
    
#     print("\n• Price by Accommodation Capacity:")
#     for guests, row in accom_analysis.head(8).iterrows():
#         price_per_guest = row['Avg_Price'] / guests if guests > 0 else 0
#         print(f"  - {guests} guests: ${row['Avg_Price']:.2f} avg (${price_per_guest:.2f} per guest), {row['Listing_Count']} listings")
    
#     # Calculate price elasticity between accommodation sizes
#     print("\n• Price Elasticity Between Accommodation Sizes:")
#     prev_price = None
#     prev_guests = None
#     for guests, row in accom_analysis.iterrows():
#         if prev_price is not None and prev_guests is not None:
#             price_increase_pct = ((row['Avg_Price'] - prev_price) / prev_price) * 100
#             capacity_increase_pct = ((guests - prev_guests) / prev_guests) * 100
#             if capacity_increase_pct > 0:
#                 elasticity = price_increase_pct / capacity_increase_pct
#                 print(f"  - {prev_guests} → {guests} guests: {price_increase_pct:.1f}% price increase, elasticity: {elasticity:.2f}")
        
#         prev_price = row['Avg_Price']
#         prev_guests = guests
# else:
#     print('No data loaded to analyze property characteristics.')

# =============================================================================
# SECTION 6: ADVANCED ANALYSIS (FUTURE WORK)
# =============================================================================

# This section outlines planned advanced analyses that will be conducted in future iterations
# of this project. These analyses will provide deeper insights into the Airbnb market dynamics.

# Future advanced analysis work items:

# 6.1 Outlier Detection and Handling
# • Use IQR method to identify outliers in price and ratings
# • Analyze characteristics of high-value properties (location, type, amenities)
# • Identify undervalued or overvalued properties
# • Visualize outlier distribution across different property types

# 6.2 Feature Correlations Analysis
# • Create correlation heatmaps for numerical features
# • Analyze main factors influencing price
# • Study relationships between ratings and other variables
# • Extract valuable insights for pricing strategy

# 6.3 Temporal Analysis
# • Analyze the impact of host experience on prices and ratings
# • Categorize hosts by experience level (novice, established, veteran)
# • Investigate the relationship between host experience and revenue potential
# • Identify how experience affects guest satisfaction

# 6.4 Market Segmentation Analysis
# • Create market segments based on price quartiles
# • Analyze characteristics and differences between market segments
# • Study property type distribution across different price points
# • Provide targeted business recommendations for different market segments

# =============================================================================
# SECTION 7: BUSINESS INSIGHTS & RECOMMENDATIONS (FUTURE WORK)
# =============================================================================

# This section will synthesize all findings into actionable business insights and
# recommendations. This represents planned future work that will be completed after
# the advanced analyses are conducted.

# Future business insights and recommendations work:

# 7.1 Key Findings Summary
# • Market Structure Insights: Overall market size, distribution, and concentration
# • Geographical Insights: High-value areas, best value-for-money locations, investment opportunities
# • Price Determinants: Ranking of main variables influencing pricing
# • Property Characteristics Analysis: Market performance by property and room types
# • Customer Satisfaction Analysis: Key factors affecting ratings

# 7.2 Business Recommendations
# • For Property Investors: Investment locations, property types, expected returns
# • For Current Hosts: Price optimization, amenity improvements, rating enhancement
# • For Airbnb Platform: Market expansion, host education, dynamic pricing
# • For Travelers: Best value accommodations, premium options, budget choices

# 7.3 Market Opportunities
# • Underdeveloped Markets: Areas with high ratings but limited supply
# • Price Optimization Opportunities: Listings with significant price differences from similar properties
# • Differentiation Strategies: Unique selling points for different property types and locations
# • Seasonal Strategies: Pricing recommendations based on market trends

