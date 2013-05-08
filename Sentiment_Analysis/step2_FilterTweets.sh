####################### Main Script File which runs every other python files and other tools###################################################

language_option=$1		####	Argument 1 : Language of the tweet
inputFileStep1=$2		####	Argument 2 : Input file containing the tweets downloaded from the database for a particular language
test_train_cutoffrange=$3	####	Argument 3 : Cuts train and test set
				####	Example	: specifying 4000 will cut the train size to 4000 tweets and the rest as test tweets	

if [ "$4" == "" ]; then
	data_path='data/'
else
	data_path=$4		####	Argument 4 : Data folder where the content is located. By default points to data/ folder
fi

script_path='scripts/' 
tokenizer_path=$script_path'ark-tweet-nlp-0.3.2/'
tagger_path=$script_path'ark-tweet-nlp-0.3.2/'

#inputFileStep1=$data_path'input_step1'$test_or_train_option'.txt'
inputFileStep2=$data_path'input_step2.txt'
tweetIdFileStep1=$data_path'tweet_id_Step1.txt'
inputFileStep3=$data_path'input_step3.txt'
inputFileStep4=$data_path'input_step4.txt'
inputFileStep5=$data_path'input_step5.txt'
inputFileStep6Train=$data_path'input_step5-t.txt'
inputFileStep6Test=$data_path'input_step5-T.txt'
classFileNameTrain=$data_path'classFileName-t.txt'
classFileNameTest=$data_path'classFileName-T.txt'

classFileName=$data_path'classFileName.txt'

filterScript='step1_FilterTweets.py'
tokenizerScript='twokenize.sh'
postProcessTokenizerScript='step3_PostProcess_Tokenized_Tweets.py'
taggerScript='runTagger.sh'
classSeparatingScript='step5_findClasses.py'
testTrainSeparatingScript='separateTestTrainTweets.py'
extractFeatureEmoticonScript='step6_ExtractEmoticonFeatures.py'


################################################################   STEP 1 #################################################

#Input : File containing tweets extracted from Db - All the tweets which contain sentiment words
#Output : File with tweets containing sentiment tag at its end
#Description : Takes the input as the file with tweets from the database and outputs the tweets which ends with sentiment hashtags

python $script_path$filterScript $inputFileStep1 $language_option $inputFileStep2 $tweetIdFileStep1 &&


################################################################   STEP 2 #################################################

####################################################### CMU Tokenizer Toolkit ###########################################
#Input : Input file containing sentiment tweets
#Output : Tokenized File containing sentiment tweets
#Description : Takes the input as the file with sentiment tweets, gives the input to the CMU Tokenizer and outputs the file with tokenized tweets


echo 'Tokenizing tweets.....................' &&

sh $tokenizer_path$tokenizerScript $inputFileStep2 > $inputFileStep3 &&

echo 'Done with Tokenizing'  &&

echo '' &&

################################################################   STEP 3 #################################################

#Input : Tokened Tweets file from CMU Tweet tokenizer
#Output : File containing post processed tokenized output
#Description : Takes the input as the file with tokenized tweets by CMU tokenizer and outputs the post processed output

echo 'Post Processing tokenized tweets.....................' &&

python $script_path$postProcessTokenizerScript $inputFileStep3 $language_option > $inputFileStep4 &&

echo 'Done with Post Processing the tokenized tweets'  &&

echo '' &&


################################################################   STEP 4 #################################################

#Input : Tokened Tweets file from CMU Tweet tokenizer
#Output : File containing post processed tokenized output
#Description : Takes the input as the file with tokenized tweets by CMU tokenizer and outputs the post processed output

echo 'Finding the classes.............' &&

python $script_path$classSeparatingScript $language_option $inputFileStep4 $inputFileStep5 $classFileName &&

echo 'Done with Finding the classes'  &&

echo ''


###############################################################    STEP 5 ###################################################

#Input : Tokenized Tweet files, Segregating Range - range which divides test and train files
#Output : Train ant Test tweets and class filenames
#Description : Takes the input as the file with tokenized tweets and separates test and train Files and classes


if [ "$test_train_cutoffrange" -gt 0 ]; then
	echo 'Separating Test and Train files ........................' &&

	python $script_path$testTrainSeparatingScript $test_train_cutoffrange $inputFileStep5 $classFileName $inputFileStep6Train $classFileNameTrain $inputFileStep6Test $classFileNameTest

	echo 'Test and Train files separated'
fi
