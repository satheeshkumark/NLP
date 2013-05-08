test_or_train_option=$1
corpus_option=$2
classifier_option=$3 ############################### '-bi' or '-tri'

data_path='data/'
script_path='scripts/'

inputFileStep2=$data_path'step2_'$corpus_option'InputCorpus'$test_or_train_option'.txt'
#inputFileStep2=$data_path'Facebook_statuses.txt'
inputFileStep3=$data_path'step3_'$corpus_option'TokenizedCorpus'$test_or_train_option$classifier_option'.txt'
inputFileStep4=$data_path'step4_'$corpus_option'TokenizedCorpus_PostProcessed'$test_or_train_option$classifier_option'.txt'
outputFileStep4_emoticonFeatures=$data_path'step4_Output_EmoticonFeatures_'$corpus_option$test_or_train_option$classifier_option'.txt'
outputFileStep4_ReplyFeatures=$data_path'step4_Output_ReplyFeatures_'$corpus_option$test_or_train_option$classifier_option'.txt'
inputFileStep5=$data_path'step5_'$corpus_option'InputCorpus_EmoticonRmvd'$test_or_train_option$classifier_option'.txt'
inputFileStep6=$data_path'step6_'$corpus_option'InputCorpus_Parsed'$test_or_train_option$classifier_option'.txt'
inputFileStep7=$data_path'step7_'$corpus_option'InputCorpus_Parsed'$test_or_train_option$classifier_option'.txt'
tagSequenceFile_Step7=$data_path'step7_'$corpus_option'tagSequenceFile'$test_or_train_option$classifier_option'.txt'

tokenizer_path=$script_path'ark-tweet-nlp-0.3.2/'
tagger_path=$script_path'ark-tweet-nlp-0.3.2/'
postProcessTokenizerScript=$script_path'step3_PostProcess_Tokenized_Tweets.py'
extractFeatureEmoticonScript=$script_path'step4_ExtractEmoticonFeatures.py'
tokenizerScript='twokenize.sh'
taggerScript='runTagger.sh'
parserOtptPostProcessScript='step6_PostProcessParserResult.py'


################################################################   STEP 2 #################################################

####################################################### CMU Tokenizer Toolkit ###########################################
#Input : Input file containing Training or testing tweets
#Output : Tokenized File containing training or testing tweets
#Description : Takes the input as the file with input tweets, gives the input to the CMU Tokenizer and outputs the file with tokenized tweets


echo 'Tokenizing tweets.....................' &&

sh $tokenizer_path$tokenizerScript $inputFileStep2 > $inputFileStep3 &&

echo 'Done with Tokenizing' &&

echo '' &&

################################################################   STEP 3 #################################################

#Input : Tokenized Tweets file from CMU Tweet tokenizer
#Output : File containing post processed tokenized output
#Description : Takes the input as the file with tokenized tweets by CMU tokenizer and outputs the post processed output

echo 'Post Processing tokenized tweets.....................' &&

python $postProcessTokenizerScript $inputFileStep3 > $inputFileStep4 &&

echo 'Done with Post Processing the tokenized tweets'  &&

echo '' &&

################################################################   STEP 4 #################################################

#Input : Tokenized Tweets file from CMU Tweet tokenizer
#Output : File containing post processed tokenized output
#Description : Takes the input as the file with tokenized tweets by CMU tokenizer and outputs the post processed output

echo 'Finding Feature values from emoticons.............' &&

python $extractFeatureEmoticonScript $inputFileStep4 $outputFileStep4_emoticonFeatures $inputFileStep5 $outputFileStep4_ReplyFeatures &&

echo 'Done with extracting Features from Emoticon'  &&

echo '' &&

################################################################   STEP 5 #################################################
####################################################### CMU Parser Toolkit ###########################################
#Input : Post Processed Input File containing Tokenized tweets
#Output : Parsed Un post Processed File containing the best parse for each tweet
#Description : Takes the input as the file with tokenized tweets, gives the input to the CMU Tokenizer and outputs the file with parsed tweets

echo 'Tagging the tweets............................' &&

sh $tagger_path$taggerScript $inputFileStep5 > $inputFileStep6 &&

echo 'Done with Tagging the tokenized tweets' &&

###############################################################   STEP 6 ##################################################
###########################################################################################################################

#Input : File containing Parsed Tweets
#Output : Files containing output and parses separately
#Description : Takes the input as the file with tokenized tweets, gives the input to the CMU Tokenizer and outputs the file with parsed tweets

echo 'Post processing Parsed sentences' &&

python $script_path$parserOtptPostProcessScript $inputFileStep6 $inputFileStep7 $tagSequenceFile_Step7 &&

echo 'Done with post processing the parsed sentences'
