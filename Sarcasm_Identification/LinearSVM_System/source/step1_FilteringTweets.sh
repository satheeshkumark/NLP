##

####################### Extracting Tweets from db ###################################################

#Input : File containing tweets extracted from Db - sarcastic Tweets
#Output : File with tweets containing sarcasm tag at its end
#Description : Takes the input as the file with tweets from the database and outputs the tweets which ends with sarcasm


language_option=$1

data_path='data/'
script_path='scripts/' 
filterScript='step1_FilterSarcasticTweets.py'
inputFileStep1=$data_path'step1_Input.txt'
inputFileStep2=$data_path'step2_Input.txt'
tweetIdFileStep1=$data_path'step1_Tweet_Id.txt'

echo 'Filtering Sarcastic Tweets from db.....................'  &&

python $script_path$filterScript $inputFileStep1 $language_option $inputFileStep2 $tweetIdFileStep1 &&

echo 'Done with Filtering Tweets --- Tweet ids are also generated separately'  &&

echo ''
