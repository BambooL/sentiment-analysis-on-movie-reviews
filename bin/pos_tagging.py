import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import movie_reviews
from nltk.tokenize import sent_tokenize, word_tokenize
import nltk
import re


f1=file('../data/1.txt','r')
f2=file('../data/2.txt','r')
f3=file('../data/3.txt','r')
f4=file('../data/4.txt','r')
f5=file('../data/5.txt','r')
n=file('../data/n.txt','r')
y=file('../data/t.txt','r')


i=0;
while(1):     
  line=f1.readline();

  if (line):
  	result=[];
  	sep=re.split("\.|!|\?", line);
  	for item in sep:
  	  item=word_tokenize(item);
  	  result.extend(nltk.pos_tag(item));

  	for each in result:
  		if (each[1]=="JJ" or each[1]=="JJS" or each[1]=="VB"):
  			print each;

    i++;
  	


  else:
  	break


