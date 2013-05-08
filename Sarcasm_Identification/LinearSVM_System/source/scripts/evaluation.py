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


def findFScore(svmOutClassList,goldOutClassList,numberOfClasses,totalNoOfLines) :
	totalretrievedMap = dict()
	totalcorrectMap = dict()

	totalcountMap = dict()	

	for i in range(0,totalNoOfLines) :
		predvalue = int(svmOutClassList[i])
		goldvalue = int(goldOutClassList[i]) + 1
		
		if goldvalue in totalcountMap :
			totalcountMap[goldvalue] += 1.0
		else :
			totalcountMap[goldvalue] = 1.0

		if predvalue in totalretrievedMap :
			totalretrievedMap[predvalue] += 1.0
		else :
			totalretrievedMap[predvalue] = 1.0

		if predvalue == goldvalue :
			if predvalue in totalcorrectMap :
				totalcorrectMap[predvalue] += 1.0
			else :
				totalcorrectMap[predvalue] = 1.0
	
	for i in range(1,numberOfClasses+1) :
		#print 'total correct map :',i,totalcorrectMap[i]
		#print 'total retrieved map : ',i,totalretrievedMap[i]
		#print 'total count map : ',i,totalcountMap[i]
		if i not in totalcorrectMap :
			print i,' not in TotalCorrectMap'
		if i not in totalretrievedMap :
			print i,' not in TotalRetrievedMap'
		precision = float(totalcorrectMap[i]/totalretrievedMap[i])
		recall = float(totalcorrectMap[i]/totalcountMap[i])
		print 'class name : ',str(i)
		outputstring = 'Precision : ' + str(precision)
		print outputstring
		outputstring = 'Recall : ' + str(recall)
		print outputstring

def findAccuracy(svmOutClassList,goldOutClassList,accuracyClass) :
	totalcorrectClassification = 0.0	

	for i in range(0,len(svmOutClassList)) :
		if int(svmOutClassList[i]) == accuracyClass and (int(goldOutClassList[i]) + 1) == accuracyClass :
			totalcorrectClassification += 1.0
		elif int(svmOutClassList[i]) != accuracyClass and (int(goldOutClassList[i]) + 1) != accuracyClass :
			totalcorrectClassification += 1.0 

	accuracy = float(totalcorrectClassification/len(svmOutClassList))
	print 'Accuracy of Classifying Sarcastic Tweets ------------------ ',str(accuracy)

if __name__ == '__main__' :
	svmOutClassList = []
	goldOutClassList = []
	svmoutputfilename = sys.argv[1]
	goldclassfilename = sys.argv[2]
	numberOfClasses = int(sys.argv[3])
	totalNoOfLines = int(sys.argv[4])
	accuracyClass = int(sys.argv[5])


	print
	print
	print

	print 'Number of classes : ',numberOfClasses
	print 'Accuracy classes : ',accuracyClass

	print '################## Evaluation Results #############'

	svmOutClassList = readFileIntoList(svmoutputfilename)
	goldOutClassList = readFileIntoList(goldclassfilename)

	print set(svmOutClassList)
	print set(goldOutClassList)

	findFScore(svmOutClassList,goldOutClassList,numberOfClasses,totalNoOfLines)
	findAccuracy(svmOutClassList,goldOutClassList,accuracyClass)
