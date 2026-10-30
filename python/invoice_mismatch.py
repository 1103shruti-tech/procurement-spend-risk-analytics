
from pathlib import Path
import pandas as pd

project_folder = Path(__file__).resolve().parent.parent
raw_folder = project_folder / "data" / "raw"
processed_folder = project_folder / "data" / "processed"
processed_folder.mkdir(parents=True, exist_ok=True)

# Load invoices and purchase orders
invoices = pd.read_csv(raw_folder / "invoices.csv")
purchase_orders = pd.read_csv(raw_folder / "purchase_orders.csv")

# Match each invoice to its purchase order
comparison = invoices.merge(
    purchase_orders[["po_id", "po_amount"]],
    on="po_id",
    how="left"
)

# Calculate the difference between invoice and PO amounts
comparison["amount_difference"] = (
    comparison["invoice_amount"] - comparison["po_amount"]
).round(2)

# Flag invoices that exceed the PO amount
comparison["review_required"] = (
    comparison["invoice_amount"] > comparison["po_amount"]
)

# Save all invoice comparisons
output_file = processed_folder / "invoice_mismatch.csv"
comparison.to_csv(output_file, index=False)

print("INVOICE MISMATCH ANALYSIS")
print(f"Total invoices checked: {len(comparison)}")
print(f"Invoices requiring review: {comparison['review_required'].sum()}")
print(f"Results saved to: {output_file}")

print("\nSample invoices requiring review:")
print(
    comparison[comparison["review_required"]][
        ["invoice_id", "po_id", "invoice_amount", "po_amount", "amount_difference"]
    ].head(10).to_string(index=False)
)
