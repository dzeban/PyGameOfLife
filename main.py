#!/usr/bin/env python

import pygame
from pygame.locals import *

import game
from menu import *

#WIDTH = 320
#HEIGHT = 240
WIDTH = 800
HEIGHT = 600
SCREEN_SIZE = (WIDTH, HEIGHT)

menu = None

pygame.init()
pygame.key.set_repeat(199,69) #(delay,interval)

surface = pygame.display.set_mode(SCREEN_SIZE)
surface.fill((51,51,51))

if not pygame.display.get_init():
    pygame.display.init()

if not pygame.font.get_init():
    pygame.font.init()

def reinit(menu):
    surface.fill((51,51,51))
    menu.draw()
    pygame.display.update()

def start_custom_game():
    game.main()
    reinit(menu)

def start_premade_game():
    menu = Menu()
    menu.init(['Blinker', 'Beacon','Toad'], surface)
    reinit(menu)

    while 1:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_UP:
                    menu.draw(-1)

                if event.key == K_DOWN:
                    menu.draw(1)

                if event.key == K_RETURN:
                    pos = menu.get_position()
                    game.main(menu.lista[pos])

                if event.key == K_ESCAPE:
                    return

                pygame.display.update()
            elif event.type == QUIT:
                pygame.display.quit()
                sys.exit()

        pygame.time.wait(8)

if __name__ == "__main__":
    menu = Menu()
    menu.init(['Start custom game','Choose premade constructions','Quit'], surface)
    reinit(menu)

    while 1:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_UP:
                    menu.draw(-1)
                if event.key == K_DOWN:
                    menu.draw(1)
                if event.key == K_RETURN:
                    if menu.get_position() == 2:
                        pygame.display.quit()
                        sys.exit()
                    if menu.get_position() == 0:
                        start_custom_game()
                    if menu.get_position() == 1:
                        start_premade_game()                         
                if event.key == K_ESCAPE:
                    pygame.display.quit()
                    sys.exit()
                pygame.display.update()
            elif event.type == QUIT:
                pygame.display.quit()
                sys.exit()

        pygame.time.wait(8)
