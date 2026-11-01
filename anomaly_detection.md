\# Anomaly Detection – Procurement Analytics



\## Objective

Identify unusual invoice transactions using the Isolation Forest machine learning algorithm.



\## Dataset

\- Total invoice records analysed: 510

\- Data source: Synthetic procurement dataset

\- Features used:

&#x20; - Invoice amount

&#x20; - Purchase order amount

&#x20; - Amount difference

&#x20; - Invoice-to-PO ratio



\## Methodology

1\. Combined invoice and purchase order datasets using `po\_id`.

2\. Created amount difference and invoice-to-PO ratio features.

3\. Created synthetic test labels using invoice discrepancies and duplicate invoice IDs.

4\. Applied the Isolation Forest algorithm.

5\. Compared model predictions against synthetic test labels.



\## Model Configuration

\- Algorithm: Isolation Forest

\- Number of estimators: 100

\- Contamination: 5%

\- Random state: 42



\## Preliminary Results



| Metric | Result |

|---|---:|

| Total invoices | 510 |

| Known synthetic test anomalies | 35 |

| Model-flagged anomalies | 25 |

| Precision | 60% |

| Recall | 42.86% |



\## Interpretation

These metrics measure agreement with the rule-based synthetic test labels, not performance against independently verified real-world fraud cases.


\## Limitations

\- The dataset is synthetic and does not represent real company transactions.

\- Test labels are rule-based and combine invoice discrepancies with duplicate invoice IDs.

\- Model performance is preliminary and requires further tuning and validation.

\- An anomaly flag does not establish fraud or wrongdoing.

\- Human review is required before any business decision.



## Output Files
- `anomaly_detection_results.csv`
- `anomaly_detection_metrics.csv`



\## Technology

Python, Pandas, Scikit-learn, Isolation Forest

