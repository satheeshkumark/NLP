# coding: UTF-8

import sys
import codecs
import string

inputfilename = sys.argv[1]
outputfilename = sys.argv[2]
startFeatureValue = int(sys.argv[3])

fin = codecs.open(inputfilename)
fout = codecs.open(outputfilename,'w')

for inputline in fin :
	outputstring = ''
	inputline = inputline.strip('\r\n')
	inputline = inputline.strip(' ')
	inputList = inputline.split('\t')
	featurevalue = startFeatureValue
	for element in inputList :
		if int(element) != 0 :
			outputstring += str(featurevalue) + ':' + str(element) + ' '
		featurevalue += 1
	outputstring = outputstring.strip()
	outputstring += '\r\n'
	fout.write(outputstring)
fin.close()
fout.close()
