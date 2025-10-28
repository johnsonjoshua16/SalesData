## 🛒 Sales Data Analysis

A simple Python project that uses **Pandas** to analyze sales performance over a given time period.

## 📂 Project Overview
This project demonstrates:
- How to create and load a dataset with Pandas
- How to compute descriptive statistics for sales data
- How to structure small data analysis scripts for GitHub

## 🚀 Features
- Load sales data from a dictionary or CSV file
- Display tabular data
- Generate summary statistics with `pandas.DataFrame.describe()`

## 🧰 Requirements
Install dependencies with:
```bash
pip install -r requirements.txt
```

## ▶️ Usage
Run the script:
```bash
python src/analyze_sales.py
```
Output includes:
- The sales dataset table
- Statistical summary (mean, std, min, max, etc.)

## 📈 Example Output
```yaml
📊 Sales Data:
# Example Output (Sales Data)

SalesData:
  - Date: "2025-01-01"
    Product: "Laptop"
    Units_Sold: 12
    Revenue: 11400
    Profit: 10830.0

  - Date: "2025-01-02"
    Product: "Phone"
    Units_Sold: 28
    Revenue: 17360
    Profit: 15624.0

  - Date: "2025-01-03"
    Product: "Tablet"
    Units_Sold: 15
    Revenue: 6000
    Profit: 6000.0

-----------------------------------------

Summary:
  Total_Sales: 500000
  Average_Profit: 10325.4
  Best_Selling_Product: "Phone"
  Top_Region: "South"


```

## 🧩 Future Improvements

- Add regional performance breakdowns
- Export reports as Excel or PDF
- Build an interactive dashboard with Plotly or Streamlit

## 🧑‍💻 Author
Joshua Johnson — Data Science Trainee & Python Developer


## Contact
Joshua Johnson (@johnsonjoshua16) <br>
Data Science Trainee and Python Developer. <br>
London, UK. <br>
Feel free to open an issue or submit a PR if you'd like to contribute or suggest improvements!
