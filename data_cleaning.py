import pandas as pd

def clean_sales_data(file_path):
    df = pd.read_csv(file_path)

    # Standardize and fix 'Order Date'
    df['Order Date'] = pd.to_datetime(df['Order Date'].astype(str).str.replace("'", "").str.strip(), errors='coerce')

    # Fill missing values
    df['Customer Name'] = df['Customer Name'].fillna('Unknown')
    df['Quantity'] = df['Quantity'].fillna(0)
    df['Unit Price'] = df['Unit Price'].fillna(0)

    # Calculate Total Revenue if missing or incorrect
    df['Total Revenue'] = df['Quantity'] * df['Unit Price']

    # Remove duplicates
    df = df.drop_duplicates()

    # Remove wrong data (negative values)
    df = df[(df['Quantity'] >= 0) & (df['Unit Price'] >= 0) & (df['Total Revenue'] >= 0)]

    # Drop unnecessary columns
    if 'Order ID' in df.columns:
        df = df.drop(columns=['Order ID'])

    return df

def clean_mine_data(file_path):
    df = pd.read_csv(file_path)

    # Fix 'Date' column format
    df['Date'] = pd.to_datetime(df['Date'].astype(str).str.replace("'", "").str.strip(), errors='coerce')

    # Fill missing values with 0
    df = df.fillna(0)

    # Remove duplicates
    df = df.drop_duplicates()

    # Remove wrong data (e.g., negative numbers)
    for col in ['Pulse', 'Maxpulse', 'Calories']:
        if col in df.columns:
            df = df[df[col] >= 0]

    return df

# File names
sales_input = 'Sales.csv'
mine_input = 'Mine.csv'
sales_output = 'Cleaned_Sales.csv'
mine_output = 'Cleaned_Mine.csv'

# Clean and save
cleaned_sales = clean_sales_data(sales_input)
cleaned_mine = clean_mine_data(mine_input)

cleaned_sales.to_csv(sales_output, index=False)
cleaned_mine.to_csv(mine_output, index=False)

print("✅ Data cleaning completed.")
print(f"→ Saved: {sales_output}")
print(f"→ Saved: {mine_output}")
