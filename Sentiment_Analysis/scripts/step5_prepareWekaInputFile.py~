import sys
import codecs

#4.$emoticonFeatureValuesFileName	4.$replyFeatureValuesFileName		5.$indPolarityFeaturesFileName		
#6.$posnegPolarityFeaturesFileName	7.$totalPolarityFeaturesFileName	8.$step6_TopicFeatureValues
#9.$interjectionFeatureFileName		10.$interjectionFeatureFileName

def formWekaHeaders(NGramLength,fout) :
	headerList = []
	headerList.append('@relation Twitter' + '\r\n' + '\r\n')
	# 1. Tweet input file
	for i in range(1,NGramLength + 1) :
		headerList.append('@attribute text' + str(i) + ' numeric' + '\r\n')

	# 2. Emoticon input file
	headerList.append('@attribute smilingEmoticon {0,1}' + '\r\n')
	headerList.append('@attribute winkingEmoticon {0,1}' + '\r\n')
	headerList.append('@attribute smirkingEmoticon {0,1}' + '\r\n')
	headerList.append('@attribute neutralEmoticon {0,1}' + '\r\n')
	headerList.append('@attribute worriedEmoticon {0,1}' + '\r\n')
	headerList.append('@attribute sadEmoticon {0,1}' + '\r\n')
	headerList.append('@attribute kissingEmoticon {0,1}' + '\r\n')
	headerList.append('@attribute tongueStickOutEmoticon {0,1}' + '\r\n')
	headerList.append('@attribute angryEmoticon {0,1}' + '\r\n')
	headerList.append('@attribute triumphEmoticon {0,1}' + '\r\n')
	headerList.append('@attribute fearEmoticon {0,1}' + '\r\n')
	headerList.append('@attribute tiredEmoticon {0,1}' + '\r\n')
	headerList.append('@attribute surpriseEmoticon {0,1}' + '\r\n')
	headerList.append('@attribute exclamationFeature {0,1}' + '\r\n')
	headerList.append('@attribute questionmarkFeature {0,1}' + '\r\n')
	
	#3. Reply input file name	
	#headerList.append('@attribute reply_feature {0,1,2,3,4,5,6,7,8}' + '\r\n')
	
	#4. Polarity input features file name	
	for i in range(1,11) :	
		#headerList.append('@attribute indPolarityFeature' + str(i) + ' {0,1,2,3,4,5,6,7,8}' + '\r\n')
		headerList.append('@attribute indPolarityFeature' + str(i) + ' numeric' + '\r\n')
	
	#headerList.append('@attribute posnegPolarityFeature1 {0,1,2,3,4,5,6,7,8}' + '\r\n')
	#headerList.append('@attribute posnegPolarityFeature2 {0,1,2,3,4,5,6,7,8}' + '\r\n')
	#headerList.append('@attribute totalPolarityFeature {-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8}' + '\r\n')
	headerList.append('@attribute posnegPolarityFeature1 numeric' + '\r\n')
	headerList.append('@attribute posnegPolarityFeature2 numeric' + '\r\n')
	headerList.append('@attribute totalPolarityFeature numeric' + '\r\n')
	
	#Interjection feature values file
	#headerList.append('@attribute interjectionFeature{0,1,2,3,4,5,6,7,8,9,10}' + '\r\n')

	#Class value file	
	headerList.append('@attribute classname{1,2,3,4,5,6,7,8}' + '\r\n' + '\r\n')
	headerList.append('@data' + '\r\n' + '\r\n')

	for line in headerList :
		fout.write(line)

def readFeatureValues(mergefilename,classfilename,outputfilename,NGramLength,featureLength,EmoticonStartFeatureValue) :
	fin = []
	
	cin = codecs.open(classfilename)
	fout = codecs.open(outputfilename,'w')
	formWekaHeaders(NGramLength,fout)

	fin = codecs.open(mergefilename)

	for inputline in fin:
		outputstring = ''
		inputList = inputline.strip('\r\n').split()
		tempMap = dict()
		firstelement = 0
		classvalue = ''
		for element in inputList :
			if firstelement == 0 :
				classvalue = str(element)
				outputstring = ''
				firstelement = 1
				continue
			element1 = element.split(':')
			tempMap[element1[0]] = element1[1]
		for k in range(1,NGramLength + 1) :
			if str(k) in tempMap :
				outputstring += str(tempMap[str(k)]) + ','
			else :
				outputstring += str(0) + ','
		for k in range(EmoticonStartFeatureValue,EmoticonStartFeatureValue + 15 + 10 + 2 + 1) :
			if str(k) in tempMap :
				outputstring += str(tempMap[str(k)]) + ','
			else :
				outputstring += str(0) + ','
		outputstring += classvalue + '\r\n'
		fout.write(outputstring)
		#break
	fin.close()

	cin.close()
	fout.close()


if __name__ == '__main__' :
	filenames = []
	outputfilename = sys.argv[1]
	classfilename = sys.argv[2]
	mergefilename = sys.argv[3]	
	#NGramLength = int(sys.argv[3])
	#featureLength = int(sys.argv[4])
	NGramLength = 3723
	featureLength = NGramLength
	EmoticonStartFeatureValue = 7387
	readFeatureValues(mergefilename,classfilename,outputfilename,NGramLength,featureLength,EmoticonStartFeatureValue)

