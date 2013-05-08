import sys
import codecs

'''

####################################################### File Description #####################################################################

Input : File containing tokenized tweets
Output1 : File with tweets with the class information removed
Output2 : File with class information of the tweets processed
Description : Takes the input as the file with tokenized tweets and outputs the tweets and class names separately

'''

language_option = sys.argv[1]
inputfilename = sys.argv[2]
outputfilename = sys.argv[3]
outputclassfilename = sys.argv[4]

keyword1 = []
keyword2 = []
keyword3 = []
keyword4 = []
keyword5 = []
keyword6 = []
keyword7 = []
keyword8 = []
if language_option == 'en' :
	keyword1 = ['#joy', '#joyful', '#enjoy', '#enjoying', '#happy', '#happiness', '#ecstatic']
	keyword2 = ['#sad', '#sadness']
	keyword3 = ['#anger','#angry']
	keyword4 = ['#disgust','#disgusted']
	keyword5 = ['#fear','#afraid']
	keyword6 = ['#surprise','#surprised']
	keyword7 = ['#pride','#proud']
	keyword8 = ['#contempt']
elif language_option == 'es' :
	keyword1 = ['#ecstatic','#alegria','#alegre','#felicidad', '#extatico']
	keyword2 = ['#triste','#tristeza']
	keyword3 = ['#ira','#enojado','#ragia']
	keyword4 = ['#asco','#asqueado','#repugnancia']
	keyword5 = ['#miedo']
	keyword6 = ['#sorpresa','#sorprendido']
	keyword7 = ['#orgullo', '#orgulloso']
	keyword8 = ['#desprecio']


tweetExamples = []
tweetClasses = []

fin = codecs.open(inputfilename,'UTF-8') 
for inputline in fin :
	inputlist = inputline.split()
	classname = inputlist[len(inputlist) - 1]
	popelement = inputlist.pop(len(inputlist) - 1)
	inputline = ' '.join(inputlist)
	if(len(inputline) == 0) :
		continue
	if classname in keyword1 :
		classname = str(1) + '\r\n'
	elif classname in keyword2:
		classname = str(2) + '\r\n'
	elif classname in keyword3 :
		classname = str(3) + '\r\n'
	elif classname in keyword4 :
		classname = str(4) + '\r\n'
	elif classname in keyword5 :
		classname = str(5) + '\r\n'
	elif classname in keyword6 :
		classname = str(6) + '\r\n'
	elif classname in keyword7 :
		classname = str(7) + '\r\n'
	elif classname in keyword8 :
		classname = str(8) + '\r\n'
	else :
		continue
	inputline = inputline + '\r\n'
	tweetExamples.append(inputline)
	tweetClasses.append(classname)
fin.close()

fileout = codecs.open(outputfilename,'w')
classout = codecs.open(outputclassfilename,'w')

for i in range(0,len(tweetExamples)) :
	fileout.write(tweetExamples[i])
	classout.write(tweetClasses[i])

fileout.close()
classout.close()

print 'Classes Found'
