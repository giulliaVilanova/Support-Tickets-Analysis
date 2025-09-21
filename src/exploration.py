import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

def load_data(path):
    # Parse '.' as thousands separator and treat empty strings as NaN.
    # This converts columns like "error_rate_pct" that appear as "5.451.200.538" into integers.
    df = pd.read_csv(path, thousands='.', na_values=['', 'NaN', 'nan'])
    return df

def run(df: pd.DataFrame, outdir: str):
    os.makedirs(outdir, exist_ok=True)

    if "priority" in df.columns:
        pri_counts = df["priority"].value_counts()
        pri_counts.to_csv(os.path.join(outdir, "priority_counts.csv"))

    for col in ["downtime_min", "error_rate_pct", "description_length"]:
        if col in df.columns:
            plt.figure(figsize=(10, 4))
            sns.histplot(df[col], kde=False)
            plt.title(f"Histograma - {col}")
            plt.savefig(os.path.join(outdir, f"{col}_hist.png"))
            plt.close()

    for col in ["region", "industry", "booking_channel", "customer_tier"]:
        if col in df.columns:
            plt.figure(figsize=(10, 4))
            sns.countplot(x=df[col])
            plt.title(f"Countplot - {col}")
            plt.savefig(os.path.join(outdir, f"{col}_countplot.png"))
            plt.close()