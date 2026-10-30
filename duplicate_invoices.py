
from pathlib import Path
import pandas as pd

project_folder = Path(__file__).resolve().parent.parent
raw_folder = project_folder / "data" / "raw"
processed_folder = project_folder / "data" / "processed"
processed_folder.mkdir(parents=True, exist_ok=True)

# Load invoice data
invoices = pd.read_csv(raw_folder / "invoices.csv")

# Find invoice IDs that appear more than once
duplicate_rows = invoices[
    invoices.duplicated(subset=["invoice_id"], keep=False)
].sort_values("invoice_id")

# Save duplicate records for review
output_file = processed_folder / "duplicate_invoices.csv"
duplicate_rows.to_csv(output_file, index=False)

print("DUPLICATE INVOICE ANALYSIS")
print(f"Total invoice records: {len(invoices)}")
print(f"Duplicate invoice rows flagged: {len(duplicate_rows)}")
print(f"Unique invoice IDs duplicated: {duplicate_rows['invoice_id'].nunique()}")
print(f"Results saved to: {output_file}")

print("\nDuplicate records:")
if duplicate_rows.empty:
    print("No duplicate invoice IDs found.")
else:
    print(duplicate_rows.to_string(index=False))
