import codecs
import codecs
import string
import re
import sys

inputdirectoryname=
outputfilename = sys.argv[2]
queryStringList = (sys.argv[3]).split('_')
clustername = ' '.join(queryStringList).lower()

fin = codecs.open(inputfilename)
inputstring = fin.read()
inputstringlower = inputstring.lower()
fin.close()
if(inputstringlower.find(clustername) != -1) :
	fout = codecs.open(outputfilename,'w')
	fout.write(inputstring)
	fout.close()
