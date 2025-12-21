# Import sys module to access system-specific parameters and functions
import sys
# Import os module to interact with the operating system
import os
# Append the parent directory to the system path to allow importing modules from there
sys.path.append(os.path.dirname(__file__) + "/..")
# Import pandas for data manipulation and analysis
import pandas as pd
# Import matplotlib.pyplot for creating static, animated, and interactive visualizations
import matplotlib.pyplot as plt
# Import seaborn for statistical data visualization
import seaborn as sns

# Define a function to parse and analyze sales data, including visualization
def parsedata(data):
    # Compute Revenue and Profit
    # Create a DataFrame from the input data dictionary
    df = pd.DataFrame(data)
    # Calculate revenue by multiplying units sold by price per unit
    df["Revenue"] = df["Units_Sold"] * df["Price_per_Unit"]
    # Calculate profit by applying the discount to the revenue
    df["Profit"] = df["Revenue"] * (1 - df["Discount"]/100)

    # Generate descriptive statistics for the DataFrame
    summary = df.describe()
    # Print the summary statistics
    print(summary)

    # Print a header for the sales data section
    print("📊 Sales Data:")

    # Print sales data in the specified format
    # Iterate over each row in the DataFrame
    for index, row in df.iterrows():
        # Print the date for the current row
        print(f"  - Date: \"{row['Date']}\"")
        # Print the product for the current row
        print(f"    Product: \"{row['Product']}\"")
        # Print the units sold for the current row
        print(f"    Units_Sold: {row['Units_Sold']}")
        # Print the revenue for the current row, converted to integer
        print(f"    Revenue: {int(row['Revenue'])}")
        # Print the profit for the current row
        print(f"    Profit: {row['Profit']}")

    # Print a separator line
    print("\n-----------------------------------------")
    # Print a header for the summary section
    print("\nSummary:")
    # Print the total sales by summing all revenue values and converting to integer
    print(f"  Total_Sales: {int(df['Revenue'].sum())}")
    # Print the average profit, formatted to one decimal place
    print(f"  Average_Profit: {df['Profit'].mean():.1f}")
    # Print the best-selling product by finding the product with the maximum total units sold
    print(f"  Best_Selling_Product: \"{df.groupby('Product')['Units_Sold'].sum().idxmax()}\"")
    # Print the top region by finding the region with the maximum total revenue
    print(f"  Top_Region: \"{df.groupby('Region')['Revenue'].sum().idxmax()}\"")
    # Create a line plot showing revenue over time by product using seaborn
    sns.lineplot(data=df, x="Date", y="Revenue", hue="Product")
    # Set the title of the plot
    plt.title("Revenue Over Time by Product")
    # Set the x-axis label
    plt.xlabel("Date")
    # Set the y-axis label
    plt.ylabel("Revenue")
    # Add a legend with the title "Product"
    plt.legend(title="Product")
    # Display the plot
    plt.show()

# Define another function to parse and analyze sales data, similar to parsedata but without visualization
def pdata(data):
    # Compute Revenue and Profit
    # Create a DataFrame from the input data dictionary
    df = pd.DataFrame(data)
    # Calculate revenue by multiplying units sold by price per unit
    df["Revenue"] = df["Units_Sold"] * df["Price_per_Unit"]
    # Calculate profit by applying the discount to the revenue
    df["Profit"] = df["Revenue"] * (1 - df["Discount"]/100)

    # Generate descriptive statistics for the DataFrame
    summary = df.describe()
    # Print the summary statistics
    print(summary)

    # Print a header for the sales data section
    print("📊 Sales Data:")

    # Print sales data in the specified format
    # Iterate over each row in the DataFrame
    for index, row in df.iterrows():
        # Print the date for the current row
        print(f"  - Date: \"{row['Date']}\"")
        # Print the product for the current row
        print(f"    Product: \"{row['Product']}\"")
        # Print the units sold for the current row
        print(f"    Units_Sold: {row['Units_Sold']}")
        # Print the revenue for the current row, converted to integer
        print(f"    Revenue: {int(row['Revenue'])}")
        # Print the profit for the current row
        print(f"    Profit: {row['Profit']}")

    # Print a separator line
    print("\n-----------------------------------------")
    # Print a header for the summary section
    print("\nSummary:")
    # Print the total sales by summing all revenue values and converting to integer
    print(f"  Total_Sales: {int(df['Revenue'].sum())}")
    # Print the average profit, formatted to one decimal place
    print(f"  Average_Profit: {df['Profit'].mean():.1f}")
    # Print the best-selling product by finding the product with the maximum total units sold
    print(f"  Best_Selling_Product: \"{df.groupby('Product')['Units_Sold'].sum().idxmax()}\"")
    # Print the top region by finding the region with the maximum total revenue
    print(f"  Top_Region: \"{df.groupby('Region')['Revenue'].sum().idxmax()}\"")
    # Create a line plot showing revenue over time by product using seaborn
    sns.lineplot(data=df, x="Date", y="Revenue", hue="Product")
    # Set the title of the plot
    plt.title("Revenue Over Time by Product")
    # Set the x-axis label
    plt.xlabel("Date")
    # Set the y-axis label
    plt.ylabel("Revenue")
    # Add a legend with the title "Product"
    plt.legend(title="Product")
    # Display the plot
    plt.show()

# Prompt the user to enter the sales data file path or press Enter to use default data
userinput = input("Enter the sales data file path (or press Enter to use default data): ")
# Check if the user provided a non-empty input
if userinput.strip():
    # Import the userinput module to process the file
    import data.userinput as ui
else:
    # Import the default data
    from data.data import data
    # Call the pdata function with the default data
    pdata(data)
       
