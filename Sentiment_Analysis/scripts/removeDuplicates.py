import sys
import codecs

'''

####################################################### File Description #####################################################################

Input : File containing duplicate entries as a single column
Output : File containing entries as a single column with duplicated removed
Description : Takes the input as the file with duplicate entries in a single column and returns a file with duplicates removed

'''

inputfilename = sys.argv[1]
fin = codecs.open(inputfilename)
tokenset = set()
tokenlist = []

for inputline in fin :
	inputline = inputline.strip('\r\n')
	inputline = inputline.strip()
	tokenset.add(inputline)

tokenlist = list(tokenset)
tokenlist.sort()

for element in tokenlist :
	print element

fin.close()
