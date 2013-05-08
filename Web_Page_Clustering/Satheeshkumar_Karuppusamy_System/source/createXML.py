import codecs
import codecs
import string
import re
import sys

fileList = []
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
	#print xmldesc
	printXMLHeader(entityname)	
	
	for key in clusterMap :
		printEntityHeader(key)
		printDocTag(clusterMap[key])
		printEntityTail()		
	
	#printDiscardedTag()

	outputstring += xmltail
	outputstring += '\r\n'
	#print xmltail

#def printDiscardedTag() :
#	global fileList

#	printDiscHead()
#	printDocTag(fileList)
#	printDiscTail()

#def printDiscHead() :
#	global outputstring
#	global discheader
#	outputstring += discheader
#	outputstring += '\r\n'
#	#print dischead

#def printDiscTail() :
#	global outputstring
#	global disctail
#	outputstring += disctail
#	outputstring += '\r\n'	
#	#print disctail

def printDocTag(docList) :
	global docTag
	global docTailTag
	global outputstring

	for element in docList :
		element = int(element)
		outputstring1 = docTag + '\"' + str(element) + '\"' + docTailTag
		outputstring += outputstring1
		outputstring += '\r\n'
		#print outputstring1

def printEntityHeader(clusterid) :
	global entityheader
	global outputstring

	newentityheader = entityheader + '\"' + str(clusterid) + '\"' + '>'
	outputstring += newentityheader
	outputstring += '\r\n'
	#print newentityheader	

def printEntityTail() :
	global entitytail
	global outputstring

	newentitytail = entitytail
	outputstring += newentitytail
	outputstring += '\r\n'
	#print newentitytail

def printXMLHeader(entityname) :
	global xmlheader	
	global outputstring

	newxmlheader = xmlheader + '\"' + entityname + '\">'
	outputstring += newxmlheader
	outputstring += '\r\n'
	#print newxmlheader

def formFileList(maxlen) :
	global fileList
	global outputstring

	fileList = [x for x in range(maxlen + 1)]


def parseARFFFile(arfffilename,mappingfile) :
	global clusterMap
	global fileList
	global outputstring

	fin1 = codecs.open(arfffilename)
	fin2 = codecs.open(mappingfile)

	for inputline1 in fin1 :
		inputline1 = inputline1.strip('\r\n')
		inputline1 = inputline1.strip()
		if(inputline1.startswith('@') or len(inputline1) == 0) :
			continue
		inputlist1 = inputline1.split(',')
		clustername = inputlist1[-1]
		clustername = clustername.strip('cluster')
		clusterid = int(clustername)
		inputline2 = fin2.next()
		inputline2 = inputline2.strip('\r\n')
		inputline2 = inputline2.strip()
		fileid = int(inputline2)
		if clusterid in clusterMap :
			templist = clusterMap[clusterid]
			templist.append(inputline2)
			clusterMap[clusterid] = templist
			fileList.remove(fileid)
		else :
			templist = []
			templist.append(inputline2)
			clusterMap[clusterid] = templist
			fileList.remove(fileid)
	fin1.close()
	fin2.close()

def writeOutputFile(outputfilename) :
	global outputstring
	fout = codecs.open(outputfilename,'w')
	fout.write(outputstring)
	outputstring += '\r\n'
	fout.close()

if __name__ == '__main__' :
	inputfilelength = int(sys.argv[1])
	arfffilename = sys.argv[2]
	mappingfilename = sys.argv[3]
	entityname = sys.argv[4]
	outputfilename = sys.argv[5]

	entityList = entityname.split('_')
	entityname = ' '.join(entityList)

	formFileList(inputfilelength)
	parseARFFFile(arfffilename,mappingfilename)

	printXmlTags(entityname)
	writeOutputFile(outputfilename)
