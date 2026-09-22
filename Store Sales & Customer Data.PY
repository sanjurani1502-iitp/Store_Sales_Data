import pandas as pd
import numpy as np

# Sample Store Dataset
data = {
    'OrderID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Customer_City': ['Delhi', 'Mumbai', 'Delhi', 'Chennai', 'Delhi', 'Mumbai', None, 'Chennai', 'Delhi', 'Mumbai'],
    'Category': ['Electronics', 'Clothing', 'Electronics', 'Clothing', 'Electronics', 'Furniture', 'Clothing', 'Electronics', 'Clothing', 'Furniture'],
    'Sales_Amount': [15000, 2200, 45000, None, 12000, 8500, 1800, 32000, 2500, 14000],
    'Quantity': [1, 2, 3, 1, 1, 2, 1, 2, 3, 1],
    'Rating': [4.5, 3.8, 4.9, 4.0, np.nan, 3.5, 4.2, 4.8, 3.9, 4.1]
}

df = pd.DataFrame(data)
print("Data Successfully Loaded!")
print(df)

print(df.info())
print(df.isnull().sum())

# 1. Sales_Amount ko median se fill karein
sales_median = df['Sales_Amount'].median()
df['Sales_Amount'].fillna(sales_median, inplace=True)

# 2. Customer_City ko 'Unknown' se fill karein
df['Customer_City'].fillna('Unknown', inplace=True)

# Verification - Cleaning ke baad ka status check karein
print("\n--- Cleaning Ke Baad Dataset ---")
print(df)

Rating_mean = df['Rating'].mean()
df['Rating'].fillna(Rating_mean, inplace=True)

print(df)

Category_summary =df.groupby('Category').agg(
    Total_salees = ('Sales_Amount', 'sum'),
    Average_rating = ('Rating', 'mean'),
)
print("\n--- Category Wise Summary ---")
print(Category_summary)

city_sales = df.groupby('Customer_City')['Sales_Amount'].sum().sort_values(ascending=False)

print("\n--- Revenue By City ---")
print(city_sales)

df['Price_per_unit'] = df['Sales_Amount'] / df['Quantity']

print("\n--- Price Per Unit ---")
print(df[['OrderID', 'Price_per_unit']])