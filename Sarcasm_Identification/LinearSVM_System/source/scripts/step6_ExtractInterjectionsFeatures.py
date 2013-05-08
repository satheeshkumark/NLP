import sys
import codecs
import string

inputfilename = sys.argv[1]
interjectionfilename = sys.argv[2]
outputfilename = sys.argv[3]
startFeatureValue = int(sys.argv[4])
wekaoutputfile = outputfilename + '.weka'

fin1 = codecs.open(inputfilename)
fin2 = codecs.open(interjectionfilename)
fout = codecs.open(outputfilename,'w')
fout1 = codecs.open(wekaoutputfile,'w')

interjectionList = []
for inputline in fin2 :
	inputline = inputline.strip('\r\n')
	inputline = inputline.strip()
	interjectionList.append(inputline)
fin2.close()

for inputline in fin1 :
	outputstring = ''
	inputline = inputline.strip('\r\n')
	inputline = inputline.strip(' ')
	inputList = inputline.split()
	interjectionflag = 0
	for element in inputList :
		if element in interjectionList :
			interjectionflag += 1

	if interjectionflag != 0 :
		outputstring += str(startFeatureValue) + ':' + str(interjectionflag) + ' '
	

	outputstring = outputstring.strip()
	outputstring += '\r\n'
	fout.write(outputstring)
	fout1.write(str(interjectionflag) + '\r\n')
fin1.close()
fout.close()
fout1.close()
