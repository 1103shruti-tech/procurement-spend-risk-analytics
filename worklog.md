# Procurement Spend and Vendor Risk Analytics

## Project Work Log

### October 28, 2026
- Created the GitHub repository.
- Created the local project folder structure.
- Verified Python installation.
- Created a Python virtual environment.
- Installed pandas, NumPy, scikit-learn, and Matplotlib.

## Next Steps
- Learn procurement and procure-to-pay basics.
- Generate synthetic purchase order, receipt, invoice, and payment data.
- Analyze procurement data using SQL and Python.
- Build a Tableau dashboard.
- Develop vendor risk and anomaly detection analyses.

- Created the Procure-to-Pay (P2P) process flow diagram.
- Added invoice matching and discrepancy investigation steps.

- Reviewed the purchase order data in Excel.
- Calculated total purchase order value: 12,744,797.
- Sorted vendor spending to identify the highest-spend vendor.
- Identified vendor V003 as the highest-spend vendor, with 983,439 across 34 orders.

- Checked 510 invoice records for invoice amounts exceeding purchase order amounts.
- Flagged 15 invoices for review due to amount discrepancies; these are review flags, not confirmed fraud.

- Checked invoice records for repeated invoice IDs.
- Identified 10 unique invoice IDs appearing more than once, resulting in 20 rows in the duplicate-invoice review file.
- Duplicate records were flagged for investigation; duplicates alone do not confirm fraud.

- Imported all five raw CSV datasets into a SQLite database.
- Executed SQL vendor spend analysis and verified V003 as the highest-spend vendor, with 983,439 across 34 purchase orders.
- Executed SQL invoice mismatch analysis and identified 15 invoices with invoice amounts exceeding purchase order amounts.
- Executed SQL duplicate invoice analysis and identified 10 duplicated invoice IDs, each appearing twice.
- Ran an overall SQL summary query confirming 20 vendors, 500 purchase orders, and total purchase order spend of 12,744,797.
- Saved four SQL analysis queries in vendor_spend_analysis.sql.

- Updated the Tableau dashboard with an invoice discrepancy KPI showing 15 flagged invoices.
- Added vendor-wise invoice amount discrepancy analysis.
- Improved dashboard layout and sizing for desktop viewing.
- Published the updated Procurement Spend and Vendor Risk Analytics dashboard to Tableau Public.
