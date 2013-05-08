import sys
import codecs


def mergeFeatureFiles(classfile,featureFileList,outputfilename) :
	classList = []
	featureList = []

	fin1 = codecs.open(classfile)
	noLines = 0
	for inputline in fin1 :
		inputline = inputline.strip('\r\n')
		inputline = inputline.strip()
		classList.append(inputline)
		noLines += 1
	fin1.close()

	i = 0
	while(i<noLines) :
		i += 1
		temp = ''
		featureList.append(temp)

	fileid = 0
	print 'length of Feature List ----- ',len(featureList)
	while(fileid < len(featureFileList)) :
		i = 0
		featureFile = featureFileList[fileid]
		fin2 = codecs.open(featureFile)
		for inputline in fin2 :
			inputline = inputline.strip('\r\n')
			inputline = inputline.strip()
			inputlineold = featureList[i]
			inputlineold += ' ' + inputline
			featureList[i] = inputlineold.strip()
			i += 1
		fin2.close()
		fileid += 1

	fout = codecs.open(outputfilename,'w')
	i = 0
	for i in range(0,noLines) :
		classvalue = int(classList[i])
		outputstring = str(classvalue) + ' ' + str(featureList[i]) + '\r\n'
		outputstring = outputstring.strip(' ')
		fout.write(outputstring)		
		#print outputstring
	fout.close()


if __name__ == '__main__' :
	argslen = len(sys.argv)
	classfilename = sys.argv[1]
	outputfilename = sys.argv[2]
	featureFileList = []
	i = 3
	while(i<argslen) :
		featureFileList.append(sys.argv[i])
		i += 1 

	mergeFeatureFiles(classfilename,featureFileList,outputfilename)
