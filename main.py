#!/usr/bin/env python3
# coding=utf-8
"""
Game of Life implementation
Rules:
    - Any cell with less than 2 neighbors or more than 3 dies
    - Any dead cell with exactly 3 neighbors becomes alive
"""
import os
import random
import time
from copy import deepcopy

import colorama
from colorama import Back, Fore


def display_grid(grid):
    lines = []
    for column in grid:
        row_text = ""
        for cell in column:
            if cell:
                row_text += Back.WHITE + Fore.WHITE + "  " + Back.RESET
            else:
                row_text += "  "
        lines.append(row_text.rstrip())
    os.system('cls' if os.name == 'nt' else 'clear')
    print('\n'.join(lines), flush=True)


def check_neighbors(grid, column, row):
    neighbors = 0
    values = (-1, 0, 1)
    for x in values:
        for y in values:
            if not (x == 0 and y == 0) and 0 < column + x < len(grid) and 0 < row + y < len(grid[column + x]) and \
                    grid[column + x][row + y]:
                neighbors += 1
    return neighbors


def tick_grid(grid):
    grid_cpy = deepcopy(grid)
    for column in range(len(grid_cpy)):
        for row in range(len(grid_cpy[column])):
            neighbors = check_neighbors(grid_cpy, column, row)
            if neighbors < 2:
                grid[column][row] = False
            elif neighbors > 3:
                grid[column][row] = False
            elif neighbors == 3:
                grid[column][row] = True


def main():
    colorama.init()
    grid = [[random.choice((False, True)) for _ in range(50)] for _ in range(50)]
    while True:
        display_grid(grid)
        time.sleep(.3)
        tick_grid(grid)


if __name__ == '__main__':
    main()
