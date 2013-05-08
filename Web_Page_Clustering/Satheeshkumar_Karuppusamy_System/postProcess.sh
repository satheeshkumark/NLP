#!/usr/bin/env bash

SOURCE_PATH='source/'
ARFF_PATH='data/webps/arff_files/'
WEKA_JAR_PATH='source/weka/weka-3-6-9/weka.jar'
#WEKA_OUTPUT_PATH='data/webps/arff/weka_output/'

totalfiles=(123 001 003 099 099 099 032)
clustername=(Abby_Watkins Cathie_Ely Dan_Rhone Jane_Hunter Michael_Howard Thomas_Baker Tim_Whisler)

#################### Gets the input as the output arff file and forms the xml clustering file

for i in {0..6}
	do
		inputlength=${totalfiles[i]}
		arfffilename=$ARFF_PATH${clustername[i]}'_out.arff'
		mappingfilename=$ARFF_PATH${clustername[i]}'.arff.mapping'
		entityname=$clustername
		outputfilename=$ARFF_PATH${clustername[i]}'.clust.xml'
		python $SOURCE_PATH'createXML.py' $inputlength $arfffilename $mappingfilename $entityname $outputfilename
		echo 'done with processing '$outputfilename	
	done
