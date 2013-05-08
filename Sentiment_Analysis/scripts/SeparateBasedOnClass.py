import sys
import codecs

'''

####################################################### File Description #####################################################################

Input : Tweets File, Class File
Output1 : Separate files for each class
Description : Takes the input as the file with tokenized tweets and outputs the tweets and class names separately

'''


def separateClasses(tweetList,classList,outputFileName,outputClassFileName,thresholdCount) :
	cset = set(classList)
	tempMap = dict()
	for element in cset :
		tempMap[int(element)] = []
	for i in range(0,len(tweetList)) :
		className = classList[i]
		if int(className) in tempMap and len(tempMap[int(className)]) < thresholdCount:
			tempMap[int(className)].append(tweetList[i])
	writeCombinedOutput(outputFileName,outputClassFileName,tempMap)
	writeBinaryClassInputFiles(outputClassFileName,tempMap)

def writeCombinedOutput(outputFileName,outputClassFileName,tempMap) :
	fout1 = codecs.open(outputFileName,'w')
	fout2 = codecs.open(outputClassFileName,'w')
	for key in sorted(tempMap.iterkeys()) :
		tweetList = tempMap[key]
		classId = str(key)
		for i in range(0,len(tweetList)) :
			fout1.write(tweetList[i] + '\r\n')
			fout2.write(classId + '\r\n')
	fout1.close()
	fout2.close()

def writeBinaryClassInputFiles(outputClassFileName,tempMap) :
	for key in sorted(tempMap.iterkeys()) :
		classId = key	
		fout1 = codecs.open(outputClassFileName + str(classId),'w')
		for key1 in sorted(tempMap.iterkeys()) :
			tweetList = tempMap[key1]
			ouputClassFilename = outputClassFileName + str(classId)
			for i in range(0,len(tweetList)) :
				if int(key1) == classId :
					fout1.write(str(2) + '\r\n')
				else :
					fout1.write(str(1) + '\r\n')
		fout1.close()

def readFileContentInList(inputfilename) :
	inputList = []
	fin = codecs.open(inputfilename)
	for inputline in fin :
		inputList.append(inputline.strip('\r\n'))
	fin.close()
	return inputList

if __name__ == '__main__' :
	thresholdCount = int(sys.argv[1])
	tweetFileName = sys.argv[2]
	classFileName = sys.argv[3]
	outputFileName = sys.argv[4]
	outputClassFileName = sys.argv[5]

	tweetList = readFileContentInList(tweetFileName)
	classList = readFileContentInList(classFileName)
	separateClasses(tweetList,classList,outputFileName,outputClassFileName,thresholdCount)

