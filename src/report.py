import os
import pandas as pd

def run(df: pd.DataFrame, outdir: str):
    os.makedirs(outdir, exist_ok=True)

    insights = []
    recommendations = []

    if "priority" in df.columns and "downtime_min" in df.columns:
        max_downtime_priority = df.groupby("priority")["downtime_min"].mean().idxmax()
        insights.append(f"Tickets com prioridade '{max_downtime_priority}' têm o maior downtime médio.")

    if "company_size_cat" in df.columns and "priority" in df.columns:
        pivot = pd.crosstab(df["company_size_cat"], df["priority"], normalize="index")
        if "Enterprise" in pivot.index:
            critical_ratio = pivot.loc["Enterprise"].get("critical", 0)
            insights.append(f"Clientes Enterprise têm {critical_ratio:.0%} de tickets críticos.")

    if "region" in df.columns and "downtime_min" in df.columns:
        worst_region = df.groupby("region")["downtime_min"].mean().idxmax()
        insights.append(f"A região com maior downtime médio é '{worst_region}'.")

    recommendations.append("Criar fila de escalonamento automático para tickets com critical_impact_flag.")
    recommendations.append("Focar suporte em regiões com maior downtime e clientes Enterprise.")

    report_path = os.path.join(outdir, "report.txt")
    with open(report_path, "w") as f:
        f.write("=== RELATÓRIO DE INSIGHTS ===\n\n")
        f.write("PRINCIPAIS DESCOBERTAS:\n")
        for i, item in enumerate(insights, start=1):
            f.write(f"{i}. {item}\n")
        f.write("\nRECOMENDAÇÕES:\n")
        for i, rec in enumerate(recommendations, start=1):
            f.write(f"{i}. {rec}\n")

    print(f"Relatório gerado em: {report_path}")
