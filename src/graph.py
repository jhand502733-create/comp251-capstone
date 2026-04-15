class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, start, end, weight):
        if start not in self.graph:
            self.graph[start] = []

        if end not in self.graph:
            self.graph[end] = []

        self.graph[start].append((end, weight))

    def display(self):
        for node in self.graph:
            print(node, "->", self.graph[node])
