from unittest import TestCase
from src.GraphAlgo import GraphAlgo


class TestGraphAlgo(TestCase):
    algo = GraphAlgo()
    graph = algo.graph

    def test_load_from_json(self):
        g_algo = GraphAlgo()
        file1 = '../data/A5.json'
        file2 = '../data/A1.json'
        file3 = '../data/A3.json'
        g_algo.load_from_json(file1)
        graph = g_algo.graph
        self.assertEqual(graph.v_size(), 48)
        g_algo.load_from_json(file2)
        self.assertEqual(graph.v_size(), 17)
        g_algo.load_from_json(file3)
        self.assertEqual(graph.v_size(), 49)

    def test_shortest_path(self):
        g_algo = GraphAlgo()
        file1 = '../data/A1.json'
        g_algo.load_from_json(file1)
        self.assertEqual(g_algo.shortest_path(0, 8), (22.59506068993273, [0, 1, 2, 6, 7, 8]))
        self.assertEqual(g_algo.shortest_path(0, 16), (1.3118716362419698, [0, 16]))
        self.assertEqual(g_algo.shortest_path(16, 3), (14.129670896183516, [16, 0, 1, 2, 3]))

    def test_tsp(self):
        g_algo = GraphAlgo()
        file1 = '../data/A0.json'
        file2 = '../data/A1.json'
        g_algo.load_from_json(file1)
        cities = []
        for n in g_algo.graph.nodes.values():
            cities.append(n.id)
        self.assertEqual(g_algo.TSP(cities), ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 14.470852790366884))
        g_algo.load_from_json(file2)
        cities = []
        for n in g_algo.graph.nodes.values():
            cities.append(n.id)
        self.assertEqual(g_algo.TSP(cities),
                         ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], 22.63446693792369))

    def test_center_point(self):
        g_algo = GraphAlgo()
        file1 = '../data/A0.json'
        file2 = '../data/A1.json'
        file3 = '../data/A2.json'
        file4 = '../data/A3.json'
        file5 = '../data/A4.json'
        file6 = '../data/A5.json'
        # file1000 = '../data/1000Nodes.json'
        g_algo.load_from_json(file1)
        self.assertEqual(g_algo.centerPoint(), (7, 6.806805834715163))
        g_algo.load_from_json(file2)
        self.assertEqual(g_algo.centerPoint(), (8, 9.925289024973141))
        g_algo.load_from_json(file3)
        self.assertEqual(g_algo.centerPoint(), (0, 7.819910602212574))
        g_algo.load_from_json(file4)
        self.assertEqual(g_algo.centerPoint(), (2, 8.182236568942237))
        g_algo.load_from_json(file5)
        self.assertEqual(g_algo.centerPoint(), (6, 8.071366078651435))
        g_algo.load_from_json(file6)
        self.assertEqual(g_algo.centerPoint(), (40, 9.291743173960954))

    def test_isConnected(self):
        g_algo = GraphAlgo()
        file1 = '../data/A0.json'
        file2 = '../data/A1.json'
        file3 = '../data/A2.json'
        file4 = '../data/A3.json'
        file5 = '../data/A4.json'
        file6 = '../data/A5.json'
        g_algo.load_from_json(file1)
        self.assertTrue(g_algo.isConnected())
        g_algo.load_from_json(file2)
        self.assertTrue(g_algo.isConnected())
        g_algo.load_from_json(file3)
        self.assertTrue(g_algo.isConnected())
        g_algo.load_from_json(file4)
        self.assertTrue(g_algo.isConnected())
        g_algo.load_from_json(file5)
        self.assertTrue(g_algo.isConnected())
        g_algo.load_from_json(file6)
        self.assertTrue(g_algo.isConnected())
