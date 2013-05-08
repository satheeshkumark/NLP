import sys
import codecs

'''

####################################################### File Description #####################################################################

Input : Tweets File, Class File
Output1 : Separate Test and Train Files
Description : Takes the input as the file with tokenized tweets and outputs the tweets and class names separately

'''


def divideOutput(inputFileName,outputfile1,outputfile2,cutoffrange) :
	fin = codecs.open(inputFileName)
	fout1 = codecs.open(outputfile1,'w')
	fout2 = codecs.open(outputfile2,'w')
	inputlineno = 0
	for inputline in fin :
		inputlineno += 1
		if inputlineno <= cutoffrange :
			fout1.write(inputline)
		else :
			fout2.write(inputline)
	fout1.close()
	fout2.close()
	fin.close()

if __name__ == '__main__' :
	cutoffrange = int(sys.argv[1])
	tweetFileName = sys.argv[2]
	classFileName = sys.argv[3]
	outputFileName1 = sys.argv[4]
	classFileName1 = sys.argv[5]
	outputFileName2 = sys.argv[6]
	classFileName2 = sys.argv[7]

	print outputFileName1,outputFileName2

	divideOutput(tweetFileName,outputFileName1,outputFileName2,cutoffrange)
	divideOutput(classFileName,classFileName1,classFileName2,cutoffrange)

