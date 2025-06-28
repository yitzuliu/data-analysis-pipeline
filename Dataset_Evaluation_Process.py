import pandas as pd
import numpy as np
import os
import warnings

def calculate_data_quality_metrics(df, dataset_name):
    """Calculate comprehensive data quality metrics for a dataset"""
    
    # Basic metrics
    total_rows = df.shape[0]
    total_columns = df.shape[1]
    total_cells = total_rows * total_columns
    
    # Missing data metrics
    missing_cells = df.isnull().sum().sum()
    missing_ratio = missing_cells / total_cells if total_cells > 0 else 0
    completeness_score = (1 - missing_ratio) * 100
    
    # Duplicate analysis
    duplicate_rows = df.duplicated().sum()
    duplicate_ratio = duplicate_rows / total_rows if total_rows > 0 else 0
    uniqueness_score = (1 - duplicate_ratio) * 100
    
    # Data type consistency (numeric vs object columns)
    numeric_cols = len(df.select_dtypes(include=[np.number]).columns)
    object_cols = len(df.select_dtypes(include=['object']).columns)
    datetime_cols = len(df.select_dtypes(include=['datetime64']).columns)
    
    # Overall quality score (weighted average)
    overall_quality = (completeness_score * 0.6 + uniqueness_score * 0.4)
    
    quality_metrics = {
        'dataset_name': dataset_name,
        'total_rows': total_rows,
        'total_columns': total_columns,
        'missing_cells': missing_cells,
        'missing_ratio': missing_ratio,
        'completeness_score': completeness_score,
        'duplicate_rows': duplicate_rows,
        'uniqueness_score': uniqueness_score,
        'numeric_columns': numeric_cols,
        'object_columns': object_cols,
        'datetime_columns': datetime_cols,
        'overall_quality_score': overall_quality
    }
    
    return quality_metrics

def display_quality_metrics(quality_metrics):
    """Display data quality metrics in a formatted way"""
    
    print(f"\n📊 DATA QUALITY METRICS:")
    print(f"  🎯 Completeness Score: {quality_metrics['completeness_score']:.1f}%")
    print(f"  🔄 Uniqueness Score: {quality_metrics['uniqueness_score']:.1f}%")
    print(f"  🏆 Overall Quality Score: {quality_metrics['overall_quality_score']:.1f}%")
    
    if quality_metrics['duplicate_rows'] > 0:
        print(f"  ⚠️  Duplicate rows: {quality_metrics['duplicate_rows']:,}")
    
    # Quality assessment
    score = quality_metrics['overall_quality_score']
    if score >= 90:
        quality_level = "Excellent ⭐⭐⭐"
    elif score >= 75:
        quality_level = "Good ⭐⭐"
    elif score >= 60:
        quality_level = "Fair ⭐"
    else:
        quality_level = "Poor ⚠️"
    
    print(f"  📈 Quality Level: {quality_level}")

# Function to safely load and inspect datasets
def load_and_inspect_dataset(filename, dataset_name):
    """Load dataset and return basic information"""
    try:
        file_path = os.path.join(data_path, filename)
        
        # Load dataset based on file extension
        if filename.endswith('.csv'):
            df = pd.read_csv(file_path)
            
            # Store dataset
            datasets[dataset_name] = df
            
            # Display information for CSV
            display_dataset_info(filename, dataset_name, df=df)
            
        elif filename.endswith('.xlsx') or filename.endswith('.xls'):
            # Load all sheets from Excel file
            excel_file = pd.ExcelFile(file_path)
            sheet_names = excel_file.sheet_names
            
            # Load all sheets into a dictionary
            excel_data = {}
            for sheet_name in sheet_names:
                sheet_df = pd.read_excel(file_path, sheet_name=sheet_name)
                excel_data[sheet_name] = sheet_df
                
                # Store each sheet individually in datasets
                if len(sheet_names) == 1:
                    sheet_key = dataset_name
                else:
                    sheet_key = f"{dataset_name}_{sheet_name}"
                datasets[sheet_key] = sheet_df
            
            # Display comprehensive information for all sheets
            display_dataset_info(filename, dataset_name, excel_data=excel_data)
                
        else:
            return None, f"Unsupported file format for {filename}"
        
        return True, "Success"
        
    except Exception as e:
        return None, f"Error loading {filename}: {str(e)}"

