# Support-Tickets-Analysis

# 📊 Análise de Tickets de Suporte / Support Tickets Analysis

Este repositório contém uma análise exploratória de **50.000 tickets de
suporte**, com foco em entender padrões de **prioridade** e gerar
**insights para tomada de decisão** sem o uso de IA avançada.

This repository contains an exploratory analysis of **50,000 support
tickets**, focusing on understanding **priority patterns** and
generating **insights for decision-making** without advanced AI.

------------------------------------------------------------------------

## 🗂 Estrutura do Projeto / Project Structure

    .
    ├── data/                 # CSV ou dados brutos / raw dataset
    ├── notebooks/            # Notebooks Jupyter (exploração inicial) / Jupyter notebooks
    ├── src/                  # Código principal / main source code
    │   ├── data_loader.py
    │   ├── preprocessing.py
    │   ├── eda.py
    │   ├── patterns.py
    │   └── report.py
    ├── requirements.txt      # Dependências / dependencies
    └── README.md

------------------------------------------------------------------------

## 🚀 Como Rodar / How to Run

### 🔹 PT-BR

1.  Criar ambiente virtual:

``` bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

2.  Instalar dependências:

``` bash
pip install -r requirements.txt
```

3.  Executar análise:

``` bash
python src/main.py
```

### 🔹 EN

1.  Create a virtual environment:

``` bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

2.  Install dependencies:

``` bash
pip install -r requirements.txt
```

3.  Run the analysis:

``` bash
python src/main.py
```

------------------------------------------------------------------------

## 📈 Etapas / Steps

-   **Exploração dos Dados / Data Exploration** → distribuição de
    prioridades, análise de variáveis numéricas e categóricas.
-   **Preparação / Preparation** → tratamento de dados ausentes, criação
    de variáveis derivadas.
-   **Descoberta de Padrões / Pattern Discovery** → comparação entre
    prioridade e variáveis de negócio.
-   **Relatório / Report** → principais descobertas e recomendações
    práticas.

------------------------------------------------------------------------

## 🛠 Tecnologias / Technologies

-   Python 3.11+
-   pandas, numpy
-   matplotlib, seaborn
-   scikit-learn (opcional)