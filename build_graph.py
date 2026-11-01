import pandas as pd
import re
import networkx as nx
import pickle

df = pd.read_json("raw_data_te.jsonl", lines=True, encoding="utf-8")
df = df[["author_screen_name", "tweet_text"]].dropna()

mention_pattern = re.compile(r"@([A-Za-z0-9_]+)")
df["mentions"] = df["tweet_text"].apply(mention_pattern.findall)

G = nx.DiGraph()
for author, mentions in zip(df["author_screen_name"], df["mentions"]):
    src = author.lower()
    for m in mentions:
        tgt = m.lower()
        if src == tgt:
            continue
        if G.has_edge(src, tgt):
            G[src][tgt]["weight"] += 1
        else:
            G.add_edge(src, tgt, weight=1)

print("Nodes:", G.number_of_nodes(), "Edges:", G.number_of_edges())

print("Total tweets:", len(df))
print("Tweets with mentions:", (df["mentions"].str.len() > 0).sum())

with open("mention_graph.pkl", "wb") as f:
    pickle.dump(G, f)
print("Saved graph to mention_graph.pkl")

