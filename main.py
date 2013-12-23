#!/usr/bin/env python3
import random, os, time, sys, math
import colorama
colorama.init()

try:
	from Tkinter import *
except ImportError:
	try:
		from tkinter import *
	except ImportError:
		GUI = False

gridhsize = 50
gridvsize = 50
#try:
#	root = Tk()
#except:
#	pass

def populateGrid():
	global grid
	global grid1 
	grid = {}
	for num in range(gridhsize):
		grid1 = {}
		for num1 in range(gridvsize):
			grid1.update({num1: False})
		grid.update({num: grid1})

#def populateGUI():
#	global cellFrame
#	cellFrame = {}
#	for num in range(gridhsize):
#		cellFrame1 = {}
#		for num1 in range(gridvsize):
#			cellFrame1.update({num1: ' '})
#		cellFrame.update({num: cellFrame1})
#
#	for column in range(gridhsize):
#		colFrame = Frame(root)
#		colFrame.pack(side = "top")
#		for row in range(gridvsize):
#			cellFrame[column][row] = Frame(colFrame, height=10,width=10, relief=RAISED, bd=2)
#			cellFrame[column][row].pack(side = "left")

def randomizeGrid():
	global grid
	random1 = random.randint(0, gridhsize * gridvsize)
	for num in range(random1):
		column = random.randint(0, gridhsize-1)
		row = random.randint(0, gridvsize-1)
		grid[column][row] = True

def remTrailWhite(text):
	#Removes trailing whitespace
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
	os.system('cls' if os.name=='nt' else 'clear')
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
	values = [-1,0,1]
	for x in values:
		for y in values:
			if not (x == 0 and y == 0):
				try:
					if grid[column+x][row+y]:
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
			elif not(grid[column][row]) and neighbors == 3:
				grid1[column][row] = True
	grid = grid1
	showGrid()

#def updateGUI():
#	global cellFrame
#	for column in range(gridhsize):
#		for row in range(gridvsize):
#			cellFrame[column][row].configure(background='black')
			
def CLI():
	#iterations = 0
	populateGrid()
	randomizeGrid()
	showGrid()
	while True:
		tickGrid()
		time.sleep(.3)
		#iterations += 1
		#if iterations % 100 == 0:
			

#def GUI():
#	populateGrid()
#	randomizeGrid()
#	'''
#	while True:
#		tickGrid()
#	'''
#	populateGUI()
#	mainloop()
#	updateGUI()

try:
	if sys.argv[1] == "cli" or sys.argv[1] == "CLI":
		CLI()
	elif sys.argv[1] == "gui" or sys.argv[1] == "GUI":
		GUI()
except IndexError:
	print("Usage: "+str(sys.argv[0])+" (CLI/cli|GUI/gui)")
	print(sys.argv[1])
	
