#!/usr/bin/env python3
import os
import random
import time

import colorama

colorama.init()

gridhsize = 50
gridvsize = 50


def populateGrid():
    global grid
    global grid1
    grid = {}
    for num in range(gridhsize):
        grid1 = {}
        for num1 in range(gridvsize):
            grid1.update({num1: False})
        grid.update({num: grid1})


def randomizeGrid():
    global grid
    random1 = random.randint(0, gridhsize * gridvsize)
    for num in range(random1):
        column = random.randint(0, gridhsize - 1)
        row = random.randint(0, gridvsize - 1)
        grid[column][row] = True


def remTrailWhite(text):
    # Removes trailing whitespace
    if text == gridhsize * "  ":
        text = ""
    elif text[-2:] == "  ":
        text = remTrailWhite(text[:-2])
    return text


def optimizeText(rowText):
    newText = ""
    splitText = rowText.split("\n")
    for text in splitText:
        if text:
            text = remTrailWhite(text)
        newText += text + "\n"
    return newText


def showGrid():
    os.system('cls' if os.name == 'nt' else 'clear')
    rowText = ""
    for row in range(gridvsize):
        for column in range(gridhsize):
            if grid[column][row]:
                rowText += colorama.Back.WHITE + colorama.Fore.WHITE + "  " + colorama.Back.RESET
            elif not grid[column][row]:
                rowText += "  "
        rowText += "\n"
    print(optimizeText(rowText))


def checkNeighbors(column, row):
    neighbors = 0
    values = [-1, 0, 1]
    for x in values:
        for y in values:
            if not (x == 0 and y == 0):
                try:
                    if grid[column + x][row + y]:
                        neighbors += 1
                except KeyError:
                    pass
    return neighbors


def tickGrid():
    global grid
    grid1 = grid
    for column in range(gridhsize):
        for row in range(gridvsize):
            neighbors = checkNeighbors(column, row)
            if neighbors < 2:
                grid1[column][row] = False
            elif neighbors > 3:
                grid1[column][row] = False
            elif not (grid[column][row]) and neighbors == 3:
                grid1[column][row] = True
    grid = grid1
    showGrid()


def main():
    populateGrid()
    randomizeGrid()
    showGrid()
    while True:
        tickGrid()
        time.sleep(.3)


if __name__ == '__main__':
    main()
