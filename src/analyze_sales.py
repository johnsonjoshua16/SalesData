import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import pandas as pd
import matplotlib.pyplot as plt
from data.data import data

def load_sales_data():
    """
    Load or create the sales dataset.

    Returns:
        pd.DataFrame: DataFrame containing sales data.
    """
    return pd.DataFrame(data)

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

def visualize_sales(df: pd.DataFrame, save_path: str = None):
    """
    Create a bar chart showing total revenue per product.

    Args:
        df (pd.DataFrame): Sales dataset.
        save_path (str, optional): File path to save the plot.
    """
    df["Total_Revenue"] = df["Units_Sold"] * df["Price_per_Unit"]
    revenue_summary = df.groupby("Product")["Total_Revenue"].sum().sort_values(ascending=False)

    plt.figure(figsize=(8, 5))
    plt.bar(revenue_summary.index, revenue_summary.values)
    plt.title("💰 Total Revenue by Product")
    plt.xlabel("Product")
    plt.ylabel("Revenue ($)")
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.tight_layout()

    if save_path:
        plt.savefig(save_path)
        print(f"\n✅ Chart saved to {save_path}")
    else:
        plt.show()

if __name__ == "__main__":
    df = load_sales_data()
    analyze_sales(df)
    visualize_sales(df, save_path="../data/revenue_chart.png")
