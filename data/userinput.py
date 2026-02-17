import pandas as pd
import sys
import os

# Append the parent directory to the system path to allow importing modules from there
sys.path.append(os.path.dirname(__file__) + "/..")


from src.salesdata import parsedata

path = input("Enter file path: ").strip('"') #remove any surrounding quotes

try:
    #read mode, ignoring encoding errors
    with open(path, "r", errors="ignore") as f:
        # Read all lines, strip whitespace, and filter out empty lines
        lines = [line.strip() for line in f if line.strip()]

    if not lines:
        print("Error: The file is empty or contains no valid lines.")
        exit(1)

    rows = [line.split() for line in lines]   # split on *any* whitespace

    # Check if there are any rows after splitting; if not, print error and exit
    if not rows:
        print("Error: No data rows found after splitting.")
        exit(1)

    # Extract the first row as column headers
    columns = rows[0]
    # Initialize a dictionary with column names as keys and empty lists as values
    data = {col: [] for col in columns}
    # Iterate over the remaining rows (data rows)
    for row in rows[1:]:
        if len(row) != len(columns):
            print(f"Error: Row has {len(row)} values but expected {len(columns)}. Skipping row: {row}")
            continue
        # Append each value to the corresponding column list
        for col, value in zip(columns, row):
            data[col].append(value)

    # Call the parsedata function with the loaded data to process and display it
    parsedata(data)

# Handle the case where the file is not found
except FileNotFoundError:
    print(f"Error: File '{path}' not found.")
# Handle any other exceptions that may occur
except Exception as e:
    print(f"An error occurred: {e}")

        