def display_dataset_info(filename, dataset_name, df=None, excel_data=None):
    """Display comprehensive information for a dataset (CSV or Excel with all sheets)"""
    
    print(f"\n{'='*60}")
    print(f"DATASET: {dataset_name.upper()}")
    print(f"{'='*60}")
    print(f"📁 File: {filename}")
    
    # Handle CSV files
    if df is not None and excel_data is None:
        print(f"📋 File Type: CSV")
        print(f"📊 Shape: {df.shape[0]:,} rows × {df.shape[1]} columns")
        print(f"💾 Memory usage: {df.memory_usage(deep=True).sum() / 1024**2:.2f} MB")
        
        print(f"\n📋 Column Names:")
        for i, col in enumerate(df.columns, 1):
            print(f"  {i:2d}. {col}")
        
        print(f"\n🔍 Data Types:")
        print(df.dtypes.value_counts())
        
        # Missing data analysis
        print(f"\n🕳️  Missing Data Analysis:")
        total_cells = df.shape[0] * df.shape[1]
        missing_cells = df.isnull().sum().sum()
        missing_percentage = (missing_cells / total_cells) * 100 if total_cells > 0 else 0
        
        print(f"  • Total missing cells: {missing_cells:,} ({missing_percentage:.1f}%)")
        
        # Missing data by column
        missing_by_column = df.isnull().sum()
        columns_with_missing = missing_by_column[missing_by_column > 0].sort_values(ascending=False)
        
        if len(columns_with_missing) > 0:
            print(f"  • Columns with missing data:")
            for col, missing_count in columns_with_missing.head(5).items():
                col_percentage = (missing_count / df.shape[0]) * 100
                print(f"    - {col}: {missing_count:,} ({col_percentage:.1f}%)")
        else:
            print(f"  • No missing data found! ✅")
        
        # Calculate and display quality metrics for CSV
        quality_metrics = calculate_data_quality_metrics(df, dataset_name)
        display_quality_metrics(quality_metrics)
    
    # Handle Excel files with all sheets
    elif excel_data is not None:
        sheet_names = list(excel_data.keys())
        total_sheets = len(sheet_names)
        print(f"📋 File Type: Excel with {total_sheets} sheet(s)")
        print(f"� Sheet Names: {sheet_names}")
        
        # Calculate total statistics across all sheets
        total_rows = sum(excel_data[sheet].shape[0] for sheet in sheet_names)
        total_memory = sum(excel_data[sheet].memory_usage(deep=True).sum() for sheet in sheet_names) / 1024**2
        
        print(f"📊 Total Data: {total_rows:,} rows across all sheets")
        print(f"💾 Total Memory usage: {total_memory:.2f} MB")
        
        # Display information for each sheet
        for i, sheet_name in enumerate(sheet_names, 1):
            sheet_df = excel_data[sheet_name]
            print(f"\n{'-'*50}")
            print(f"SHEET {i}/{total_sheets}: {sheet_name.upper()}")
            print(f"{'-'*50}")
            print(f"📊 Shape: {sheet_df.shape[0]:,} rows × {sheet_df.shape[1]} columns")
            
            print(f"\n📋 Column Names:")
            for j, col in enumerate(sheet_df.columns, 1):
                print(f"  {j:2d}. {col}")
            
            print(f"\n🔍 Data Types:")
            print(sheet_df.dtypes.value_counts())
            
            # Missing data analysis for each sheet
            print(f"\n🕳️  Missing Data Analysis:")
            total_cells = sheet_df.shape[0] * sheet_df.shape[1]
            missing_cells = sheet_df.isnull().sum().sum()
            missing_percentage = (missing_cells / total_cells) * 100 if total_cells > 0 else 0
            
            print(f"  • Total missing cells: {missing_cells:,} ({missing_percentage:.1f}%)")
            
            # Missing data by column for this sheet
            missing_by_column = sheet_df.isnull().sum()
            columns_with_missing = missing_by_column[missing_by_column > 0].sort_values(ascending=False)
            
            if len(columns_with_missing) > 0:
                print(f"  • Columns with missing data:")
                for col, missing_count in columns_with_missing.head(3).items():
                    col_percentage = (missing_count / sheet_df.shape[0]) * 100
                    print(f"    - {col}: {missing_count:,} ({col_percentage:.1f}%)")
            else:
                print(f"  • No missing data found! ✅")
            
            # Calculate and display quality metrics for each sheet
            sheet_quality_metrics = calculate_data_quality_metrics(sheet_df, f"{dataset_name}_{sheet_name}")
            display_quality_metrics(sheet_quality_metrics)
            
            # Calculate and display quality metrics for CSV
            quality_metrics = calculate_data_quality_metrics(df, dataset_name)
            display_quality_metrics(quality_metrics)

    
# Define data path
data_path = "Datasource/"

# Dictionary to store all datasets
datasets = {}

# count of successfully loaded datasets
count = 0

# Load all datasets from the specified directory
for filename in os.listdir(data_path):
    # Skip temporary files and hidden files
    if filename.startswith('.') or filename.startswith('~$'):
        continue
        
    # Only process supported file types
    if not (filename.endswith('.csv') or filename.endswith('.xlsx') or filename.endswith('.xls')):
        continue
        
    dataset_name = os.path.splitext(filename)[0]
    result, message = load_and_inspect_dataset(filename, dataset_name)
    if result is None:
        print(f"❌ {message}")
    else:
        count += 1
print(f"\n Successfully loaded {count} datasets from the directory '{data_path}'.")


    
