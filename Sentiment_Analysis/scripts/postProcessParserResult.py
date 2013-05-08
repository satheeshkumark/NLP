import sys
import codecs


inputfilename = sys.argv[1]
outputsentencefile = sys.argv[2]
outputtagfile = sys.argv[3]

fin = codecs.open(inputfilename)
fout1 = codecs.open(outputsentencefile,'w')
fout2 = codecs.open(outputtagfile,'w')

for inputline in fin :
	inputline = inputline.strip('\r\n')
	inputline = inputline.strip()
	parselist = inputline.split('\t')
	if len(parselist) != 4 :
		continue
	inputSentence = parselist[0].lower() + '\r\n'
	posTagSequence = parselist[1] + '\r\n'
	confidenceMeasure = parselist[2].lower() + '\r\n'
	
	fout1.write(inputSentence)
	fout2.write(posTagSequence)

fout1.close()
fout2.close()
