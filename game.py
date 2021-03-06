#!/usr/bin/env python

from __future__ import print_function

# import the pygame module, so you can use it
import pygame
from pygame.locals import *

import pattern as Pattern
from config import *

import sys
import random

#from IPython.core import ultratb
#sys.excepthook = ultratb.FormattedTB(mode='Verbose',
             #color_scheme='Linux', call_pdb=1)

CELL_SIZE = 8
SCREEN_CELLS = (WIDTH/CELL_SIZE, HEIGHT/CELL_SIZE)

# initialize the pygame module
pygame.init()
pygame.display.set_caption("Game of Life")
screen = pygame.display.set_mode(SCREEN_SIZE)

ALIVE_IMG = pygame.image.load(ALIVE_IMG_PATH).convert()
DEAD_IMG = pygame.image.load(DEAD_IMG_PATH).convert()
CURSOR_DEAD_IMG = pygame.image.load(CURSOR_DEAD_IMG_PATH).convert()
CURSOR_ALIVE_IMG = pygame.image.load(CURSOR_ALIVE_IMG_PATH).convert()

 
class Cell(pygame.Rect):
    DEAD = 0
    ALIVE = 1
    state = DEAD
    next_state = DEAD
    is_cursor = False

    def __init__(self, x, y):
        self.state = self.DEAD
        self.rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, 
                                     CELL_SIZE, CELL_SIZE)
        self.img = DEAD_IMG
        self.location = (self.rect.x, self.rect.y)
    
    # Make cell alive
    def alive(self):
        self.next_state = self.ALIVE
        if self.is_cursor:
            self.img = CURSOR_ALIVE_IMG
        else:
            self.img = ALIVE_IMG

    # Make cell dead
    def dead(self):
        self.next_state = self.DEAD
        if self.is_cursor:
            self.img = CURSOR_DEAD_IMG
        else:
            self.img = DEAD_IMG

    def cursor(self):
        self.is_cursor = True
        if self.state is self.ALIVE:
            self.img = CURSOR_ALIVE_IMG
        else:
            self.img = CURSOR_DEAD_IMG

    def uncursor(self):
        self.is_cursor = False
        if self.state is self.ALIVE:
            self.img = ALIVE_IMG
        else:
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

        self.draw()

    def draw(self):
        for j in xrange(self.height):
            for i in xrange(self.width):
                self.cells[i][j].state = self.cells[i][j].next_state

        for j in xrange(self.height):
            for i in xrange(self.width):
                cell = self.cells[i][j]
                self.screen.blit(cell.img, cell.location)


def initialize(grid, pattern_name):
    cells = grid.cells
    x = SCREEN_CELLS[0] / 2
    y = SCREEN_CELLS[1] / 2

    # If pattern name is not set - fill with random
    if pattern_name is None:
        for j in xrange(grid.height):
            for i in xrange(grid.width):
                if random.randint(0, 1) == 1:
                    cells[i][j].alive()
        return

    # Draw specific pattern
    if pattern_name is 'Blinker':
        pattern = Pattern.blinker
    elif pattern_name is 'Beacon':
        pattern = Pattern.beacon
    elif pattern_name is 'Toad':
        pattern = Pattern.toad
    elif pattern_name is "Pentomino":
        pattern = Pattern.pentomino
    #elif pattern_name is 'Gosper_glider_gun':
        #pattern = Pattern.glider_gun

    for j, row in enumerate(pattern):
        for i, val in enumerate(row):
            if val == 1:
                cells[x + i][y + j].alive()

def launch_with_grid(grid):
    # define a variable to control the main loop
    running = True

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

        grid.update()
        pygame.display.update()
        pygame.time.delay(DELAY)

# define a main function
def launch(screen, pattern=None):
    grid = Grid(screen, SCREEN_CELLS)
    initialize(grid, pattern)
    launch_with_grid(grid)

# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    launch(screen)

