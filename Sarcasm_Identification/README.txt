===================================================================================== README =========================================================================


To run Premilinary Linear SVM System,please follow below steps

To preprocess tweets,

The following values should be passsed to command line wherever required

$test_option = '-t' for train and '-T' for test data
$corpus_option = 'NS' or 'PS' or 'PNS' or 'PS'
$classifier_option = '-bi' or '-tri'

1. Enter into 'LinearSVM_System/source/' folder and run following commands

2. bash step2_PreProcessing_Tweets.sh $test_or_train_option $corpus_option $classifier_option

3. bash step3_FormFeatures.sh $test_or_train_option $corpus_option $classifier_option

4. bash step4_MergeFeatures.sh $test_or_train_option $corpus_option $classifier_option

5. bash step4_Run_SVM_Classifier.sh $test_or_train_option $corpus_option $classifier_option

6. bash step5_prepareWekaInput.sh $test_or_train_option $corpus_option $classifier_option

To run the systems which are Implemented with Dimensionality techniques, please follow below steps

1. Enter into 'SystemWithPCA/MODELS' folder to load the trained model into weka

2. To load Train 'ARFF' files Enter into 'SystemWithPCA/Train_Input' folder to load the training file into weka

3. To load test 'ARFF' files Enter into 'SystemWithPCA/Test_Input' folder to load the test file into weka

4. Select and run the weka classifier


NOTE : 

'NS' - Negative vs Sarcasm Classifier
'PS' - Positive vs Sarcasm Classifier
'PNS-bi' - Non-Sarcasm vs Sarcasm classifier
'PNS-tri' - Positive vs Negative vs Sarcasm classifier

Models, input test and train files are named with the combination of above words. Load the model and arff files of same type.
