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
         Date Product  Units_Sold  Price_per_Unit Region
0  2025-01-01  Laptop          10             900  North
1  2025-01-02   Phone          25             600  South
...

📈 Descriptive Statistics:
       Units_Sold  Price_per_Unit
count     8.00000        8.000000
mean     15.25000      558.750000
std       5.59362      240.553108
min       8.00000      300.000000
max      25.00000      950.000000
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
