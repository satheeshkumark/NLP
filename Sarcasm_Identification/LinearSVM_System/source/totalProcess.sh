test_or_train_option=$1
corpus_option=$2
classifier_option=$3 ############################### '-bi' or '-tri'


echo 'Preprocessing tweets'
bash step2_PreProcessing_Tweets.sh $test_or_train_option $corpus_option $classifier_option

echo 'Forming the features for the '$corpus_option$test_or_train_option$classifier_option' system'
bash step3_FormFeatures.sh $test_or_train_option $corpus_option $classifier_option

echo 'Merging the feature values for the '$corpus_option$test_or_train_option$classifier_option' system'
bash step4_MergeFeatures.sh $test_or_train_option $corpus_option $classifier_option

echo 'Generating weka input file for the '$corpus_option$test_or_train_option$classifier_option' system'
bash step5_prepareWekaInput.sh $test_or_train_option $corpus_option $classifier_option

echo 'Weka input file generated successfully'
