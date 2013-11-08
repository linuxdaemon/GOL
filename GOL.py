#!/usr/bin/python
import random, os, time, sys
#try:
#	from Tkinter import *
#except ImportError:
#	from Tkinter import *

gridhsize = 30
gridvsize = 30

#root = Tk()

def isOnCorner(y,x):
	if (x == gridhsize-1 and y == gridvsize-1) or (x == gridhsize-1 and y == 0) or (x == 0 and y == gridvsize-1) or (x == 0 and y == 0):
		return True
	else:
		return False

def isOnBorder(y,x):
	if (x == gridhsize-1 or x == 0) and not (y == gridvsize-1 or y == 0):
		return True
	elif (y == gridvsize-1 or y == 0) and not (x == gridhsize01 or x == 0):
		return True
	else:
		return False

def onBorder(y,x):
	if isOnBorder(y,x):
		if x == gridhsize-1:
			return "Right"
		elif x == 0:
			return "Left"
		elif y == gridvsize-1:
			return "Bottom"
		elif y == 0:
			return "Top"

def onCorner(y,x):
	if y == 0 and x == 0:
		return "TopLeft"
	elif y == 0 and x == gridhsize-1:
		return "TopRight"
	elif y == gridvsize-1 and x == 0:
		return "BottomLeft"
	elif y == gridvsize-1 and x == gridhsize-1:
		return "BottomRight"

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
				rowText += "[@]"
			elif grid[column][row] == "false":
				rowText += "[ ]"
		print(rowText)

def checkNeighbors(column, row):
	neighbors = 0
	if isOnCorner(row,column):
		corner = True
		whichCorner = onCorner(row,column)
	if isOnBorder(row,column):
		border = True
		whichBorder = onBorder(row,column)
	if not (border or corner):
		for m in [-1,0,1]:
			for n in [-1,0,1]:
				if n == 0 and m == 0: pass
				if grid[column+m][row+n] == "true": neighbors += 1
	elif border:
		if whichBorder == "Top":
			
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
		showGrid()

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

#try:
#	if sys.argv[1] == cli or sys.argv[1] == CLI:
#		CLI()
#	elif sys.argv[1] == gui or sys.argv[1] == GUI:
#		GUI()
#except:
#	print "Usage: "+str(sys.argv[0])+" (CLI/cli|GUI/gui)"
#	print sys.argv[1]
CLI()	
