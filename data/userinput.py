path = input("Enter file path: ").strip('"')

with open(path, "r", errors="ignore") as f:
    lines = [line.strip() for line in f if line.strip()]

rows = [line.split() for line in lines]   # split on ANY whitespace