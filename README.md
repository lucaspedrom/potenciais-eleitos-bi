# Potenciais Eleitos - Business Intelligence (BI)

Repositório analítico contendo o relatório em **Power BI Project (`.pbip`)** e suas respectivas bases de dados em formato colunar **Apache Parquet**, desenvolvido para análise e classificação de candidatos nas eleições de 2022 e 2024.

---

## 🎯 Sobre o Projeto

O objetivo do relatório é cruzar os dados oficiais do Tribunal Superior Eleitoral (TSE) para mapear o cenário eleitoral e classificar o potencial de candidaturas (ex.: *Potencial Eleito*, *Candidato Desafiante*, *Eleito*).

Principais análises contempladas:
* **Desempenho Eleitoral:** Comparação dos votos nominais válidos com o quociente eleitoral, votos de corte e votos dos eleitos.
* **Financiamento de Campanha:** Prestação de contas, teto de gastos e repasses de recursos partidários.
* **Geografia do Voto:** Presença e força partidária distribuída por município, estado e região.

---

## 📁 Estrutura do Repositório

```text
├── dashboard/
│   ├── Relatórios dos Potenciais Eleitos 2024.pbip   # Arquivo principal do Power BI Project
│   ├── Relatórios dos Potenciais Eleitos 2024.Report/ # Páginas, visuais e layouts
│   └── Relatórios dos Potenciais Eleitos 2024.SemanticModel/ # Modelo semântico em TMDL
├── data/
│   └── parquet/                                     # Bases analíticas colunares (.parquet)
├── src/
│   └── transformer/
│       └── csv_to_parquet.py                        # Utilitário de conversão CSV -> Parquet
├── .gitignore
└── README.md
```

---

## 📊 Bases de Dados (`data/parquet/`)

O modelo semântico consome diretamente 12 tabelas consolidadas em Parquet:

* **Dimensões:**
  * `d_estados.parquet`: Unidades federativas, tetos de gastos e votos de corte estaduais/federais.
  * `d_municipio.parquet`: Cidades, código TSE/IBGE, população, quociente eleitoral e limites municipais.
  * `d_partidos.parquet`: Partidos e federações partidárias.
  * `d_faixa_populacao.parquet`: Segmentação de municípios por porte populacional.

* **Fatos:**
  * `f_candidato.parquet` / `f_candidato_suporte.parquet`: Candidaturas municipais de 2024 (Prefeito e Vereador) e cálculo de potencial.
  * `f_candidato_2022.parquet` / `f_candidato_2022_suporte.parquet`: Candidaturas gerais de 2022 (Deputados).
  * `f_votacao_candidato.parquet`: Votação nominal apurada por turno e cargo.
  * `f_prestacao_contas.parquet`: Dados de despesas, receitas e limites de campanha.
  * `f_partido_distribuicao_candidato.parquet` (2024 e 2022): Distribuição de verbas de campanha aos candidatos.

---

## 🚀 Como Abrir e Visualizar o Relatório

1. Tenha o **Microsoft Power BI Desktop** instalado.
2. Clone o repositório:
   ```bash
   git clone <URL_DO_REPOSITORIO>
   ```
3. Abra o arquivo:
   ```
   dashboard/Relatórios dos Potenciais Eleitos 2024.pbip
   ```
4. O Power BI Desktop abrirá o relatório consumindo os arquivos da pasta `data/parquet/`.

> **Dica de Configuração (Parâmetro de Dados):**
> Caso queira redefinir a pasta dos arquivos em sua máquina, acesse no menu do Power BI:
> **Página Inicial > Transformar Dados > Editar Parâmetros** e atualize o parâmetro `CaminhoDados` apontando para o caminho absoluto da sua pasta `data/parquet`.

---

## 🛠️ Tecnologias Utilizadas

* **Power BI Desktop (PBIP & TMDL):** Modelagem semântica, DAX e visualizações.
* **Apache Parquet:** Armazenamento colunar comprimido para alta performance analítica.
* **Python (pandas / pyarrow):** Engenharia de transformação e conversão de dados.
