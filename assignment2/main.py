from __future__ import annotations
from pathlib import Path

from .loader import load_sales_data
from .analysis import (
    total_revenue,
    revenue_by_region,
    top_products_by_revenue,
    monthly_revenue,
    best_salesperson,
    average_revenue_per_sale,
    revenue_by_product,
    top_salesperson_per_region,
)


def _print_header(title: str) -> None:
    print()
    print("=" * len(title))
    print(title)
    print("=" * len(title))


def _print_dict_table(data: dict[str, float], col1: str, col2: str = "Value") -> None:
    max_key_len = max(len(k) for k in data.keys())
    print(f"{col1:<{max_key_len}}   {col2}")
    print("-" * (max_key_len + 10))
    for k, v in data.items():
        print(f"{k:<{max_key_len}}   {v:,.2f}")


def _print_list_table(items, col1="Item", col2="Value"):
    max_key_len = max(len(k) for k, _ in items)
    print(f"{col1:<{max_key_len}}   {col2}")
    print("-" * (max_key_len + 10))
    for (name, val) in items:
        print(f"{name:<{max_key_len}}   {val:,.2f}")


def _print_region_salesperson_table(data: dict[str, tuple[str, float]]):
    max_region_len = max(len(r) for r in data.keys())
    print(f"{'Region':<{max_region_len}}   Salesperson        Revenue")
    print("-" * (max_region_len + 25))
    for region, (person, revenue) in data.items():
        print(f"{region:<{max_region_len}}   {person:<15}   {revenue:,.2f}")


def run_analysis():
    data_path = Path(__file__).parent / "data" / "sales.csv"
    records = load_sales_data(data_path)

    _print_header("Assignment 2: Sales Data Analysis")

    # Total revenue
    total = total_revenue(records)
    print(f"Total Revenue: {total:,.2f}")

    # Revenue by region
    _print_header("Revenue by Region")
    region_revenue = dict(sorted(revenue_by_region(records).items()))
    _print_dict_table(region_revenue, col1="Region", col2="Revenue")

    # Top 3 products
    _print_header("Top 3 Products by Revenue")
    top_products = top_products_by_revenue(records, n=3)
    _print_list_table(top_products, col1="Product", col2="Revenue")

    # Monthly revenue
    _print_header("Monthly Revenue")
    month_rev = sorted(monthly_revenue(records).items())
    _print_list_table(month_rev, col1="Month", col2="Revenue")

    # Best salesperson
    _print_header("Best Salesperson")
    best = best_salesperson(records)
    if best is None:
        print("No sales found")
    else:
        name, value = best
        print(f"{name} — {value:,.2f}")

    # Average revenue per sale
    _print_header("Average Revenue Per Sale")
    avg = average_revenue_per_sale(records)
    print(f"Average revenue per sale: {avg:,.2f}")

    # Revenue by product
    _print_header("Revenue by Product")
    prod_rev = dict(sorted(revenue_by_product(records).items()))
    _print_dict_table(prod_rev, col1="Product", col2="Revenue")

    # Top salesperson per region
    _print_header("Top Salesperson Per Region")
    region_top = top_salesperson_per_region(records)
    _print_region_salesperson_table(region_top)


if __name__ == "__main__":
    run_analysis()
