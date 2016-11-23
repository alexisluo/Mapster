import pymongo
from Tokenizer import *
from collections import Counter
import nltk
import json

class TweetsHandler():
	tokenizer =  Tokenizer()

	def tweetsToWords(self, filename):
		tweetTokens = []
		with open(fname, 'r') as f:
			for line in f:
				tweet = json.loads(line)

				if 'text' not in tweet.keys():
					continue

				#lineTokens = self.tokenizer.tokenize(tweet['text'])
				lineTokens = nltk.word_tokenize(tweet['text'])
				print lineTokens

				tagged = nltk.pos_tag(lineTokens)
				tokenJJ = [term for term in tagged 
						if (term[1] == 'JJ' or term[1] == 'JJR' or term[1] == 'JJS')] # only adjective

				tweetTokens += tokenJJ

		return tweetTokens

	def countAssociation(self, tweetTokens):
		cnt = Counter()
		cnt.update(tweetTokens)
		return cnt.most_common(20)

handler = TweetsHandler()
tweetTokens = handler.tweetsToWords('Samsung.json')
countAssociation = handler.countAssociation(tweetTokens)
print countAssociation