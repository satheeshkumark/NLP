import re
import sys
import codecs
import string

startFeatureValue = int(sys.argv[1])		########### last feature value of polarity feature value + 1..
inputfile = sys.argv[2]				########### output file from mallet.. usually 'step6_Mallet_Output-t.txt'

fin = codecs.open(inputfile)
thresholdprob = 0.01

for inputline in fin :
	outputstring = ''
	tempMap = dict()
	tempMap.clear()	
	if inputline.startswith('#') :
		continue
	inputline = inputline.strip('\r\n')
	inputline = inputline.strip('\t')
	inputline = inputline.strip()
	inputList = inputline.split('\t')

	i = 2
	while(i < len(inputList)) :
		key = int(inputList[i])
		value = float(inputList[i+1])
		tempMap[key] = value;		
		i += 2

	maxkey = max(tempMap, key=tempMap.get)
	maxvalue = tempMap[maxkey]
	
	for key in sorted(tempMap.iterkeys()) :
		if tempMap[key] > thresholdprob :
			outputstring += str(startFeatureValue + key) + ':' + str(1) + ' '
			#str(tempMap[key]) + ' '
		#else :
			#outputstring += str(startFeatureValue + key) + ':' + str(0) + ','

	outputstring = outputstring.strip(' ')
	print outputstring

fin.close()
