# Exploratory Data Analysis (EDA) Workflow for Airbnb Cleaned Dataset

# 1. Import necessary libraries
# (e.g., pandas, numpy, matplotlib, seaborn)
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 2. Load the cleaned Airbnb dataset
# (e.g., read the CSV file generated from the ETL process)
try:
    df = pd.read_csv('Datasource/airbnb_clean.csv')
    print('✅ Airbnb cleaned dataset loaded successfully.')
except Exception as e:
    print(f'❌ Error loading dataset: {e}')
    df = None

# 3. Preview the dataset
# (e.g., use head(), info(), describe() to understand the data)
# Write your code to preview the data below:


# 4. Check for missing values and data types
# (e.g., isnull().sum(), dtypes)
# Write your code to check missing values and types below:


# 5. Univariate analysis
# (e.g., plot distributions of Price, Review Scores Rating, etc.)
# Write your code for univariate plots below:


# 6. Bivariate analysis
# (e.g., analyze relationships between variables, such as Price vs. Neighbourhood)
# Write your code for bivariate analysis below:


# 7. Outlier detection and handling
# (e.g., boxplots, identify extreme values)
# Write your code for outlier analysis below:


# 8. Feature correlations
# (e.g., correlation matrix, heatmap)
# Write your code for correlation analysis below:


# 9. Geographical or categorical analysis
# (e.g., analyze by Neighbourhood, Room Type, Property Type)
# Write your code for categorical/geographical analysis below:


# 10. Summarize findings and next steps
# (e.g., write a summary of key insights and plan for further analysis or modeling)
# Write your summary or notes below:


# 11. Prepare data for modeling
# (e.g., select features, handle categorical variables, split data into train/test sets)
# Write your code for data preparation below:


# 12. Choose and train a model
# (e.g., linear regression, decision tree, random forest, etc.)
# Write your code to define and train the model below:


# 13. Evaluate model performance
# (e.g., use metrics like RMSE, MAE, accuracy, confusion matrix, etc.)
# Write your code to evaluate the model below:


# 14. Interpret results and next steps
# (e.g., analyze feature importance, discuss findings, plan for model improvement)
# Write your interpretation and notes below:

