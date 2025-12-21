# Import pandas library for data manipulation and analysis
import pandas as pd

# Prompt the user to enter the file path and remove any surrounding quotes
path = input("Enter file path: ").strip('"')

# Try to open and process the file
try:
    # Open the file in read mode, ignoring encoding errors
    with open(path, "r", errors="ignore") as f:
        # Read all lines, strip whitespace, and filter out empty lines
        lines = [line.strip() for line in f if line.strip()]
    
    # Check if there are any valid lines; if not, print error and exit
    if not lines:
        print("Error: The file is empty or contains no valid lines.")
        exit(1)
    
    # Split each line into a list of values using any whitespace as delimiter
    rows = [line.split() for line in lines]   # split on ANY whitespace
    
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
        # Check if the row has the same number of values as columns
        if len(row) != len(columns):
            print(f"Error: Row has {len(row)} values but expected {len(columns)}. Skipping row: {row}")
            continue
        # Append each value to the corresponding column list
        for col, value in zip(columns, row):
            data[col].append(value)
    
    # Convert the dictionary to a pandas DataFrame for further processing
    df = pd.DataFrame(data)
    # Print success message and display the first few rows of the DataFrame
    print("Data loaded successfully:")
    print(df.head())
    
# Handle the case where the file is not found
except FileNotFoundError:
    print(f"Error: File '{path}' not found.")
# Handle any other exceptions that may occur
except Exception as e:
    print(f"An error occurred: {e}")

        
