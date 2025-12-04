from assignment2.loader import SaleRecord
from assignment2.analysis import (
    total_revenue,
    revenue_by_region,
    top_products_by_revenue,
    monthly_revenue,
    best_salesperson,
)


def _sample_records():
    return [
        SaleRecord(1, "2024-01-01", "North", "Laptop", 2, 1000.0, "Alice"),   # 2000
        SaleRecord(2, "2024-01-02", "North", "Mouse", 5, 20.0, "Bob"),        # 100
        SaleRecord(3, "2024-02-01", "West", "Laptop", 1, 900.0, "Alice"),     # 900
        SaleRecord(4, "2024-02-03", "West", "Tablet", 3, 300.0, "Charlie"),   # 900
        SaleRecord(5, "2024-02-10", "East", "Mouse", 10, 15.0, "Bob"),        # 150
    ]


def test_total_revenue():
    records = _sample_records()
    assert total_revenue(records) == 4050.0


def test_revenue_by_region():
    records = _sample_records()
    result = revenue_by_region(records)

    assert result["North"] == 2100.0  # 2000 + 100
    assert result["West"] == 1800.0   # 900 + 900
    assert result["East"] == 150.0
    assert len(result) == 3


def test_top_products_by_revenue():
    records = _sample_records()
    top_two = top_products_by_revenue(records, n=2)

    assert top_two[0] == ("Laptop", 2900.0)  # 2000 + 900
    assert top_two[1] == ("Tablet", 900.0)


def test_monthly_revenue():
    records = _sample_records()
    result = monthly_revenue(records)

    assert result["2024-01"] == 2100.0
    assert result["2024-02"] == 1950.0
    assert len(result) == 2


def test_best_salesperson():
    records = _sample_records()
    name, value = best_salesperson(records)

    assert name == "Alice"
    assert value == 2900.0


def test_best_salesperson_empty():
    assert best_salesperson([]) is None
