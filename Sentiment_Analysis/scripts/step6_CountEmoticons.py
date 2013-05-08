import re
import sys
import codecs
import string


inputfile = '../data/emoticonsFeatureValue.txt'
fin1 = codecs.open(inputfile)
smilingEmFlag = 0
winkEmFlag = 0
smirkEmFlag = 0
neutralEmFlag = 0
wrdEmFlag = 0
sadEmFlag = 0
kssngEmFlag = 0
tngStkEmFlag = 0
angryEmFlag = 0
trmphEmFlag = 0
fearEmFlag = 0
trdEmFlag = 0
srpriseEmFlag = 0
exclamationFlag = 0
questionMarkFlag = 0

for inputline in fin1 :
	inputline = inputline.strip('\r\n')
	inputline = inputline.strip()
	inputList = []
	inputList = inputline.split('\t')
	#inputList = [element.strip() for element in inputList]

	#print inputList

	if(int(inputList[0]) == 1) :
		#print inputList
		#print 'smiling : here : ',len(inputList),'    ',inputList[0]
		smilingEmFlag += 1
	if(int(inputList[1]) == 1) :
		winkEmFlag += 1
	if(int(inputList[2]) == 1) :
		smirkEmFlag += 1
	if(int(inputList[3]) == 1) :
		neutralEmFlag += 1
	if(int(inputList[4]) == 1) :
		wrdEmFlag += 1
	if(int(inputList[5]) == 1) :
		sadEmFlag += 1
	if(int(inputList[6]) == 1) :
		kssngEmFlag += 1
	if(int(inputList[7]) == 1) :
		tngStkEmFlag += 1
	if(int(inputList[8]) == 1) :
		angryEmFlag += 1
	if(int(inputList[9]) == 1) :
		trmphEmFlag += 1
	if(int(inputList[10]) == 1) :
		fearEmFlag += 1
	if(int(inputList[11]) == 1) :
		trdEmFlag += 1
	if(int(inputList[12]) == 1) :
		srpriseEmFlag += 1
	if(int(inputList[13]) == 1) :
		#print 'exclamation : here'
		exclamationFlag += 1
	if(int(inputList[14]) == 1) :
		#print 'question : here'
		questionMarkFlag += 1

fin1.close()

print 'Smiling Emoticon flag : ', smilingEmFlag
print 'Winking Emoticon flag : ', winkEmFlag
print 'Smirk Emoticon flag : ', smirkEmFlag
print 'Netural Emoticon flag : ', neutralEmFlag
print 'Weird Emoticon flag : ', wrdEmFlag
print 'Sad Emoticon flag : ', sadEmFlag
print 'Kissing Emoticon flag : ', kssngEmFlag
print 'Tongue Sticking Emoticon flag : ', tngStkEmFlag
print 'Angry Emoticon flag : ', angryEmFlag
print 'Triumph Emoticon flag : ', trmphEmFlag
print 'Surprise Emoticon flag : ', srpriseEmFlag
print 'Fear Emoticon flag : ', fearEmFlag
print 'Tired Emoticon flag : ', trdEmFlag
print 'Exclamation Emoticon flag : ', exclamationFlag
print 'Question Mark Emoticon Flag : ', questionMarkFlag

