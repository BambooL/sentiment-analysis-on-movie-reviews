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

stopset = set(stopwords.words('english'))

def word_feats(str):
  words=[]
  sep=re.split("\.|!|\?", str)
  for item in sep:
    item=word_tokenize(item)
    words.extend(nltk.pos_tag(item))
  res=[]
  # for each in words:
  #   if (each[1]=="JJ" or each[1]=="JJS" or each[1]=="VB"):
  #     res.append(each[0])

#--------------------------------------------------------------------------------------------
  # Choose the feature, from the top to bottom: Uni-gram, Uni-gram without stop words, Bi-gram,
  # tri-gram. If you adopted the Bi-gram or Tri-gram, please use different returns
  
  # dict1= dict([(word, True) for word in str.split(" ") if word not in stopset])
  dict1= dict([(word, True) for word in words if word not in stopset])
  # dict2= dict([(word, True) for word in ngrams(str, 2).split("&&") if word not in stopset] )
  # dict3= dict([word, True] for word in ngrams(str, 3).split("&&") )

  # dict1.update(dict2)
  # dict1.update(dict3)
  # print dict1
  return dict1
#--------------------------------------------------------------------------------------------


def ngrams(input, n):
  input = input.split(' ')
  output = ""
  for i in range(len(input)-n+1):
  	for j in range(i,i+n):
  		output+=input[j]+" "
  	output+="&&"
  return output[0:-3]


# read from file
f1=file('../data/balance/1.txt','r')
f2=file('../data/balance/2.txt','r')
f3=file('../data/balance/3.txt','r')
f4=file('../data/balance/4.txt','r')
f5=file('../data/balance/5.txt','r')
n=file('../data/balance/n.txt','r')
y=file('../data/balance/t.txt','r')

# five labels
# get the feature
onefeats = [(word_feats(line), 'one') for line in f1.readlines()]
twofeats = [(word_feats(line), 'two') for line in f2.readlines()]
threefeats = [(word_feats(line), 'thre') for line in f3.readlines()]
fourfeats = [(word_feats(line), 'four') for line in f4.readlines()]
fivefeats = [(word_feats(line), 'five') for line in f5.readlines()]
# yfeats = [(word_feats(movie_reviews.words(fileids=[f])), 'y') for f in yids]
 
# Separate into training/ testing set (3:1)
onecutoff = len(onefeats)*3/4
twocutoff = len(twofeats)*3/4
threecutoff = len(threefeats)*3/4
fourcutoff = len(fourfeats)*3/4
fivecutoff = len(fivefeats)*3/4


# 2 labels: good and not good 
trainfeats = onefeats[len(onefeats)/5:onecutoff] + twofeats[:twocutoff]+ threefeats[:threecutoff]+ fourfeats[:fourcutoff]+ fivefeats[:fivecutoff]
testfeats = onefeats[onecutoff:] + twofeats[twocutoff:]+ threefeats[threecutoff:]+ fourfeats[fourcutoff:]+ fivefeats[fivecutoff:]

print 'train on %d instances, test on %d instances' % (len(trainfeats), len(testfeats))
 
classifier = NaiveBayesClassifier.train(trainfeats)
print 'accuracy:', nltk.classify.util.accuracy(classifier, testfeats)

classifier.show_most_informative_features()

nfeats = [(word_feats(line), 'n') for line in n.readlines()]
yfeats = [(word_feats(line), 'y') for line in y.readlines()]

ncutoff = len(nfeats)*3/4
ycutoff = len(yfeats)*3/4

antrainfeats = nfeats[:ncutoff] + yfeats[:ycutoff]
antestfeats = nfeats[ncutoff:] + yfeats[ycutoff:]
print 'train on %d instances, test on %d instances' % (len(antrainfeats), len(antestfeats))

classifier = NaiveBayesClassifier.train(antrainfeats)

print 'accuracy:', nltk.classify.util.accuracy(classifier, antestfeats)
classifier.show_most_informative_features()

refsets = collections.defaultdict(set)
testsets = collections.defaultdict(set)

for i, (feats, label) in enumerate(antestfeats):
  refsets[label].add(i)
  observed = classifier.classify(feats)
  testsets[observed].add(i)

print 'y precision:', nltk.metrics.precision(refsets['y'], testsets['y'])
print 'y recall:', nltk.metrics.recall(refsets['y'], testsets['y'])
print 'y F-measure:', nltk.metrics.f_measure(refsets['y'], testsets['y'])
print 'n precision:', nltk.metrics.precision(refsets['n'], testsets['n'])
print 'n recall:', nltk.metrics.recall(refsets['n'], testsets['n'])
print 'n F-measure:', nltk.metrics.f_measure(refsets['n'], testsets['n'])


