import sys
import codecs

uniqueterms = set()
uniquetermids = dict()
unigramcountmap = dict()
bigramterms = set()
bigramtermids = dict()
featureid = 1
classList = []

keyword1 = ['#joy', '#joyful', '#enjoy', '#enjoying', '#happy', '#happiness', '#ecstatic']
keyword2 = ['#sad', '#sadness']

posClassValue = 1
negClassValue = -1


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


def findFeatureIds() :
	global uniqueterms
	global bigramterms
	global uniquetermids
	global bigramtermids
	global featureid	

	for element in uniqueterms :
		uniquetermids[element] = featureid
		featureid = featureid + 1

	for element in bigramterms :	
		bigramtermids[element] = featureid
		featureid = featureid + 1


def findUnigramFreq(inputline,tempmap) :
	global uniquetermids
	inputline = inputline.strip('\r\n')
	inputline = inputline.strip(' ')
	inputlist = inputline.split(' ')

	for element in inputlist :
		if element in uniqueterms :
			element1 = uniquetermids[element]	
			if element1 in tempmap :
				tempmap[element1] += 1
			else :
				tempmap[element1] = 1
	return tempmap

def findBigramFreq(inputline,tempmap) :
	global bigramtermids
	inputline = inputline.strip('\r\n')
	inputline = inputline.strip(' ')
	inputlist = inputline.split(' ')

	for i in range(1,len(inputlist)) :
		currentterm = str(tuple(inputlist[i-1:i+1]))
		if currentterm in bigramtermids :
			element1 = bigramtermids[currentterm]
			if element1 in tempmap :
				tempmap[element1] += 1
			else :
				tempmap[element1] = 1
	return tempmap

def combineFeatures(tempmap,fout,lineno) :
	global classList
	sortedlist = tempmap.keys()
	sortedlist.sort()
	outputstring = ''	

	for key in sortedlist :
		outputstring += str(key) + ":" + str(tempmap[key]) + ' '

	outputstring = str(classList[lineno]) + ' ' + outputstring
	#outputstring = outputstring.strip(' ')
	#outputstring = outputstring.strip('\t') 
	outputstring += '\r\n'
	fout.write(outputstring)

def readClassValues(classfilename) :
	global classList
	global keyword1
	global keyword2
	global posClassValue
	global negClassValue

	i = 0
	fin = codecs.open(classfilename)

	for inputline in fin :
		inputline = inputline.strip('\r\n')
		inputline = inputline.strip()
		if inputline in keyword1 :
			classList.append(posClassValue)
		else :
			classList.append(negClassValue)
	fin.close()	

if __name__ == '__main__' :
	test_train_option = sys.argv[1]
	classfilename = sys.argv[2]
	inputfilename = sys.argv[3]
	unigramfilename = sys.argv[4]
	bigramfilename = sys.argv[5]
	outputfilename = sys.argv[6]
	featuremap = dict()

	readUnigrams(unigramfilename)
	readBigrams(bigramfilename)
	readClassValues(classfilename)
	findFeatureIds()

	fin = codecs.open(inputfilename,'UTF-8')
	fout = codecs.open(outputfilename,'w')
	lineno = 0
	for inputline in fin :
		#if lineno == 10 :
			#break
		featuremap.clear()
		featuremap = findUnigramFreq(inputline,featuremap)
		#print 'unigram----',featuremap
		featuremap = findBigramFreq(inputline,featuremap)		
		#print 'bigram----',featuremap
		combineFeatures(featuremap,fout,lineno)
		lineno += 1
		
	fout.close()
	fin.close()
