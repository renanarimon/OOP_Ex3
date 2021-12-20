from GraphInterface import GraphInterface


class DigGraph(GraphInterface):
    def _init_(self):
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
        if node_id in self.nodes:
            childrenTmp = self.all_out_edges_of_node(node_id)
            parentsTmp = self.all_in_edges_of_node(node_id)

            for n in childrenTmp:
                self.remove_edge(node_id, n)
                del self.children[n][node_id]
                self.MC+=1
            for n in parentsTmp:
                del self.parents[n][node_id]
                self.MC+=1
            del self.nodes[node_id]
            return True
        else: return False

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        if node_id1 and node_id2 in self.nodes\
         and node_id1 in self.children and node_id2 in self.parents:
            del self.parents[node_id2][node_id1]
            del self.children[node_id1][node_id2]
            self.MC += 1
            self.edgesAmount -= 1
            return True
        else:
            return False
