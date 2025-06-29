import pandas as pd
import numpy as np
import os

#Read the Airbnb dataset
Airbnb_df = pd.read_excel(os.path.join("Datasource", "airbnb.xlsx"))
print("=== Dataset retrieve successfully ===")
# Display the shape of the dataset
print(f"Dataset Overview: {Airbnb_df.shape[0]:,} x {Airbnb_df.shape[1]}")
# Display the first few rows of the dataset

# Cleaning the dataset
Airbnb_df = Airbnb_df.dropna(subset=['Host Id', 'Review Scores Rating (bin)', 'Review Scores Rating'])
#Delte "Review Scores Rating (bin)" column
Airbnb_df = Airbnb_df.drop(columns=['Review Scores Rating (bin)'])

Airbnb_df.to_excel(os.path.join("Datasource", "airbnb_clean.xlsx"), index=False)

