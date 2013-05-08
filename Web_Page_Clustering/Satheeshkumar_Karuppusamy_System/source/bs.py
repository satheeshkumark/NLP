from bs4 import BeautifulSoup
import codecs
import bleach
import codecs
import string
from nltk.tokenize import sent_tokenize
import re

sentenceList = []
formattingTags = ['script','style','noscript']
spaceChars = ['\'','\"','-','\(','\)','\{','\}','\[','\]',':','\,','\&amp\;','\;']

def removeValuesFromList(inputList):
	inputList = [element.strip() for element in inputList]
	return [element for element in inputList if len(element) > 0]

def postProcess(clean) :
	global sentenceList
	inputList = clean.split('\n')
	inputList = removeValuesFromList(inputList)
	inputText = ' '.join(inputList)
	inputList = sent_tokenize(inputText)
	for element in inputList :
		sentenceList.append(element)
		print element
	return sentenceList

def replaceSpaceChars(clean) :
	global spaceChars

	#clean = filter(lambda x: x in string.printable, clean)
	
	outputstr = ''
	for element in clean :
		if element in string.printable :
			outputstr += element
		else :
			outputstr += ' '
		
	replpattern = ' '
	for element in spaceChars :
		outputstr = re.sub(element,replpattern,outputstr)
	return outputstr

# Stripping the content of the html file using mozilla bleach

def striptTags(html,stripTagList) :
	clean = bleach.clean(html, tags=[], strip=True)
	clean = replaceSpaceChars(clean)
	#print clean	
	postProcess(clean)

def stripJavaScriptTags(fileContent) :
	global formattingTags
	soup = BeautifulSoup(fileContent)
	for element in formattingTags :
		toExtract = soup.findAll(element)
		for item in toExtract:
			item.extract()
	return soup

def stripFormattingTags(fileContent) :
	global formattingTags
	fileContent = stripJavaScriptTags(fileContent)
	striptTags(fileContent,formattingTags)

if __name__ == '__main__' :
	inputFileName = sys.argv[1]	
	#inputFileName = '../data/index2.html'
	fin = codecs.open(inputFileName,encoding = 'iso-8859-1')
	fileContent = fin.read()
	fin.close()
	stripFormattingTags(fileContent)
