"""Sankey Diagram: Superstore Sales — Segment → Category → Sub-Category
Style: Apple Income Statement (dollar labels, color-coded flows)
Data: https://www.kaggle.com/datasets/rohitsahoo/sales-forecasting
Install: pip install plotly pandas kagglehub
"""

import kagglehub
import pandas as pd
import plotly.graph_objects as go

path = kagglehub.dataset_download("rohitsahoo/sales-forecasting")
df = pd.read_csv(f"{path}/train.csv", encoding="latin-1")


def fmt(val):
    """Format dollar values: $1.1M or $328K."""
    if val >= 1_000_000:
        return f"${val / 1_000_000:.1f}M"
    return f"${val / 1_000:,.0f}K"


seg_cat = df.groupby(["Segment", "Category"])["Sales"].sum().reset_index()
cat_sub = df.groupby(["Category", "Sub-Category"])["Sales"].sum().reset_index()

seg_totals = df.groupby("Segment")["Sales"].sum()
cat_totals = df.groupby("Category")["Sales"].sum()
sub_totals = df.groupby("Sub-Category")["Sales"].sum()

segments = ["Consumer", "Corporate", "Home Office"]
categories = ["Technology", "Furniture", "Office Supplies"]
subcategories = sub_totals.sort_values(ascending=False).index.tolist()

node_labels = (
    [f"{s}\n{fmt(seg_totals[s])}" for s in segments]
    + [f"{c}\n{fmt(cat_totals[c])}" for c in categories]
    + [f"{s}\n{fmt(sub_totals[s])}" for s in subcategories]
)

all_names = segments + categories + subcategories
node_index = {name: i for i, name in enumerate(all_names)}

cat_solid = {
    "Technology":      "#4285F4",
    "Furniture":       "#34A853",
    "Office Supplies": "#EA4335",
}
cat_transparent = {
    "Technology":      "rgba(66, 133, 244, 0.35)",
    "Furniture":       "rgba(52, 168, 83, 0.35)",
    "Office Supplies": "rgba(234, 67, 53, 0.35)",
}

seg_colors = ["#6c757d", "#868e96", "#adb5bd"]
cat_colors = [cat_solid[c] for c in categories]

sub_parent = cat_sub.set_index("Sub-Category")["Category"]
sub_colors = [cat_solid[sub_parent[s]] for s in subcategories]

node_colors = seg_colors + cat_colors + sub_colors

sources, targets, values, link_colors = [], [], [], []

for _, row in seg_cat.iterrows():
    sources.append(node_index[row["Segment"]])
    targets.append(node_index[row["Category"]])
    values.append(round(row["Sales"], 2))
    link_colors.append(cat_transparent[row["Category"]])

for _, row in cat_sub.iterrows():
    sources.append(node_index[row["Category"]])
    targets.append(node_index[row["Sub-Category"]])
    values.append(round(row["Sales"], 2))
    link_colors.append(cat_transparent[row["Category"]])

fig = go.Figure(go.Sankey(
    arrangement="snap",
    node=dict(
        pad=14,
        thickness=30,
        label=node_labels,
        color=node_colors,
        line=dict(width=0),
    ),
    link=dict(
        source=sources,
        target=targets,
        value=values,
        color=link_colors,
    ),
))

fig.update_layout(
    title=dict(
        text="Superstore Sales Breakdown",
        font=dict(size=22),
        x=0.5,
    ),
    font=dict(size=12, family="Arial"),
    paper_bgcolor="white",
    plot_bgcolor="white",
    margin=dict(l=10, r=150, t=80, b=40),
)
fig.show()
