import networkx as nx, pickle
with open("mention_graph.pkl", "rb") as f:
    G = pickle.load(f)
nx.to_pandas_edgelist(G).to_csv("edges.csv", index=False)  # source,target,weight
print("Saved edges.csv")