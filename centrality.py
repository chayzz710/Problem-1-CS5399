import networkx as nx
import pandas as pd
import pickle

with open("mention_graph.pkl", "rb") as f:
    G = pickle.load(f)
print("Loaded graph:", G.number_of_nodes(), "nodes")

print("Computing in-degree...")
in_deg = nx.in_degree_centrality(G)
print("Computing betweenness (sampled)...")
btw = nx.betweenness_centrality(G, k=500, seed=42)
print("Computing PageRank...")
pr = nx.pagerank(G, weight="weight")

# Save all scores to CSV (useful for Neo4j later)
res = pd.DataFrame({"in_degree": in_deg, "betweenness": btw, "pagerank": pr})
res.index.name = "user"
res.to_csv("centrality_scores.csv")
print("Saved centrality_scores.csv")

for col in res.columns:
    print(f"\nTop 10 by {col}:")
    print(res[col].sort_values(ascending=False).head(10).to_string())