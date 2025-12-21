# Define a dictionary containing sample sales data for demonstration purposes
# This data includes various attributes for sales transactions
data = {
    # List of dates for each sales transaction (50 entries)
    "Date": [
        "2025-01-01","2025-01-02","2025-01-03","2025-01-04","2025-01-05",
        "2025-01-06","2025-01-07","2025-01-08","2025-01-09","2025-01-10",
        "2025-01-11","2025-01-12","2025-01-13","2025-01-14","2025-01-15",
        "2025-01-16","2025-01-17","2025-01-18","2025-01-19","2025-01-20",
        "2025-01-21","2025-01-22","2025-01-23","2025-01-24","2025-01-25",
        "2025-01-26","2025-01-27","2025-01-28","2025-01-29","2025-01-30",
        "2025-01-31","2025-02-01","2025-02-02","2025-02-03","2025-02-04",
        "2025-02-05","2025-02-06","2025-02-07","2025-02-08","2025-02-09",
        "2025-02-10","2025-02-11","2025-02-12","2025-02-13","2025-02-14",
        "2025-02-15","2025-02-16","2025-02-17","2025-02-18","2025-02-19"
    ],
    # List of products sold in each transaction (50 entries)
    "Product": [
        "Laptop","Phone","Tablet","Monitor","Laptop","Phone","Tablet","Monitor","Laptop","Phone",
        "Tablet","Monitor","Laptop","Phone","Tablet","Monitor","Laptop","Phone","Tablet","Monitor",
        "Laptop","Phone","Tablet","Monitor","Laptop","Phone","Tablet","Monitor","Laptop","Phone",
        "Tablet","Laptop","Phone","Tablet","Monitor","Laptop","Phone","Tablet","Monitor","Laptop",
        "Phone","Tablet","Monitor","Laptop","Phone","Tablet","Monitor","Laptop","Phone","Tablet"
    ],
    # List of units sold for each transaction (50 entries)
    "Units_Sold": [
        12,28,15,13,10,24,18,14,13,26,17,15,11,25,19,13,14,27,16,14,
        12,25,17,15,10,24,18,13,12,26,16,14,28,17,15,13,27,19,14,13,
        25,16,14,12,26,18,15,14,27,17
    ],
    # List of price per unit for each product (50 entries)
    "Price_per_Unit": [
        950,620,400,310,960,630,395,315,940,610,405,320,970,640,390,305,950,615,410,300,
        960,625,395,310,945,605,400,325,950,620,385,960,630,405,315,940,610,400,305,950,
        625,410,320,960,615,395,310,945,605,400
    ],
    # List of regions where sales occurred (50 entries)
    "Region": [
        "North","South","East","West","North","South","East","West","North","South",
        "East","West","North","South","East","West","North","South","East","West",
        "North","South","East","West","North","South","East","West","North","South",
        "East","North","South","East","West","North","South","East","West","North",
        "South","East","West","North","South","East","West","North","South","East"
    ],
    # List of salespeople involved in each transaction (50 entries)
    "Salesperson": [
        "Alice","Brian","Chloe","David","Ella","Frank","Grace","Hannah","Ian","Jade",
        "Kyle","Liam","Mia","Noah","Olivia","Paul","Quinn","Ryan","Sophie","Tom",
        "Uma","Victor","Will","Xenia","Yara","Zane","Ava","Ben","Cara","Dean",
        "Ella","Alice","Brian","Chloe","David","Ella","Frank","Grace","Hannah","Ian",
        "Jade","Kyle","Liam","Mia","Noah","Olivia","Paul","Quinn","Ryan","Sophie"
    ],
    # List of customer types for each transaction (50 entries)
    "Customer_Type": [
        "Retail","Corporate","Retail","Corporate","Retail","Corporate","Retail","Corporate","Corporate","Retail",
        "Retail","Corporate","Retail","Corporate","Retail","Corporate","Corporate","Retail","Retail","Corporate",
        "Retail","Corporate","Retail","Corporate","Retail","Corporate","Retail","Corporate","Retail","Corporate",
        "Retail","Retail","Corporate","Retail","Corporate","Retail","Corporate","Retail","Corporate","Corporate",
        "Retail","Retail","Corporate","Retail","Corporate","Retail","Corporate","Retail","Corporate","Retail"
    ],
    # List of payment methods used for each transaction (50 entries)
    "Payment_Method": [
        "Card","Online","Cash","Online","Card","Cash","Online","Card","Online","Cash",
        "Card","Online","Card","Online","Cash","Card","Cash","Online","Card","Online",
        "Card","Cash","Online","Card","Online","Cash","Card","Online","Card","Cash",
        "Online","Card","Online","Cash","Online","Card","Cash","Online","Card","Online",
        "Cash","Card","Online","Card","Cash","Online","Card","Online","Cash","Card"
    ],
    # List of discount percentages applied to each transaction (50 entries)
    "Discount": [
        5,10,0,8,6,5,12,4,7,9,0,10,6,5,8,4,5,10,6,7,
        5,9,0,8,6,5,10,4,7,6,5,5,10,8,6,5,12,4,7,6,
        5,10,4,7,6,5,12,4,7,5
    ],
    # List of revenue generated from each transaction (50 entries)
    "Revenue": [
        11400,17360,6000,4030,9600,15120,7110,4410,12220,15860,
        6855,4800,10670,16000,7410,3965,13300,16605,6560,4200,
        11520,15625,6715,4650,9450,14520,7200,4225,11400,16120,
        6160,26640,10710,6090,4030,12720,11550,7600,5600,3950,
        15500,10250,5740,9600,15625,7410,5980,13320,10900,6800
    ],
    # List of profit generated from each transaction (50 entries)
    "Profit": [
        10830.0,15624.0,6000.0,3707.6,9024.0,14364.0,6256.8,4233.6,11346.0,14425.4,
        6855.0,4320.0,10014.8,15200.0,6813.0,3805.4,11935.0,14944.5,6160.0,3900.0,
        10944.0,14156.25,6715.0,4278.0,8883.0,13794.0,6480.0,4065.0,10830.0,14516.0,
        6160.0,23976.0,9645.0,5781.0,3707.6,11184.0,10710.0,6840.0,5040.0,3550.0,
        13950.0,9225.0,5156.0,9120.0,14062.5,6813.0,5381.0,11988.0,10350.0,6460.0
    ]
}

# Note: This is sample data; any data can be used, not just this.
