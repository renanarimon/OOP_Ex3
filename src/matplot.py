import matplotlib.pyplot as plt

from src.GraphAlgo import GraphAlgo

g_algo = GraphAlgo()
file = '../data/A1.json'
g_algo.load_from_json(file)
graph = g_algo.graph

x = []
y = []
for n in graph.nodes.values():
    src_x = n.pos[0]
    src_y = n.pos[1]
    for k in graph.all_out_edges_of_node(n.id):
        dest = graph.nodes.get(k)
        dest_x = dest.pos[0]
        dest_y = dest.pos[1]
        plt.annotate("", xy=(src_x, src_y), xytext=(dest_x, dest_y), arrowprops=dict(arrowstyle="->"))

    plt.annotate(n.id, (src_x, src_y))
    x.append(n.pos[0])
    y.append(n.pos[1])


plt.title(file.title())
plt.scatter(x, y, c='red')
plt.gca().invert_yaxis()
plt.show()
