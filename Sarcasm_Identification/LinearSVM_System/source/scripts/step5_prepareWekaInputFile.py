import sys
import codecs

#4.$emoticonFeatureValuesFileName	4.$replyFeatureValuesFileName		5.$indPolarityFeaturesFileName		
#6.$posnegPolarityFeaturesFileName	7.$totalPolarityFeaturesFileName	8.$step6_TopicFeatureValues
#9.$interjectionFeatureFileName		10.$interjectionFeatureFileName

def formWekaHeaders(fout) :
	headerList = []
	headerList.append('@relation Twitter' + '\r\n' + '\r\n')
	# 1. Tweet input file
	headerList.append('@attribute tweet_text string' + '\r\n')

	# 2. Emoticon input file
	headerList.append('@attribute smilingEmoticon{0,1}' + '\r\n')
	headerList.append('@attribute winkingEmoticon{0,1}' + '\r\n')
	headerList.append('@attribute smirkingEmoticon{0,1}' + '\r\n')
	headerList.append('@attribute neutralEmoticon{0,1}' + '\r\n')
	headerList.append('@attribute worriedEmoticon{0,1}' + '\r\n')
	headerList.append('@attribute sadEmoticon{0,1}' + '\r\n')
	headerList.append('@attribute kissingEmoticon{0,1}' + '\r\n')
	headerList.append('@attribute tongueStickOutEmoticon{0,1}' + '\r\n')
	headerList.append('@attribute angryEmoticon{0,1}' + '\r\n')
	headerList.append('@attribute triumphEmoticon{0,1}' + '\r\n')
	headerList.append('@attribute fearEmoticon{0,1}' + '\r\n')
	headerList.append('@attribute tiredEmoticon{0,1}' + '\r\n')
	headerList.append('@attribute surpriseEmoticon{0,1}' + '\r\n')
	headerList.append('@attribute exclamationFeature{0,1}' + '\r\n')
	headerList.append('@attribute questionmarkFeature{0,1}' + '\r\n')
	
	#3. Reply input file name	
	headerList.append('@attribute reply_feature {0,1,2,3,4,5,6,7,8}' + '\r\n')
	
	#4. Polarity input features file name	
	#headerList.append('@attribute indPolarityFeature numeric' + '\r\n')
	#headerList.append('@attribute posnegPolarityFeature{0,1}' + '\r\n')
	#headerList.append('@attribute totalPolarityFeature{0,1}' + '\r\n')
	
	#Interjection feature values file
	headerList.append('@attribute interjectionFeature{0,1,2,3,4,5,6,7,8,9,10}' + '\r\n')

	#Class value file	
	headerList.append('@attribute classname{0,1}' + '\r\n' + '\r\n')
	headerList.append('@data' + '\r\n' + '\r\n')

	for line in headerList :
		fout.write(line)

def readFeatureValues(filenames,inputlength,classfilename,outputfilename) :
	fin = []
	
	cin = codecs.open(classfilename)
	fout = codecs.open(outputfilename,'w')
	formWekaHeaders(fout)

	for i in range(0,len(filenames)) :
		tempfin = codecs.open(filenames[i])
		fin.append(tempfin)

	for i in range(0,inputlength) :
		outputstring = ''
		for j in range(0,len(filenames)) :
			#print j,filenames[j]
			if j == 0 :
				outputstring += '\'' + fin[j].next().strip('\r\n') + '\'' + ','
				#print outputstring
			else :
				inputList = fin[j].next().strip('\r\n').split('\t')
				for element in inputList :				
					outputstring += str(element.strip('\t')) + ','
		outputstring = outputstring + cin.next()
		fout.write(outputstring)
	
	for i in range(len(filenames)) :
		fin[i].close()

	cin.close()
	fout.close()


if __name__ == '__main__' :
	filenames = []
	numberOfTweets = int(sys.argv[1])
	outputfilename = sys.argv[2]
	classfilename = sys.argv[3]
	for i in range(4,len(sys.argv)) :
		filenames.append(sys.argv[i])
	readFeatureValues(filenames,numberOfTweets,classfilename,outputfilename)

