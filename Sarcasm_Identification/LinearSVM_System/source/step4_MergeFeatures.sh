test_or_train_option=$1	############################ '-t' or '-T'
corpus_option=$2     ############################### 'PNS' or 'PS' or 'NS'
classifier_option=$3 ############################### '-bi' or '-tri'


data_path='data/'
script_path='scripts/'

#classfilename=$data_path'fbclass.txt'
classfilename=$data_path'step2_'$corpus_option'InputCorpus'$classifier_option$test_or_train_option'-class.txt'
SVMInputFile=$data_path'SVMInput_'$corpus_option$classifier_option$test_or_train_option'.txt'

unigramFeatureValuesFileName=$data_path'unigramFeatureValues_'$corpus_option$test_or_train_option$classifier_option'.txt'
bigramFeatureValuesFileName=$data_path'bigramFeatureValues_'$corpus_option$test_or_train_option$classifier_option'.txt'
trigramFeatureValuesFileName=$data_path'trigramFeatureValues_'$corpus_option$test_or_train_option$classifier_option'.txt'

indPolarityFeaturesFileName=$data_path'indPolarityFeatureValues_'$corpus_option$test_or_train_option$classifier_option'.txt'
posnegPolarityFeaturesFileName=$data_path'posnegPolarityFeatureValues_'$corpus_option$test_or_train_option$classifier_option'.txt'
totalPolarityFeaturesFileName=$data_path'totalPolarityFeatureValues_'$corpus_option$test_or_train_option$classifier_option'.txt'

emoticonFeaturesFileName=$data_path'step4_Output_EmoticonFeatures_'$corpus_option$test_or_train_option$classifier_option'.txt'
emoticonFeatureValuesFileName=$data_path'step6_EmoticonFeatureValues_'$corpus_option$test_or_train_option$classifier_option'.txt'
interjectionFeatureFileName=$data_path'step6_InterjectionFeatureValues_'$corpus_option$test_or_train_option$classifier_option'.txt'
step6_TopicFeatureValues=$data_path'step6_TopicFeatureValues_'$corpus_option$test_or_train_option$classifieroption'.txt'

replyFeatureValuesFileName=$data_path'step6_ReplyFeaturesValues_'$corpus_option$test_or_train_option$classifier_option'.txt'

MergeFeaturesScript=$script_path'step7_MergeFeatures.py'


python $MergeFeaturesScript $classfilename $SVMInputFile $unigramFeatureValuesFileName $bigramFeatureValuesFileName $trigramFeatureValuesFileName $emoticonFeatureValuesFileName $replyFeatureValuesFileName $indPolarityFeaturesFileName $posnegPolarityFeaturesFileName $totalPolarityFeaturesFileName $interjectionFeatureFileName

#$replyFeatureValuesFileName


#$bigramFeatureValuesFileName $trigramFeatureValuesFileName

#$posnegPolarityFeaturesFileName


#$emoticonFeatureValuesFileName
#$step6_TopicFeatureValues

#$posnegPolarityFeaturesFileName $totalPolarityFeaturesFileName

#$trigramFeatureValuesFileName $unigramFeatureValuesFileName $bigramFeatureValuesFileName
# $totalPolarityFeaturesFileName $interjectionFeatureFileName


#$bigramFeatureValuesFileName $trigramFeatureValuesFileName $emoticonFeatureValuesFileName $interjectionFeatureFileName 

# $bigramFeatureValuesFileName 
#$emoticonFeatureValuesFileName $step6_TopicFeatureValues


#$unigramFeatureValuesFileName
#$bigramFeatureValuesFileName
#$trigramFeatureValuesFileName
#$emoticonFeatureValuesFileName
#$indPolarityFeaturesFileName $posnegPolarityFeaturesFileName $totalPolarityFeaturesFileName


####Features By Order :

#1.$unigramFeatureValuesFileName	2.$bigramFeatureValuesFileName		3.$trigramFeatureValuesFileName	
#4.$emoticonFeatureValuesFileName	4.$replyFeatureValuesFileName		5.$indPolarityFeaturesFileName		
#6.$posnegPolarityFeaturesFileName	7.$totalPolarityFeaturesFileName	8.$step6_TopicFeatureValues
#9.$interjectionFeatureFileName		#10.$interjectionFeatureFileName


