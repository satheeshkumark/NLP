import sys
import codecs

NRCdict = set()
Intrjndict = set()

def readDict(dictfile) :
	global NRCdict
	fin = codecs.open(dictfile)	
	lineno = 0
	for inputline in fin :
		lineno += 1
		if lineno < 31 :
			continue
		inputline = inputline.strip('\r\n')
		inputline = inputline.strip(' ')
		inputlist = inputline.split('\t')
		NRCdict.add(inputlist[0])
	fin.close()

	#print 'Length of NRC dictionary : ',len(NRCdict)
	#print

def readIntrjn(intnfile) :
	global Intrjndict
	fin = codecs.open(intnfile)	
	lineno = 0
	for inputline in fin :
		inputline = inputline.strip('\r\n')
		inputline = inputline.strip(' ')
		Intrjndict.add(inputline)
	fin.close()

def readInterjections(dictfile) :
	global NRCdict
	fin = codecs.open(dictfile)	
	lineno = 0
	for inputline in fin :
		lineno += 1
		if lineno < 31 :
			continue
		inputline = inputline.strip('\r\n')
		inputline = inputline.strip(' ')
		inputlist = inputline.split(' ')
		NRCdict.add(inputlist[0])
	fin.close()

def findTwitterWordCount(inputfilename) :
	uniqueterms = set()	
	totalterms = 0
	fin = codecs.open(inputfilename)
	dictterms = set()
	dicttermsList = []
	intrterms = set()
	intrtermsList = []
	global NRCdict
	global Intrjndict
	
	for inputline in fin :
		inputline = inputline.strip('\r\n')
		inputline = inputline.strip(' ')
		inputlist = inputline.split(' ')
		totalterms += len(inputlist)
		for element in inputlist :
			if len(element.strip()) == 0 :
				continue
			uniqueterms.add(element)
			if element.lower() in NRCdict :
				dictterms.add(element)
				dicttermsList.append(element)
			if element.lower() in Intrjndict :
				intrterms.add(element)
				intrtermsList.append(element)
	fin.close()

	print 'count of uniqueterms : ',len(uniqueterms)
	print 'total number of words : ',totalterms
	print 'Average Length of a tweet : ',totalterms/15000
	print 'Number of unique terms covered by dictionary',len(dictterms)
	print 'Total number of terms covered by dictionary',len(dicttermsList)
	print 'Total number of Interjection terms',len(Intrjndict)
	print 'Number of unique Interjections',len(intrterms)
	print 'Total number of interjection terms in tweets',len(intrtermsList)

def findEmoticonCount(inputfilename) :
	emoticonCountMap = dict()
	emoticonNameList = ['Smiling Emoticons Count','Wink Emoticons Count','Smirking Emoticon Count','Neutral Emoticon Count','Worried Emoticon Count','Sad Emoticon Count','Kissing Emoticon Count','Tongue StuckOut Emoticon Count','Angry Emoticon Count','Triumph Emoticon Count','Fear Emoticon Count','Tired Emoticon Count','Surprise Emoticon Count',' ','Exclamation emoticon Count','Question emoticon Count']

	fin = codecs.open(inputfilename)

	for inputline in fin :
		inputline = inputline.strip('\r\n')
		inputline = inputline.strip(' ')
		inputlist = inputline.split('\t')
		#print len(inputlist)
		#print inputlist
		for i in range(0,len(inputlist)) :
			if i in emoticonCountMap :
				emoticonCountMap[i] += int(inputlist[i])
			else :
				emoticonCountMap[i] = int(inputlist[i])

	fin.close()

	for key in sorted(emoticonCountMap.iterkeys()) :
		index = int(key)
		outputstring = str(emoticonNameList[index]) + '\t' + str(emoticonCountMap[key])
		print outputstring

def findInterjectionCount(inputfilename) :
	inputlineno = 0
	global Intrjndict
	positiveMap = dict()
	negativeMap = dict()
	sarcasticMap = dict()
	finalIntrjnSet = set()

	fin = codecs.open(inputfilename)

	for inputline in fin :
		inputline = inputline.strip('\r\n')
		inputline = inputline.strip()

		inputlist = inputline.split()
		if inputlineno < 5000 :
			for element in inputlist :
				if element in Intrjndict :
					if element in positiveMap :
						positiveMap[element] += 1
					else :
						positiveMap[element] = 1
		elif inputlineno < 10000 :
			for element in inputlist :
				if element in Intrjndict :
					if element in negativeMap :
						negativeMap[element] += 1
					else :
						negativeMap[element] = 1
		else :
			for element in inputlist :
				if element in Intrjndict :
					if element in sarcasticMap :
						sarcasticMap[element] += 1
					else :
						sarcasticMap[element] = 1
		inputlineno += 1

	fin.close()

	print 'Positive interjections -------------------------------'

	for element in positiveMap :
		if positiveMap[element] > 10 :
			#print element,positiveMap[element]
			finalIntrjnSet.add(element)

	print '-------------------------------------------------------'
					
	print 'Negative interjections -------------------------------'

	for element in negativeMap :
		if negativeMap[element] > 10 :
			#print element,negativeMap[element]
			finalIntrjnSet.add(element)

	print '-------------------------------------------------------'

	print 'Sarcasm interjections -------------------------------'

	for element in sarcasticMap :
		if sarcasticMap[element] > 10 :
			#print element,sarcasticMap[element]
			finalIntrjnSet.add(element)

	print '-------------------------------------------------------'


	for element in finalIntrjnSet :
		print element
if __name__ == '__main__' :

	#readDict('../data/dict/NRC-Emotion-Lexicon-v0.92/NRC-Emotion-Lexicon-v0.92/NRC-emotion-lexicon-wordlevel-alphabetized-v0.92.txt')
	readIntrjn('../data/interjections.txt')

	#print 'Training set Statistics ---------------------------------- '
	#findTwitterWordCount('../data/step5_PNSInputCorpus_EmoticonRmvd-t.txt')
	#findEmoticonCount('../data/step4_Output_EmoticonFeaturesPNS_-t.txt')
	#print
	#print 'Test set Statistics ------------------------------------- '
	#findTwitterWordCount('../data/step5_PNSInputCorpus_EmoticonRmvd-T.txt')
	#findEmoticonCount('../data/step4_Output_EmoticonFeaturesPNS_-T.txt')

	findInterjectionCount('../data/step5_PNSInputCorpus_EmoticonRmvd-t-tri.txt')
