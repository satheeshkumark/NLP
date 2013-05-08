import re
import sys
import codecs
import string
from nltk import bigrams
from nltk import trigrams

NgramMap = dict()

def readNgramFile(filename) :
	global NgramMap

	fin = codecs.open(filename)

	for inputline in fin :
		inputline = inputline.strip('\r\n')
		inputline = inputline.strip()
		inputline = inputline.strip('(')
		inputline = inputline.strip(')')
		inputList = inputline.split(',')
		inputList = [element.strip(' ') for element in inputList]
		inputList = [element.strip('\'') for element in inputList]
		inputline = tuple(inputList)
		inputline = ' '.join(inputline)
		if inputline not in NgramMap :
			#print inputline
			NgramMap[inputline] = 0
	fin.close()

def countNgrams(filename,startvalue) :
	global NgramMap
	fin = codecs.open(filename)

	#print 'inside count n grams'

	for inputline in fin :	
		inputline = inputline.strip('\r\n')
		inputline = inputline.strip()
		inputList = inputline.split(' ')
		#print inputline,len(inputList)
		if len(inputList) <= 2 :
			continue
		prevelement1 = inputList[0]
		prevelement2 = inputList[1]
		for i in range(2,len(inputList)):
			currentelement = inputList[i]
			element = prevelement1 + ' ' + prevelement2 + ' ' + currentelement
			#print element			
			if element in NgramMap :
				NgramMap[element] += 1
			else :
				print 'else part'
			prevelement1 = prevelement2
			prevelement2 = currentelement

	fin.close()

	for element in NgramMap :
		if NgramMap[element] > 10 :
			print element,'\t',startvalue
			startvalue += 1
	
if __name__ == '__main__' :
	NgramFile = sys.argv[1]
	tweetinputfile = sys.argv[2]
	startvalue = int(sys.argv[3])
	readNgramFile(NgramFile)
	countNgrams(tweetinputfile,startvalue)
