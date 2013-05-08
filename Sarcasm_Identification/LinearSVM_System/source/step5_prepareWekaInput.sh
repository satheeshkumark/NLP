test_or_train_option=$1
corpus_option=$2
classifier_option=$3 ############################### '-bi' or '-tri'

data_path='data/'
weka_data_path='data/weka_data/'
script_path='scripts/'

tweetinputFile=$data_path'step5_'$corpus_option'InputCorpus_EmoticonRmvd'$test_or_train_option$classifier_option'.txt'
emoticonFeatureFile=$data_path'step4_Output_EmoticonFeatures_'$corpus_option$test_or_train_option$classifier_option'.txt'
replyFeatureFile=$data_path'step4_Output_ReplyFeatures_'$corpus_option$test_or_train_option$classifier_option'.txt'
posnegPolarityFile=$data_path'posnegPolarityFeatureValues_'$corpus_option$test_or_train_option$classifier_option'.txt.weka'
totalPolarityFile=$data_path'totalPolarityFeatureValues_'$corpus_option$test_or_train_option$classifier_option'.txt.weka'
interjectionFile=$data_path'step6_InterjectionFeatureValues_'$corpus_option$test_or_train_option$classifier_option'.txt.weka'
classfilename=$data_path'step2_'$corpus_option'InputCorpus'$classifier_option$test_or_train_option'-class.txt'

prepareWekaInputScript=$script_path'step5_prepareWekaInputFile.py'

numberOfLines=$(wc -l <$tweetinputFile)
outputfilename=$weka_data_path'WekaOutput'$corpus_option$test_or_train_option$classifier_option'.arff'
echo 'input file name : '$tweetinputFile
python $prepareWekaInputScript $numberOfLines $outputfilename $classfilename $tweetinputFile $emoticonFeatureFile $replyFeatureFile $interjectionFile

#$interjectionFile

#$posnegPolarityFile

#$totalPolarityFile

#$replyFeatureFile

#$emoticonFeatureFile $replyFeatureFile
# $posnegPolarityFile $totalPolarityFile $interjectionFile


#$emoticonFeatureFile $replyFeatureFile $posnegPolarityFile $totalPolarityFile $interjectionFile
