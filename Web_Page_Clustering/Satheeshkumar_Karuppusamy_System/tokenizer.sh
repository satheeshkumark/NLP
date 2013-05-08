#!/usr/bin/env bash

SOURCE_PATH='source/'
PARSER_PATH='source/stanford-parser-2012-11-12/'
TXT_FILES_PATH='data/webps/txt_web_pages/'
TOKENIZED_FILES_PATH='data/webps/tokenized_web_pages/'


############### Gets the input txt files and sends them to Stanford Tokenizer and forms the tokenized output

for filename in $(find $TXT_FILES_PATH -type f -iname "*.merged")
	do
		IFS='\/'
		patharray=($filename)
		echo 'Processing ' $filename' ......'
		lenparray=${#patharray[@]}
		optfilename=${patharray[lenparray-1]}
		optclustername=${patharray[lenparray-2]}
		optpersonname=${patharray[lenparray-3]}
		IFS=''
		outputfilename=$TOKENIZED_FILES_PATH'/'$optpersonname'/'$optclustername'/'$optfilename'.tokenized'
		java -cp $PARSER_PATH'/stanford-parser.jar' edu.stanford.nlp.process.PTBTokenizer -preserveLines $filename > $outputfilename
		echo
	done

