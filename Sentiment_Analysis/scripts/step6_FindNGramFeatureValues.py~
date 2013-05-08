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

def formUnigramFeatures(inputline,fout1) :
	tempMap = dict()
	tempMap.clear()	
	global outputstring
	global termFeatureMap

	outputstring = ''
	unigramstring = ''

	inputList = inputline.split(' ')
	if len(inputList) == 0 :
		unigramstring += '\r\n'
		fout1.write(unigramstring)	
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
	unigramstring += '\r\n'
	fout1.write(unigramstring)	
	#outputstring += unigramstring

def formBiGramFeatures(inputline,fout2) :
	tempMap = dict()
	tempMap.clear()
	global outputstring
	global termFeatureMap
	bigramstring = ''

	inputList = inputline.split(' ')
	if len(inputList) == 0 :
		bigramstring += '\r\n'
		fout2.write(bigramstring)	
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

	bigramstring = bigramstring.strip(' ')
	bigramstring += '\r\n'
	fout2.write(bigramstring)
	#if len(bigramstring) > 0 and len(outputstring) > 0:
		#outputstring += ' ' + bigramstring
	#elif len(outputstring) == 0 :
		#outputstring += bigramstring

def formTriGramFeatures(inputline,fout3) :
	tempMap = dict()
	tempMap.clear()
	global outputstring
	global termFeatureMap
	trigramstring = ''

	inputList = inputline.split(' ')
	if len(inputList) <= 2 :
		#print outputstring
		trigramstring += '\r\n'	
		fout3.write(trigramstring)
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
	trigramstring += '\r\n'	
	fout3.write(trigramstring)

	#if len(trigramstring) > 0 and len(outputstring) > 0:
	#	outputstring += ' ' + trigramstring
	#elif len(outputstring) == 0 :
	#	outputstring += trigramstring

	#print outputstring


if __name__ == '__main__' :
	tweetfilename = sys.argv[1]		####### input filename containing tweets. 'input_step6'$test_or_train_option'.txt' when training
	unigramfilename = sys.argv[2]		####### unigrams feature values.usually 'unigramFeatures_corpusoption.txt' during both test and train
	bigramfilename = sys.argv[3]		####### usually 'bigramFeatures_corpusoption.txt' during both test and train
	trigramfilename = sys.argv[4]		####### usually 'trigramFeatures_corpusoption.txt' during both test and train
	unigramOutputFeatureFile = sys.argv[5]
	bigramOutputFeatureFile = sys.argv[6]
	trigramOutputFeatureFile = sys.argv[7]

	readNgrams(unigramfilename)
	readNgrams(bigramfilename)
	readNgrams(trigramfilename)

	fin = codecs.open(tweetfilename)
	fout1 = codecs.open(unigramOutputFeatureFile,'w')
	fout2 = codecs.open(bigramOutputFeatureFile,'w')
	fout3 = codecs.open(trigramOutputFeatureFile,'w')
	for inputline in fin :
		inputline = inputline.strip('\r\n')
		inputline = inputline.strip()
		formUnigramFeatures(inputline,fout1)
		formBiGramFeatures(inputline,fout2)
		formTriGramFeatures(inputline,fout3)
	fin.close()
	fout1.close()
	fout2.close()
	fout3.close()


