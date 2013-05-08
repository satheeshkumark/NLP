outputFileName=$1
####	INPUT 	: Output file where the tweets need to be downloaded
####	OUTPUT  : Output file containing downloaded tweets
####	Description	:	Downloads tweets using twitter API
 
#### 	Give some location in hard disk which have more disk space. 
####	BEWARE..!!!!! Giving same name will override the already downloaded json file.
####	This script needs to be restarted every morning
script_path='scripts/'
enDataPath='data/'
esDataPath='data1/'
ruDataPath='data2/'
faDataPath='data3/'
keywordPath='keywords/'

####	These files contain the search terms for each tweet for each language. Need to be updated depending on the requiement 
downloadScript=$script_path'step0_downloadTweets.py'
enkeyWordFile=$enDataPath$keywordPath'en-keywords.txt'
eskeyWordFile=$esDataPath$keywordPath'es-keywords.txt'
rukeyWordFile=$ruDataPath$keywordPath'ru-keywords.txt'
fakeyWordFile=$faDataPath$keywordPath'fa-keywords.txt'

####	Download the tweets which has those kewords. Output will be in json format. Feed the json input to next script for further processing.

python $downloadScript $enkeyWordFile $eskeyWordFile $rukeyWordFile $fakeyWordFile > $outputFileName
