"""Minimal Sankey Diagram in Python using Plotly.
Install: pip install plotly
"""

import plotly.graph_objects as go

# Define nodes
node_labels = [
    "Solar", "Wind", "Hydro",       # sources (0-2)
    "Electricity",                    # middle  (3)
    "Residential", "Commercial", "Industrial"  # sinks (4-6)
]

# Define links: source -> target with values
links = dict(
    source=[0, 1, 2, 3, 3, 3],
    target=[3, 3, 3, 4, 5, 6],
    value= [40, 35, 25, 30, 25, 45],
)

fig = go.Figure(go.Sankey(
    node=dict(
        pad=20,
        thickness=30,
        label=node_labels,
        color=["#f9d71c", "#4dc9f6", "#3498db",
               "#95a5a6", "#2ecc71", "#e74c3c", "#9b59b6"],
    ),
    link=links,
))

fig.update_layout(title_text="Energy Flow – Sankey Diagram", font_size=14)
fig.show()
