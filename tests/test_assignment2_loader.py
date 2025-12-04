from pathlib import Path
from assignment2.loader import load_sales_data, SaleRecord


def test_load_sales_data_real_file():
    csv_path = Path("assignment2/data/sales.csv")
    records = load_sales_data(csv_path)

    # Check row count (should be exactly 30)
    assert len(records) == 30

    # Validate first row
    r1 = records[0]
    assert isinstance(r1, SaleRecord)
    assert r1.order_id == 1001
    assert r1.date == "2024-01-05"
    assert r1.region == "North"
    assert r1.product == "Laptop"
    assert r1.quantity == 2
    assert r1.unit_price == 950.00
    assert r1.salesperson == "Alice"
    assert r1.revenue == 2 * 950.00

    # Validate a row from the middle
    r15 = records[14]   # this is order_id 1015
    assert r15.order_id == 1015
    assert r15.product == "Mouse"
    assert r15.revenue == 15 * 18.00

    # Validate last row
    r30 = records[-1]
    assert r30.order_id == 1030
    assert r30.salesperson == "Alice"
    assert r30.revenue == 30 * 21.00
