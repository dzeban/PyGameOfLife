Game of Life for ETN device
===========================

Description
-----------

Implementation of John Conway's "Game of Life". 

The Game of Life is a cellular automaton devised by the British mathematician
John Horton Conway in 1970

The "game" is a zero-player game, meaning that its evolution is determined by
its initial state, requiring no further input. One interacts with the Game of
Life by creating an initial configuration and observing how it evolves or, for
advanced players, by creating patterns with particular properties.

The universe of the Game of Life is an infinite two-dimensional orthogonal grid
of square cells, each of which is in one of two possible states, alive or dead.
Every cell interacts with its eight neighbours, which are the cells that are
horizontally, vertically, or diagonally adjacent. At each step in time, the
following transitions occur:

1. Any live cell with fewer than two live neighbours dies, 
   as if caused by under-population.
2. Any live cell with two or three live neighbours lives on 
   to the next generation.
3. Any live cell with more than three live neighbours dies, 
   as if by overcrowding.
4. Any dead cell with exactly three live neighbours becomes 
   a live cell, as if by reproduction.

The initial pattern constitutes the seed of the system. The first generation is
created by applying the above rules simultaneously to every cell in the
seed—births and deaths occur simultaneously, and the discrete moment at which
this happens is sometimes called a tick (in other words, each generation is a
pure function of the preceding one). The rules continue to be applied
repeatedly to create further generations.

Prerequisites
-------------

* python 2
* pygame and its dependencies

To install dependencies, use [pipenv](https://docs.pipenv.org/):

    $ pipenv install pygame

To launch a game just:

    $ pipenv run main.py

To launch a game without X server issue:

	$ export SDL_VIDEODRIVER=directfb
	$ pipenv run main.py

Features:

* Level editor
* Predefined patterns

Level editor
------------

Move cursor with arrows. To toggle cell press keys 1..9. To launch the game
press "Enter".

Predefined patterns
-------------------

Just choose a pattern and see how it evolves.
