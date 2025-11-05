## 🛒 Sales Data 

[![License: MIT](https://img.shields.io/badge/License-MIT-red.svg)](LICENSE)  
[![Status: In Development](https://img.shields.io/badge/Status-in--Development-orange.svg)]()

<p align="center">
- A simple Python project that uses <b>Pandas</b> to analyze sales performance over a given time period. -
</p>

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

📈 Descriptive Statistics:
       Units_Sold  Price_per_Unit   Discount       Revenue        Profit
count   50.000000       50.000000  50.000000     50.000000     50.000000
mean    17.520000      581.100000   6.400000   9821.500000   9070.389000
std      5.511546      249.027271   2.784798   4828.518306   4351.878368
min     10.000000      300.000000   0.000000   3950.000000   3550.000000
25%     13.250000      391.250000   5.000000   6022.500000   5835.750000
50%     15.500000      605.000000   6.000000   9525.000000   8953.500000
75%     22.750000      865.000000   8.000000  13155.000000  11787.750000
max     28.000000      970.000000  12.000000  26640.000000  23976.000000

--------------------------------AND/OR----------------------------------

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
