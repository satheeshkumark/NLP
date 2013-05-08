# coding: UTF-8

import re
import sys
import codecs
import string

inputfilename = sys.argv[1]		#### input_step5-t.txt
outputfilename1 = sys.argv[2]		#### emoticonFeatureValues_Step6-t.txt
outputfilename2 = sys.argv[3]		#### input_step6-t.txt
startFeatureValue = int(sys.argv[4])	#### 49104 for now --- trigram final feature + 1
fin1 = codecs.open(inputfilename,'UTF-8')
fout1 = codecs.open(outputfilename1,'w')
fout2 = codecs.open(outputfilename2,'w')

endFeatureValue = startFeatureValue + 16
featureList = range(startFeatureValue,endFeatureValue)
#element1 = '☺'

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


for inputline in fin1 :	
	inputline = inputline.strip('\r\n')
	inputline = inputline.strip()
	inputList = inputline.split(' ')
	outputstring = ''
	#smilingEmFlag = 0
	#winkEmFlag = 0
	#smirkEmFlag = 0
	#neutralEmFlag = 0
	#wrdEmFlag = 0
	#sadEmFlag = 0
	#kssngEmFlag = 0
	#tngStkEmFlag = 0
	#angryEmFlag = 0
	#trmphEmFlag = 0
	#fearEmFlag = 0
	#trdEmFlag = 0
	#srpriseEmFlag = 0
	#exclamationFlag = 0
	#questionMarkFlag = 0
	featureString = ''
	tempMap = dict()

	for featureId in featureList :
		tempMap[featureId] = 0
	
	for element in inputList :
		element = element.strip()

		listId = 0		
		if(string.find(element,'!') != -1) :
			exclamationFeatureId = featureList[len(featureList)-1]
			tempMap[exclamationFeatureId] = 1
			#exclamationFlag = 1
		if(string.find(element,'?') != -1) :
			questionFeatureId = featureList[len(featureList)-2]
			tempMap[questionFeatureId] = 1
			#questionMarkFlag = 1

		element = element.replace('!',' ')
		element = element.replace('?',' ')

		if len(element) == 0 :
			continue

		if element.upper() in smilingEmoticonsList :
			tempMap[startFeatureValue] = 1
			#smilingEmFlag = 1			
		elif element in winkEmoticonList :
			tempMap[startFeatureValue + 1] = 1
			#winkEmFlag = 1
		elif element in smirkingEmoticonList :
			tempMap[startFeatureValue + 2] = 1
			#smirkEmFlag = 1
		elif element in neutralEmoticonList :
			tempMap[startFeatureValue + 3] = 1
			#neutralEmFlag = 1
		elif element in worriedEmoticonList :
			tempMap[startFeatureValue + 4] = 1
			#wrdEmFlag = 1
		elif element in sadEmoticonList :
			tempMap[startFeatureValue + 5] = 1
			#sadEmFlag = 1
		elif element in kissingEmoticonList :
			tempMap[startFeatureValue + 6] = 1
			#kssngEmFlag = 1
		elif element in tongueStuckOutEmoticonList :
			tempMap[startFeatureValue + 7] = 1
			#tngStkEmFlag = 1
		elif element in angryEmoticonList :
			tempMap[startFeatureValue + 8] = 1
			#angryEmFlag = 1
		elif element in triumphEmoticonList :
			tempMap[startFeatureValue + 9] = 1
			#trmphEmFlag = 1
		elif element in fearEmoticonList :
			tempMap[startFeatureValue + 10] = 1
			#fearEmFlag = 1
		elif element in tiredEmoticonList :
			tempMap[startFeatureValue + 11] = 1
			#trdEmFlag = 1
		elif element in surpriseEmoticonList :
			tempMap[startFeatureValue + 12] = 1
			#srpriseEmFlag = 1
		else :
			#element.decode('ascii','replace').replace(u'u\fffd',' ')
			#element = "".join((c if ord(c) < 128 else ' ' for c in element))		
			#element = element.strip()
			#element = "".join((c if ord(c) < 128 else ' ' for c in element))
			if(re.search('[^a-zA-Z0-9]',element) or len(element) == 0) :
				continue
			outputstring += element + ' '

	outputstring = outputstring.strip() + '\r\n'
	#featureString += str(smilingEmFlag) + '\t' + str(winkEmFlag) + '\t' + str(smirkEmFlag) + '\t' + str(neutralEmFlag) + '\t'
	#featureString += str(wrdEmFlag) + '\t' + str(sadEmFlag) + '\t' + str(kssngEmFlag) + '\t' + str(tngStkEmFlag) + '\t'
	#featureString += str(angryEmFlag) + '\t' + str(trmphEmFlag) + '\t' + str(fearEmFlag) + '\t' + str(trdEmFlag) + '\t'
	#featureString += str(srpriseEmFlag) + '\t' + str(exclamationFlag) + '\t' + str(questionMarkFlag) + '\r\n'
	
	for key in sorted(tempMap.iterkeys()) :
		if tempMap[key] == 1 :
			featureString += str(key) + ':' + str(tempMap[key]) + ' '

	featureString = featureString.strip(' ')
	featureString += '\r\n'			
	
	fout1.write(featureString)		
	fout2.write(outputstring)

fin1.close()
fout2.close()

