#!/usr/bin/env python

"""
Nice predefined patterns.
"""

toad = [
        [0, 1, 1, 1],
        [1, 1, 1, 0]
        ]

blinker = [
        [1, 1, 1]
        ]

beacon = [
        [1, 1, 0, 0],
        [1, 1, 0, 0],
        [0, 0, 1, 1],
        [0, 0, 1, 1]
        ]

pentomino = [
        [0, 0, 1, 1, 0],
        [0, 1, 1, 0, 0],
        [0, 0, 1, 0, 0],
        ]

glider_gun = [ [ 0 for i in xrange(37) ] for i in xrange(10) ]
glider_gun[1][25] = 1

glider_gun[2][23] = 1
glider_gun[2][25] = 1

glider_gun[3][22] = 1
glider_gun[3][21] = 1
glider_gun[3][36] = 1
glider_gun[3][35] = 1
glider_gun[3][13] = 1
glider_gun[3][14] = 1


glider_gun[4][22] = 1
glider_gun[4][21] = 1
glider_gun[4][36] = 1
glider_gun[4][35] = 1
glider_gun[4][12] = 1
glider_gun[4][16] = 1

glider_gun[5][22] = 1
glider_gun[5][21] = 1
glider_gun[5][1] = 1
glider_gun[5][2] = 1
glider_gun[5][11] = 1
glider_gun[5][17] = 1

glider_gun[6][23] = 1
glider_gun[6][25] = 1
glider_gun[6][1] = 1
glider_gun[6][2] = 1
glider_gun[6][11] = 1
glider_gun[6][17] = 1
glider_gun[6][15] = 1
glider_gun[6][18] = 1

glider_gun[7][25] = 1
glider_gun[7][11] = 1
glider_gun[7][17] = 1

glider_gun[8][12] = 1
glider_gun[8][16] = 1

glider_gun[9][13] = 1
glider_gun[9][14] = 1

