import sys
import codecs

stopwordList = []
unigramCountMap = dict()
bigramCountMap = dict()
trigramCountMap = dict()
thresholdUniCount = 5
thresholdBiCount = 10
thresholdTriCount = 5
featureid = 1

def formUnigramFeatures(tweetfilename,unigramfilename) :
	unigramterms = set()
	global stopwordList
	global unigramCountMap
	global featureid
	
	fin = codecs.open(tweetfilename)

	for inputline in fin :
		inputline = inputline.strip('\r\n')
		inputline = inputline.strip()
		inputList = inputline.split(' ')
		for element in inputList :
			if element not in stopwordList :
				if len(element) == 0 :
					continue
				unigramterms.add(element)
				if element in unigramCountMap :
					unigramCountMap[element] += 1
				else :
					unigramCountMap[element] = 1
	fin.close()

	fout = codecs.open(unigramfilename,'w')
	unigramTermsList = list(unigramterms)
	unigramTermsList.sort()

	for element in unigramTermsList :
		if unigramCountMap[element] > thresholdUniCount :
			outputstring = element
			outputstring += '\t' + str(featureid)
			#outputstring += '\t' + str(unigramCountMap[element])
			outputstring +=  '\r\n'
			fout.write(outputstring)
			featureid += 1
	fout.close()		

def formBiGramFeatures(tweetfilename,bigramfilename) :
	bigramterms = set()
	global bigramCountMap
	global thresholdBiCount
	global featureid

	fin = codecs.open(tweetfilename)

	for inputline in fin :
		inputline = inputline.strip('\r\n')
		inputList = inputline.split(' ')
		if len(inputList) == 0 :
			continue
		prevelement = inputList[0]
		#print inputList
		for i in range(1,len(inputList)):
			currentelement = inputList[i]
			currentelement = currentelement.strip()
			if len(currentelement) == 0:
				continue
			element = prevelement + ' ' + currentelement
			bigramterms.add(element)
			if element in bigramCountMap :
				bigramCountMap[element] += 1
			else :
				bigramCountMap[element] = 1			
			prevelement = currentelement
	fin.close()

	fout = codecs.open(bigramfilename,'w')
	bigramTermsList = list(bigramterms)
	bigramTermsList.sort()

	for element in bigramTermsList :
		if bigramCountMap[element] > thresholdBiCount :
			outputstring = element
			outputstring += '\t' + str(featureid)
			#outputstring += '\t' + str(bigramCountMap[element])
			outputstring += '\r\n'
			fout.write(outputstring)
			featureid += 1
	fout.close()	


def formTriGramFeatures(tweetfilename,trigramfilename) :
	trigramterms = set()
	global trigramCountMap
	global thresholdTriCount
	global featureid

	fin = codecs.open(tweetfilename)

	for inputline in fin :
		inputline = inputline.strip('\r\n')
		inputline = inputline.strip()
		inputList = inputline.split(' ')
		if len(inputList) <= 2 :
			continue

		prevelement1 = inputList[0]
		prevelement2 = inputList[1]
		for i in range(2,len(inputList)):
			currentelement = inputList[i]
			element = prevelement1 + ' ' + prevelement2 + ' ' + currentelement
			trigramterms.add(element)
			if element in trigramCountMap :
				trigramCountMap[element] += 1
			else :
				trigramCountMap[element] = 1		
			prevelement1 = prevelement2
			prevelement2 = currentelement

	fin.close()

	fout = codecs.open(trigramfilename,'w')
	trigramTermsList = list(trigramterms)
	trigramTermsList.sort()

	for element in trigramTermsList :
		if trigramCountMap[element] >= thresholdTriCount :
			outputstring = element
			outputstring += '\t' + str(featureid)
			#outputstring += '\t' + str(trigramCountMap[element])
			outputstring +=  '\r\n'
			fout.write(outputstring)
			featureid += 1
	fout.close()	

def readStopWordFile(stopwordfile) :
	global stopwordList

	fin = codecs.open(stopwordfile)
	for inputline in fin :
		inputline = inputline.strip('\r\n')
		inputline = inputline.strip()
		stopwordList.append(inputline)
	fin.close()

if __name__ == '__main__' :
	tweetfilename = sys.argv[1]		####### input filename containing tweets.'step5_PNSInputCorpus_EmoticonRmvd-t.txt' when training
	unigramfilename = sys.argv[2]		####### unigrams to be generated as output--- unigrams file usually 'unigramFeatures.txt' 
	bigramfilename = sys.argv[3]		####### bigrams to be generated -- 'bigramFeatures.txt' during both test and train
	trigramfilename = sys.argv[4]		####### trigrams to be generated --  'trigramFeatures.txt' during both test and train
	stopwordfile = sys.argv[5]		####### Twitter stopword file
	#outputfilename = sys.argv[6]

	readStopWordFile(stopwordfile)

	formUnigramFeatures(tweetfilename,unigramfilename)
	formBiGramFeatures(tweetfilename,bigramfilename)
	formTriGramFeatures(tweetfilename,trigramfilename)
