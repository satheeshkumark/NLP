#!/usr/bin/env bash

SOURCE_PATH='source/'
TXT_FILES_PATH='data/webps/txt_web_pages/'

################### Merges the title content file and the actual text content

for filename in $(find $TXT_FILES_PATH -type f -iname "*.out")
	do	
		mergefilename=$filename'.meta'
		outputfilename=$filename'.merged'
		cat $filename $mergefilename > $outputfilename
		echo
	done
