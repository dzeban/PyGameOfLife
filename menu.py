'''
@author: avalanchy (at) google mail dot com
@version: 0.1; python 2.7; pygame 1.9.2pre; SDL 1.2.14; MS Windows XP SP3
@date: 2012-04-08
@license: This document is under GNU GPL v3

README on the bottom of document.

@font: from http://www.dafont.com/coders-crux.font
      more abuot license you can find in data/coders-crux/license.txt
'''

import pygame

if not pygame.display.get_init():
    pygame.display.init()

if not pygame.font.get_init():
    pygame.font.init()

class Menu:
    items = []
    fields = []
    font_size = 20
    font_path = 'data/coders_crux/coders_crux.ttf'
    font = pygame.font.Font
    surface = pygame.Surface
    nitems = 0
    color_bg = (51, 51, 51)
    color_text = (255, 255, 153)
    color_selection = (153, 102, 255)
    position_selected = 0
    position_dest = (0, 0)
    menu_width = 0
    menu_height = 0

    class Field:
        text = ''
        surface = pygame.Surface
        rect = pygame.Rect
        rect_dest = pygame.Rect

    def move_menu(self, top, left):
        self.position_dest = (top, left)

    def set_colors(self, text, selection, background):
        self.color_bg = background
        self.color_text = text
        self.color_selection = selection

    def set_fontsize(self, font_size):
        self.font_size = font_size

    def set_font(self, path):
        self.font_path = path

    def get_position(self):
        return self.position_selected

    def __init__(self, items, surface):
        self.items = items
        self.surface = surface
        self.nitems = len(self.items)
        self.create()

    def draw(self, move=0):
        if move:
            self.position_selected += move

            if self.position_selected == -1:
                self.position_selected = self.nitems - 1

            self.position_selected %= self.nitems

        menu = pygame.Surface((self.menu_width, self.menu_height))
        menu.fill(self.color_bg)

        rect_dest = self.fields[self.position_selected].rect_dest
        pygame.draw.rect(menu, self.color_selection, rect_dest)

        for i in xrange(self.nitems):
            menu.blit(self.fields[i].surface, self.fields[i].rect)

        self.surface.blit(menu, self.position_dest)
        return self.position_selected

    def create(self):
        margin = 0
        self.menu_height = 0
        self.font = pygame.font.Font(self.font_path, self.font_size)

        for i in xrange(self.nitems):
            self.fields.append(self.Field())
            self.fields[i].text = self.items[i]
            self.fields[i].surface = self.font.render(self.fields[i].text, 1, self.color_text)

            self.fields[i].rect = self.fields[i].surface.get_rect()
            margin = int(self.font_size * 0.2)

            height = self.fields[i].rect.height
            self.fields[i].rect.left = margin
            self.fields[i].rect.top = margin + (margin*2 + height) * i

            width = self.fields[i].rect.width + margin * 2
            height = self.fields[i].rect.height + margin * 2
            left = self.fields[i].rect.left - margin
            top = self.fields[i].rect.top - margin

            self.fields[i].rect_dest = (left, top, width, height)
            if width > self.menu_width:
                self.menu_width = width
            self.menu_height += height

        x = self.surface.get_rect().centerx - self.menu_width / 2
        y = self.surface.get_rect().centery - self.menu_height / 2
        mx, my = self.position_dest
        self.position_dest = (x + mx, y + my)
