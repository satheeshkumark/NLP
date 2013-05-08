import sys
import codecs

termFeatureMap = dict()
outputstring = ''

def readNgrams(inputfilename) :
	global termFeatureMap

	fin = codecs.open(inputfilename)

	for inputline in fin :
		inputline = inputline.strip('\r\n')
		inputline = inputline.strip()
		inputList = inputline.split('\t')
		term = inputList[0].strip()
		featureid = int(inputList[1])
		termFeatureMap[term] = featureid
	fin.close()

def formUnigramFeatures(inputline) :
	tempMap = dict()
	tempMap.clear()	
	global outputstring
	global termFeatureMap

	outputstring = ''
	unigramstring = ''

	inputList = inputline.split(' ')
	if len(inputList) == 0 :
		return
	inputList = inputline.split()
	for element in inputList :
		if element in termFeatureMap :
			key = termFeatureMap[element]
		else :
			continue
		if key in tempMap :
			tempMap[key] += 1
		else :
			tempMap[key] = 1

	keylist = tempMap.keys()
	keylist.sort()

	for element in keylist :
		unigramstring += str(element) + ':' + str(tempMap[element]) + ' '

	unigramstring = unigramstring.strip(' ')
	outputstring += unigramstring

def formBiGramFeatures(inputline) :
	tempMap = dict()
	tempMap.clear()
	global outputstring
	global termFeatureMap
	bigramstring = ''

	inputList = inputline.split(' ')
	if len(inputList) == 0 :
		return

	prevelement = inputList[0]
	for i in range(1,len(inputList)):
		currentelement = inputList[i]
		element = prevelement + ' ' + currentelement
		if element in termFeatureMap :
			key = int(termFeatureMap[element])
		else :
			continue
		if key in tempMap :
			tempMap[key] += 1
		else :
			tempMap[key] = 1
		prevelement = currentelement

	keylist = tempMap.keys()
	keylist.sort()

	for element in keylist  :
		bigramstring += str(element) + ':' + str(tempMap[element]) + ' '

	bigramstring = bigramstring.strip(',')
	if len(bigramstring) > 0 and len(outputstring) > 0:
		outputstring += ' ' + bigramstring
	elif len(outputstring) == 0 :
		outputstring += bigramstring

def formTriGramFeatures(inputline) :
	tempMap = dict()
	tempMap.clear()
	global outputstring
	global termFeatureMap
	trigramstring = ''

	inputList = inputline.split(' ')
	if len(inputList) <= 2 :
		print outputstring
		return

	prevelement1 = inputList[0]
	prevelement2 = inputList[1]
	for i in range(2,len(inputList)):
		currentelement = inputList[i]
		element = prevelement1 + ' ' + prevelement2 + ' ' + currentelement
		if element in termFeatureMap :
			key = int(termFeatureMap[element])
		else :
			continue
		if key in tempMap :
			tempMap[key] += 1
		else :
			tempMap[key] = 1		
		prevelement1 = prevelement2
		prevelement2 = currentelement

	keylist = tempMap.keys()
	keylist.sort()

	for element in keylist  :
		trigramstring += str(element) + ':' + str(tempMap[element]) + ' '

	trigramstring = trigramstring.strip(' ')
	if len(trigramstring) > 0 and len(outputstring) > 0:
		outputstring += ' ' + trigramstring
	elif len(outputstring) == 0 :
		outputstring += trigramstring

	print outputstring


if __name__ == '__main__' :
	tweetfilename = sys.argv[1]		####### input filename containing tweets. usually 'input_step6-t.txt' when training
	unigramfilename = sys.argv[2]		####### filename with unigrams feature values.usually 'unigramFeatures.txt' during both test and train
	bigramfilename = sys.argv[3]		####### usually 'bigramFeatures.txt' during both test and train
	trigramfilename = sys.argv[4]		####### usually 'trigramFeatures.txt' during both test and train
	#outputfilename = sys.argv[6]

	readNgrams(unigramfilename)
	readNgrams(bigramfilename)
	readNgrams(trigramfilename)

	fin = codecs.open(tweetfilename)
	for inputline in fin :
		inputline = inputline.strip('\r\n')
		inputline = inputline.strip()
		formUnigramFeatures(inputline)
		formBiGramFeatures(inputline)
		formTriGramFeatures(inputline)
	fin.close()

