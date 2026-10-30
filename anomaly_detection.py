import pandas as pd
from pathlib import Path
from sklearn.ensemble import IsolationForest
from sklearn.metrics import precision_score, recall_score

# Project paths
BASE_DIR = Path(__file__).resolve().parent.parent
RAW_DIR = BASE_DIR / "data" / "raw"
PROCESSED_DIR = BASE_DIR / "data" / "processed"
PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

# Load datasets
invoices = pd.read_csv(RAW_DIR / "invoices.csv")
purchase_orders = pd.read_csv(RAW_DIR / "purchase_orders.csv")

# Combine invoices with purchase orders
df = invoices.merge(
    purchase_orders[["po_id", "po_amount"]],
    on="po_id",
    how="left"
)

# Feature engineering
df["amount_difference"] = (
    df["invoice_amount"] - df["po_amount"]
)

df["invoice_to_po_ratio"] = (
    df["invoice_amount"] / df["po_amount"].replace(0, 1)
)

# Identify known test anomalies for evaluation
df["known_anomaly"] = (
    (df["invoice_amount"] > df["po_amount"]) |
    (df["invoice_id"].duplicated(keep=False))
).astype(int)

# Model features
features = df[
    [
        "invoice_amount",
        "po_amount",
        "amount_difference",
        "invoice_to_po_ratio"
    ]
].fillna(0)

# Isolation Forest model
model = IsolationForest(
    n_estimators=100,
    contamination=0.05,
    random_state=42
)

df["model_prediction"] = model.fit_predict(features)

# -1 means anomaly; 1 means normal
df["model_anomaly"] = (
    df["model_prediction"] == -1
).astype(int)

# Model evaluation against injected test flags
precision = precision_score(
    df["known_anomaly"],
    df["model_anomaly"],
    zero_division=0
)

recall = recall_score(
    df["known_anomaly"],
    df["model_anomaly"],
    zero_division=0
)

# Save results
df.to_csv(
    PROCESSED_DIR / "anomaly_detection_results.csv",
    index=False
)

metrics = pd.DataFrame({
    "metric": ["Precision", "Recall", "Known test anomalies",
               "Model flagged anomalies"],
    "value": [
        round(precision, 4),
        round(recall, 4),
        int(df["known_anomaly"].sum()),
        int(df["model_anomaly"].sum())
    ]
})

metrics.to_csv(
    PROCESSED_DIR / "anomaly_detection_metrics.csv",
    index=False
)

print("ANOMALY DETECTION COMPLETED")
print("--------------------------------")
print("Total invoices:", len(df))
print("Known test anomalies:", df["known_anomaly"].sum())
print("Model flagged anomalies:", df["model_anomaly"].sum())
print("Precision:", round(precision, 4))
print("Recall:", round(recall, 4))
print("Output files saved in data/processed/")