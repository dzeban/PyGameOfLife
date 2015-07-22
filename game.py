#!/usr/bin/env python

from __future__ import print_function

# import the pygame module, so you can use it
import pygame
from pygame.locals import *

import sys
import random

#from IPython.core import ultratb
#sys.excepthook = ultratb.FormattedTB(mode='Verbose',
             #color_scheme='Linux', call_pdb=1)

#WIDTH = 320
#HEIGHT = 240
WIDTH = 800
HEIGHT = 600
SCREEN_SIZE = (WIDTH, HEIGHT)

CELL_SIZE = 8
SCREEN_CELLS = (WIDTH/CELL_SIZE, HEIGHT/CELL_SIZE)

# initialize the pygame module
pygame.init()
pygame.display.set_caption("Game of Life")
screen = pygame.display.set_mode(SCREEN_SIZE)

ALIVE_IMG = pygame.image.load("data/alive.png").convert()
DEAD_IMG = pygame.image.load("data/dead.png").convert()
 
class Cell(pygame.Rect):
    DEAD = 0
    ALIVE = 1
    state = DEAD
    next_state = DEAD

    def __init__(self, x, y):
        self.state = self.DEAD
        self.rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, 
                                     CELL_SIZE, CELL_SIZE)
        self.img = DEAD_IMG
        self.location = (self.rect.x, self.rect.y)
    
    # Make cell alive
    def alive(self):
        self.next_state = self.ALIVE
        self.img = ALIVE_IMG

    # Make cell dead
    def dead(self):
        self.next_state = self.DEAD
        self.img = DEAD_IMG
    
class Grid:
    def __init__(self, screen, dimensions):
        self.width = dimensions[0]
        self.height = dimensions[1]
        self.screen = screen
        self.cells = []

        self.cells = [[None for x in xrange(self.height)] for x in xrange(self.width)] 

        for j in xrange(self.height):
            for i in xrange(self.width):
                self.cells[i][j] = Cell(i, j)

    # Calculate next cell state based on neighbors state.
    # Game rules implementation.
    def update_cell(self, cell, neighbors):
        alives = 0

        for n in neighbors:
            if n.state is Cell.ALIVE:
                alives = alives + 1

        if cell.state is Cell.DEAD:
            if alives == 3:
                cell.alive()
        else:
            if (alives < 2) or (alives > 3):
                cell.dead()

    # Get neighbors for (i, j) cell from grid
    def get_neighbors(self, i, j):
        neighbors = []

        # Size of a grid
        X = self.width - 1
        Y = self.height - 1

        # WTF?
        indices = lambda x, y : [(x2, y2) for x2 in range(x-1, x+2)
                                               for y2 in range(y-1, y+2)
                                                   if (-1 < x <= X and
                                                       -1 < y <= Y and
                                                       (x != x2 or y != y2) and
                                                       (0 <= x2 <= X) and
                                                       (0 <= y2 <= Y))]

        neighbors = []
        for pos in indices(i, j):
            neighbors.append(self.cells[pos[0]][pos[1]])

        return neighbors

    # Update whole grid
    def update(self):
        for j in xrange(self.height):
            for i in xrange(self.width):
                neighbors = self.get_neighbors(i, j)
                self.update_cell(self.cells[i][j], neighbors)

        for j in xrange(self.height):
            for i in xrange(self.width):
                self.cells[i][j].state = self.cells[i][j].next_state

        for j in xrange(self.height):
            for i in xrange(self.width):
                cell = self.cells[i][j]
                self.screen.blit(cell.img, cell.location)

def initialize(grid, pattern):
    cells = grid.cells
    i = SCREEN_CELLS[0] / 2
    j = SCREEN_CELLS[1] / 2
    print(i, j, len(cells))
    if pattern is 'Blinker':
        cells[i][j - 1].alive()
        cells[i][j].alive()
        cells[i][j + 1].alive()
    elif pattern is 'Beacon':
        cells[i - 2][j - 2].alive()
        cells[i - 1][j - 2].alive()
        cells[i - 2][j - 1].alive()
        cells[i - 1][j - 1].alive()

        cells[i][j].alive()
        cells[i + 1][j].alive()
        cells[i][j + 1].alive()
        cells[i + 1][j + 1].alive()

    elif pattern is 'Toad':
        cells[i - 2][j + 1].alive()
        cells[i - 1][j + 1].alive()
        cells[i][j + 1].alive()
        cells[i - 1][j].alive()
        cells[i][j].alive()
        cells[i + 1][j].alive()
    else:
        for j in xrange(grid.height):
            for i in xrange(grid.width):
                if random.randint(0, 1) == 1:
                    cells[i][j].alive()

# define a main function
def main(pattern=None):

    # define a variable to control the main loop
    running = True

    grid = Grid(screen, SCREEN_CELLS)
    initialize(grid, pattern)

    # main loop
    while running:
        # event handling, gets all event from the eventqueue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
            if event.key == K_ESCAPE:
                return
            print(event)

        grid.update()
        pygame.display.update()
        pygame.time.delay(30)


# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()

