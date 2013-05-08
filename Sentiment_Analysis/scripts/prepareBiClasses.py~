import sys
import codecs

inputClasses = []
uniqueClasses = set()

def readInputClassFile(inputClassFilename) :
	global inputClasses
	global uniqueClasses

	fin = codecs.open(inputClassFilename)
	for inputline in fin :
		inputline = inputline.strip('\r\n')
		inputline = inputline.strip()
		inputClasses.append(inputline)
	fin.close()

	uniqueClasses = set(inputClasses)

def formBiClass(outputClassFileName,classNo) :
	global inputClasses
	global uniqueClasses

	fout = codecs.open(outputClassFileName,'w')
	for element in inputClasses :
		if element == classNo :
			outputstring = str(1) + '\r\n'
		else :
			outputstring = str(2) + '\r\n'
		fout.write(outputstring)
	fout.close()

def formNewClasses(inputClassFileName) :
	global uniqueClasses

	for element in uniqueClasses :
		outputClassFileName = inputClassFileName + str(element)
		formBiClass(outputClassFileName,element)

if __name__ == '__main__' :
	inputClassFileName = sys.argv[1]
	readInputClassFile(inputClassFileName)
	formNewClasses(inputClassFileName)
