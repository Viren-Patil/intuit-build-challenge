# Assignment 2: Sales Data Analysis Using Functional Programming (Python)

This assignment implements a complete analytical workflow for CSV based sales data using **pure Python functional programming techniques**, without relying on external libraries such as pandas.  
All analysis is performed through generator expressions, dictionary accumulation, lambda based sorting, and composable functions that operate on typed data models.

---

## Dataset

The dataset is located at:

`assignment2/data/sales.csv`

It contains **30 rows** of realistic sales transactions with the following schema:

```
| Column       | Description                                |
|--------------|--------------------------------------------|
| order_id     | Unique sale identifier                     |
| date         | ISO format date (YYYY-MM-DD)               |
| region       | Geographical sales region                  |
| product      | Product name                               |
| quantity     | Units sold                                 |
| unit_price   | Price per unit                             |
| salesperson  | Person who executed the transaction        |
```

This dataset is intentionally diverse across products, salespeople, regions, and months so that each analytic query produces meaningful and interpretable output.

---

## File Structure

```
assignment2/
│
├── data/
│ └── sales.csv
│
├── loader.py # Data model + CSV loader
├── analysis.py # Functional programming analysis functions
├── main.py # Console report runner
└── README.md
```


---

## 3. Implementation Overview

### loader.py

Defines:

- `SaleRecord` — a dataclass representing one row of sales data  
- `load_sales_data(path)` — loads all records into memory  
- `iter_sales_data(path)` — a generator based lazy loader

Each `SaleRecord` also includes a computed `revenue` property (`quantity * unit_price`).

---

### analysis.py

Implements fully functional style analytical routines over a list of `SaleRecord` objects.

### Core Analytical Functions

- `total_revenue(records)`  
- `revenue_by_region(records)`  
- `top_products_by_revenue(records, n=3)`  
- `monthly_revenue(records)`  
- `best_salesperson(records)`

These use:

- generator expressions  
- lambdas for key extraction  
- dictionary accumulation  
- functional transformations  
- pure functions (no printing, no side effects)

### Advanced Analysis

- `average_revenue_per_sale(records)`
- `revenue_by_product(records)`
- `top_salesperson_per_region(records)`

---

## Run the analysis (main.py)

Runs the full analysis pipeline:

1. Loads the CSV dataset  
2. Computes all analytics  
3. Formats output into aligned tables  
4. Prints a clean, structured report to the console  

Run with:

```bash
python -m assignment2.main
```

Sample output:

```
===============================
Assignment 2: Sales Data Analysis
===============================
Total Revenue: 68,430.87

=====================
Revenue by Region
=====================
East        13,210.94
North       21,399.00
South       15,582.45
West        18,238.48

...

==================
Revenue by Product
==================
Product    Revenue
------------------
Keyboard   1,341.00
Laptop     9,255.00
Monitor    3,529.97
Mouse      2,561.00
Tablet     5,470.00

==========================
Top Salesperson Per Region
==========================
Region   Salesperson        Revenue
------------------------------
North   Alice             4,120.00
West    Frank             1,780.00
East    Alice             1,860.00
South   Diana             999.97
```

## Testing

Tests are located in the repository level `tests/` directory:

```
tests/
│
├── test_assignment2_loader.py
└── test_assignment2_analysis.py
```

Tests verify:

- CSV parsing correctness
- Field type conversion
- Revenue computation logic
- All analysis functions
- Edge cases (such as empty lists)
- Deterministic results using a controlled sample dataset

Run tests:

```bash
pytest
```