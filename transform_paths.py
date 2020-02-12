# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 14:45:35 2020

@author: ator-
"""

import numpy as np

G = np.identity(1005)
# https://snap.stanford.edu/data/email-Eu-core.html
with open("email-Eu-core.txt") as f:
    for r in f:
        x, y = (int(x) for x in r.split())
        #print(x, y)
        G[x, y] = 1
print("G paths, length 1", G.sum())
G_i = G
for i in range(2, 10):
    # Maatrikskorrutise kasutamisest pikkusega N teede leidmiseks:
    # https://math.stackexchange.com/questions/1890620/finding-path-lengths-by-the-power-of-adjacency-matrix-of-an-undirected-graph
    G_i = np.greater(G_i @ G, 0).astype(int)
    print("G paths length", i, G_i.sum())
