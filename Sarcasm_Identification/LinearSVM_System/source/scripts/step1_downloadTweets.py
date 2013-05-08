from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream


consumer_key="BX3UqzPqiOi6VRgwtJcCzg"	
consumer_secret="wgNIds2V7r8nTw7jbiZUKzFg1PD8eHxqgRz2TZQKiwo"
access_token="75971241-PEqQbUaJCHYWjQT0YzNm6qAYjP8ecmuqGHyxPP2lL"
access_token_secret="1KJf00iEr3B1vvrAXmjWWf0lMxC5SUg7ADtKWhAlsk"

class StdOutListener(StreamListener):
	def on_data(self, data):
		print data
		return True

	def on_error(self, status):
		print status

if __name__ == '__main__':
	l = StdOutListener()
	auth = OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)

	stream = Stream(auth, l)
	englishkeywords = ["#sarcasm","#sarcasmo","#sarcastic","#quotes"]
	#englishkeywords = ['#anger', '#angry', '#disgust', '#disgusted', '#fear', '#afraid', '#joy', '#joyful', '#enjoy', '#enjoying', '#sad', '#sadness', '#surprise', '#surprised', '#happy', '#happiness', '#ecstatic','#pride','#proud','#contempt','#sarcasm']
	#spanishkeywords = ['#ira', '#enojado', '#asco', '#asqueado', '#miedo', '#alegria', '#alegre', '#triste', '#tristeza', '#sorpresa', '#sorprendido', '#felicidad', '#extatico', '#orgullo', '#orgulloso', '#rabia', '#repugnancia', '#diversion', '#desprecio']
	spanishkeywords = []
	keywords = englishkeywords + spanishkeywords		
	stream.filter(track=keywords)
