from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import codecs
import sys

consumer_key="XXXXXXXXXXXXXXXXXXXXXXXXXXX"	
consumer_secret="XXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
access_token="XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
access_token_secret="XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

class StdOutListener(StreamListener):
	def on_data(self, data):
		print data
		return True

	def on_error(self, status):
		print status

if __name__ == '__main__':
	filenames = []
	keywords = []
	for i in range(1,len(sys.argv)) :
		filenames.append(sys.argv[i])
	for filename in filenames :
		fin = codecs.open(filename)
		for inputline in fin :
			inputline = inputline.strip('\r\n')
			keywords.append(inputline)
		fin.close()
	l = StdOutListener()
	auth = OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)

	stream = Stream(auth, l)		
	stream.filter(track=keywords)
