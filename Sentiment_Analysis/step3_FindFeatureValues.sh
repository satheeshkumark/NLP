####################################### Shell script to calculate all the feature values ###################################

test_or_train_option=$1		####	Argument 1 : '-t' for test Dataset '-T' for train Dataset.
				####	NOTE : Test should always be run before train(for generating n gram features).			 
inputfilename=$2		####	Argument 2(optional) : '-x' default argument : the output of previous step i.e., filtering is used
				####	any train file name contains the tweets
tweetCutoffRange=$3		####	Argument 3(any number) : Number of tweets in each class of emotions
language_option=$4		####	Argument 4 : 'en' for English, 'es' for spanish, 'fa' for Farsi, 'ru' for Russian

if [ "$5" == "" ]; then
	DATA_PATH='data/'	####	Argument 5 : Folder where the data resides
else				####	NOTE : Dictionary based features can be applied only for those language which has dicionary
	DATA_PATH=$5
fi

SCRIPT_PATH='scripts/'
MALLET_PATH=$SCRIPT_PATH'mallet-2.0.7/'
tagger_path=$SCRIPT_PATH'ark-tweet-nlp-0.3.2/'
tokenizer_path=$SCRIPT_PATH'ark-tweet-nlp-0.3.2/'
dictionaryFile='data/NRC-Emotion-Lexicon-v0.92/NRC-emotion-lexicon-wordlevel-alphabetized-v0.92.txt'
totalNGramFeatures=50000	#### maximum allowed number of NGrams
totalEmoticonFeatures=`expr $totalNGramFeatures + 16`
#### Total Features until emoticon features
totalTopicFeatures=`expr $totalEmoticonFeatures + 100`

inputFileStep5=$DATA_PATH'input_step5'$test_or_train_option'.txt'
inputFileStep55=$DATA_PATH'input_step55'$test_or_train_option'.txt'
inputFileStep6=$DATA_PATH'input_step6'$test_or_train_option'.txt'
inputFileStep7=$DATA_PATH'input_step7'$test_or_train_option'.txt'
inputFileStep8=$DATA_PATH'input_step8'$test_or_train_option'.txt'
tagSequenceFile_Step8=$DATA_PATH'tagSequenceFile_Step8.txt'
taggerScript='runTagger.sh'
tokenizerScript='twokenize.sh'

if [ "$inputfilename" == "-x" ]; then
	inputfilename=$inputFileStep5
fi

indPolarityFileName=$DATA_PATH'step6_PolInd'$test_or_train_option'.txt' 
posNegPolarityFileName=$DATA_PATH'step6_PolPosNeg'$test_or_train_option'.txt'
totalPolarityFileName=$DATA_PATH'step6_PolTotal'$test_or_train_option'.txt'

unigramFeatures=$DATA_PATH'unigramFeatures.txt'
bigramFeatures=$DATA_PATH'bigramFeatures.txt'
trigramFeatures=$DATA_PATH'trigramFeatures.txt'
unigramFeatureFileName=$DATA_PATH'step6_UnigramFeatureOutput'$test_or_train_option'.txt'
bigramFeatureFileName=$DATA_PATH'step6_BigramFeatureOutput'$test_or_train_option'.txt'
trigramFeatureFileName=$DATA_PATH'step6_TrigramFeatureOutput'$test_or_train_option'.txt'
stopwordfile=$DATA_PATH'emptystopword.txt'
topicFeatureValues=$DATA_PATH'step6_TopicFeatureValues'$test_or_train_option'.txt'

classSeparatingScript=$SCRIPT_PATH'SeparateBasedOnClass.py'
extractEmoticonFeatureScript=$SCRIPT_PATH'step6_ExtractEmoticonFeatures.py'
extractNGramFeatureValues=$SCRIPT_PATH'step6_FindNGramFeatureValues.py'
extractPolarityFeaturesScript=$SCRIPT_PATH'step6_ExtractPolarityFeatures.py'
extractNGramFeaturesScript=$SCRIPT_PATH'step5_FindNGrams.py'
parserOptPostProcessScript='postProcessParserResult.py'
formMalletInputScript=$SCRIPT_PATH'step6_FormMalletInput.py'
extractTopicFeatureValues=$SCRIPT_PATH'step6_ExtractTopicFeatureValues.py'

classFileName=$DATA_PATH'classFileName'$test_or_train_option'.txt'
outputClassFileName=$DATA_PATH'classFileName'$test_or_train_option'_f.txt'

if [ "$tweetCutoffRange" -gt 0 ]; then
	python $classSeparatingScript $tweetCutoffRange $inputfilename $classFileName $inputFileStep55 $outputClassFileName
	inputfilename=$inputFileStep55	
fi

#####################################################	Extract Emoticon Features	#############################


python $extractEmoticonFeatureScript $inputfilename $DATA_PATH'step6_EmoticonFeatureValues'$test_or_train_option'.txt' $inputFileStep6 $totalNGramFeatures


#####################################################	Extract N Gram Features		##############################


if [ "$test_or_train_option" == "-t" ]; then
	python $extractNGramFeaturesScript $inputFileStep6 $unigramFeatures $bigramFeatures $trigramFeatures $stopwordfile
fi

####################################################### CMU Parser Toolkit ###########################################
#Input : Post Processed Input File containing Tokenized sentiment tweets
#Output : Parsed Un post Processed File containing the best parse for each tweet
#Description : Takes the input as the file with sentiment tweets, gives the input to the CMU Tokenizer and outputs the file with tokenized tweets


bash $tagger_path$taggerScript $inputFileStep6 > $inputFileStep7


###################################	Post Processing Parsed Tweets		######################################


python $SCRIPT_PATH$parserOptPostProcessScript $inputFileStep7 $inputFileStep8 $tagSequenceFile_Step8 &&


###################################	Extract N-Gram Feature Values		######################################


python $extractNGramFeatureValues $inputFileStep6 $unigramFeatures $bigramFeatures $trigramFeatures $unigramFeatureFileName $bigramFeatureFileName $trigramFeatureFileName


###################################	Topic Modelling Using Mallet		#######################################

python $formMalletInputScript $inputFileStep6 > $DATA_PATH'step6_Mallet_Input'$test_or_train_option'.txt'


$MALLET_PATH'bin/mallet' import-file --input $DATA_PATH'step6_Mallet_Input'$test_or_train_option'.txt' --output $DATA_PATH'step6_Mallet_Input'$test_or_train_option'.mallet' --keep-sequence --remove-stopwords


$MALLET_PATH'bin/mallet' train-topics --input $DATA_PATH'step6_Mallet_Input'$test_or_train_option'.mallet' --num-topics 100 --output-state $DATA_PATH'step6_Mallet_Topic_State'$test_or_train_option'.gz' --output-topic-keys $DATA_PATH'step6_Mallet_Output_Keys'$test_or_train_option'.txt' --output-doc-topics $DATA_PATH'step6_Mallet_Output'$test_or_train_option'.txt'


python $extractTopicFeatureValues $totalEmoticonFeatures $DATA_PATH'step6_Mallet_Output'$test_or_train_option'.txt' > $topicFeatureValues


###################################	Extract Polarity Based Features using NRC-Emoticon Dictionary	##############

if [ "$language_option" == "en" ]; then
	python $extractPolarityFeaturesScript $dictionaryFile $inputFileStep6 $totalTopicFeatures $indPolarityFileName $posNegPolarityFileName $totalPolarityFileName
fi

