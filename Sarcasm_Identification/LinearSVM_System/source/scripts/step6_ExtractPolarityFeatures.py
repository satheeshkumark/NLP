import sys
import codecs
import string

angerPolarMap = dict()
anticipationPolarMap = dict()
disgustPolarMap = dict()
fearPolarMap = dict()
joyPolarMap = dict()
negativePolarMap = dict()
positivePolarMap = dict()
sadnessPolarMap = dict()
surprisePolarMap = dict()
trustPolarMap = dict()
wordsList = []

def readDictFile(dictfilename) :
	global angerPolarMap
	global anticipationPolarMap
	global disgustPolarMap
	global fearPolarMap
	global joyPolarMap
	global negativePolarMap
	global positivePolarMap
	global sadnessPolarMap
	global surprisePolarMap
	global trustPolarMap
	global wordsList

	fin = codecs.open(dictfilename)

	inputlineno = 0
	for inputline in fin :
		if inputlineno < 31 :
			inputlineno += 1
			continue
		#print 'inside here'
		inputline = inputline.strip('\r\n')
		inputline = inputline.strip()
		inputList = inputline.split('\t')
		wordsList.append(inputList[0])
		key = inputList[0]
		value = int(inputList[2])
		angerPolarMap[key] = value
		
		inputline = fin.next()
		inputline = inputline.strip('\r\n')
		inputline = inputline.strip()
		inputList = inputline.split('\t')
		key = inputList[0]
		value = int(inputList[2])
		anticipationPolarMap[key] = value
		
		inputline = fin.next()
		inputline = inputline.strip('\r\n')
		inputline = inputline.strip()
		inputList = inputline.split('\t')
		key = inputList[0]
		value = int(inputList[2])
		disgustPolarMap[key] = value
		
		inputline = fin.next()
		inputline = inputline.strip('\r\n')
		inputline = inputline.strip()
		inputList = inputline.split('\t')
		key = inputList[0]
		value = int(inputList[2])
		fearPolarMap[key] = value
		
		inputline = fin.next()
		inputline = inputline.strip('\r\n')
		inputline = inputline.strip()
		inputList = inputline.split('\t')
		key = inputList[0]
		value = int(inputList[2])
		joyPolarMap[key] = value

		inputline = fin.next()
		inputline = inputline.strip('\r\n')
		inputline = inputline.strip()
		inputList = inputline.split('\t')
		key = inputList[0]
		value = int(inputList[2])
		negativePolarMap[key] = value

		inputline = fin.next()
		inputline = inputline.strip('\r\n')
		inputline = inputline.strip()
		inputList = inputline.split('\t')
		key = inputList[0]
		value = int(inputList[2])
		positivePolarMap[key] = value

		inputline = fin.next()
		inputline = inputline.strip('\r\n')
		inputline = inputline.strip()
		inputList = inputline.split('\t')
		key = inputList[0]
		value = int(inputList[2])
		sadnessPolarMap[key] = value

		inputline = fin.next()
		inputline = inputline.strip('\r\n')
		inputline = inputline.strip()
		inputList = inputline.split('\t')
		key = inputList[0]
		value = int(inputList[2])
		surprisePolarMap[key] = value

		inputline = fin.next()
		inputline = inputline.strip('\r\n')
		inputline = inputline.strip()
		inputList = inputline.split('\t')
		key = inputList[0]
		value = int(inputList[2])
		trustPolarMap[key] = value

	fin.close()

