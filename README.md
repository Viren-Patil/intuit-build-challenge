# Viren Patil 04/12/2025

# Intuit Build Challenge (Python)

This repository contains my solutions to the Intuit SDE 1 Build Challenge. Each assignment is implemented as an independent module, with a shared test suite.

## Repository Structure

```
intuit_build_challenge/
│
├── assignment1/
│ ├── buffer.py
│ ├── producer.py
│ ├── consumer.py
│ ├── main.py
│ ├── README.md
│
├── assignment2/
│ ├── data/
│ │ └── sales.csv
│ ├── loader.py
│ ├── analysis.py
│ ├── main.py
│ ├── README.md
│
├── tests/
│ ├── test_assignment1_buffer.py
│ ├── test_assignment1_integration.py
│
├── requirements.txt
└── README.md
```


## Assignment 1

Assignment 1 is implemented inside the `assignment1/` folder.  
It covers:

- thread synchronization  
- blocking queue implementation  
- wait and notify mechanism  
- concurrent producer and consumer threads  

Detailed documentation for this assignment is here:

👉 **[assignment1/README.md](assignment1/README.md)**

## Running Assignment 1

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the demo (from the repository root):

```bash
python -m assignment1.main
```

Running Tests:

All tests use pytest. From the repository root:

```bash
pytest
```

---

## Assignment 2

Assignment 2 is implemented inside the `assignment2/` folder.

It focuses on CSV data analysis using pure Python functional programming, without pandas.

The dataset (`sales.csv`) contains 30 rows of realistic sales transactions. The solution demonstrates:

- generator expressions
- lambda based sorting
- grouping using dictionary accumulation
- clean pure functions for analysis
- composable functional transformations
- formatted console reporting

Core Analysis Functions

- total revenue
- revenue by region
- revenue by month
- top products by revenue
- best salesperson

Advanced Analysis

- average revenue per sale
- revenue by product
- top salesperson per region

Detailed documentation for this assignment is here:

👉 **[assignment2/README.md](assignment2/README.md)**

## Running Assignment 2

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the demo (from the repository root):

```bash
python -m assignment2.main
```

Running Tests:

All tests use pytest. From the repository root:

```bash
pytest
```


