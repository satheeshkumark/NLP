import codecs
import sys

inputfilename = sys.argv[1]

hashtags = ['#happy','#sad','#sarcastic','#sarcasm']
fin = codecs.open(inputfilename)

for inputline in fin :
	inputline = inputline.strip('\r\n')
	inputline = inputline.strip()
	for element in hashtags :
		inputline = inputline.rstrip(element)
	print inputline.strip()

fin.close()
