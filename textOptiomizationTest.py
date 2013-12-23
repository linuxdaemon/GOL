#!/usr/bin/env python3

def remTrailWhite(text):
	if text == 40 * "  ":
		text = ""
	elif text[-2:] == "  ":
		text = remTrailWhite(text[:-2])
	return text

def optimizeText(text):
	newText = ""
	splitText = text.split("\n")
	for line in splitText:
		if line:
			text = remTrailWhite(line)
		newText += text + "\n"
	return newText

row = (20 * "..  ") + "\n"
blankRow = (40 * "  ") + "\n"

grid = 20 * (row + blankRow)
print(optimizeText(grid))
