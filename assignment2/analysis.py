from __future__ import annotations

from collections import defaultdict
from typing import Dict, List, Tuple, Optional

from .loader import SaleRecord


def total_revenue(records: List[SaleRecord]) -> float:
    """
    Compute total revenue across all sales records.
    """
    return sum(record.revenue for record in records)


def revenue_by_region(records: List[SaleRecord]) -> Dict[str, float]:
    """
    Compute total revenue grouped by sales region.
    """
    revenue = defaultdict(float)

    for record in records:
        revenue[record.region] += record.revenue

    # I am converting here, the defaultdict back to a plain dict for cleaner output
    return dict(revenue)


def top_products_by_revenue(records: List[SaleRecord], n: int = 3) -> List[Tuple[str, float]]:
    """
    Compute the top N products by total revenue.
    """
    revenue_per_product = defaultdict(float)

    for record in records:
        revenue_per_product[record.product] += record.revenue

    # Sort by revenue in descending order, then by product name for stability
    sorted_items = sorted(revenue_per_product.items(), key=lambda kv: (-kv[1], kv[0]))

    return sorted_items[:n]


def monthly_revenue(records: List[SaleRecord]) -> Dict[str, float]:
    """
    Compute total revenue per month.
    """
    revenue = defaultdict(float)

    for record in records:
        month_key = record.date[:7]  # "YYYY-MM"
        revenue[month_key] += record.revenue

    return dict(revenue)


def best_salesperson(records: List[SaleRecord]) -> Optional[Tuple[str, float]]:
    """
    Determine the salesperson with the highest total revenue.
    """
    if not records:
        return None

    revenue_per_person = defaultdict(float)

    for record in records:
        revenue_per_person[record.salesperson] += record.revenue

    # Finding the salesperson with maximum revenue
    name, value = max(revenue_per_person.items(), key=lambda kv: kv[1])

    return name, value

def average_revenue_per_sale(records: list[SaleRecord]) -> float:
    """
    Calculating the average revenue per sale
    """
    if not records:
        return 0.0
    
    return sum(r.revenue for r in records) / len(records)

def revenue_by_product(records: list[SaleRecord]) -> dict[str, float]:
    '''
    Calculating the total revenue by product
    '''
    revenue = defaultdict(float)
    for r in records:
        revenue[r.product] += r.revenue

    return dict(revenue)

def top_salesperson_per_region(records: list[SaleRecord]) -> dict[str, tuple[str, float]]:
    '''
    Finding the top salesperson in every region
    '''
    regions = defaultdict(lambda: defaultdict(float))

    for r in records:
        regions[r.region][r.salesperson] += r.revenue

    result = {}
    for region, sales_dict in regions.items():
        name, value = max(sales_dict.items(), key=lambda kv: kv[1])
        result[region] = (name, value)

    return result

