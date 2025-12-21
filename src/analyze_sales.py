# Import sys module to access system-specific parameters and functions
import sys
# Import os module to interact with the operating system
import os
# Append the parent directory to the system path to allow importing modules from there
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

# Import pandas for data manipulation and analysis
import pandas as pd
# Import matplotlib.pyplot for creating static, animated, and interactive visualizations
import matplotlib.pyplot as plt
# Import the data from the data module
from data.data import data

# Define a function to load or create the sales dataset
def load_sales_data():
    """
    Load or create the sales dataset.

    Returns:
        pd.DataFrame: DataFrame containing sales data.
    """
    # Create and return a DataFrame from the imported data
    return pd.DataFrame(data)

# Define a function to perform basic descriptive analysis on sales data
def analyze_sales(df: pd.DataFrame):
    """
    Perform basic descriptive analysis on sales data.

    Args:
        df (pd.DataFrame): The sales dataset.

    Returns:
        pd.DataFrame: Summary statistics of numeric columns.
    """
    # Print a header for the sales data section
    print("\n📊 Sales Data:")
    # Print the entire DataFrame
    print(df)

    # Print a header for the descriptive statistics section
    print("\n📈 Descriptive Statistics:")
    # Generate and print summary statistics for the DataFrame
    summary = df.describe()
    print(summary)

    # Return the summary statistics
    return summary

# Define a function to create a bar chart showing total revenue per product
def visualize_sales(df: pd.DataFrame, save_path: str = None):
    """
    Create a bar chart showing total revenue per product.

    Args:
        df (pd.DataFrame): Sales dataset.
        save_path (str, optional): File path to save the plot.
    """
    # Calculate total revenue for each product by multiplying units sold by price per unit
    df["Total_Revenue"] = df["Units_Sold"] * df["Price_per_Unit"]
    # Group by product, sum the total revenue, and sort in descending order
    revenue_summary = df.groupby("Product")["Total_Revenue"].sum().sort_values(ascending=False)

    # Create a new figure with specified size
    plt.figure(figsize=(8, 5))
    # Create a bar chart with products on x-axis and revenue on y-axis
    plt.bar(revenue_summary.index, revenue_summary.values)
    # Set the title of the chart
    plt.title("💰 Total Revenue by Product")
    # Set the x-axis label
    plt.xlabel("Product")
    # Set the y-axis label
    plt.ylabel("Revenue ($)")
    # Add a grid on the y-axis with dashed lines and transparency
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    # Adjust layout to prevent clipping
    plt.tight_layout()

    # Check if a save path is provided
    if save_path:
        # Save the plot to the specified path
        plt.savefig(save_path)
        # Print confirmation message with the save path
        print(f"\n✅ Chart saved to {save_path}")
    else:
        # Display the plot
        plt.show()

# Check if this script is being run directly (not imported as a module)
if __name__ == "__main__":
    # Load the sales data into a DataFrame
    df = load_sales_data()
    # Perform analysis on the data
    analyze_sales(df)
    # Visualize the data and save the chart to the specified path
    visualize_sales(df, save_path="../data/revenue_chart.png")
