import math
import sys

import pygame
from pygame import Color, display, gfxdraw
from pygame.constants import RESIZABLE
import pygame_gui

from src.Button import Button
from src.DiGraph import Node
from src.GraphAlgo import GraphAlgo

g_algo = GraphAlgo()
file = '../data/A1.json'
g_algo.load_from_json(file)
graph = g_algo.graph

R, WIDTH, HEIGHT = 15, 1080, 720
pygame.init()
screen = display.set_mode((WIDTH, HEIGHT), depth=32, flags=RESIZABLE)
clock = pygame.time.Clock()
pygame.font.init()

FONT = pygame.font.SysFont('Arial', 20, bold=True)


def scale(data, min_screen, max_screen, min_data, max_data):
    return ((data - min_data) / (max_data - min_data)) * (max_screen - min_screen) + min_screen


# def floatNum(n:Node,i: int):
#     return float(n.pos.split(",")[i])


min_x = float(min(list(graph.nodes.values()), key=lambda node: node.pos[0]).pos[0])
min_y = float(min(list(graph.nodes.values()), key=lambda node: node.pos[1]).pos[1])
max_x = float(max(list(graph.nodes.values()), key=lambda node: node.pos[0]).pos[0])
max_y = float(max(list(graph.nodes.values()), key=lambda node: node.pos[1]).pos[1])


def gui_scale(data, x=False, y=False):
    if x:
        return scale(data, 50, screen.get_width() - 50, min_x, max_x)
    if y:
        return scale(data, 50, screen.get_height() - 50, min_y, max_y)


def drawNode(n1: Node):
    x = gui_scale(float(n1.pos[0]), x=True)
    y = gui_scale(float(n1.pos[1]), y=True)
    gfxdraw.filled_circle(screen, int(x), int(y),
                          R, blue)
    gfxdraw.aacircle(screen, int(x), int(y),
                     R, Color(255, 255, 102))
    id_srf = FONT.render(str(n.id), True, yellow)
    rect = id_srf.get_rect(center=(x, y))
    screen.blit(id_srf, rect)

def draw_arrow(screen, colour, start, end):
    pygame.draw.line(screen,colour,start,end,2)
    rotation = math.degrees(math.atan2(start[1]-end[1], end[0]-start[0]))+90
    pygame.draw.polygon(screen, white, ((end[0]+20*math.sin(math.radians(rotation)),
                                               end[1]+20*math.cos(math.radians(rotation))),
                                              (end[0]+20*math.sin(math.radians(rotation-120)),
                                               end[1]+20*math.cos(math.radians(rotation-120))),
                                              (end[0]+20*math.sin(math.radians(rotation+120)),
                                               end[1]+20*math.cos(math.radians(rotation+120)))))


def DrawArrow(screen, x, y, color, angle=0):
    def rotate(pos, angle):
        cen = (5 + x, 0 + y)
        angle *= -(math.pi / 180)
        cos_theta = math.cos(angle)
        sin_theta = math.sin(angle)
        ret = ((cos_theta * (pos[0] - cen[0]) - sin_theta * (pos[1] - cen[1])) + cen[0],
               (sin_theta * (pos[0] - cen[0]) + cos_theta * (pos[1] - cen[1])) + cen[1])
        return ret

    p0 = rotate((0 + x, -4 + y), angle + 90)
    p1 = rotate((0 + x, 4 + y), angle + 90)
    p2 = rotate((10 + x, 0 + y), angle + 90)

    pygame.draw.polygon(screen, color, [p0, p1, p2])

def drawEdge(n: Node, color: Color):
    src = n
    for k in graph.all_out_edges_of_node(n.id):
        dest = graph.nodes.get(k)
        src_x = gui_scale(src.pos[0], x=True)
        src_y = gui_scale(src.pos[1], y=True)
        dest_x = gui_scale(dest.pos[0], x=True)
        dest_y = gui_scale(dest.pos[1], y=True)

        # pygame.draw.polygon(screen, (0, 0, 0),
        #                     ((0, 100), (0, 200), (200, 200), (200, 300), (300, 150), (200, 0), (200, 100)))

        # DrawArrow(screen, (src_x-10, src_y-10), (dest_x-10, dest_y-10), white)
        pygame.draw.line(screen, color, (src_x, src_y), (dest_x, dest_y))


while (True):
    # check events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)

    screen.fill(gray)

    # plot graph
    for n in graph.nodes.values():
        drawNode(n)
        drawEdge(n, Color(21, 239, 246))

    btnLoad = Button("load", (0, 0), font=20, bg=white)
    btnLoad.show()
    btnSave = Button("save", (40, 0), font=20, bg=white)
    btnSave.show()

    pygame.display.update()

    clock.tick(60)
