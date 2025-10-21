# Etapa 3 — Mini Comitê de Política Monetária (Turma 02 - 2025/2)

## Grupo 2 — Escopo
- Curva de Juros (Parte 1): referência em janeiro de 2008.
- Parte 2 — Estimar a taxa de juros real: usar dados do IPCA e taxas nominais.
  - Fase inicial: base de dados 2019–2020 (Grupo 2).
  - Fase estendida: base de dados 2011–2020 (Grupo 2).

## Objetivos
1. Estimar a curva de juros para a data de referência do grupo (jan/2008) usando Python.
2. Analisar a curva (curto vs. longo prazo, relação com economia, política monetária, impactos em finanças pessoais).
3. Estimar a taxa de juros real (aproximação com IPCA) e discutir resultados.

## Materiais de apoio
- Notebook oficial (Jupyter) mencionado nas orientações: “Etapa 3 - Curva de Juros - scriptfinal.ipynb”.
- Página “Materiais de apoio” e “Envio da tarefa da etapa 3” (Canvas).

## Estrutura sugerida do repositório
```
.
├─ data/
│  ├─ raw/             # fontes originais (ex.: taxas, IPCA)
│  └─ processed/       # dados tratados
├─ notebooks/
│  └─ etapa3_curva_juros_grupo2.ipynb
├─ src/
│  ├─ fetch/           # download/coleta de dados
│  ├─ processing/      # limpeza e transformação
│  ├─ modeling/        # estimação da curva e taxa real
│  └─ viz/             # gráficos
└─ README.md
```

## Requisitos
- Python 3.10+
- Jupyter Notebook ou JupyterLab
- Bibliotecas sugeridas: pandas, numpy, matplotlib/plotly, seaborn, statsmodels, scikit-learn, yfinance (se aplicável).

Crie um `requirements.txt` (exemplo):
```
pandas
numpy
matplotlib
seaborn
plotly
statsmodels
scikit-learn
yfinance
jupyter
```

## Passo a passo — Parte 1 (Curva de Juros)
1. Preparar ambiente Python e Jupyter.
2. Obter as séries necessárias para a data de referência (jan/2008):
   - Taxas de juros por diferentes prazos (curva a termo).
   - Fontes possíveis: BCB/SGS, ANBIMA, provedores públicos.
3. Estimar a curva de juros no notebook `notebooks/etapa3_curva_juros_grupo2.ipynb`.
4. Produzir gráficos e análises:
   - Tendências de curto e longo prazo.
   - Relação com variáveis macro (Selic, inflação, câmbio, desemprego, etc.).
   - Implicações de política monetária e finanças pessoais.

## Passo a passo — Parte 2 (Taxa de juros real)
1. Selecionar a janela de dados:
   - Fase 1 (inicial): 2019–2020 (Grupo 2).
   - Fase 2 (estendida): 2011–2020 (Grupo 2).
2. Obter IPCA (inflação) e taxas nominais correspondentes.
3. Calcular taxa de juros real aproximada (ex.: Fisher aproximado) e/ou estimar via modelos (ex.: regressão) conforme orientações.
4. Documentar resultados e comparação entre janelas (2019–2020 vs. 2011–2020).

## Entregáveis esperados
- Notebook com código reprodutível para a Parte 1 e Parte 2.
- Visualizações (gráficos) e interpretação dos resultados.
- Este `README.md` atualizado com instruções para reprodução.

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

## Git — inicialização e commit inicial
```powershell
git init
git add .
git commit -m "chore: inicializa Etapa 3 (Grupo 2) e README"
git branch -M main
```

## Criar repositório no GitHub (opções)
- Usando GitHub CLI (recomendado):
  ```powershell
  gh repo create PUC-Etapa3-Grupo2 --source . --public --confirm
  git push -u origin main
  ```
  Requer estar logado: `gh auth login`.

- Usando token pessoal (PAT) via HTTPS:
  ```powershell
  git remote add origin https://github.com/<seu-usuario>/PUC-Etapa3-Grupo2.git
  git push -u origin main
  ```
  Na primeira autenticação, informe o usuário e o PAT.

## Observações
- Garanta versionamento de dados (ou mantenha `data/raw` fora do repositório, via `.gitignore`, se forem arquivos grandes/sigilosos).
- Documente as fontes e datas de coleta.
- Valide os resultados com o notebook de apoio oficial.
