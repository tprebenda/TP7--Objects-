# Troy Prebenda
# TP7, Ex2: La classe Graph

#!/usr/bin/python

class Graph:
    def __init__(self):
        self._nodes = set()
        self._out = {}
        self._weight = {}

    def __len__(self):
        return len(self._nodes)

    def __iter__(self):
        return iter(self._nodes)
    
    def __next__(self):
        if self.count = 0:
            self.val = next(self.myiter)
        self.count -= 1
        return self.val

    def add_node(self, u):
        if u not in self._nodes:
            self._nodes.add(u)
            self._out[u] = set()

    def add_edge(self, u, v, weight=None):
        self.add_node(u)
        self.add_node(v)
        self._out[u].add(v)
        self._weight[(u, v)] = weight



if __name__== "__main__":
    g = Graph()
