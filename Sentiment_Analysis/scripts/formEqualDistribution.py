import sys
import codecs

def readFile(tweetFileName,classFileName) :
	classMap = dict()
	fin1 = codecs.open(tweetFileName)
	fin2 = codecs.open(classFileName)

	for inputline1 in fin1 :
		inputline1 = inputline1.strip('\r\n')
		inputline2 = fin2.next().strip('\r\n')
		if inputline2 not in classMap :
			classMap[inputline2] = []
			classMap[inputline2].append(inputline1)
		else :
			if(len(classMap[inputline2]) < 750) :
				classMap[inputline2].append(inputline1)
	fin1.close()
	fin2.close()

	fout1 = codecs.open('newinput_step5-T.txt','w')
	fout2 = codecs.open('newclassFileName-T.txt','w')

	for key in classMap :
		for element in classMap[key] :
			fout1.write(element + '\r\n')
			fout2.write(key + '\r\n')
	fout1.close()
	fout2.close()

if __name__ == '__main__' :
	tweetFileName = '../data/input_step5-T.txt'
	classFileName = '../data/classFileName-T.txt'
	readFile(tweetFileName,classFileName)
