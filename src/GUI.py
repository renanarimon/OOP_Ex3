import math
import sys

import pygame
from pygame import Color, display, gfxdraw
from pygame.constants import RESIZABLE
import pygame_gui
import numpy as np

from src.DiGraph import Node
from src.GraphAlgo import GraphAlgo
from src.InputBox import InputBox

g_algo = GraphAlgo()
file = '../data/A1.json'
g_algo.load_from_json(file)
graph = g_algo.graph

R, WIDTH, HEIGHT = 15, 1080, 720
gray = Color(64, 64, 64)
blue = Color(6, 187, 193)
yellow = Color(255, 255, 102)
black = Color(0, 0, 0)
white = Color(255, 255, 255)
pink = Color(255, 153, 104)

user_text = ""
color_active = white
color_pasive = black
color = color_pasive
active = False

# input_box = pygame.Rect(100, 100, 140, 32)
# text = ""

tsp = False

input_box1 = InputBox(100, 100, 140, 32)
# input_box2 = InputBox(100, 300, 140, 32)
# input_boxes = [input_box1, input_box2]

pygame.init()
screen = display.set_mode((WIDTH, HEIGHT), depth=32, flags=RESIZABLE)
background = pygame.Surface((WIDTH, HEIGHT), flags=RESIZABLE)
background.fill(gray)
clock = pygame.time.Clock()
pygame.font.init()

FONT = pygame.font.SysFont('Arial', 20)

manager = pygame_gui.UIManager((WIDTH, HEIGHT))
btnCenter = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((0, 0), (110, 50)),
                                         text='CENTER',
                                         manager=manager)
btnTsp = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((100, 0), (110, 50)),
                                      text='TSP',
                                      manager=manager)
btnShortedPath = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((200, 0), (110, 50)),
                                              text='SHORTED PATH',
                                              manager=manager)

cen = False
node = Node(0)


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


def drawNode(n1: Node, color: Color):
    x = gui_scale(float(n1.pos[0]), x=True)
    y = gui_scale(float(n1.pos[1]), y=True)
    gfxdraw.filled_circle(screen, int(x), int(y),
                          R, color)
    gfxdraw.aacircle(screen, int(x), int(y),
                     R, yellow)
    id_srf = FONT.render(str(n.id), True, yellow)
    rect = id_srf.get_rect(center=(x, y))
    screen.blit(id_srf, rect)


def drawEdge(n: Node, color: Color):
    src = n
    for k in graph.all_out_edges_of_node(n.id):
        dest = graph.nodes.get(k)
        src_x = gui_scale(src.pos[0], x=True)
        src_y = gui_scale(src.pos[1], y=True)
        dest_x = gui_scale(dest.pos[0], x=True)
        dest_y = gui_scale(dest.pos[1], y=True)

        pygame.draw.line(screen, color, (src_x, src_y), (dest_x, dest_y))


def text1(word, x, y):
    text = FONT.render("{}".format(word), True, white)
    return screen.blit(text, (x, y))


def inpt():
    word = ""
    text1("Please enter numbers: ", 300, 400)  # example asking name
    pygame.display.flip()
    done = True
    while done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    word += str(chr(event.key))
                if event.key == pygame.K_b:
                    word += chr(event.key)
                if event.key == pygame.K_c:
                    word += chr(event.key)
                if event.key == pygame.K_d:
                    word += chr(event.key)
                if event.key == pygame.K_RETURN:
                    done = False
                # events...
    return text1(word, 100, 50)


ev = None
running = True
while running:
    time_delta = clock.tick(60) / 1000.0
    # check events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == btnCenter:
                    center = g_algo.centerPoint()[0]
                    node = graph.nodes.get(center)

                if event.ui_element == btnTsp:
                    for e in pygame.event.get():
                        if e.type == pygame.KEYDOWN:
                            if e.key == pygame.K_BACKSPACE:
                                user_text = user_text[:-1]
                            else:
                                user_text += e.unicode
                    tsp = True
                    ev = event
                    print("tsp")

                    # input_box.colliderect()
                    # w = inpt()
                    # print(w)

        manager.process_events(event)
    manager.update(time_delta)
    screen.blit(background, (0, 0))
    manager.draw_ui(screen)

    # screen.fill(gray)

    if cen:
        drawNode(node, pink)
        cen = False
        pygame.display.update()

    elif tsp:
        input_box1.draw(screen)
        input_box1.handle_event(ev)
        x = inpt()
        tsp = False

    for n in graph.nodes.values():
        drawNode(n, blue)
        drawEdge(n, Color(21, 239, 246))

    pygame.display.update()

    clock.tick(60)
