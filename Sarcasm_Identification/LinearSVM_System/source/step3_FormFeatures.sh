test_or_train_option=$1	############################ '-t' or '-T'
corpus_option=$2     ############################### 'PNS' or 'PS' or 'NS'
classifier_option=$3 ############################### '-bi' or '-tri'

data_path='data/'
script_path='scripts/'
SVM_path='scripts/svm_multiclass_linux/'
MALLET_PATH=$script_path'mallet-2.0.7/'
dict_file=$data_path'dict/NRC-Emotion-Lexicon-v0.92/NRC-emotion-lexicon-wordlevel-alphabetized-v0.92.txt'


twitterinputfile=$data_path'step5_'$corpus_option'InputCorpus_EmoticonRmvd'$test_or_train_option$classifier_option'.txt'
unigramfilename=$data_path'unigramFeatures_'$corpus_option'.txt'
bigramfilename=$data_path'bigramFeatures_'$corpus_option'.txt'
trigramfilename=$data_path'trigramFeatures_'$corpus_option'.txt'
#unigramfilename=$data_path'unigramFeatures_PNS.txt'
#bigramfilename=$data_path'bigramFeatures_PNS.txt'
#trigramfilename=$data_path'trigramFeatures_PNS.txt'
interjectionFileName=$data_path'interjections.txt'

unigramFeatureValuesFileName=$data_path'unigramFeatureValues_'$corpus_option$test_or_train_option$classifier_option'.txt'
bigramFeatureValuesFileName=$data_path'bigramFeatureValues_'$corpus_option$test_or_train_option$classifier_option'.txt'
trigramFeatureValuesFileName=$data_path'trigramFeatureValues_'$corpus_option$test_or_train_option$classifier_option'.txt'

indPolarityFeaturesFileName=$data_path'indPolarityFeatureValues_'$corpus_option$test_or_train_option$classifier_option'.txt'
posnegPolarityFeaturesFileName=$data_path'posnegPolarityFeatureValues_'$corpus_option$test_or_train_option$classifier_option'.txt'
totalPolarityFeaturesFileName=$data_path'totalPolarityFeatureValues_'$corpus_option$test_or_train_option$classifier_option'.txt'

replyFeaturesFileName=$data_path'step4_Output_ReplyFeatures_'$corpus_option$test_or_train_option$classifier_option'.txt'
replyFeatureValuesFileName=$data_path'step6_ReplyFeaturesValues_'$corpus_option$test_or_train_option$classifier_option'.txt'

#$data_path'step4_Output_EmoticonFeatures_'$corpus_option$test_or_train_option$classifier_option'.txt'
emoticonFeaturesFileName=$data_path'step4_Output_EmoticonFeatures_'$corpus_option$test_or_train_option$classifier_option'.txt'
#echo 'emoticonFeatures File name -----------------------',$classifieroption
emoticonFeatureValuesFileName=$data_path'step6_EmoticonFeatureValues_'$corpus_option$test_or_train_option$classifier_option'.txt'
interjectionFeatureFileName=$data_path'step6_InterjectionFeatureValues_'$corpus_option$test_or_train_option$classifier_option'.txt'

echo 'InterjectionFile name -------------- ',$interjectionFeatureFileName

stopwordfilename=$data_path'stopwords.txt'
#NGramFeatureOutputFile=$data_path'FValues_NGramFeatures_'$corpus_option$test_or_train_option$classifier_option'.txt'
SVMInputFile=$data_path'SVMInput_'$corpus_option$classifier_option$test_or_train_option'.txt'
classfilename=$data_path'step2_'$corpus_option'InputCorpus'$classifier_option$test_or_train_option'-class.txt'

MergeFeaturesScript=$script_path'step7_MergeFeatures.py'
extractNGramFeaturesScript=$script_path'step5_FindNGrams.py'
extractNGramFeatureValuesScript=$script_path'step6_FindNGramFeatureValues.py'
extractEmoticonFeatureValuesScript=$script_path'step6_ExtractEmoticonFeatures.py'
extractPolarityFeatureValuesScript=$script_path'step6_ExtractPolarityFeatures.py'
extractInterjectionFeaturesScript=$script_path'step6_ExtractInterjectionsFeatures.py'

