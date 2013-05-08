import codecs
import codecs
import string
import re
import sys

###### File for generating ARFF file mapping -- tells which lines of ARFF represents which data point


inputfilename = sys.argv[1]
outputfilename = sys.argv[2]

fin = codecs.open(inputfilename)
fout = codecs.open(outputfilename,'w')

inputlineno = 0
for inputline in fin :
	inputline = inputline.strip('\r\n')
	inputline = inputline.strip()
	if(inputline.startswith('@') or len(inputline) == 0) :
		continue
	else :
		outputlist = inputline.split('\'')
		classnumber = outputlist[-1].strip('\,')
		classnumber = classnumber + '\r\n'
		fout.write(classnumber)
fout.close()
fin.close()	

