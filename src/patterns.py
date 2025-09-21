import pandas as pd
import matplotlib.pyplot as plt
import os

from pandas import pivot


def run(df: pd.DataFrame, outdir: str):
    os.makedirs(outdir, exist_ok=True)

    if "priority" in df.columns and "customer_tier" in df.columns:
        pivot = pd.crosstab(df["priority"], df["customer_tier"], normalize="index")
        pivot.to_csv(os.path.join(outdir, "priority_customer_tier.csv"))

    if "region" in df.columns and "downtime_min" in df.columns:
        region_stats = df.groupby("region")["downtime_min"].mean().sort_values(ascending=False)
        region_stats.to_csv(os.path.join(outdir, "region_downtime_min.csv"))
        region_stats.plot(kind="barh", title="Mean Downtime by region")
        plt.tight_layout()
        plt.savefig(os.path.join(outdir, "region_downtime_min.png"))
        plt.close()