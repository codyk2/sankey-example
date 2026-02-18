# Minimal Sankey Diagram in R using networkD3
# Install: install.packages("networkD3")

library(networkD3)

# Define nodes
nodes <- data.frame(name = c(
  "Solar",      # 0
  "Wind",       # 1
  "Hydro",      # 2
  "Electricity",# 3
  "Residential",# 4
  "Commercial", # 5
  "Industrial"  # 6
))

# Define links (source -> target -> value)
links <- data.frame(
  source = c(0, 1, 2, 3, 3, 3),
  target = c(3, 3, 3, 4, 5, 6),
  value  = c(40, 35, 25, 30, 25, 45)
)

# Create Sankey diagram
sankey <- sankeyNetwork(
  Links  = links,
  Nodes  = nodes,
  Source = "source",
  Target = "target",
  Value  = "value",
  NodeID = "name",
  units  = "TWh",
  fontSize = 14,
  nodeWidth = 30
)

sankey
