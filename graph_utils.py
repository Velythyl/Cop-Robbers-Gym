import copy

import igraph
import numpy as np
class Graph:
    def __init__(self, igraph_graph):
        igraph_graph = igraph.from_adjacency


        self.igraph = igraph_graph
        self._rep = np.array(self.igraph.get_adjacency(), dtype=int)
        self._attr = np.zeros(self._rep.shape[0], dtype=int)

    def set_cr(self, nodes, is_cop):
        self._attr[nodes] = 1 if is_cop else -1