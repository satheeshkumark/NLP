import sys
import codecs

classlist = ['anger', 'angry', 'disgust', 'disgusted', 'fear', 'afraid', 'joy', 'joyful', 'enjoy', 'enjoying', 'sad', 'sadness', 'surprise', 'surprised', 'happy', 'happiness', 'ecstatic','pride','proud','contempt','ira', 'enojado', 'asco', 'asqueado', 'miedo', 'alegria', 'alegre', 'triste', 'tristeza', 'sorpresa', 'sorprendido', 'felicidad', 'extatico', 'orgullo', 'orgulloso', 'rabia', 'repugnancia', 'diversion', 'desprecio']


def classifyFiles(inputfilename,filename) :
	global classlist
	outputfilename = 'outputs/' + filename + '_' + inputfilename
	fin = codecs.open(inputfilename,'UTF-8')
	fout = codecs.open(outputfilename,'w','UTF-8')
	
	for inputline in fin :
		inputlist = inputline.split('\t')
		classid = int(inputlist[0])
		outputstring = inputlist[1]
		if classid == classlist.index(filename) :
			outputstring = str(1) + ' ' + outputstring
			fout.write(outputstring)
		else :
			outputstring = str(-1) + ' ' + outputstring
			fout.write(outputstring)
	fout.close()
	fin.close()

if __name__ == '__main__' :
	inputfilename = sys.argv[1]

	for element in classlist :
		classifyFiles(inputfilename,element)
