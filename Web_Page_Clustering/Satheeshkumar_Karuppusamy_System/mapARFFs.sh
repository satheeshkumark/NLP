#!/usr/bin/env bash

TOKENIZED_FILES_PATH='data/webps/tokenized_web_pages/'
#FILTERED_TOKENIZED_FILES_PATH='data/webps/tokenized_filtered_webpages/'
SOURCE_PATH='source/'
ARFF_PATH='data/webps/arff_files/'
DISCARDED_FILE_PATH='data/webps/discarded_files/'

WEKA_JAR_PATH='source/weka/weka-3-6-9/weka.jar'
ARFF_CONVERTER_CLASS='weka.core.converters.TextDirectoryLoader'

LOGFILE1='log_filter_discrading.log'
LOGFILE2='log_createARFF.log'
clustername=(Abby_Watkins Cathie_Ely Dan_Rhone Jane_Hunter Michael_Howard Thomas_Baker Tim_Whisler)

>$LOGFILE1
>$LOGFILE2


################################################Generates ARFF files which needs to be given as input to Weka

for i in {0..6}
	do
		#dirname=$FILTERED_TOKENIZED_FILES_PATH${clustername[i]}
		dirname=$TOKENIZED_FILES_PATH${clustername[i]}
		echo 'Processing '$dirname'.........' >>$LOGFILE2
		IFS='\/'
		patharray=($dirname)
		lenparray=${#patharray[@]}
		optclustername=${patharray[lenparray-1]}
		IFS=''
		java -cp $WEKA_JAR_PATH $ARFF_CONVERTER_CLASS -dir $dirname > $ARFF_PATH$optclustername'.arff'
		echo 'Done with generating ARFF file for '$dirname'.............' >>$LOGFILE2
		echo
	done


################################################# Finds the mapping of the inputline and the filenumber after some files are being discarded

for i in {0..6}
	do
		inputfilename=$ARFF_PATH${clustername[i]}'.arff'
		echo $inputfilename
		outputfilename=$inputfilename'.mapping'
		python $SOURCE_PATH'findARFFMapping.py' $inputfilename $outputfilename
		echo 'Done with generating ARFF Mapping file for '$inputfilename
		echo
	done

