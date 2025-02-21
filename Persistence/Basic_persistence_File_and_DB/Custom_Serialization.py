import json
class Graph:
    def __init__(self):
        self.nodes = []
        self.edges = []

    def add_node(self, value):
        self.nodes.append(value)

    def add_edge(self, node1, node2):
        self.edges.append((node1, node2))

    def to_dict(self):
        return {"nodes": self.nodes, "edges": self.edges}

graph = Graph()
graph.add_node("A")
graph.add_node("B")
graph.add_edge("A", "B")

json_graph = json.dumps(graph.to_dict())
print(json_graph)
