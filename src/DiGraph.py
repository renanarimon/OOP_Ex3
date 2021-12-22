import math
import functools

from GraphInterface import GraphInterface


class DiGraph(GraphInterface):
    nodes = {}
    edgesAmount = 0
    children = {}
    parents = {}
    MC = 0

    def __init__(self):
        self.nodes = {}
        self.edgesAmount = 0
        self.children = {}
        self.parents = {}
        self.MC = 0

    def v_size(self) -> int:
        return len(self.nodes)

    def e_size(self) -> int:
        return self.edgesAmount

    def get_mc(self) -> int:
        return self.MC

    def get_all_v(self) -> dict:
        return self.nodes

    def all_in_edges_of_node(self, id1: int) -> dict:
        return self.parents[id1]

    def all_out_edges_of_node(self, id1: int) -> dict:
        return self.children[id1]

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        if self.nodes.get(id1) is not None and self.nodes.get(id2) is not None:
            if self.children[id1].get(id2) is not None:
                return False
            self.children[id1].update({id2: weight})
            self.parents[id2].update({id1: weight})
            self.MC += 1
            self.edgesAmount += 1
            return True
        else:
            return False

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        if node_id not in self.nodes:
            newOne = Node(node_id, pos)
            self.nodes[node_id] = newOne
            self.children[node_id] = {}
            self.parents[node_id] = {}
            self.MC += 1
            return True
        else:
            return False

    def remove_node(self, node_id: int) -> bool:
        if node_id in self.nodes:
            for n in list(self.children[node_id]):
                self.remove_edge(n, node_id)
                self.remove_edge(node_id, n)
            del self.nodes[node_id]
            return True
        else:
            return False

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        if node_id1 and node_id2 in self.nodes \
                and node_id1 in self.children.keys() and node_id2 in self.parents.keys():
            del self.parents[node_id2][node_id1]
            del self.children[node_id1][node_id2]
            self.MC += 1
            self.edgesAmount -= 1
            return True
        else:
            return False

    def __str__(self):
        return str(self.nodes)


class Node:
    def __init__(self, id1: int, pos: tuple = None):
        self.pos = pos
        self.id = id1
        self.father = None
        self.weight = math.inf
        self.visited = 0

    def __lt__(self, other):
        return self.weight < getattr(other, 'weight', other)

    def __eq__(self, other):
        return self.weight == getattr(other, 'weight', other)

    def __str__(self) -> str:
        st = str(self.id)
        return st

    def pos_to_string(self):
        string = "{},{},{}".format(self.pos[0], self.pos[1], self.pos[2])
        return string


class Edge:
    def __init__(self, src: int, w: float, dest: int):
        self.src = src
        self.w = w
        self.dest = dest

