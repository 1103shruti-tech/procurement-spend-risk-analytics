
from pathlib import Path
import pandas as pd

# Find the project folder and load the purchase order data
project_folder = Path(__file__).resolve().parent.parent
data_file = project_folder / "data" / "raw" / "purchase_orders.csv"

purchase_orders = pd.read_csv(data_file)

# Calculate total spend and number of purchase orders per vendor
vendor_spend = (
    purchase_orders.groupby("vendor_id")
    .agg(
        total_spend=("po_amount", "sum"),
        number_of_orders=("po_id", "count")
    )
    .reset_index()
    .sort_values("total_spend", ascending=False)
)

# Display the top 10 vendors
print("\nTOP 10 VENDORS BY PROCUREMENT SPEND")
print(vendor_spend.head(10).to_string(index=False))

# Save the full results
output_file = project_folder / "data" / "processed" / "vendor_spend.csv"
output_file.parent.mkdir(parents=True, exist_ok=True)
vendor_spend.to_csv(output_file, index=False)

print(f"\nFull results saved to: {output_file}")
