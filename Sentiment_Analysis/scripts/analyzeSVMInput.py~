import sys
import codecs


def readFileIntoList(filename) :
	tempList = []
	
	fin = codecs.open(filename)
	for inputline in fin :	
		inputline = inputline.strip('\r\n')
		inputlist = inputline.split(' ')
		classvalue = int(inputlist[0])
		tempList.append(classvalue)
	fin.close()

	return tempList

if __name__ == '__main__' :
	svmOutClassList = []
	svmoutputfilename = sys.argv[1]

	print
	print
	print

	print '################## Evaluation Results #############'

	svmOutClassList = readFileIntoList(svmoutputfilename)

	print set(svmOutClassList)
#	printCounts(svmOutClassList)


#	findFScore(svmOutClassList,goldOutClassList,numberOfClasses)

	#print 'len of svmoutclasslist --- ',len(svmOutClassList)
	#print 'len of goldoutclasslist --- ',len(goldOutClassList)
	#for i in range(1,9) :
		#findAccuracy(svmOutClassList,goldOutClassList,i)
