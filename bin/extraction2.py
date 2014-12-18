import json
import urllib
import urllib2
import random
from pygoogle import pygoogle
# Aspect Extraction

import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import movie_reviews
from nltk.corpus import stopwords
import collections
import nltk.metrics
import nltk.classify.util
from nltk.tokenize import sent_tokenize, word_tokenize
import nltk
import re
from nltk.stem import *
from nltk.stem.snowball import SnowballStemmer
from nltk.corpus import wordnet
from nltk.corpus import wordnet as wn


def similarity(seed, word):
	a=wn.synsets(seed[0],pos='n')[0]
	if (wn.synsets(word,pos='n')==[]): return 0;
	b=wn.synsets(word,pos='n')[0]

	maxN=a.path_similarity(b)
	for item in seed:
		a=wn.synsets(item)[0]
		if a.lch_similarity(b)>maxN:
			maxN=a.lch_similarity(b)

	return min


agent=file('user_agents.txt','r')



def search(searchfor):
	g = pygoogle(searchfor)
	return g.get_result_count()

# def search(searchfor):
#     query = urllib.urlencode({'q': searchfor})
#     url = urllib2.Request('http://ajax.googleapis.com/ajax/services/search/web?v=1.0&%s' % query)
#     user_agent = agent.readline().split("\n")[0]
#     url.add_header('User-agent', user_agent)
#     search_response = urllib2.urlopen(url)
#     search_results = search_response.read()
#     results = json.loads(search_results)
#     data = results['responseData']
#     return data['cursor']['estimatedResultCount']

def pmi(word1, word2):
	result=float(search(word1+" "+word2))/(float(search(word1))*float(search(word2))) 
	return result



f=file('../data/trial.txt', 'r')
f1=file('../data/balance/1.txt','r')
f2=file('../data/balance/2.txt','r')
f3=file('../data/balance/3.txt','r')
f4=file('../data/balance/4.txt','r')
f5=file('../data/balance/5.txt','r')
n=file('../data/balance/n.txt','r')
y=file('../data/balance/t.txt','r')

# seed=["plot", "cast", "actor", "music", "story", "stereotype", "character", "acting", "director", "producer", "scene", "book", "adaptation"]
stemmer = SnowballStemmer("english")
part_discriminator="of movie"



for line in f2.readlines():
	words=[]
	sep=re.split("\.|!|\?", line)
	for item in sep:
		item=word_tokenize(item)
		words.extend(nltk.pos_tag(item))
	res=[]
	for each in words:
		if (each[1]=="NN" or each[1]=="NNS"):
			item = stemmer.stem(each[0])
			if (not (item in res)):
				res.append(item)
				print item+" :: "
				print pmi(item,part_discriminator)

			# if (not (each[0] in seed) and sim>5):
			

# print "-----------------------------------------------------------"
# print "-----------------------------------------------------------"
# print "seed"
# print seed









