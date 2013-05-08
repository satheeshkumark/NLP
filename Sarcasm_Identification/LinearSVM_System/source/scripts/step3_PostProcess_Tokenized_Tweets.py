import sys
import codecs

'''

Input : Tokened Tweets file from CMU Tweet tokenizer
Output : File containing post processed tokenized output
Description : Takes the input as the file with tokenized tweets by CMU tokenizer and outputs the post processed output

'''

inputfilename = sys.argv[1]
fin = codecs.open(inputfilename,'UTF-8')

keywords = ['sarcasm','sarcastic']

for inputline in fin :
	inputlist = inputline.split('\t')
	outputstring = inputlist[0]
	outputstring1 = outputstring.split(' ')
	outputstring = ''
	for element in outputstring1 :
		if element.startswith('@') :
			outputstring += '@DEFAULT_USER' + ' '
		elif element.startswith('http://') or element.startswith('https://') :
			outputstring += 'DEFAULT_URL' + ' '
		else :
			outputstring += element	+ ' '

	outputstring = outputstring.strip(' ')
	print outputstring

fin.close()
