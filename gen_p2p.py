
from pathlib import Path
import pandas as pd
import numpy as np

# Use the project folder as the base directory
BASE_DIR = Path(__file__).resolve().parent.parent
RAW_DIR = BASE_DIR / "data" / "raw"
RAW_DIR.mkdir(parents=True, exist_ok=True)

rng = np.random.default_rng(42)
n = 500

# Vendor master
vendors = pd.DataFrame({
    "vendor_id": [f"V{i:03d}" for i in range(1, 21)],
    "vendor_name": [f"Vendor {i:02d}" for i in range(1, 21)],
    "category": rng.choice(
        ["IT", "Office Supplies", "Facilities", "Travel"],
        size=20
    ),
    "risk_rating": rng.choice(
        ["Low", "Medium", "High"],
        size=20,
        p=[0.5, 0.35, 0.15]
    )
})

# Purchase orders
po_ids = [f"PO{i:05d}" for i in range(1, n + 1)]
vendor_ids = rng.choice(vendors["vendor_id"], size=n)
amounts = rng.integers(500, 50000, size=n).astype(float)
quantities = rng.integers(1, 101, size=n)

purchase_orders = pd.DataFrame({
    "po_id": po_ids,
    "vendor_id": vendor_ids,
    "po_date": pd.to_datetime(
        rng.choice(pd.date_range("2026-01-01", "2026-09-30"), n)
    ),
    "quantity_ordered": quantities,
    "po_amount": amounts,
    "currency": "INR"
})

# Receipts: normally match the ordered quantity
receipts = purchase_orders[["po_id", "quantity_ordered"]].copy()
receipts = receipts.rename(
    columns={"quantity_ordered": "quantity_received"}
)
receipts["receipt_id"] = [f"GR{i:05d}" for i in range(1, n + 1)]
receipts = receipts[["receipt_id", "po_id", "quantity_received"]]

# Invoices: normally match purchase order amounts
invoices = purchase_orders[["po_id", "vendor_id", "po_amount"]].copy()
invoices = invoices.rename(columns={"po_amount": "invoice_amount"})
invoices["invoice_id"] = [f"INV{i:05d}" for i in range(1, n + 1)]
invoices["invoice_date"] = (
    pd.to_datetime(purchase_orders["po_date"])
    + pd.to_timedelta(rng.integers(1, 15, n), unit="D")
)
invoices = invoices[
    ["invoice_id", "po_id", "vendor_id", "invoice_date", "invoice_amount"]
]

# Inject known issues so we can test detection later
mismatch_rows = rng.choice(n, size=15, replace=False)
invoices.loc[mismatch_rows, "invoice_amount"] *= 1.25

duplicate_invoices = invoices.iloc[:10].copy()
invoices = pd.concat([invoices, duplicate_invoices], ignore_index=True)
# Payments
payments = invoices[["invoice_id", "invoice_amount", "invoice_date"]].copy()
payments = payments.rename(columns={"invoice_amount": "payment_amount"})
payments["payment_id"] = [
    f"PAY{i:05d}" for i in range(1, len(payments) + 1)
]
payments["payment_date"] = (
    pd.to_datetime(payments["invoice_date"])
    + pd.to_timedelta(rng.integers(1, 46, len(payments)), unit="D")
)
payments = payments[
    ["payment_id", "invoice_id", "payment_amount", "payment_date"]
]

# Save all datasets
datasets = {
    "vendors.csv": vendors,
    "purchase_orders.csv": purchase_orders,
    "receipts.csv": receipts,
    "invoices.csv": invoices,
    "payments.csv": payments,
}

for filename, dataframe in datasets.items():
    dataframe.to_csv(RAW_DIR / filename, index=False)

print("Dataset generation complete!")
print(f"Files saved to: {RAW_DIR}")
for filename, dataframe in datasets.items():
    print(f"{filename}: {len(dataframe)} rows")
