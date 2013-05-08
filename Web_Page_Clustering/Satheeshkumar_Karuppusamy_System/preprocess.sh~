#!/usr/bin/env bash

SOURCE_PATH='source/'
SENTENCE_SPLITTER_PATH='source/splitta.1.03'
SENTENCE_SPLITTER_MODEL_PATH=$SENTENCE_SPLITTER_PATH'/model_nb' 
SENTENCE_SPLITTER_SVM_PATH=$SENTENCE_SPLITTER_PATH'/model_svm' 
HTML_FILES_PATH='data/webps/web_pages/'
#HTML_FILES_PATH='data/webps/web_pages/Abby_Watkins/raw/'
PARSE_HTML_FILE=$SOURCE_PATH'parseHTMLFiles.py'
TXT_OUTPUT_PATH='data/webps/txt_web_pages/'
#OUTPUTFILE='../../webps/web_pages/Abby_Watkins/outputs/'


############# Performs Preprocessing
############# Gets the input html format and converts, pre-processes them into output-text file

for filename in $(find $HTML_FILES_PATH -type f -iname "index.html")
	do
		IFS='\/'	
		patharray=($filename)
		echo 'Processing ' $filename' ......'
		lenparray=${#patharray[@]}
		optdirname=${patharray[lenparray-4]}
		optclustername=${patharray[lenparray-2]}
		optfilename=${patharray[lenparray-1]}
		IFS=''
		outputfilename=$TXT_OUTPUT_PATH'/'$optdirname'/'$optclustername'/'$optfilename'.out'
		python $PARSE_HTML_FILE $filename $outputfilename 
		echo
	done
