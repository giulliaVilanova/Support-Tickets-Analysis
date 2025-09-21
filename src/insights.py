import pandas as pd
import os

def run(df: pd.DataFrame, outdir: str):
    insights = []
    recs = []

    if "priority" in df.columns and "downtime_min" in df.columns:
        top = df.groupby("priority")["downtime_min"].mean().idxmax()
        insights.append(f"Priority with highest downtime: {top}")

    if "company_size_cat" in df.columns and "priority" in df.columns:
        pivot = pd.crosstab(df["company_size_cat"], df["priority"], normalize="index")

        if "Enterprise" in pivot.index:
            critical_ratio = pivot.loc["Enterprise"].get("Critical", 0)
            insights.append(f"Critical ratio: {critical_ratio:.2f}")

    if "region" in df.columns and "downtime_min" in df.columns:
        region = df.groupby("region")["downtime_min"].mean().idxmax()
        insights.append(f"Region with highest downtime: {region}")

    recs.append("Create auto escalation rule for tickets with critical_impact_flag.")
    recs.append("Increase support on the regions with the biggest downtime.")

    with open(os.path.join(outdir, "insights.txt"), "w") as f:
        f.write("FINDINGS:\n")
        for i in insights:
            f.write(f"{i}\n")
        f.write("\nRECOMMENDATIONS:\n")
        for r in recs:
            f.write(f" - {r}\n")