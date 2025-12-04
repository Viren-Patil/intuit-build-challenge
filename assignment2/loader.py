from __future__ import annotations

import csv
from dataclasses import dataclass
from pathlib import Path
from typing import List, Iterable


@dataclass(frozen=True)
class SaleRecord:
    """
    Represents a single sales transaction loaded from the CSV file.
    """

    order_id: int
    date: str
    region: str
    product: str
    quantity: int
    unit_price: float
    salesperson: str

    @property
    def revenue(self) -> float:
        """
        Compute the revenue for this record: quantity times unit price.
        """
        return self.quantity * self.unit_price


def load_sales_data(csv_path: Path | str) -> List[SaleRecord]:
    """
    Load sales data from a CSV file into a list of SaleRecord objects.
    """
    path = Path(csv_path)
    records: List[SaleRecord] = []

    with path.open(mode="r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Convert raw string values to appropriate types.
            record = SaleRecord(
                order_id=int(row["order_id"]),
                date=row["date"],
                region=row["region"],
                product=row["product"],
                quantity=int(row["quantity"]),
                unit_price=float(row["unit_price"]),
                salesperson=row["salesperson"],
            )
            records.append(record)

    return records