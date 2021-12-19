from GraphInterface import GraphInterface


class DigGraph(GraphInterface):
    def _init_(self):
        self.nodes = {}
        self.edgesAmount = 0
        self.children = {}
        self.parents = {}
        self.MC = 0

    def v_size(self) -> int:
        pass

    def e_size(self) -> int:
        pass

    def get_mc(self) -> int:
        pass

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        if id1 and id2 in self.nodes and id1 != id2:
            self.children[id1].update({id2: weight})
            self.parents[id2].update({id1: weight})
            self.MC += 1
            self.edgesAmount += 1
            return True
        else:
            return False

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        if node_id not in self.nodes:
            self.nodes[node_id] = pos
            self.children[node_id] = {}
            self.parents[node_id] = {}
            self.MC += 1
            return True
        else:
            return False

    def remove_node(self, node_id: int) -> bool:
        pass

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        pass


