import nltk
nltk.data.path.append('/Users/user/Documents/B4B/nltk_data') #your nltk data dir path
from nltk.corpus import stopwords
import string
import re 
 
regex_str = [
    r'<[^>]+>', # HTML tags
    r'(?:@[\w_]+)', # @-mentions
    r"(?:\#+[\w_]+[\w\'_\-]*[\w_]+)", # hash-tags
    r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&amp;+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+', # URLs
 
    r'(?:(?:\d+,?)+(?:\.?\d+)?)', # numbers
    r"(?:[a-z][a-z'\-_]+[a-z])", # words with - and '
    r'(?:[\w_]+)', # other words
    r'(?:\S)' # anything else
]

tokens_re = re.compile(r'('+'|'.join(regex_str)+')', re.VERBOSE | re.IGNORECASE)
punctuation = list(string.punctuation)
stop_words = stopwords.words('english') + punctuation + ['rt', 'via']

class Tokenizer():

	def preprocess(self, str):
		return tokens_re.findall(str)
	
	def tokenize(self, str):
		terms_only = [term for term in self.preprocess(str) 
					if term not in stop_words 
					and not term.startswith(('#', '@'))]

		return terms_only
