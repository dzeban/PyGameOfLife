#!/usr/bin/env python

import pygame
from pygame.locals import *

import game
import editor

from menu import *
from config import *
import sys


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
    editor.main(surface)
    reinit(menu)

def new_menu( options, surface ):
  menu = Menu()
  menu.init(options, surface)
  return(menu)

def start_premade_game():
    sub_options = ['Blinker', 'Beacon','Toad']
    menu = new_menu( sub_options, surface )

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
                    game.launch(surface, menu.lista[pos])
                    reinit(menu)

                if event.key == K_ESCAPE:
                    return

                pygame.display.update()
            elif event.type == QUIT:
                pygame.display.quit()
                sys.exit()

        pygame.time.wait(8)


if __name__ == "__main__":
    main_options = ['Start custom game','Choose premade constructions','Quit']
    menu = new_menu( main_options, surface )

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
                        menu = new_menu( main_options, surface )
                        reinit(menu)

                if event.key == K_ESCAPE:
                    pygame.display.quit()
                    sys.exit()
                pygame.display.update()
            elif event.type == QUIT:
                pygame.display.quit()
                sys.exit()

        pygame.time.wait(8)
