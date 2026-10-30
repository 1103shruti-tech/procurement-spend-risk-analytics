# Procurement Spend and Vendor Risk Analytics

## Project Overview
An end-to-end procurement analytics project focused on analyzing purchase order spend, monitoring vendor activity, and identifying invoice exceptions and duplicate records.

The project uses synthetic Procure-to-Pay (P2P) data to demonstrate how data analytics can support procurement operations, financial controls, and vendor risk monitoring.

## Business Objectives
- Analyze procurement spend across vendors.
- Identify high-spend vendors.
- Detect invoice amounts exceeding purchase order amounts.
- Identify duplicate invoice records.
- Support invoice exception review and procurement controls.

## Tools and Technologies
- **Python:** Data generation, data cleaning, and analysis.
- **SQL (SQLite):** Data querying and exception analysis.
- **Tableau Public:** Interactive dashboard and data visualization.
- **Excel:** Initial data exploration.
- **Draw.io:** Procure-to-Pay process mapping.

## Dataset
The project uses synthetic procurement datasets:

| Dataset | Records |
|---|---:|
| Vendors | 20 |
| Purchase Orders | 500 |
| Receipts | 500 |
| Invoices | 510 |
| Payments | 510 |

## Key Findings
- Total purchase order spend: 12,744,797 (currency not specified).
- Highest-spend vendor: V003, with 983,439 across 34 purchase orders.
- 15 invoices flagged where invoice amounts exceeded purchase order amounts.
- 10 duplicated invoice IDs identified, each appearing twice.

These findings represent review flags in synthetic data and do not establish fraud or actual vendor misconduct.

## Tableau Dashboard
The dashboard includes:
- Invoice exception KPI showing 15 flagged invoices.
- Vendor spend analysis.
- Vendor-wise invoice amount discrepancy analysis.

**[View Interactive Tableau Dashboard](https://public.tableau.com/app/profile/shruti.mishra3540/viz/Procurement_Spend_Risk_Analytics/Dashboard1)**

## Project Structure
- `data/` – Raw and processed datasets.
- `python/` – Data generation and analysis scripts.
- `sql/` – SQL queries and SQLite database.
- `tableau/` – Tableau workbook files.
- `process/` – Procure-to-Pay process map.
- `docs/` – Project worklog.
- `alteryx/` – Reserved for future Alteryx materials.
## Business Value
This project demonstrates how procurement data can be transformed into actionable insights to improve spend visibility, identify invoice exceptions, and strengthen financial review processes.

## Data Disclaimer
All datasets are synthetically generated for learning and portfolio demonstration purposes. They do not represent actual company, supplier, or transaction records.# procurement-spend-risk-analytics
Procurement spend, vendor risk, anomaly detection and GenAI analytics portfolio project.
