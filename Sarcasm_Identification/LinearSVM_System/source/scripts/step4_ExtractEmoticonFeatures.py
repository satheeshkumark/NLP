# coding: UTF-8

import re
import sys
import codecs
import string

inputfilename = sys.argv[1]		#### step4_'$corpus_option'TokenizedCorpus_PostProcessed'$test_or_train_option'.txt
outputfilename1 = sys.argv[2]		#### step4_Output_EmoticonFeatures'$corpus_option'_'$test_or_train_option'.txt
outputfilename2 = sys.argv[3]		#### step5_'$corpus_option'InputCorpus_EmoticonRmvd'$test_or_train_option'.txt
outputfilename3 = sys.argv[4]		#### step4_Output_ReplyFeature'$corpus_option'_'$test_or_train_option'.txt
startFeatureValue = 0
replyFeatureCount = 0
fin1 = codecs.open(inputfilename,'UTF-8')
fout1 = codecs.open(outputfilename1,'w')
fout2 = codecs.open(outputfilename2,'w')
fout3 = codecs.open(outputfilename3,'w')

endFeatureValue = startFeatureValue + 15
featureList = range(startFeatureValue,endFeatureValue)

smilingEmoticonsList = ['😊', '😃', '😁', '😄','😂', '😅', '😀', '😆', '😇', '😈', '😉', '😉', '😋 ', '😌', '😍', '😎', '😥', '😸', '😹', '😹', '😺', '😻', '😼', '🙅', '🙋',':-)', ':)', ':o)', ':]', ':3', ':c)', ':>', '=]', '8)', '=)', ':}', ':^)', ':っ)',';)', ':-D', ':D', '8-D', '8D', 'x-D', 'xD', 'X-D', 'XD', '=-D', '=D', '=-3', '=3', 'B^D',':\'-)',':\')','♥',':))',':-))', '❤', '^_^','):',':\'))','<3']
winkEmoticonList = [';-)', ';)', '*-)', '*)', ';-]', ';]', ';D', ';^)', ':-\,']
smirkingEmoticonList = ['😏', '😬']
neutralEmoticonList = ['😐', '😑', '😒',':-|']
worriedEmoticonList = ['😓', '😰','😞']
sadEmoticonList = ['😔', '😟', '😢', '😣', '😧', '😭', '😰', '😿', '</3',':\'-(' ':\'(',':(',';(','(:', ':\'(','☹']
kissingEmoticonList = ['😗', '😘', '😙', '😚', '😽']
tongueStuckOutEmoticonList = ['😝', '😜', '😝']
angryEmoticonList = ['😠','😡', '😾',':-||',':@']
triumphEmoticonList = ['✌','👍']
fearEmoticonList = ['😨', '😱']
tiredEmoticonList = ['😩', '😪', '😫', '😴', '😵', '🙀']
surpriseEmoticonList = ['😮', '😲', '😳', '😶']
DEFAULT_USER = '@DEFAULT_USER'

print featureList

print 'feature List -------------------- ',startFeatureValue + featureList[len(featureList)-1]


for inputline in fin1 :	
	inputline = inputline.strip('\r\n')
	inputline = inputline.strip()
	inputList = inputline.split(' ')
	outputstring = ''
	featureString = ''
	featureString1 = ''
	tempMap = dict()
	replyFeatureCount = 0

	for featureId in featureList :
		tempMap[featureId] = 0
	
	for element in inputList :
		element = element.strip()
		
		listId = 0		
		if(string.find(element,'!') != -1) :
			exclamationFeatureId = featureList[len(featureList)-2]
			tempMap[exclamationFeatureId] = 1
		if(string.find(element,'?') != -1) :
			questionFeatureId = featureList[len(featureList)-3]
			tempMap[questionFeatureId] = 1

		element = element.replace('!',' ')
		element = element.replace('?',' ')

		if len(element) == 0 :
			continue

		if element.upper() in smilingEmoticonsList :
			tempMap[startFeatureValue] = 1
		elif element in winkEmoticonList :
			tempMap[startFeatureValue + 1] = 1
		elif element in smirkingEmoticonList :
			tempMap[startFeatureValue + 2] = 1
		elif element in neutralEmoticonList :
			tempMap[startFeatureValue + 3] = 1
		elif element in worriedEmoticonList :
			tempMap[startFeatureValue + 4] = 1
		elif element in sadEmoticonList :
			tempMap[startFeatureValue + 5] = 1
		elif element in kissingEmoticonList :
			tempMap[startFeatureValue + 6] = 1
		elif element in tongueStuckOutEmoticonList :
			tempMap[startFeatureValue + 7] = 1
		elif element in angryEmoticonList :
			tempMap[startFeatureValue + 8] = 1
		elif element in triumphEmoticonList :
			tempMap[startFeatureValue + 9] = 1
		elif element in fearEmoticonList :
			tempMap[startFeatureValue + 10] = 1
		elif element in tiredEmoticonList :
			tempMap[startFeatureValue + 11] = 1
		elif element in surpriseEmoticonList :
			tempMap[startFeatureValue + 12] = 1
		elif element == DEFAULT_USER :
			replyFeatureCount += 1
			#tempMap[len(featureList)-1] += 1			
			#outputstring += element + ' '
		else :
			if(re.search('[^a-zA-Z0-9]',element) or len(element) == 0) :
				continue
			outputstring += element + ' '

	outputstring = outputstring.strip() + '\r\n'
	featureString1 = str(replyFeatureCount) + '\r\n'
	
	for key in sorted(tempMap.iterkeys()) :
		featureString += str(tempMap[key]) + '\t'

	featureString = featureString.strip('\t')
	featureString += '\r\n'			
	
	fout1.write(featureString)		
	fout2.write(outputstring)
	fout3.write(featureString1)

fin1.close()
fout2.close()
fout3.close()

