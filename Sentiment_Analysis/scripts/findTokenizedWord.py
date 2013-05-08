import sys
import codecs

if __name__ == '__main__' :
	inputfilename = sys.argv[1]
	fin = codecs.open(inputfilename,'UTF-8')
	for inputline in fin :
		inputlist = inputline.split('\t')
		print inputlist[0]
	fin.close()
