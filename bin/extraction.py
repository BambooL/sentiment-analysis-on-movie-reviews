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


f=file('../data/trial.txt', 'r')
f1=file('../data/balance/1.txt','r')
f2=file('../data/balance/2.txt','r')
f3=file('../data/balance/3.txt','r')
f4=file('../data/balance/4.txt','r')
f5=file('../data/balance/5.txt','r')
n=file('../data/balance/n.txt','r')
y=file('../data/balance/t.txt','r')

seed=["plot", "cast", "actor", "music", "story", "stereotype", "character", "acting", "director", "producer", "scene", "book", "adaptation"]
stemmer = SnowballStemmer("english")

for line in f3.readlines():

	seed2=""
	words=[]
	sep=re.split("\.|!|\?", line)
	for item in sep:
		item=word_tokenize(item)
		words.extend(nltk.pos_tag(item))
	res=[]
	for each in words:
		if (each[1]=="NN" or each[1]=="NNS"):
			try:
				item = stemmer.stem(each[0])
			except UnicodeDecodeError:
				continue
			res.append(item)
			sim=similarity(seed,item)
			# if (not (each[0] in seed) and sim>5):
			if (sim>5):
				seed2=seed2+" "+ item
	d = open('3_aspect.txt', 'a')
	d.write(seed2+"\n")
	d.close()

# print "-----------------------------------------------------------"
# print "-----------------------------------------------------------"
# print "aspect"
# print seed2