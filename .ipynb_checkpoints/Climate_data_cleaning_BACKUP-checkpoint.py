import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('climate_action_data.csv')

# Data inspection
print("Initial dataset shape:", df.shape)
print("\nData types:\n", df.dtypes)
print("\nMissing values:\n", df.isnull().sum())
print("\nDuplicate rows:", df.duplicated().sum())

# Data cleaning steps
# 1. Replace 'error' entries with NaN
df.replace('error', np.nan, inplace=True)

# 2. Convert numeric columns to appropriate types
numeric_cols = ['Soil_Moisture(%)', 'Soil_pH', 'Temperature(C)', 'Humidity(%)', 
                'Fertilizer_Recommended(kg/ha)', 'Irrigation_Recommended(mm)']
for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# 3. Handle missing dates (drop rows where Date is missing)
df = df.dropna(subset=['Date'])

# 4. Handle missing crop types (fill with 'Unknown' or drop)
df = df.dropna(subset=['Crop_Type'])

# 5. Remove duplicate records
df = df.drop_duplicates()

# 6. For other missing numeric values, fill with column median
for col in numeric_cols:
    df[col] = df[col].fillna(df[col].median())

# Final inspection
print("\nCleaned dataset shape:", df.shape)
print("\nMissing values after cleaning:\n", df.isnull().sum())

# Descriptive statistics
print("Descriptive Statistics:\n", df.describe())

# Crop distribution
print("\nCrop Type Distribution:\n", df['Crop_Type'].value_counts())

# Visualizations
# 1. Distribution of numeric variables
numeric_cols = ['Soil_Moisture(%)', 'Soil_pH', 'Temperature(C)', 'Humidity(%)', 
                'Fertilizer_Recommended(kg/ha)', 'Irrigation_Recommended(mm)']
df[numeric_cols].hist(bins=20, figsize=(12, 10))
plt.tight_layout()
plt.show()

# 2. Correlation heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(df[numeric_cols].corr(), annot=True, cmap='coolwarm', center=0)
plt.title('Correlation Heatmap of Soil and Environmental Variables')
plt.show()

# 3. Crop-wise analysis
crop_stats = df.groupby('Crop_Type')[numeric_cols].mean().sort_values('Soil_Moisture(%)', ascending=False)
print("\nCrop-wise Average Metrics:\n", crop_stats)

# 4. High temperature analysis
high_temp_crops = df[df['Temperature(C)'] > 30]
high_temp_stats = high_temp_crops.groupby('Crop_Type')['Irrigation_Recommended(mm)'].mean()
print("\nIrrigation Recommendations for Crops with Temp > 30°C:\n", high_temp_stats)