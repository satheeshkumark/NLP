import sys
import codecs

uniqueterms = set()
uniquetermids = dict()
unigramcountmap = dict()
bigramterms = set()
bigramtermids = dict()

def findUnigramFreq(inputline,fout) :
	global uniquetermids
	inputline = inputline.strip('\r\n')
	inputline = inputline.strip('\n')
	inputline = inputline.strip(' ')
	inputlist = inputline.split(' ')
	tempmap = dict()
	tempmap.clear()
	classid = 0
	finalelement = ''
	sortedlist = []

	for element in inputlist :
		element = element.lstrip('#')
		element1 = uniquetermids[element]	
		if element1 in tempmap :
			tempmap[element1] += 1
		else :
			tempmap[element1] = 1
		finalelement = element

	classid = classlist.index(finalelement)
	outputstring = ''	
	
	sortedlist = tempmap.keys()
	sortedlist.sort()	

	for key in sortedlist :
		outputstring += str(key) + ":" + str(tempmap[key]) + ' '

	outputstring = str(classid) + '\t' + outputstring
	outputstring = outputstring.strip(' ') 
	outputstring += '\n'
	#print 'unigram frequencies'
	#print outputstring
	fout.write(outputstring)

def findBigramFreq(inputline,fout1) :
	global bigramtermids
	inputline = inputline.strip('\r\n')
	inputline = inputline.strip('\n')
	inputline = inputline.strip(' ')
	inputlist = inputline.split(' ')
	tempmap = dict()
	tempmap.clear()
	currentterm = ''
	classid = 0

	previousterm = '<s>'
	for element in inputlist :
		element = element.lstrip('#')	
		currentterm = previousterm + '$#_#$' + element
		element1 = bigramtermids[currentterm]
		if element1 in tempmap :
			tempmap[element1] += 1
		else :
			tempmap[element1] = 1
		previousterm = element
	currentterm = previousterm + '$#_#$' + '</s>'
	element1 = bigramtermids[currentterm]

	classid = classlist.index(previousterm)

	if element1 in tempmap :
		tempmap[element1] += 1
	else :
		tempmap[element1] = 1	
	
	outputstring = ''

	for key in tempmap :
		outputstring += str(key) + ":" + str(tempmap[key]) + ' '

	outputstring = str(classid) + '\t' + outputstring
	outputstring = outputstring.strip(' ') 
	outputstring += '\n'
	#print 'bigram frequencies'
	fout1.write(outputstring)


def findFrequencies(inputfilename) :
	fin = codecs.open(inputfilename,'UTF-8')

	for inputline in fin :
		inputline = inputline.strip('\r\n')
		inputline = inputline.strip('\n')
		inputline = inputline.strip()
		inputlist = inputline.split(' ')
		previousterm = '<s>'
		currentterm = ''
		for element in inputlist :
			element = element.lstrip('#')
			currentterm = previousterm + '$#_#$' + element
			bigramterms.add(currentterm)
			uniqueterms.add(element)
			previousterm = element
		currentterm = previousterm + '$#_#$' + '</s>'
		#print currentterm
		bigramterms.add(currentterm)

	i = 1
	for element in uniqueterms :
		uniquetermids[element] = i
		i = i + 1
	#print 'number of unique unigram terms',len(uniqueterms),i

	i = 1
	for element in bigramterms :	
		bigramtermids[element] = i
		i = i + 1		

	#print 'number of unique bigram terms',len(bigramterms),i
	fin.close()

def readUnigrams(unigramfilename) :
	global uniqueterms

	fin = codecs.open(unigramfilename)

	for inputline in fin :
		inputline = inputline.strip('\r\n')
		inputline = inputline.strip()
		uniqueterms.add(inputline)

	fin.close()
	
def readBigrams(bigramfilename) :
	global bigramterms

	fin = codecs.open(bigramfilename)

	for inputline in fin :
		inputline = inputline.strip('\r\n')
		inputline = inputline.strip()
		bigramterms.add(inputline)

	fin.close()

if __name__ == '__main__' :
	test_train_option = sys.argv[1]
	unigramfilename = sys.argv[2]
	bigramfilename = sys.argv[3]
	inputfilename = sys.argv[4]
	outputunigramfilename = unigramfilename + test_train_option + '.frequency'
	outputbigramfilename = bigramfilename + test_train_option + '.frequency'

	readUnigrams(unigramfilename)
	readBigrams(bigramfilename)

	findFrequencies(inputfilename)

	fin = codecs.open(inputfilename,'UTF-8')
	fout = codecs.open(outputunigramfilename,'w')
	fout1 = codecs.open(outputbigramfilename,'w')	
	for inputline in fin :
		findUnigramFreq(inputline,fout)
		findBigramFreq(inputline,fout1)
	fout.close()
	fout1.close()
	fin.close()
