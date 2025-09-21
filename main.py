import logging
from src import exploration, preparation, patterns, insights, report

logger = logging.getLogger(__name__)

def main():
    # Configuração básica de logging (nível INFO). Ajuste para DEBUG se quiser mais detalhes.
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    data_path = "data/support_tickets.csv"
    outdir = "outputs/"

    logger.info("Iniciando pipeline")
    logger.info("Parâmetros: data_path=%s, outdir=%s", data_path, outdir)

    logger.info("Carregando dados…")
    df = exploration.load_data(data_path)
    logger.info("Dados carregados: %s linhas x %s colunas", df.shape[0], df.shape[1])

    logger.info("Executando exploração…")
    exploration.run(df, outdir)
    logger.info("Exploração concluída")

    logger.info("Executando preparação…")
    df = preparation.run(df, outdir)
    logger.info("Preparação concluída. Novo shape: %s linhas x %s colunas", df.shape[0], df.shape[1])

    logger.info("Executando análise de padrões…")
    patterns.run(df, outdir)
    logger.info("Análise de padrões concluída")

    logger.info("Gerando insights…")
    insights.run(df, outdir)
    logger.info("Geração de insights concluída")

    logger.info("Gerando report…")
    report.run(df, outdir)  # <- Etapa 4
    logger.info("Geração de report concluída")

    logger.info("Pipeline finalizado com sucesso")

if __name__ == "__main__":
    main()