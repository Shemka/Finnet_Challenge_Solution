# nodevectors and csrgraph must be installed: run 'pip install nodevectors csrgraph' to install
# module nodevectors work on sparse matrix, so it much faster to fit.
# GitHub link to this repository: https://github.com/VHRanger/nodevectors
import pandas as pd
import networkx as nx
import numpy as np
from nodevectors import Node2Vec

edges = pd.read_csv('finnet_data/edges.csv')
G = nx.from_pandas_dataframe(edges, 'id_1', 'id_2')

g2v = Node2Vec(n_components=100, walklen=4)
g2v.fit(G)

# File size is about 2GB
g2v.save_vectors("n2v.bin")