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


def findFScore(svmOutClassList,goldOutClassList,numberOfClasses) :
	totalretrievedMap = dict()
	totalcorrectMap = dict()

	totalcountMap = dict()

	for i in range(1,numberOfClasses + 1) :
		totalcountMap[i] = 0.0
		totalretrievedMap[i] = 0.0	
		totalcorrectMap[i] = 0.0
	
	for i in range(0,len(svmOutClassList)) :
		predvalue = int(svmOutClassList[i])
		goldvalue = int(goldOutClassList[i])
		
		if goldvalue in totalcountMap :
			totalcountMap[goldvalue] += 1.0

		if predvalue in totalretrievedMap :
			totalretrievedMap[predvalue] += 1.0
		
		if predvalue == goldvalue :
			#if predvalue in totalcorrectMap :
			totalcorrectMap[predvalue] += 1.0
	
	for i in range(1,numberOfClasses+1) :
		if totalretrievedMap[i] != 0.0 :
			precision = float(totalcorrectMap[i]/totalretrievedMap[i])
		else :
			precision = 0.0
		if totalcountMap[i] != 0 :
			recall = float(totalcorrectMap[i]/totalcountMap[i])
		else :
			recall = 0.0
		print 'class name : ',str(i)
		print 'Total Count of Tweets : ',totalcountMap[i]
		print 'Retrieved Count of Tweets : ',totalretrievedMap[i]
		print 'Correctly Retrieved Count of Tweets : ',totalcorrectMap[i]
		outputstring = 'Precision : ' + str(precision)
		print outputstring
		outputstring = 'Recall : ' + str(recall)
		print outputstring
		print

	print
	print

def findAccuracy(svmOutClassList,goldOutClassList,accuracyClass) :
	totalcorrectClassification = 0.0	

	for i in range(0,len(svmOutClassList)) :
		if int(svmOutClassList[i]) == accuracyClass and (int(goldOutClassList[i])) == accuracyClass :
			totalcorrectClassification += 1.0
		elif int(svmOutClassList[i]) != accuracyClass and (int(goldOutClassList[i])) != accuracyClass :
			totalcorrectClassification += 1.0 

	accuracy = float(totalcorrectClassification/len(svmOutClassList))
	print 'Accuracy for Classifying Class No : ',accuracyClass,'Tweets ------------------ ',str(accuracy)
	print 'Total CorrectClassification ---- '

def printCounts(inputList) :
	outputMap = dict()
	
	for element in inputList :
		if element in outputMap :
			outputMap[element] += 1
		else :
			outputMap[element] = 1

	for element in outputMap :
		print element,outputMap[element]

if __name__ == '__main__' :
	svmOutClassList = []
	goldOutClassList = []
	svmoutputfilename = sys.argv[1]
	goldclassfilename = sys.argv[2]
	numberOfClasses = int(sys.argv[3])
	#totalNoOfLines = int(sys.argv[4])
	#accuracyClass = int(sys.argv[4])


	print
	print
	print

	#print 'Number of classes : ',numberOfClasses

	#print '################## Evaluation Results #############'

	svmOutClassList = readFileIntoList(svmoutputfilename)
	goldOutClassList = readFileIntoList(goldclassfilename)

	#print set(svmOutClassList)
	#printCounts(svmOutClassList)
	#print set(goldOutClassList)
	#printCounts(goldOutClassList)


	findFScore(svmOutClassList,goldOutClassList,numberOfClasses)

	#print 'len of svmoutclasslist --- ',len(svmOutClassList)
	#print 'len of goldoutclasslist --- ',len(goldOutClassList)
	#for i in range(1,9) :
		#findAccuracy(svmOutClassList,goldOutClassList,i)