def formPolarityFeatures(inputfilename,featureid,indpolarfile,tweetpolarfile,totaltweetpolarfile,tweetpolarfileweka,totaltweetpolarfileweka) :
	tempmap = dict()
	global angerPolarMap
	global anticipationPolarMap
	global disgustPolarMap
	global fearPolarMap
	global joyPolarMap
	global negativePolarMap
	global positivePolarMap
	global sadnessPolarMap
	global surprisePolarMap
	global trustPolarMap
	global wordsList

	fout1 = codecs.open(indpolarfile,'w')
	fout2 = codecs.open(tweetpolarfile,'w')
	fout3 = codecs.open(totaltweetpolarfile,'w')
	fout4 = codecs.open(tweetpolarfileweka,'w')
	fout5 = codecs.open(totaltweetpolarfileweka,'w')

	fin = codecs.open(inputfilename)
	for inputline in fin :
		inputline = inputline.strip('\r\n')
		inputline = inputline.strip()
		inputlist = inputline.split(' ')
		for element in inputlist :
			if element in angerPolarMap :
				if featureid not in tempmap :
					tempmap[featureid] = angerPolarMap[element]
				else :
					tempmap[featureid] += angerPolarMap[element]
				if featureid+1 not in tempmap :
					tempmap[featureid + 1] = anticipationPolarMap[element]
				else :
					tempmap[featureid + 1] += anticipationPolarMap[element]
				if featureid+2 not in tempmap :
					tempmap[featureid + 2] = disgustPolarMap[element]
				else :
					tempmap[featureid + 2] += disgustPolarMap[element]
				if featureid+3 not in tempmap :
					tempmap[featureid + 3] = fearPolarMap[element]
				else :
					tempmap[featureid + 3] += fearPolarMap[element]
				if featureid+4 not in tempmap :
					tempmap[featureid + 4] = joyPolarMap[element]
				else :
					tempmap[featureid + 4] += joyPolarMap[element]
				if featureid+5 not in tempmap :
					tempmap[featureid + 5] = negativePolarMap[element]
				else :
					tempmap[featureid + 5] += negativePolarMap[element]			
				if featureid+6 not in tempmap :
					tempmap[featureid + 6] = positivePolarMap[element]
				else :
					tempmap[featureid + 6] += positivePolarMap[element]
				if featureid+7 not in tempmap :
					tempmap[featureid + 7] = sadnessPolarMap[element]
				else :
					tempmap[featureid + 7] += sadnessPolarMap[element]
				if featureid+8 not in tempmap :
					tempmap[featureid + 8] = surprisePolarMap[element]
				else :
					tempmap[featureid + 8] += surprisePolarMap[element]
				if featureid+9 not in tempmap :
					tempmap[featureid + 9] = surprisePolarMap[element]
				else :
					tempmap[featureid + 9] += surprisePolarMap[element]

		positive = 0
		negative = 0
		total = 0
		outputstring1 = ''
		outputstring2 = ''
		outputstring3 = ''

		for i in range(featureid,featureid+10) :
			if tempmap[i] > 0 :
				outputstring1 += str(i) + ':' + str(tempmap[i]) + ' '
				if(i==(featureid+1) or i==(featureid+4) or i==(featureid+6) or i==(featureid+8) or i==(featureid+9)) :
					positive += 1
				else :
					negative += 1
		
		outputstring1 = outputstring1.strip()
		
		if positive > 0 :
			outputstring2 += str(featureid + 10) + ':' + str(positive) + ' '
		if negative > 0 :
			outputstring2 += str(featureid + 11) + ':' + str(negative) + ' '
		outputstring2 = outputstring2.strip()
		
		total = positive - negative

		if total != 0 :
			outputstring3 = str(featureid + 12) + ':' + str(total)

		#print 'outputstring1 : ',outputstring1
		#print 'outputstring2 : ',outputstring2
		#print 'outputstring3 : ',outputstring3

		for element in tempmap :
			tempmap[element] = 0

		posnegtweetpolarityweka = str(positive)  + '\t' + str(negative) + '\r\n'
		totaltweetpolarityweka = str(positive - negative) + '\r\n'

		fout1.write(outputstring1 + '\r\n')
		fout2.write(outputstring2 + '\r\n')
		fout3.write(outputstring3 + '\r\n')
		fout4.write(posnegtweetpolarityweka)
		fout5.write(totaltweetpolarityweka)
	fin.close()
	fout1.close()
	fout2.close()
	fout3.close()
	fout4.close()
	fout5.close()

if __name__ == '__main__' :
	dictfilename = sys.argv[1]		########## data/NRC-Emotion-Lexicon-v0.92/NRC-emotion-lexicon-wordlevel-alphabetized-v0.92.txt'
	inputfilename = sys.argv[2]		########## usually 'input_step6'$test_or_train_option'.txt'
	featureid = int(sys.argv[3])		########## start feature value : see in step3_FormFeatures.sh
	indpolarfile = sys.argv[4]		########## output file with individual polarity values -- polarity value for each emotion
	tweetpolarfile = sys.argv[5]		########## output file to find the polarity of positive and negative values
	totaltweetpolarfile = sys.argv[6]	########## output file to find the polarity value of total tweets..  

	tweetpolarfileweka = sys.argv[5] + '.weka'		########## output file to find the polarity of positive and negative values
	totaltweetpolarfileweka = sys.argv[6] + '.weka'	########## output file to find the polarity value of total tweets..  


	readDictFile(dictfilename)
	formPolarityFeatures(inputfilename,featureid,indpolarfile,tweetpolarfile,totaltweetpolarfile,tweetpolarfileweka,totaltweetpolarfileweka)

