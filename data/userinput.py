import pandas as pd

path = input("Enter file path: ").strip('"')

try:
    with open(path, "r", errors="ignore") as f:
        lines = [line.strip() for line in f if line.strip()]
    
    if not lines:
        print("Error: The file is empty or contains no valid lines.")
        exit(1)
    
    rows = [line.split() for line in lines]   # split on ANY whitespace
    
    if not rows:
        print("Error: No data rows found after splitting.")
        exit(1)
    
    columns = rows[0]
    data = {col: [] for col in columns}
    for row in rows[1:]:
        for col, value in zip(columns, row):
            data[col].append(value)
    
    # Convert to DataFrame for further processing if needed
    df = pd.DataFrame(data)
    print("Data loaded successfully:")
    print(df.head())
    
except FileNotFoundError:
    print(f"Error: File '{path}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")
        
