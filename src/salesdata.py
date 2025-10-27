import pandas as pd

# Read dataset from clipboard or manually save as sales_data.csv
data = {
    "Date": ["2025-01-01", "2025-01-02", "2025-01-03", "2025-01-04", "2025-01-05", "2025-01-06", "2025-01-07", "2025-01-08"],
    "Product": ["Laptop", "Phone", "Tablet", "Monitor", "Laptop", "Phone", "Tablet", "Monitor"],
    "Units_Sold": [10, 25, 15, 12, 8, 20, 18, 14],
    "Price_per_Unit": [900, 600, 400, 300, 950, 620, 390, 310],
    "Region": ["North", "South", "East", "West", "North", "South", "East", "West"]
}

df = pd.DataFrame(data)
print(df)

print(df.describe())

