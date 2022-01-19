import enum
import pygame as pg
from random import random
from collections import deque

def get_rect(x, y): 
     return x * TILE + 1, y * TILE + 1, TILE - 2, TILE - 2

def get_next_nodes(x, y):
    check_next_node = lambda x, y: True if  0 <= x < cols and 0 <= y < rows and not grid[y][x] else False
    ways = [-1, 0], [0, -1], [1, 0], [0, 1]
    return [(x + dx, y + dy) for dx, dy in ways if check_next_node(x + dx, y + dy)]

cols, rows = 25, 15
TILE = 60

pg.init()
sc = pg.display.set_mode([cols * TILE, rows * TILE])
clock = pg.time.Clock()

grid = [[1 if random() < 0.2 else 0 for col in range(cols)] for row in range(rows)]

graph = {}
for y, row in enumerate(grid):
    for x, col in enumerate(row):
        if not col:
            graph[(x, y)] =  graph.get((x, y), []) + get_next_nodes(x,y)

while True:
    #fill screeen
    sc.fill(pg.Color('black'))
    #draw grid
    [[pg.draw.rect(sc, pg.Color('darkorange'), get_rect(x, y), border_radius = TILE // 5) for x, col in enumerate(row) if col] for y, row in enumerate(grid)]

    #pygame nessecery lines
    [exit() for event in pg.event.get() if event.type == pg.QUIT]
    pg.display.flip()
    clock.tick(7)