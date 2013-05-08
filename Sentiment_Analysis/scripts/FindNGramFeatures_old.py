import sys
import codecs
from nltk import bigrams
from nltk import trigrams

unigramterms = set()
bigramterms = set()
trigramterms = set()
stopWordsList = []
data_path = '../data/'


def findNgrams(inputfilename) :
	global unigramterms
	global bigramterms
	global trigramterms
	global stopWordsList

	print 'Finding uni, bi and tri-grams'

	fin = codecs.open(inputfilename)

	lineno = 0
	for inputline in fin :
		lineno += 1
		print 'processing ',lineno
		inputline = inputline.strip('\r\n')
		inputline = inputline.strip()
		wordlist = inputline.split(' ')
		for inputword in wordlist :
			inputword = inputword.strip()
			if inputword not in stopWordsList :
				unigramterms.add(inputword)

		bigramset = bigrams(wordlist)
		for element in bigramset :
			bigramterms.add(element)
	
		trigramset = trigrams(wordlist)
		for element in trigramset :
			trigramterms.add(element)
		
	fin.close()

	print 'Done with finding uni and bigrams'

def readStopWords(stopwordfile) :
	global stopWordsList

	fin = codecs.open(inputfilename)

	for inputline in fin :
		inputline = inputline.strip('\r\n')
		inputline = inputline.strip()
		stopWordsList.append(inputline)
	
	fin.close()


def printDetails(inputoption) :
	global unigramterms
	global bigramterms
	global data_path
	
	unigramotptfilename = data_path + 'unigramfile' + inputoption + '.txt'
	bigramotptfilename = data_path + 'bigramfile' + inputoption + '.txt'
	trigramotptfilename = data_path + 'trigramfile' + inputoption + '.txt'

	fin1 = codecs.open(unigramotptfilename,'w')
	fin2 = codecs.open(bigramotptfilename,'w')
	fin3 = codecs.open(trigramotptfilename,'w')

	for element in unigramterms :
		element = str(element) + '\r\n'
		fin1.write(element)

	for element in bigramterms :
		element = str(element) + '\r\n'
		fin2.write(element)

	for element in trigramterms :
		element = str(element) + '\r\n'
		fin3.write(element)

	fin1.close()
	fin2.close()
	fin3.close()

if __name__ == '__main__' :
	inputoption = sys.argv[1]
	stopwordfile = sys.argv[2]
	inputfilename = sys.argv[3]
	readStopWords(stopwordfile)
	findNgrams(inputfilename)
	printDetails(inputoption)

