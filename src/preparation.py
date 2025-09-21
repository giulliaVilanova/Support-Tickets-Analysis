import pandas as pd
import numpy as np
import os

def run(df: pd.DataFrame, outdir: str):
    os.makedirs(outdir, exist_ok=True)

    numeric_cols = [
        "downtime_min",
        "error_rate_pct",
        "description_length",
        "past_90d_incidents",
        "org_users",
        "customers_affected",
    ]
    for col in numeric_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    for col in ["downtime_min", "error_rate_pct", "description_length"]:
        if col in df.columns:
            median_val = df[col].median(skipna=True)
            df[col] = df[col].fillna(median_val)

    for col in ["region", "industry", "booking_channel", "customer_tier"]:
        if col in df.columns:
            df[col] = df[col].fillna("Unknown")

    if "past_90d_incidents" in df.columns and "org_users" in df.columns:
        incidents = df["past_90d_incidents"].fillna(0)
        users = df["org_users"].fillna(0)
        df["incidents_per_user"] = 0.0
        mask = users > 0
        df.loc[mask, "incidents_per_user"] = incidents[mask] / users[mask]

    impact_flags = ["payment_impact_flag", "security_incident_flag", "data_loss_flag"]
    for c in impact_flags:
        if c in df.columns:
            df[c] = df[c].fillna(0).astype(int)

    flag_series = None
    for c in impact_flags:
        s = df[c] if c in df.columns else 0
        if isinstance(s, pd.Series):
            s = s.astype(int)
        flag_series = s if flag_series is None else (flag_series | s)
    df["critical_impact_flag"] = (flag_series.astype(int) if isinstance(flag_series, pd.Series) else int(flag_series))

    df.to_csv(os.path.join(outdir, "tickets_prepared.csv"), index=False)
    return df