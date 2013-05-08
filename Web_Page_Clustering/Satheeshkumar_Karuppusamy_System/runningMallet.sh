
#!/usr/bin/env bash

MALLET_PATH='source/mallet-2.0.7/'
TOKENIZED_FILE_PATH='data/webps/tokenized_web_pages/'

clustername=(Abby_Watkins Cathie_Ely Dan_Rhone Jane_Hunter Michael_Howard Thomas_Baker Tim_Whisler)
clustercount=(14 1 3 16 33 61 11)

############################## Performs topic modelling and outputs txt file with probability a document belongs to each topic

for i in {0..6}
	do
		entityname=${clustername[i]}
		outputfilename=$entityname'.mallet'

		$MALLET_PATH'bin/mallet' import-dir --input $TOKENIZED_FILE_PATH$entityname'/' --output $MALLET_PATH$outputfilename --keep-sequence --remove-stopwords

		$MALLET_PATH'bin/mallet' train-topics --input $MALLET_PATH$entityname'.mallet' --num-topics ${clustercount[i]} --output-state $MALLET_PATH$entityname'_out.gz' --output-topic-keys $MALLET_PATH$entityname'_keys.txt' --output-doc-topics $MALLET_PATH$entityname'_composition.txt'

		echo 'Processed file '$outputfilename
	done
