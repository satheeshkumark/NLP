import re
import sys
import codecs
import string


filename = sys.argv[1]

fin = codecs.open(filename)

lineno = 0
lang = 'en'

for inputline in fin :
	outputstring = ''
	inputline = inputline.strip('\r\n')
	inputline = inputline.strip()
	outputstring += str(lineno) + ' ' + str(lang) + ' ' + str(inputline)
	outputstring = outputstring.strip()
	outputstring = '\'' + outputstring + '\''
	print outputstring
	lineno += 1

fin.close()
