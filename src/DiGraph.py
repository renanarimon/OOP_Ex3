from GraphInterface import GraphInterface


class DigGraph(GraphInterface):
    nodes = {}
    edgesAmount = 0
    children = {}
    parents = {}
    MC = 0

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
            Node(pos, node_id)
            self.nodes[node_id] = pos
            self.children[node_id] = {}
            self.parents[node_id] = {}
            self.MC += 1
            return True
        else:
            return False

    def remove_node(self, node_id: int) -> bool:
        if node_id in self.nodes:
            childrenTmp ={}
                # self.all_out_edges_of_node(node_id)
            parentsTmp = {}
        # self.all_in_edges_of_node(node_id)
        #     for n in self.all_out_edges_of_node[node_id]:
        #         childrenTmp.update(self.children[n][node_id])
        #     for n in self.all_in_edges_of_node[node_id]:
        #         parentsTmp.update(self.parents[n][node_id])

            for n in list(self.children[node_id]):
                self.remove_edge(n,node_id)
                self.remove_edge(node_id,n)
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
    def __init__(self, pos: float, id1: int):
        self.pos = pos
        self.id = id1

    def __str__(self) -> str:
        st = str(self.id)
        return st


class Edge:
    def __init__(self, src: int, w: float, dest: int):
        self.src = src
        self.w = w
        self.dest = dest

    # def __str__(self) -> str:
    #     st = "("
