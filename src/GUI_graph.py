import easygui
import pygame
from pygame import Color, display, gfxdraw
from pygame.constants import RESIZABLE
import pygame_gui
from src.DiGraph import Node
from src.GraphAlgo import GraphAlgo
from src.InputBox import InputBox

# init algo & graph
g_algo = GraphAlgo()
file = '../data/A1.json'
g_algo.load_from_json(file)
graph = g_algo.graph

R = 10
WIDTH = pygame.display.get_surface().get_width()
HEIGHT = pygame.display.get_surface().get_height()

# colors
gray = Color(64, 64, 64)
blue = Color(6, 187, 193)
blue1 = Color(21, 239, 246)
yellow = Color(255, 255, 102)
black = Color(0, 0, 0)
white = Color(255, 255, 255)
pink = Color(255, 153, 104)

# flag
action = ""
center = 0
tsp = []
ShortestPath = []

# init pygame
pygame.init()
screen = display.set_mode((WIDTH, HEIGHT), depth=32, flags=RESIZABLE)
background = pygame.Surface((WIDTH, HEIGHT), flags=RESIZABLE)
background.fill(gray)
clock = pygame.time.Clock()
pygame.font.init()

FONT = pygame.font.SysFont('Arial', 20)

manager = pygame_gui.UIManager((WIDTH, HEIGHT))
btnLoad = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((0, 0), (115, 40)),
                                       text='LOAD',
                                       manager=manager)
btnCenter = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((115, 0), (115, 40)),
                                         text='CENTER',
                                         manager=manager)
btnTsp = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((230, 0), (115, 40)),
                                      text='TSP',
                                      manager=manager)
btnShortedPath = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((345, 0), (115, 40)),
                                              text='SHORTEST PATH',
                                              manager=manager)
btnClear = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((460, 0), (115, 40)),
                                        text='CLEAR',
                                        manager=manager)


def scale(data, min_screen, max_screen, min_data, max_data):
    return ((data - min_data) / (max_data - min_data)) * (max_screen - min_screen) + min_screen


min_x = float(min(list(graph.nodes.values()), key=lambda node: node.pos[0]).pos[0])
min_y = float(min(list(graph.nodes.values()), key=lambda node: node.pos[1]).pos[1])
max_x = float(max(list(graph.nodes.values()), key=lambda node: node.pos[0]).pos[0])
max_y = float(max(list(graph.nodes.values()), key=lambda node: node.pos[1]).pos[1])

def gui_scale(data, x=False, y=False):
    if x:
        return scale(data, 50, screen.get_width() - 50, min_x, max_x)
    if y:
        return scale(data, 50, screen.get_height() - 50, min_y, max_y)


# draw
def drawNode(n1: Node, color: Color):
    x = gui_scale(float(n1.pos[0]), x=True)
    y = gui_scale(float(n1.pos[1]), y=True)
    gfxdraw.filled_circle(screen, int(x), int(y),
                          R, color)
    gfxdraw.aacircle(screen, int(x), int(y),
                     R, yellow)
    id_srf = FONT.render(str(n1.id), True, gray)
    rect = id_srf.get_rect(center=(x, y))
    screen.blit(id_srf, rect)


def drawOneEdge(src: Node, dest: Node, color: Color):
    src_x = gui_scale(src.pos[0], x=True)
    src_y = gui_scale(src.pos[1], y=True)
    dest_x = gui_scale(dest.pos[0], x=True)
    dest_y = gui_scale(dest.pos[1], y=True)
    pygame.draw.line(screen, color, (src_x, src_y), (dest_x, dest_y), width=2)


def drawEdges(n: Node, color: Color):
    for k in g_algo.graph.all_out_edges_of_node(n.id):
        dest = g_algo.graph.nodes.get(k)
        drawOneEdge(n, dest, color)


running = True
while running:
    time_delta = clock.tick(60) / 1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == btnLoad:
                    msg = "Please select a json file: "
                    file = easygui.fileopenbox(msg, '')
                    g_algo.load_from_json(file)
                    action = "clear"
                if event.ui_element == btnCenter:
                    center = g_algo.centerPoint()[0]
                    action = "center"
                if event.ui_element == btnTsp:
                    action = "tsp"
                    text = "Enter keys Of Cities: (Example:1 2 3 4)"
                    title = "TSP"
                    output = easygui.enterbox(text, title)
                    listOutput = output.split(" ")
                    listOutput = [int(x) for x in listOutput]
                    tsp = g_algo.TSP(listOutput)[0]

                if event.ui_element == btnShortedPath:
                    action = "ShortestPath"
                    text = "Enter keys Of src & dest:"
                    title = "Shortest Path"
                    output = easygui.enterbox(text, title)
                    listOutput = output.split(" ")
                    src1 = int(listOutput[0])
                    dest1 = int(listOutput[1])
                    print(src1, dest1)
                    ShortestPath = g_algo.shortest_path(src1, dest1)[1]
                    print(ShortestPath)

                if event.ui_element == btnClear:
                    action = "clear"

        manager.process_events(event)
    manager.update(time_delta)
    screen.blit(background, (0, 0))
    manager.draw_ui(screen)

    for n in g_algo.graph.nodes.values():
        drawEdges(n, blue1)

    for n in g_algo.graph.nodes.values():
        drawNode(n, blue)

    if action == "clear":
        for n in g_algo.graph.nodes.values():
            drawEdges(n, blue1)

        for n in g_algo.graph.nodes.values():
            drawNode(n, blue)

    if action == "center":
        n = g_algo.graph.nodes.get(center)
        drawNode(n, pink)
        pygame.display.flip()

    if action == "tsp":
        for i in range(len(tsp) - 1):
            src = g_algo.graph.nodes.get(tsp[i])
            dest = g_algo.graph.nodes.get(tsp[i + 1])
            drawOneEdge(src, dest, pink)
        pygame.display.flip()

    if action == "ShortestPath":
        for i in range(len(ShortestPath) - 1):
            src = g_algo.graph.nodes.get(ShortestPath[i])
            dest = g_algo.graph.nodes.get(ShortestPath[i + 1])
            drawOneEdge(src, dest, pink)
        pygame.display.flip()

    pygame.display.update()

    clock.tick(60)