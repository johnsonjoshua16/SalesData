import sys
import os
sys.path.append(os.path.dirname(__file__) + "/..")
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def parsedata(data):
    # Compute Revenue and Profit
    df = pd.DataFrame(data)
    df["Revenue"] = df["Units_Sold"] * df["Price_per_Unit"]
    df["Profit"] = df["Revenue"] * (1 - df["Discount"]/100)

    summary = df.describe()
    print(summary)

    print("📊 Sales Data:")

    # Print sales data in the specified format
    for index, row in df.iterrows():
        print(f"  - Date: \"{row['Date']}\"")
        print(f"    Product: \"{row['Product']}\"")
        print(f"    Units_Sold: {row['Units_Sold']}")
        print(f"    Revenue: {int(row['Revenue'])}")
        print(f"    Profit: {row['Profit']}")

    print("\n-----------------------------------------")
    print("\nSummary:")
    print(f"  Total_Sales: {int(df['Revenue'].sum())}")
    print(f"  Average_Profit: {df['Profit'].mean():.1f}")
    print(f"  Best_Selling_Product: \"{df.groupby('Product')['Units_Sold'].sum().idxmax()}\"")
    print(f"  Top_Region: \"{df.groupby('Region')['Revenue'].sum().idxmax()}\"")
    sns.lineplot(data=df, x="Date", y="Revenue", hue="Product")
    plt.title("Revenue Over Time by Product")
    plt.xlabel("Date")
    plt.ylabel("Revenue")
    plt.legend(title="Product")
    plt.show()
    
def pdata(data):
    # Compute Revenue and Profit
    df = pd.DataFrame(data)
    df["Revenue"] = df["Units_Sold"] * df["Price_per_Unit"]
    df["Profit"] = df["Revenue"] * (1 - df["Discount"]/100)

    summary = df.describe()
    print(summary)

    print("📊 Sales Data:")

    # Print sales data in the specified format
    for index, row in df.iterrows():
        print(f"  - Date: \"{row['Date']}\"")
        print(f"    Product: \"{row['Product']}\"")
        print(f"    Units_Sold: {row['Units_Sold']}")
        print(f"    Revenue: {int(row['Revenue'])}")
        print(f"    Profit: {row['Profit']}")

    print("\n-----------------------------------------")
    print("\nSummary:")
    print(f"  Total_Sales: {int(df['Revenue'].sum())}")
    print(f"  Average_Profit: {df['Profit'].mean():.1f}")
    print(f"  Best_Selling_Product: \"{df.groupby('Product')['Units_Sold'].sum().idxmax()}\"")
    print(f"  Top_Region: \"{df.groupby('Region')['Revenue'].sum().idxmax()}\"")
    sns.lineplot(data=df, x="Date", y="Revenue", hue="Product")
    plt.title("Revenue Over Time by Product")
    plt.xlabel("Date")
    plt.ylabel("Revenue")
    plt.legend(title="Product")
    plt.show()
    
    
userinput = input("Enter the sales data file path (or press Enter to use default data): ")
if userinput.strip():
    # Assume the file is a CSV without header, with columns in this order
    column_names = ["Date", "Product", "Units_Sold", "Price_per_Unit", "Region", "Salesperson", "Customer_Type", "Payment_Method", "Discount"]
    df = pd.read_csv(userinput, header=None, names=column_names)
    data = df.to_dict('list')
    parsedata(data)
else:
    from data.data import data
    pdata(data)
       
