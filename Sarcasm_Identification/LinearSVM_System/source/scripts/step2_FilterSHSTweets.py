import sys
import codecs

'''

####################################################### File Description #####################################################################

Input : File containing Tweets containing #sarcasm or #sarcastic hashtags
Output : File with the #sarcastic or #sarcasm hashtags at the end
Description : Takes the input as the file with tweets from the database and outputs the tweets which ends with sarcastic hashtags 

'''

inputoption = sys.argv[1]
inputfilename = sys.argv[2]
tweetlang = sys.argv[3]
outputfile1 = sys.argv[4]
outputfile2 = sys.argv[5]

fin = codecs.open(inputfilename,'UTF-8')
fout1 = codecs.open(outputfile1,'w')
fout2 = codecs.open(outputfile2,'w')

if inputoption == 'happy' and tweetlang == 'en' :
	keywords1 = ['happy']
elif inputoption == 'sad' and tweetlang == 'en' :
	keywords1 = ['sad']
elif inputoption == 'sarcasm' and tweetlang == 'en' :
	keywords1 = ['sarcastic','sarcasm']
elif inputoption == 'happy' and tweetlang == 'es' :
	keywords1 = ['felicidad']
elif inputoption == 'sad' and tweetlang == 'es' :
	keywords1 = ['triste']
elif inputoption == 'sarcasm' and tweetlang == 'es' :
	keywords1 = ['sarcasmo']

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

	for element in keywords1 :
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
