import sys
import codecs

'''

Input : Tokened Tweets file from CMU Tweet tokenizer
Output : File containing post processed tokenized output
Description : Takes the input as the file with tokenized tweets by CMU tokenizer and outputs the post processed output

'''

inputfilename = sys.argv[1]
tweetlang = sys.argv[2]
fin = codecs.open(inputfilename,'UTF-8')

keywords1 = ['anger', 'angry', 'disgust', 'disgusted', 'fear', 'afraid', 'joy', 'joyful', 'enjoy', 'enjoying', 'sad', 'sadness', 'surprise', 'surprised', 'happy', 'happiness', 'ecstatic','pride','proud','contempt','sarcasm']

keywords2 = ['ira', 'enojado', 'asco', 'asqueado', 'miedo', 'alegria', 'alegre', 'triste', 'tristeza', 'sorpresa', 'sorprendido', 'felicidad', 'extatico', 'orgullo', 'orgulloso', 'rabia', 'repugnancia', 'diversion', 'desprecio','sarcasmo']
keywords = []

if tweetlang == 'en' :
	keywords = keywords1
else :
	keywords = keywords2

for inputline in fin :
	inputlist = inputline.split('\t')
	outputstring = inputlist[0]
	outputstring1 = outputstring.split(' ')
	outputstring = ''
	for element in outputstring1 :
		if element.startswith('@') :
			outputstring += '@DEFAULT_USER' + ' '
		else :
			outputstring += element	+ ' '

	outputstring = outputstring.strip(' ')	
	outputstring = outputstring.strip('\r\n')

	for element in keywords :
		element1 = '#' + element
		if outputstring.endswith(element1) :
			print outputstring
			break

fin.close()
