#!/usr/bin/python
import random, os, time, sys
try:
	from Tkinter import *
except ImportError:
	from Tkinter import *

gridhsize = 20
gridvsize = 20

root = Tk()

def populateGrid():
	global grid
	global grid1 
	grid = {}
	for num in range(gridhsize):
		grid1 = {}
		for num1 in range(gridvsize):
			grid1.update({num1: 'false'})
		grid.update({num: grid1})

def populateGUI():
	global cellFrame
	cellFrame = {}
	for num in range(gridhsize):
		cellFrame1 = {}
		for num1 in range(gridvsize):
			cellFrame1.update({num1: ' '})
		cellFrame.update({num: cellFrame1})

	for column in range(gridhsize):
		colFrame = Frame(root)
		colFrame.pack(side = "top")
		for row in range(gridvsize):
			cellFrame[column][row] = Frame(colFrame, height=10,width=10, relief=RAISED, bd=2)
			cellFrame[column][row].pack(side = "left")

def randomizeGrid():
	global grid
	random1 = random.randint(0,gridhsize*gridvsize)
	for num in range(random1):
		column = random.randint(0,gridhsize-1)
		row = random.randint(0,gridvsize-1)
		grid[column][row] = "true"

def showGrid():
	os.system('cls' if os.name=='nt' else 'clear')
	for row in range(gridvsize):
		rowText = ""
		for column in range(gridhsize):
			if grid[column][row] == "true":
				rowText = rowText+"[+]"
			elif grid[column][row] == "false":
				rowText = rowText+"[ ]"
		print rowText

def checkNeighbors(column, row):
	neighbors = 0
	try:
		if grid[column][row+1] == "true":
			neighbors = neighbors+1
	except:
		pass
	try:
		if grid[column][row-1] == "true":
			neighbors = neighbors+1
	except:
		pass
	try:
		if grid[column+1][row] == "true":
			neighbors = neighbors+1
	except:
		pass
	try:
		if grid[column-1][row] == "true":
			neighbors = neighbors+1
	except:
		pass
	try:
		if grid[column+1][row+1] == "true":
			neighbors = neighbors+1
	except:
		pass
	try:
		if grid[column+1][row-1] == "true":
			neighbors = neighbors+1
	except:
		pass
	try:
		if grid[column-1][row+1] == "true":
			neighbors = neighbors+1
	except:
		pass
	try:
		if grid[column-1][row-1] == "true":
			neighbors = neighbors+1
	except:
		pass
	return neighbors

def tickGrid():
	global grid
	grid1 = grid
	for column in range(gridhsize):
		for row in range(gridvsize):
			if checkNeighbors(column, row) < 2:
				grid1[column][row] = "false"
				time.sleep(.001)
			elif checkNeighbors(column, row) > 3:
				grid1[column][row] = "false"
				time.sleep(.001)
			elif grid[column][row] == "false" and checkNeighbors(column, row) == 3:
				grid1[column][row] = "true"
				time.sleep(.001)
	grid = grid1
	showGrid()
	
def updateGUI():
	global cellFrame
	for column in range(gridhsize):
		for row in range(gridvsize):
			cellFrame[column][row].configure(background='black')
			
def CLI():
	populateGrid()
	randomizeGrid()
	showGrid()
	while True:
		tickGrid()

def GUI():
	populateGrid()
	randomizeGrid()
	'''
	while True:
		tickGrid()
	'''
	populateGUI()
	mainloop()
	updateGUI()

try:
	if sys.argv[1] == cli or sys.argv[1] == CLI:
		CLI()
	elif sys.argv[1] == gui or sys.argv[1] == GUI:
		GUI()
except:
	print "Usage: "+str(sys.argv[0])+" (CLI/cli|GUI/gui)"
	print sys.argv[1]
	
