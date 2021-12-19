import json
from types import SimpleNamespace

from GraphAlgoInterface import GraphAlgoInterface
from src.DiGraph import DigGraph
from src.GraphInterface import GraphInterface


class GraphAlgo(GraphAlgoInterface):

    def __init__(self):
        self.graph = DigGraph()

    def get_graph(self) -> GraphInterface:
        return self.graph

    def load_from_json(self, file_name: str) -> bool:
        with open(file_name, 'r') as file:
            self.graph = json.load(
                file, object_hook=lambda json_dict: SimpleNamespace(**json_dict))
        return True

    def save_to_json(self, file_name: str) -> bool:
        pass

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        pass

    def plot_graph(self) -> None:
        pass
