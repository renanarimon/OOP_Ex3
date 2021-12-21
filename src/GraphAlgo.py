import json
import math
import random
import queue
import sys
from typing import List

from GraphAlgoInterface import GraphAlgoInterface
from src import GUI
from src.DiGraph import DiGraph
from src.GraphInterface import GraphInterface
import GUI


class GraphAlgo(GraphAlgoInterface):
    INFINITY = math.inf

    def __init__(self, g: DiGraph = DiGraph()):
        self.graph = g

    def get_graph(self) -> GraphInterface:
        return self.graph

    def load_from_json(self, file_name: str) -> bool:
        with open(file_name, 'r') as file:
            l = json.load(file)
            ListNodes = l['Nodes']
            ListEdges = l['Edges']
        for n in ListNodes:
            try:
                pos = n['pos']
            except Exception:
                x = random.uniform(35.19, 35.22)
                y = random.uniform(32.05, 32.22)
                pos = (x, y, 0.0)

            self.graph.add_node(n['id'], pos)
        for e in ListEdges:
            self.graph.add_edge(e['src'], e['dest'], e['w'])
        return True

    def copy(self):
        g = DiGraph()
        for n in self.graph.nodes.values():
            g.add_node(n.id, n.pos)
            for k in self.graph.all_out_edges_of_node(n.id):
                w = self.graph.children[n.id][k]
                g.add_edge(n.id, k, w)
        return g

    def transpose(self):
        g = self.copy()
        tmp = g.children
        g.children = g.parents
        g.parents = tmp
        return g

    def bfs(self, g: DiGraph, nodeId: int) -> list:
        visited = [False] * (g.v_size())
        q = []
        q.append(nodeId)
        visited[nodeId] = True
        while q:
            startNode = q.pop(0)
            for e in g.all_out_edges_of_node(startNode):
                if not visited[e]:
                    q.append(e)
                    visited[e] = True
        return visited

    def isConnected(self) -> bool:
        start = self.graph.nodes[0].id
        visited = self.bfs(self.graph, start)
        for b in visited:
            if b == 0:
                return False
        visited = self.bfs(self.transpose(), start)
        for b in visited:
            if b == 0:
                return False
        return True

    def restartNodes(self):
        for n in self.graph.nodes.values():
            n.father = None
            n.weight = self.INFINITY
            n.visited = 0

    def dijkstra(self, src: int, dest: int):
        self.restartNodes()
        root = self.graph.nodes.get(src)
        root.weight = 0
        pq = queue.PriorityQueue()
        pq.put(root)
        while not pq.empty():
            curr = pq.get()
            if curr.visited == 0:  # NOT visited
                if curr.id == dest:
                    return
                curr.visited = 1
                for d in self.graph.all_out_edges_of_node(curr.id):
                    self.relax(curr.id, d)
                    pq.put(self.graph.nodes.get(d))

    def relax(self, src: int, dest: int):
        srcNode = self.graph.nodes[src]
        destNode = self.graph.nodes[dest]
        edgeWeight = self.graph.all_out_edges_of_node(src)[dest]
        if destNode.weight > srcNode.weight + edgeWeight:
            destNode.weight = srcNode.weight + edgeWeight
            destNode.father = srcNode

    def save_to_json(self, file_name: str) -> bool:
        if self.graph is None:
            return False
        dict_ans = {"Edges": [], "Nodes": []}
        for n in self.graph.nodes.values():
            node_dict = {"id": n.id}
            if n.pos is not None:
                node_dict["pos"] = n.pos_to_string()
            dict_ans["Nodes"].append(node_dict)
            for e in self.graph.all_out_edges_of_node(n.id):
                edges_dict = {"src": n.id, "w": self.graph.all_out_edges_of_node(n.id)[e], "dest": e}
                dict_ans["Edges"].append(edges_dict)
        try:
            with open(file_name, 'w') as writer:
                writer.write(json.dumps(dict_ans))
                return True
        except:
            return False
        finally:
            writer.close()

    def minShortPath(self, node_id: int, node_lst: List[int]) -> (int, list, float):
        self.dijkstra(node_id, -1)
        minWei = sys.maxsize
        ans = 0
        path = []
        for i in node_lst:
            if self.graph.nodes[i].weight < minWei:
                minWei = self.graph.nodes[i].weight
                ans = i
        last = ans
        weight_till = self.graph.nodes[last].weight
        path, weight_till = self.findParentPath(last, weight_till, path)
        path.append(node_id)
        path.reverse()
        return ans, path, weight_till

    def findParentPath(self, idCurr: int, weight: float, listAdd: list):
        while self.graph.nodes[idCurr].father is not None:
            listAdd.append(idCurr)
            weight += self.graph.nodes[idCurr].father.weight
            idCurr = self.graph.nodes[idCurr].father.id
        return listAdd, weight

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        self.dijkstra(id1, id2)
        weightAns = self.graph.nodes[id2].weight
        listAns = []
        curr = id2
        listAns, weightAns = self.findParentPath(curr, weightAns, listAns)
        listAns.append(id1)
        listAns.reverse()
        return weightAns, listAns

    def TSP(self, node_lst: List[int]) -> (List[int], float):
        ans = []
        currNode = node_lst.pop(0)
        ans.append(0)
        bestNode = 0
        weight = 0
        while len(node_lst) > 0:
            put = []
            bestNode, put, tmp_wei = self.minShortPath(currNode, node_lst)
            if bestNode != currNode:
                weight += tmp_wei
                put.pop(0)
                ans = ans + put
                node_lst.remove(bestNode)
                currNode = bestNode
            else:
                return None
        return ans, weight

    def maxShortPath(self, node_id: int) -> int:
        self.dijkstra(node_id, -1)
        maxW = -sys.maxsize
        for n in self.graph.nodes.values():
            if n.weight > maxW:
                maxW = n.weight
        return maxW

    def centerPoint(self) -> (int, float):
        if not self.isConnected():
            return -1, self.INFINITY

        minDist = sys.maxsize
        minId = 0
        for n in self.graph.nodes.values():
            maxDist = self.maxShortPath(n.id)
            if maxDist < minDist:
                minDist = maxDist
                minId = n.id
        return minId, minDist

    def plot_graph(self) -> None:
        GUI.scale()
        pass
