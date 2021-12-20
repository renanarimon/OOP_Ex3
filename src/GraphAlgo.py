import json
import math
import os
import random
import queue
import sys
from queue import PriorityQueue
from typing import List

from numpy import sort

from GraphAlgoInterface import GraphAlgoInterface
from src.DiGraph import DigGraph
from src.GraphInterface import GraphInterface


class GraphAlgo(GraphAlgoInterface):
    INFINITY = math.inf

    def __init__(self):
        self.graph = DigGraph()

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

    def restartNodes(self):
        for n in self.graph.nodes.values():
            n.father = None
            n.weight = self.INFINITY

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
                for v in self.graph.all_out_edges_of_node(curr.id):
                    self.relax(curr.id, v)
                    pq.put(self.graph.nodes.get(v))

    def relax(self, src: int, dest: int):
        srcNode = self.graph.nodes[src]
        destNode = self.graph.nodes[dest]
        edgeWeight = self.graph.all_in_edges_of_node(src)[dest]
        if destNode.weight > srcNode.weight + edgeWeight:
            destNode.weight = srcNode.weight + edgeWeight
            destNode.father = srcNode

    def save_to_json(self, file_name: str) -> bool:
        pass

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
        while self.graph.nodes[last] is not None:
            path.append(self.graph.nodes[last].father)
            weight_till += self.graph.nodes[last].father.weight
            last = self.graph.nodes[last].father
        path.append(node_id)
        return ans, path, weight_till

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        pass

    def TSP(self, node_lst: List[int]) -> (List[int], float):
        ans = []
        currNode = node_lst.pop(0)
        ans.append(0)
        bestNode = Node
        weight = 0
        while node_lst:
            bestNode, put, tmp_wei = self.minShortPath(currNode, node_lst)
            if bestNode != currNode:
                weight += tmp_wei
                put.remove(0)
                ans.append(put)
                node_lst.remove(bestNode)
                currNode = bestNode
            else:
                return None
        return ans, weight

    def plot_graph(self) -> None:
        pass
