import sys
import re


def normalize(inputstring) :
	previous = ''
	count = 0
	outputstring = ''
	lenvalue = len(inputstring)
	currentindex = 0
	for character in inputstring :
		if currentindex == 0 :
			previous = character
			count = 1
			currentindex = 1
			continue
		if character == previous :
			count += 1
		elif character != previous and count >= 2 :
			outputstring += (previous) * 2
			count = 1
		elif character != previous and count < 2 :
			outputstring += previous
			count = 1
		previous = character
	
	if count >= 2 :
		outputstring += (previous) * 2
		count = 1
	elif count < 2 :
		outputstring += previous
		count = 1
	
	return outputstring	
		
