#!/usr/bin/python
from Tkinter import *
root = Tk()
gridsize = 100
def populateGrid():
	global grid
	global grid1 
	grid = {}
	for num in range(gridsize):
		grid1 = {}
		for num1 in range(gridsize):
			grid1.update({num1: 'false'})
		grid.update({num: grid1})

def populateGUI():
	global cellFrame
	cellFrame = {}
	for num in range(gridsize):
		cellFrame1 = {}
		for num1 in range(gridsize):
			cellFrame1.update({num1: 'false'})
		cellFrame.update({num: cellFrame1})

	for column in range(gridsize):
		colFrame = Frame(root)
		colFrame.pack(side = "top")
		for row in range(gridsize):
			cellFrame[column][row] = Frame(colFrame, height=10,width=10, relief=RAISED, bd=2)
			cellFrame[column][row].pack(side = "left")

populateGUI()
mainloop()
