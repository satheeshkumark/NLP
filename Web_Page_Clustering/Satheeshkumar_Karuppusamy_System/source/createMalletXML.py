import codecs
import codecs
import string
import re
import sys

clusterMap = dict()

xmldesc = '<?xml version=\"1.0\" encoding=\"UTF-8\"?>'
xmlheader = '<clustering name='
xmltail = '</clustering>'

discheader = '\t<discarded>'
disctail = '\t</discarded>'

entityheader = '\t<entity id='
entitytail = '\t</entity>'

docTag = '\t\t<doc rank='
docTailTag = ' />'
outputstring = ''


def printXmlTags(entityname) :
	global clusterMap
	global outputstring

	outputstring += xmldesc
	outputstring += '\r\n'
	printXMLHeader(entityname)	
	
	for key in clusterMap :
		printEntityHeader(key)
		printDocTag(clusterMap[key])
		printEntityTail()

	outputstring += xmltail
	outputstring += '\r\n'


def printDocTag(docList) :
	global docTag
	global docTailTag
	global outputstring

	for element in docList :
		element = int(element)
		outputstring1 = docTag + '\"' + str(element) + '\"' + docTailTag
		outputstring += outputstring1
		outputstring += '\r\n'

def printEntityHeader(clusterid) :
	global entityheader
	global outputstring

	newentityheader = entityheader + '\"' + str(clusterid) + '\"' + '>'
	outputstring += newentityheader
	outputstring += '\r\n'

def printEntityTail() :
	global entitytail
	global outputstring

	newentitytail = entitytail
	outputstring += newentitytail
	outputstring += '\r\n'

def printXMLHeader(entityname) :
	global xmlheader	
	global outputstring

	newxmlheader = xmlheader + '\"' + entityname + '\">'
	outputstring += newxmlheader
	outputstring += '\r\n'

def writeOutputFile(outputfilename) :
	global outputstring
	fout = codecs.open(outputfilename,'w')
	fout.write(outputstring)
	outputstring += '\r\n'
	fout.close()

def parseInputFile(inputfilename) :
	global clusterMap

	fin1 = codecs.open(inputfilename)

	for inputline in fin1 :
		inputline = inputline.strip('\r\n')
		inputline = inputline.strip()
		if inputline.startswith('#') :
			continue
		inputlist = inputline.split('\t')
		key = inputlist[2]
		value = inputlist[1]
		valueList = value.split('/')
		value = int(valueList[-2])

		if key in clusterMap :
			templist = clusterMap[key]
			templist.append(value)
			clusterMap[key] = templist
		else :
			templist = []
			templist.append(value)
			clusterMap[key] = templist
	fin1.close()

if __name__ == '__main__' :
	entityname = sys.argv[1]
	inputfilename = sys.argv[2]
	outputfilename = sys.argv[3]

	entityList = entityname.split('_')
	entityname = ' '.join(entityList)

	parseInputFile(inputfilename)
	printXmlTags(entityname)
	writeOutputFile(outputfilename)
