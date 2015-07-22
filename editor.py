# import the pygame module, so you can use it
import pygame
from pygame.locals import *

# import the pygame module, so you can use it
from config import *

from game import *

# Current cursor position
CURSOR = None

def move_cursor(grid, dx, dy):
    global CURSOR
    x = CURSOR[0]
    y = CURSOR[1]

    print(x, y, dx, dy)

    grid.cells[x][y].uncursor()

    new_x = x + dx
    new_y = y + dy

    if new_x >= SCREEN_CELLS[0] or new_x < 0:
        dx = 0
    if new_y >= SCREEN_CELLS[1] or new_y < 0:
        dy = 0

    grid.cells[x + dx][y + dy].cursor()
    CURSOR = (x + dx, y + dy)

def toggle_cell(grid):
    global CURSOR
    x = CURSOR[0]
    y = CURSOR[1]

    cell = grid.cells[x][y]
    if cell.state is Cell.ALIVE:
        cell.dead()
    else:
        cell.alive()

def main(screen):
    global CURSOR

    # define a variable to control the main loop
    running = True

    grid = Grid(screen, SCREEN_CELLS)
    grid.cells[0][0].cursor()
    CURSOR = (0, 0)

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
            if event.type == KEYDOWN:
                if event.key == K_UP:
                    move_cursor(grid, 0, -1)
                if event.key == K_DOWN:
                    move_cursor(grid, 0, 1)
                if event.key == K_LEFT:
                    move_cursor(grid, -1, 0)
                if event.key == K_RIGHT:
                    move_cursor(grid, 1, 0)
                if event.key in [K_1, K_2, K_3, K_4, K_5, K_6, K_7, K_8, K_9]:
                    toggle_cell(grid)
                if event.key == K_RETURN:
                    grid.cells[CURSOR[0]][CURSOR[1]].uncursor()
                    launch_with_grid(screen, grid)

            print(event)

        grid.draw()
        pygame.display.update()
        #pygame.time.delay(DELAY)