step6_FormMalletInputScript=$script_path'step6_FormMalletInput.py'
step6_MalletInputFileName=$data_path'step6_MalletInput_'$corpus_option$test_or_train_option'.txt'
step6_MalletInputFileNameMF=$data_path'step6_MalletInput_'$corpus_option$test_or_train_option'.mallet'
step6_MalletTopicState=$data_path'step6_Mallet_Topic_State_'$corpus_option$test_or_train_option'.gz'
step6_MalletOutputKeys=$data_path'step6_Mallet_Output_Keys_'$corpus_option$test_or_train_option'.txt'
step6_MalletOutputFile=$data_path'step6_Mallet_Output_'$corpus_option$test_or_train_option'.txt'

step6_ExtractTopicFeaturesScript=$script_path'step6_ExtractTopicFeatureValues.py'
step6_TopicFeatureValues=$data_path'step6_TopicFeatureValues_'$corpus_option$test_or_train_option$classifieroption'.txt'

#trigramfinalFeatureValue=28590   ####last feature id of trigram features + 1

if [ "$test_or_train_option" == "-t" ]; then
	echo 'TRAIN : Finding feature values'
	python $extractNGramFeaturesScript $twitterinputfile $unigramfilename $bigramfilename $trigramfilename $stopwordfilename
fi

unigramFeatureCount=$(wc -l <$unigramfilename)
bigramFeatureCount=$(wc -l <$bigramfilename)
trigramFeatureCount=$(wc -l <$trigramfilename)
let trigramfinalFeatureValue=$unigramFeatureCount+$bigramFeatureCount+$trigramFeatureCount+1   ####last feature id of trigram features + 1
let emoticonfinalFeatureValue=$trigramfinalFeatureValue+15+1

python $extractNGramFeatureValuesScript $twitterinputfile $unigramfilename $bigramfilename $trigramfilename $unigramFeatureValuesFileName $bigramFeatureValuesFileName $trigramFeatureValuesFileName

python $extractEmoticonFeatureValuesScript $emoticonFeaturesFileName $emoticonFeatureValuesFileName $trigramfinalFeatureValue

python $extractEmoticonFeatureValuesScript $replyFeaturesFileName $replyFeatureValuesFileName $emoticonfinalFeatureValue

let replyfinalFeatureValue=$emoticonfinalFeatureValue+1

python $extractPolarityFeatureValuesScript $dict_file $twitterinputfile $replyfinalFeatureValue $indPolarityFeaturesFileName $posnegPolarityFeaturesFileName $totalPolarityFeaturesFileName

let finalpolarityFeatureValue=$replyfinalFeatureValue+13+1

########################################################## Extract topic based features #######################################

python $step6_FormMalletInputScript $twitterinputfile > $step6_MalletInputFileName

echo 'Done with creating Mallet input'

$MALLET_PATH'bin/mallet' import-file --input $step6_MalletInputFileName --output $step6_MalletInputFileNameMF --keep-sequence --remove-stopwords

echo 'Input file with .mallet format is created'

$MALLET_PATH'bin/mallet' train-topics --input $step6_MalletInputFileNameMF --num-topics 100 --output-state $step6_MalletTopicState --output-topic-keys $step6_MalletOutputKeys --output-doc-topics $step6_MalletOutputFile

echo 'Done with topic modelling with mallet'

python $step6_ExtractTopicFeaturesScript $finalpolarityFeatureValue $step6_MalletOutputFile > $step6_TopicFeatureValues

echo 'Extracted topic features using mallet'

###############################################################################################################################

let finaltopicFeatureValue=$finalpolarityFeatureValue+100+1

python $extractInterjectionFeaturesScript $twitterinputfile $interjectionFileName $interjectionFeatureFileName $finaltopicFeatureValue

#python $MergeFeaturesScript $classfilename $SVMInputFile $unigramFeatureValuesFileName $bigramFeatureValuesFileName $trigramFeatureValuesFileName $totalPolarityFeaturesFileName $interjectionFeatureFileName 

#$bigramFeatureValuesFileName $trigramFeatureValuesFileName $emoticonFeatureValuesFileName $interjectionFeatureFileName 

# $bigramFeatureValuesFileName 
#$emoticonFeatureValuesFileName $step6_TopicFeatureValues


#$unigramFeatureValuesFileName
#$bigramFeatureValuesFileName
#$trigramFeatureValuesFileName
#$emoticonFeatureValuesFileName
#$indPolarityFeaturesFileName $posnegPolarityFeaturesFileName $totalPolarityFeaturesFileName
