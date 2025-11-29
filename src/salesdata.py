import sys
import os
sys.path.append(os.path.dirname(__file__) + "/..")
import pandas as pd
from data.sales_data import data

# Compute Revenue and Profit
df = pd.DataFrame(data)
df["Revenue"] = df["Units_Sold"] * df["Price_per_Unit"]
df["Profit"] = df["Revenue"] * (1 - df["Discount"]/100)

print(df.head())
print(f"Total rows: {len(df)}")

df = pd.DataFrame(data)
print(df)

def analyze_sales(df: pd.DataFrame):
    """
    Perform basic descriptive analysis on sales data.

    Args:
        df (pd.DataFrame): The sales dataset.

    Returns:
        pd.DataFrame: Summary statistics of numeric columns.
    """
    print("\n📊 Sales Data:")
    print(df)
    
    print("\n📈 Descriptive Statistics:")
    summary = df.describe()
    print(summary)
    
    return summary

analyze_sales(df)


