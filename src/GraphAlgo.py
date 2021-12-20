import json
import os
from types import SimpleNamespace

from GraphAlgoInterface import GraphAlgoInterface
from src.DiGraph import DigGraph, Node, Edge
from src.GraphInterface import GraphInterface


class GraphAlgo(GraphAlgoInterface):

    def __init__(self):
        self.graph = DigGraph()

    def get_graph(self) -> GraphInterface:
        return self.graph

    def load_from_json(self, file_name: str) -> bool:
        with open(file_name, 'r') as file:
            l = json.load(file)
            ListNodes = l['Nodes']
            # Nodes = [Node(**n) for n in ListNodes]
            ListEdges = l['Edges']
            # Edges = [Edge(**e) for e in ListEdges]
        for n in ListNodes:
            self.graph.add_node(n['id'], n['pos'])
        for e in ListEdges:
            self.graph.add_edge(e['src'], e['dest'], e['w'])
        return True

    def save_to_json(self, file_name: str) -> bool:
        pass

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        pass

    def plot_graph(self) -> None:
        pass
