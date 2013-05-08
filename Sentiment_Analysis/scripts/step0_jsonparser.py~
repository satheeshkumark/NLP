import sys
import simplejson
import difflib
import codecs

filename = sys.argv[1]
outputfilename = sys.argv[2]
flag = 0

f = codecs.open(filename,'UTF-8')
outputfile = codecs.open(outputfilename,'w','UTF-8')

lineno = 0

for line in f:
	lineno += 1
	hashtags = []
	try :
		tweet = simplejson.loads(line)
	except ValueError :
		print 'this line is not a valid json string:'
		#print line
		print
		continue
	for element in tweet['entities']['hashtags'] :
		hashtags.append(element['text'].lower())
	
	if tweet.has_key("retweeted_status") or not tweet.has_key("text") or len(hashtags) == 0: 
		continue

	#print line
	tweetlang = ''

	if( (not tweet.has_key("lang")) and (not tweet['user'].has_key('lang')) ):
		print 'lang not in tweet'
		continue
	elif(tweet.has_key("lang")) :
		tweetlang = tweet['lang']
	elif(tweet['user'].has_key('lang')) :
		tweetlang = tweet['user']['lang']

	tweetid = tweet["id_str"]
	text = tweet["text"].lower()
	text = text.replace('\n',' ')
	outputstring = ''
	outputstring = tweetid + '\t' + tweet['user']['screen_name'] + '\t' + text + '\t' + tweet['created_at'] + '\t' + tweet['user']['location'] + '\t' + tweetlang
		
	geo_status = str(tweet['geo']).lower()

	if geo_status != 'none' :	
		outputstring += '\t' + str(tweet['geo']['coordinates'])
	else :
		outputstring += '\t' + geo_status

	outputstringlist = outputstring.split('\t')
	if len(hashtags) != 0:
		outputstring += '\t' + '_'.join(hashtags)
		outputstring += '\r\n'
		outputfile.write(outputstring)
		#print outputstring
outputfile.close()

