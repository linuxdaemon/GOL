#!/usr/bin/python
import random, os, time, sys
from graphics import *

gridhsize = 20
gridvsize = 20
win = GraphWin("Conway's Game of Life",800,800)

def populateGrid():
	global grid
	global grid1 
	grid = {}
	for num in range(gridhsize):
		grid1 = {}
		for num1 in range(gridvsize):
			grid1.update({num1: False})
		grid.update({num: grid1})

def populateGUI():
	''''''
	
def randomizeGrid():
	global grid
	random1 = random.randint(0,gridhsize*gridvsize)
	for num in range(random1):
		column = random.randint(0,gridhsize-1)
		row = random.randint(0,gridvsize-1)
		grid[column][row] = True

def updateCLIGrid():
	os.system('cls' if os.name=='nt' else 'clear')
	for row in range(gridvsize):
		rowText = ""
		for column in range(gridhsize):
			if grid[column][row]:
				rowText += "[+]"
			elif not grid[column][row]:
				rowText += "[ ]"
		print rowText

def checkNeighbors(column, row):
	neighbors = 0
	try:
		if grid[column][row+1]:
			neighbors += 1
	except:
		pass
	try:
		if grid[column][row-1]:
			neighbors += 1
	except:
		pass
	try:
		if grid[column+1][row]:
			neighbors += 1
	except:
		pass
	try:
		if grid[column-1][row]:
			neighbors += 1
	except:
		pass
	try:
		if grid[column+1][row+1]:
			neighbors += 1
	except:
		pass
	try:
		if grid[column+1][row-1]:
			neighbors += 1
	except:
		pass
	try:
		if grid[column-1][row+1]:
			neighbors += 1
	except:
		pass
	try:
		if grid[column-1][row-1]:
			neighbors += 1
	except:
		pass
	return neighbors

def tickGrid():
	global grid
	grid1 = grid
	for column in range(gridhsize):
		for row in range(gridvsize):
			if checkNeighbors(column, row) < 2:
				grid1[column][row] = False
				time.sleep(.001)
			elif checkNeighbors(column, row) > 3:
				grid1[column][row] = False
				time.sleep(.001)
			elif not(grid[column][row]) and checkNeighbors(column,row) == 3:
				grid1[column][row] = True
				time.sleep(.001)
	grid = grid1
	
def updateGUI():
	'''
	global cellFrame
	for column in range(gridhsize):
		for row in range(gridvsize):
			cellFrame[column][row].configure(background='black')
	'''		
def CLI():
	populateGrid()
	randomizeGrid()
	updateGrid()
	while True:
		tickGrid()
		updateGrid()

def GUI():
	populateGrid()
	randomizeGrid()
	populateGUI()
	updateGUI()
	while True:
		tickGrid()

if sys.argv
	if sys.argv[1] == "cli" or sys.argv[1] == "CLI":
		CLI()
	elif sys.argv[1] == "gui" or sys.argv[1] == "GUI":
		GUI()
	else:
		GUI()
	
except ValueError:
	print "Usage: "+str(sys.argv[0])+" (CLI/cli|GUI/gui)"
	print sys.argv[1]
	