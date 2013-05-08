import sys
import codecs

'''

####################################################### File Description #####################################################################

Input : File containing tweets extracted from Db - All the tweets which contain sentiment words
Output : File with tweets containing sentiment tag at its end
Description : Takes the input as the file with tweets from the database and outputs the tweets which ends with sentiment hashtags 

'''

print 'Filtering sentiment tweets from db.....................'

inputfilename = sys.argv[1]
tweetlang = sys.argv[2]
outputfile1 = sys.argv[3]
outputfile2 = sys.argv[4]

fin = codecs.open(inputfilename,'UTF-8')
fout1 = codecs.open(outputfile1,'w')
fout2 = codecs.open(outputfile2,'w')


keywords1 = ['anger', 'angry', 'disgust', 'disgusted', 'fear', 'afraid', 'joy', 'joyful', 'enjoy', 'enjoying', 'sad', 'sadness', 'surprise', 'surprised', 'happy', 'happiness', 'ecstatic','pride','proud','contempt']

#extra words ----- #sorrow, #tragic #tragedy

#keywords1 = ['happy','happiness','ecstatic','joy','joyful','enjoy','enjoying','sad','sadness']

keywords2 = ['ira', 'enojado', 'asco', 'asqueado', 'miedo', 'alegria', 'alegre', 'triste', 'tristeza', 'sorpresa', 'sorprendido', 'felicidad', 'extatico', 'orgullo', 'orgulloso', 'rabia', 'repugnancia', 'diversion', 'desprecio']


if tweetlang == 'en' :
	keywords = keywords1
else :
	keywords = keywords2

for inputline in fin :
	inputlist = inputline.split('\t')
	tweetid = str(inputlist[0])
	outputstring = inputlist[2]
	outputstring1 = outputstring.split(' ')
	outputstring = ''
	lenoutputstring = len(outputstring1)
	i = 0
	for element in outputstring1 :
		i += 1
		if element.startswith('@') :
			outputstring += '@default_user' + ' '
		elif element.startswith('http://') or element.startswith('https://') :
			outputstring += 'URL_LINK '
		elif element.startswith('#') and i != lenoutputstring :
			outputstring += element.lstrip('#')
		else :
			outputstring += element	+ ' '

	outputstring = outputstring.strip(' ')	
	outputstring = outputstring.strip('\r\n')

	for element in keywords :
		element1 = '#' + element
		if outputstring.endswith(element1) and len(outputstring1) > 3 :
			outputstring += '\r\n'
			fout1.write(outputstring)
			tweetid += '\r\n'
			fout2.write(tweetid)
			break

fin.close()
fout1.close()
fout2.close()

print 'Done with Parsing'
