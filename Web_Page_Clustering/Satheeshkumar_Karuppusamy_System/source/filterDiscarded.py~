import codecs
import codecs
import string
import re
import sys

inputfilename = sys.argv[1]
outputfilename = sys.argv[2]
queryString = sys.argv[3]
queryStringList = (queryString).split('_')
queryStringList = [element.lower() for element in queryStringList]
clustername = ' '.join(queryStringList).lower()

fin = codecs.open(inputfilename)
inputstring = fin.read()
inputstringlower = inputstring.lower()
fin.close()

noOfOccurances = 0
index = 0
endindex = len(inputstring)
i = 0
flag = 0

print 'queryStringList : ',queryStringList
print

for element in queryStringList :
	if(inputstringlower.find(element) == -1) :
		flag = -1
		break
	

#while True :
	#flag = inputstringlower.find(clustername,i,endindex)
	#if flag != -1 :
		#noOfOccurances += 1
	#if noOfOccurances > 2 or flag == -1 :
		#break
	#i = flag

print clustername

#if(noOfOccurances >= 2) :
#if(inputstringlower.find(clustername) != -1) :
if flag != -1 :
	print outputfilename," not discarded"
	fout = codecs.open(outputfilename,'w')
	fout.write(inputstring)
	fout.close()
else :
	print outputfilename," discarded"

