# sankey-example

Minimal Sankey diagram examples in **R** and **Python**.

## Files

| File | Language | Library |
|------|----------|---------|
| `sankey_example.R` | R | [networkD3](https://cran.r-project.org/package=networkD3) |
| `sankey_example_plotly.py` | Python | [Plotly](https://plotly.com/python/sankey-diagram/) |

## Quick Start

### R
```r
install.packages("networkD3")
source("sankey_example.R")
```

### Python
```bash
pip install plotly
python sankey_example_plotly.py
```

Both scripts visualize a simple energy-flow Sankey diagram (Solar / Wind / Hydro → Electricity → Residential / Commercial / Industrial).
