#!/usr/bin/env bash

MALLET_PATH='source/mallet-2.0.7/'
TOKENIZED_FILE_PATH='data/webps/tokenized_web_pages/'
SOURCE_PATH='source/'
XML_PATH=$MALLET_PATH'xml_outputs/'

clustername=(Abby_Watkins Cathie_Ely Dan_Rhone Jane_Hunter Michael_Howard Thomas_Baker Tim_Whisler)


#################### Processes the output from mallet and forms the xml clustering file

for i in {0..6}
	do
		entityname=${clustername[i]}
		inputfilename=$MALLET_PATH$entityname'_composition.txt'
		outputfilename=$XML_PATH$entityname'.clust.xml'
		python $SOURCE_PATH'createMalletXML.py' $entityname $inputfilename $outputfilename
	done
