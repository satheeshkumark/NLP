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
spaceChars = ['\'','\"','\(','\)','\{','\}','\[','\]',':','&amp\;']
titleText = ' '
emailregexpattern = '[^@]+@[^@]+\.[^@]+'
emailTokensSet = set()

def removeValuesFromList(inputList):
	inputList = [element.strip() for element in inputList]
	return [element for element in inputList if len(element) > 0]

def extractTitleInformation(soup) :
	global titleText
	htmlTag = soup.html

	if htmlTag != None :
		headTag = soup.html.head
		if headTag != None :
			titleTag = soup.html.head.title
		else :
			return soup
	else :
		return soup

	if titleTag != None :
		toExtract = soup.title.extract()
		titleText = toExtract.string
		if titleText == None :
			titleText = ' '
	return soup

def extractEmailTokens(sentenceList) :
	global emailregexpattern
	global emailTokensSet
	for inputline in sentenceList :
		inputList = inputline.split()
		for inputelement in inputList :
			if re.match(emailregexpattern,inputelement) :
				emailTokensSet.add(inputelement)
				emailIdList = inputelement.split('@')
				emailid = emailIdList[0].strip()
				emailTokensSet.add(emailid)
	

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
	previouschar = ''
	#print 'replace chars'
	for element in clean :
		#print 'element looping : ',element
		if element in string.printable :
			if element.isupper() and not(previouschar.isupper()) :
				outputstr += ' '			
			outputstr += element
		else :
			outputstr += ' '
		previouschar = element
	replpattern = ' '
	#print 'middle replace char'
	for element in spaceChars :
		outputstr = re.sub(element,replpattern,outputstr)
	#print 'outside replace char'
	return outputstr

# Stripping the content of the html file using mozilla bleach

def stripTags(html,stripTagList) :
	clean = bleach.clean(html, tags=[], strip=True)
	#print 'inside strip tags'
	clean = replaceSpaceChars(clean)
	#print 'outside replace characters'	
	sentenceList = postProcess(clean)
	#print 'outside post process tags'
	extractEmailTokens(sentenceList)
	#print 'outside extract emails'
	return sentenceList

def stripJavaScriptTags(fileContent) :
	global formattingTags
	soup = BeautifulSoup(fileContent)
	if soup != None :
		for element in formattingTags :
			toExtract = soup.findAll(element)
			for item in toExtract:
				item.extract()
		soup = extractTitleInformation(soup)
	return soup

def writeMetaInformation(outputFileName) :
	global titleText
	global emailTokensSet
	emailTokensList = list(emailTokensSet)
	emailTokensWord = '\r\n'.join(emailTokensList)
	outputFileName = outputFileName + '.meta'
	print 'Writing the output in ',outputFileName
	fout = codecs.open(outputFileName,'w')
	if len(titleText.strip()) > 0 :
		titleText = replaceSpaceChars(titleText)
	outputString = titleText + '\r\n' + emailTokensWord
	fout.write(outputString)
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
	#print 'inside strip formatting tags'
	fileContent = stripJavaScriptTags(fileContent)
	#print 'outside strip formatting tags'
	stripTags(fileContent,formattingTags)
	#print 'outside strip tags'
	return sentenceList

if __name__ == '__main__' :
	inputFileName = sys.argv[1]
	outputFileName = sys.argv[2]
	
	fin = codecs.open(inputFileName,encoding = 'iso-8859-1')
	fileContent = fin.read()
	fin.close()
	print 'pre processing'
	sentenceList = stripFormattingTags(fileContent)
	print 'done with preprocessing - writing the output to the outputfile'

	writeOutput(inputFileName,outputFileName,sentenceList)
	print 'done with post processing - writing the meta information to the outputfile'
	writeMetaInformation(outputFileName)

