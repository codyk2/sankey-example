# sankey-example

Sankey diagram examples in **Python** and **R**, built for a class presentation on data visualization.

## Python — Superstore Sales (`sankey_example_plotly.py`)

Uses the [Superstore Sales](https://www.kaggle.com/datasets/rohitsahoo/sales-forecasting) dataset from Kaggle (9,800 transactions across the US).

**Flow:** Customer Segment → Product Category → Sub-Category, weighted by sales revenue ($).

- **3 Segments**: Consumer ($1.1M), Corporate ($688K), Home Office ($425K)
- **3 Categories**: Technology, Furniture, Office Supplies — each color-coded (blue, green, red)
- **17 Sub-Categories**: Phones, Chairs, Storage, Tables, Binders, Machines, etc.
- Dollar values displayed on every node (Apple Income Statement style)
- Dataset is downloaded automatically via `kagglehub`

### Requirements

```bash
pip install plotly pandas kagglehub
```

### Run

```bash
python sankey_example_plotly.py
```

Opens an interactive Sankey diagram in your browser.

## R — Energy Flow (`sankey_example.R`)

A minimal hardcoded example using [networkD3](https://cran.r-project.org/package=networkD3).

**Flow:** Energy Sources (Solar, Wind, Hydro) → Electricity → End Use (Residential, Commercial, Industrial), measured in TWh.

### Requirements

```r
install.packages("networkD3")
```

### Run

```r
source("sankey_example.R")
```

Opens an interactive Sankey diagram in the RStudio Viewer or browser.

## Dataset

| File | Dataset | Source |
|------|---------|--------|
| `sankey_example_plotly.py` | Superstore Sales (9,800 rows) | [Kaggle](https://www.kaggle.com/datasets/rohitsahoo/sales-forecasting) |
| `sankey_example.R` | Hardcoded energy flow example | N/A |
