import re
import sys
import codecs
import string

unigramMap = dict()

def readUnigramFile(filename) :
	global unigramMap
	fin = codecs.open(filename)

	for inputline in fin :
		inputline = inputline.strip('\r\n')
		inputline = inputline.strip()
		if inputline not in unigramMap :
			unigramMap[inputline] = 0

	fin.close()

def countUnigrams(filename,startvalue) :
	global unigramMap
	fin = codecs.open(filename)

	for inputline in fin :
		inputline = inputline.strip('\r\n')
		inputline = inputline.strip()
		inputList = inputline.split()
		for element in inputList :
			if element in unigramMap :
				unigramMap[element] += 1 

	fin.close()

	for element in unigramMap :
		if unigramMap[element] > 2 :
			print element,'\t',startvalue
			startvalue += 1

if __name__ == '__main__' :
	unigramFile = sys.argv[1]
	tweetinputfile = sys.argv[2]
	#tweetinputfile = datapath + 'input_step6-t.txt'
	startvalue = int(sys.argv[3])
	readUnigramFile(unigramFile)
	countUnigrams(tweetinputfile,startvalue)


