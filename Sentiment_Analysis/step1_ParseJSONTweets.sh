inputJSONFile=$1
outputParseFile=$2
script_path='scripts/'
enDataPath='data/'
esDataPath='data1/'
ruDataPath='data2/'
faDataPath='data3/'
keywordPath='keywords/'

parseScript=$script_path'step0_jsonparser.py'
dbScript=$script_path'step0_InsertRecords.py'
enkeyWordFile=$enDataPath$keywordPath'en-keywords.txt'
eskeyWordFile=$esDataPath$keywordPath'es-keywords.txt'
rukeyWordFile=$ruDataPath$keywordPath'ru-keywords.txt'
fakeyWordFile=$faDataPath$keywordPath'fa-keywords.txt'


#################################

####	Input : Input JSON File containing Twitter data
####	Output : Parsed File containing tweets and their meta data

echo $outputParseFile
python $parseScript $inputJSONFile $outputParseFile

#################################

####	Input : Output of previous step. Parsed metdata file from twitter
####	Output : Inserts data in the database
####	Requirement : Have to configure the database settings within the step0_InsertRecords.py program
####	This code needs to be modified if any new language is going to be added

#python $dbScript $outputParseFile


################ Push the tweetmetadata into db depending on language and retrieve the tweets of required language.
################ The above script pushes the tweet metadata to db. NOTE : db is needed to be configured accordingly
################ The script filteringTweets.py pulls and processes tweets depending on the language

