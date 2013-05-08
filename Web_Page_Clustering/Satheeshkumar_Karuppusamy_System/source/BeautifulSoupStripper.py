from bs4 import BeautifulSoup
import codecs
import bleach
import codecs
import string
from nltk.tokenize import sent_tokenize
import re
import sys

sentenceList = []
formattingTags = ['script','style','noscript']
spaceChars = ['\'','\"','-','\(','\)','\{','\}','\[','\]',':','&amp\;']
titleText = ''

def removeValuesFromList(inputList):
	inputList = [element.strip() for element in inputList]
	return [element for element in inputList if len(element) > 0]

def extractMetaInformation(soup) :
	global titleText
	toExtract = soup.title.extract()
	titleText = toExtract.string
	return soup

def postProcess(clean) :
	global sentenceList
	inputList = clean.split('\n')
	inputList = removeValuesFromList(inputList)
	inputText = ' '.join(inputList)
	inputList = sent_tokenize(inputText)
	for element in inputList :
		sentenceList.append(element)
	return sentenceList

def replaceSpaceChars(clean) :
	global spaceChars	
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
	soup = BeautifulSoup(fileContent)
	clean = soup.get_text()
	print clean
	clean = replaceSpaceChars(clean)	
	sentenceList = postProcess(clean)
	return sentenceList

def stripJavaScriptTags(fileContent) :
	global formattingTags
	soup = BeautifulSoup(fileContent)
	for element in formattingTags :
		toExtract = soup.findAll(element)
		for item in toExtract:
			item.extract()
	soup = extractMetaInformation(soup)
	return soup

def writeMetaInformation(outputFileName) :
	global titleText
	outputFileName = outputFileName + '.meta'
	print 'Writing the output in ',outputFileName
	fout = codecs.open(outputFileName,'w')
	fout.write(titleText)
	fout.close()

def writeOutput(inputFileName,outputFileName,sentenceList) :
	print 'Writing the output in ',outputFileName
	fout = codecs.open(outputFileName,'w')
	for element in sentenceList :
		element = element + '\r\n'
		fout.write(element)
	fout.close()

def stripFormattingTags(fileContent) :
	global formattingTags
	fileContent = stripJavaScriptTags(fileContent)
	striptTags(fileContent,formattingTags)
	return sentenceList

if __name__ == '__main__' :
	#inputFileName = sys.argv[1]
	inputFileName = 'index.html'
	#outputFileName = sys.argv[2]
	outputFileName = 'index_out.html'
	fin = codecs.open(inputFileName,encoding = 'iso-8859-1')
	fileContent = fin.read()
	fin.close()
	sentenceList = stripFormattingTags(fileContent)
	writeOutput(inputFileName,outputFileName,sentenceList)
	writeMetaInformation(outputFileName)
