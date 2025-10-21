# Etapa 3 — Mini Comitê de Política Monetária (Turma 02 - 2025/2)

## Grupo 2 — Escopo
- Curva de Juros (Parte 1): referência em janeiro de 2008.
- Parte 2 — Estimar a taxa de juros nominal via regressão (Selic ~ IPCA) e analisar a taxa real:
  - Janela inicial: 2019–2020 (Grupo 2).
  - Janela estendida: 2011–2020 (Grupo 2).

## Objetivos
1. Estimar a curva de juros na data de referência do grupo (jan/2008) em Python.
2. Analisar a curva (curto vs. longo prazo, relação com economia, política monetária, finanças pessoais).
3. Parte 2: Estimar Selic por regressão linear simples em função do IPCA (sem variável tempo), apresentar equação e métricas (R², R² ajustado, teste t, p-valor) e comparar janelas.

## Estrutura do repositório
```
.
├─ data/
│  ├─ raw/             # arquivos brutos salvos pelo notebook (ipca.csv, selic.csv)
│  └─ processed/       # dados tratados (opcional)
├─ notebooks/
│  ├─ etapa3_parte1.ipynb
│  └─ etapa3_parte2.ipynb
└─ README.md
```

## Requisitos
- Python 3.9–3.11
- Jupyter Notebook ou JupyterLab
- Bibliotecas: pandas, numpy, matplotlib, seaborn, plotly, statsmodels, bcb (ou alternativa via requests)

Compatibilidade `pandas` × `bcb`:
- `python-bcb`/`bcb` 0.1.8 requer `pandas >=1.4.4,<2.0`. Se você estiver com `pandas 2.x`, escolha:
  - Downgrade do pandas (ex.: `pandas==1.5.3`), ou
  - Não usar `bcb` e buscar dados via API do BCB (exemplo abaixo).

Exemplo de `requirements.txt` (com `bcb`):
```
pandas==1.5.3
numpy
matplotlib
seaborn
plotly
statsmodels
bcb
jupyter
```

## Parte 2 — Fluxo (atual no notebook)
1) Coleta de dados (BCB/SGS):
   - IPCA mensal (%): série 433
   - Selic ao ano (%): série 432
   - Código base (notebook): `from bcb import sgs` e `sgs.get({...}, start, end)`
   - Arquivos gerados em `data/raw/`: `ipca.csv`, `selic.csv`

2) Preparos e janelas:
   - Janela 2019–2020 (preparo inicial)
   - Janela 2011–2020 (estendida)

3) Regressão linear simples (statsmodels):
   - Modelo: `Selic = β0 + β1 × IPCA`
   - Métricas reportadas: R², R² ajustado, teste t e p-valor do coeficiente de IPCA

4) Visualização (Plotly):
   - Dispersão (Selic vs IPCA) com `trendline='ols'`, anotação da equação e R²

5) Taxa real (opcional no notebook):
   - Cálculo por Fisher (aproximado e exato) para contextualização

## Alternativa sem `bcb` (mantendo `pandas 2.x`)
Exemplo para IPCA via API do BCB:
```python
import requests, pandas as pd
url = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.433/dados"
params = {"formato":"json","dataInicial":"01/01/2011","dataFinal":"31/12/2020"}
data = requests.get(url, params=params).json()
df_ipca = pd.DataFrame(data)
df_ipca["date"] = pd.to_datetime(df_ipca["data"], dayfirst=True).values.astype("datetime64[M]").astype("datetime64[ns]")
df_ipca["ipca_mom"] = pd.to_numeric(df_ipca["valor"], errors="coerce")
df_ipca = df_ipca[["date","ipca_mom"]].sort_values("date")
```

## Como executar
1. Criar e ativar ambiente (ex.: venv):
   - Windows PowerShell:
     ```powershell
     python -m venv .venv
     .\.venv\Scripts\Activate.ps1
     pip install -r requirements.txt
     ```
2. Abrir Jupyter e executar os notebooks:
   ```powershell
   jupyter notebook
   ```
3. Abra `notebooks/etapa3_parte2.ipynb` e execute em ordem: coleta (SGS), salvamento dos CSVs, join, regressões (2019–2020, 2011–2020) e gráficos.

## Observações
- Use IPCA e Selic em unidades compatíveis (ambas % a.a. ao comparar/regredir). No notebook, o IPCA mensal é anualizado antes da regressão.
- Documente fontes e datas de coleta. Evite versionar dados sensíveis/grandes.
- Para o envio, inclua prints/resumos de equação e métricas conforme orientações (equação, R², R² ajustado, teste t, p-valor).
