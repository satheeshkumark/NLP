import MySQLdb
import codecs
import sys
import datetime
import time
from stringNormalize import normalize

englishkeywords = ['anger', 'angry', 'disgust', 'disgusted', 'fear', 'afraid', 'joy', 'joyful', 'enjoy', 'enjoying', 'sad', 'sadness', 'surprise', 'surprised', 'happy', 'happiness', 'ecstatic','pride','proud','contempt','sarcasm','sarcastic','quotes']
spanishkeywords = ['ira', 'enojado', 'asco', 'asqueado', 'miedo', 'alegria', 'alegre', 'triste', 'tristeza', 'sorpresa', 'sorprendido', 'felicidad', 'extatico', 'orgullo', 'orgulloso', 'rabia', 'repugnancia', 'diversion', 'desprecio','sarcasmo']
months = ['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']

conn = MySQLdb.connect(host= "localhost",
                  user="root",
                  passwd="sat",
                  db="DR")
cur = conn.cursor()

inputfilename = sys.argv[1]

inputfile = codecs.open(inputfilename,'UTF-8')
lineno = 0
query = """INSERT INTO TWEETS(tweet_id,username,tweet_text,tweet_createdate,user_location,tweet_lang,tweet_location,tweet_hashtags) values(%s,%s,%s,%s,%s,%s,%s,%s)"""

for inputline in inputfile :
	try:
		tweethashtaglist = []
		inputline = inputline.strip('\r\n')		
		inputline = inputline.strip()
		#inputline = inputline.strip('\t')
		inputlist = inputline.split('\t')
		tweet_id = str(inputlist[0])
		username = str(inputlist[1])
		tweet_text = str(inputlist[2])
		tweet_text_list = tweet_text.split(' ')
		for i in range(0,len(tweet_text_list)):
			tweet_text_list[i] = normalize(tweet_text_list[i])
		tweet_text = ' '.join(tweet_text_list)
		rawdate = []
		rawlist = []
		rawdate = str(inputlist[3])
		rawlist = inputlist[3].split(' ')
		datev = str(rawlist[2])
		yearv = str(rawlist[5])
		monthv = months.index(rawlist[1].lower()) + 1
		monthv = str(monthv)
		timev = str(rawlist[3])
		datetimev =  yearv + '_' + monthv + '_' + datev + ' ' + timev
		tweetcreatedate = time.strftime(datetimev)
		userlocation = str(inputlist[4])
		tweetlang = str(inputlist[5])
		tweetlocation = str(inputlist[6])
		tweethashtags = str(inputlist[7])
		tweethashtaglist = tweethashtags.split('_')
		hashflag = 0

		print username,'\t',tweet_text,'\t',tweetlang,'\t',tweetcreatedate
		for element in tweethashtaglist :
			if tweetlang == 'es' :
				if element in spanishkeywords :
					hashflag = 1
				else :
					continue				
			if tweetlang == 'en' :
				if element in englishkeywords :
					hashflag = 1
				else :
					continue
		if hashflag == 1 :
			cur.execute(query,(tweet_id,username,tweet_text,tweetcreatedate,userlocation,tweetlang,tweetlocation,tweethashtags))
			print 'INSERTED'
			conn.commit()
		else :
			print 'NOT INSERTED'
	except:
		print 'exception : ',sys.exc_info()[0],sys.exc_info()[1]
		conn.rollback()

inputfile.close()

conn.close()
