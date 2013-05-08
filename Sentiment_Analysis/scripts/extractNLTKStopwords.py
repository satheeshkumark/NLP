from nltk.corpus import stopwords
import sys

#################################################################### File Description ######################################################

#Input : Nothing
#Output : NLTK stopword list
#Description : Extracts stop word list for english language from nltk collection

lang = sys.argv[1]

stopset = set(stopwords.words(lang))
stopwordslist = list(stopset)
stopwordslist.sort()

for element in stopwordslist :
	print element
