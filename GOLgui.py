#!/usr/bin/python
from graphics import *
import random
from time import sleep


def initial(D,M,win):    
    #Creates the white board background      
    for i in range (11):
        m = [] # rectangle list
        for j in range (11):
            rec = Rectangle(Point(6 + 4 * i, 6 + 4 * j), Point(10 + 4 * i, 10 + 4 * j))

            D[i][j] = 0
            rec.setFill("white")
            rec.draw(win)    
            m.append(rec)
        M.append(m)


def check(x,y,D):
    #Checks all 9 adjacent neihbors to see if "alive" and checks this number
    #means the cell should stay alive(1), die(0), or if already dead come
    #back alive(2)
    counter = 0

    if D[x+1][y] == 1:
        counter += 1
    if D[x-1][y] == 1:
        counter += 1
    if D[x][y+1] == 1:
        counter += 1
    if D[x][y-1] == 1:
        counter +=1
    if D[x+1][y+1] == 1:
        counter+=1
    if D[x+1][y-1] == 1:
        counter+= 1
    if D[x-1][y-1] == 1:
        counter += 1
    if D[x-1][y+1] == 1:
        counter +=1
    if counter<2 or counter>3:
        return 0
    if counter == 2:
        return 1
    if counter == 3:
        return 2



def main():
    win = GraphWin("Game of Life", 700, 600)
    win. setCoords(0, 0, 70, 60)

    #Initialize two dimesion arrays.
    #D records color of grids, M records rectangles
    D = []
    M = []
    C = []

    #initialize the grids to create all "white"
    for i in range(11):
        d = []
        c = []
        for j in range(11):
            d.append(0)
            c.append(0)
        D.append(d)
        C.append(c)

    initial(D,M,win)
    #Initialzes three "alive" units
    D[5][5],D[4][5] ,D[6][5]= 1,1,1
    C[5][5],C[4][5] ,C[6][5]= 1,1,1
    M[5][5].setFill("Black")
    M[4][5].setFill("Black")
    M[6][5].setFill("Black")

    #Contiually checking
    while True:
        #Purposfully not checking the "Borders" of the array
        for i in range (len(D)-1):
            for j in range(len(D[i])-1):
                #If the cell is alive
                if D[i][j] == 1:
                    #If the cell should die
                    if check(i,j,D) == 0:
                        sleep(1)
                        #Sets a temporary list to white
                        C[i][j] = 0
                        #Fills the cell white
                        M[i][j].setFill("White")
                #if the cell is dead
                if D[i][j] == 0:
                    #If the cell should be revived
                    if check(i,j,D) == 2:
                        sleep(1)
                        #Sets a temporary list to black
                        C[i][j] = 1
                        #Fills the cell black
                        M[i][j].setFill("Black")
        #Sets the main list = to the temporary list                
        D = C


main()
