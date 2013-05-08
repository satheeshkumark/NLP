import sys
import codecs

'''

####################################################### File Description #####################################################################

Input : Tokened Tweets file from CMU Tweet tokenizer
Output : File containing post processed tokenized output
Description : Takes the input as the file with tokenized tweets by CMU tokenizer and outputs the post processed output

'''

vocabset = set()
stopwordset = []
keywords1 = ['#anger', '#angry', '#disgust', '#disgusted', '#fear', '#afraid', '#joy', '#joyful', '#enjoy', '#enjoying', '#sad', '#sadness', '#surprise', '#surprised', '#happy', '#happiness', '#ecstatic','#pride','#proud','#contempt']

keywords2 = ['#ira', '#enojado', '#asco', '#asqueado', '#miedo', '#alegria', '#alegre', '#triste', '#tristeza', '#sorpresa', '#sorprendido', '#felicidad', '#extatico', '#orgullo', '#orgulloso', '#rabia', '#repugnancia', '#diversion', '#desprecio']
keywords = []


def readStopWords(stopwordfile) :
	global stopwordset
	global keywords

	inputlist = []
	fin = codecs.open(stopwordfile,'UTF-8')
	for inputline in fin :
		inputline = inputline.strip('\r\n')
		inputline = inputline.strip('')
		inputlist.append(inputline)
	if tweetlang == 'en' :
		keywords = keywords1
	else :
		keywords = keywords2


def findVocabulary(inputline) :
	inputlist = inputline.split(' ')
	for element in inputlist :
		print element

if __name__ == '__main__' :
	inputfile = sys.argv[1]
	tweetlang = sys.argv[2]
	stopwordfile = sys.argv[3]
	readStopWords(stopwordfile)
	fin = codecs.open(inputfile,'UTF-8')
	for inputline in fin :
		findVocabulary(inputline)
	fin.close()
