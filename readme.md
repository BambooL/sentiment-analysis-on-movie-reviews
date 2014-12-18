# Document

## What have been done

### Preprocessing (csvvvv.py)
* Clean the pieces of reviews with imcomplete data (such as no score or no movie name);
* Sampling from the whole dataset with random choices. We get out 11040 pieces of reviews, which include
* Transform the .txt file to .csv file in order to separate the data by the score(1.0-5.0);
* Separate the reviews into [1-5].txt files that each of them contains the reviews of a typical score;
* Merge [1-3].txt into n.txt; Merge [4-5].txt into y.txt;

### Feature (classifier.py)
* Use bag of words as the Feature
* Calculate the vector for each Document
* Example: 

```
[({'this': True, 'love': True, 'deal': False, 'tired': False, 'feel': False, 'is': 
	False, 'am': False, 'an': False,  'ca': False, 'best': False, '!': False, 'what': False, 
	'.': True, 'amazing': False, 'horrible': False, 'sworn': False, 'awesome': False, 'do': False, 
	'good': False, 'very': False, 'not': False, 'with': False, 
	'he': False, 'enemy': False, 'about': False, 'like': False]
```
* Bi-gram

### Model
* Naive Bayes
* classifier = NaiveBayesClassifier.train(trainfeats) 

### Result
* We separate the data into training set and testing set: 3:1

#### Using Bag of Words
* If we want to predict the exact score based on the reviews, which means the number of labels 
is 5. The accuracy is pretty low. We can only achieve 31.66% accuracy. The result is shown as
follows.

```
train on 8280 instances, test on 2760 instances
accuracy: 0.316555249705
Most Informative Features
                    Save = True              one : five   =     63.8 : 1.0
                    Josh = True             thre : five   =     58.2 : 1.0
                    Bush = True             thre : five   =     56.7 : 1.0
                 stupid. = True              two : five   =     42.0 : 1.0
                   Damon = True             thre : five   =     40.6 : 1.0
                  toilet = True              one : five   =     38.3 : 1.0
                  wooden = True              two : five   =     35.5 : 1.0
                  awful, = True              two : five   =     35.5 : 1.0
                  angels = True             thre : five   =     33.5 : 1.0
                   jumps = True             thre : five   =     33.5 : 1.0
```
* If we just separate the reviews into good(score[4-5]) and not good(score[1-3]). We test on the dataset again and find the accuracy is much higher.

```
train on 8278 instances, test on 2762 instances
accuracy: 0.699879590608
Most Informative Features
               horrible. = True                n : y      =     35.9 : 1.0
                 stupid. = True                n : y      =     31.6 : 1.0
                    Save = True                n : y      =     25.5 : 1.0
                   crap. = True                n : y      =     20.7 : 1.0
                  shoddy = True                n : y      =     18.5 : 1.0
               McLintock = True                n : y      =     18.5 : 1.0
                    zero = True                n : y      =     17.6 : 1.0
                   Sorry = True                n : y      =     16.3 : 1.0
                garbage. = True                n : y      =     16.3 : 1.0
                 zombies = True                n : y      =     14.1 : 1.0
```

#### Using Bi-gram
**Difference with Uni-gram**

* Some typical features in bi-gram are strongly related to the ranking, such as '2 stars' '3 stars';
* Some words does not make sense in Uni-gram show their power in this round, such as 'absolutely no';
* 'No' cases can be solved to some extent, such as 'not good'.

```
train on 8278 instances, test on 2762 instances
accuracy: 0.309633269483
Most Informative Features
                2 stars  = True              two : five   =     93.8 : 1.0
              Save your  = True              one : five   =     53.6 : 1.0
                3 stars  = True             thre : five   =     51.2 : 1.0
             films were  = True              two : five   =     48.5 : 1.0
              comes off  = True              two : five   =     48.5 : 1.0
                 it two  = True              two : five   =     48.5 : 1.0
           the machines  = True              two : five   =     48.5 : 1.0
                 as bad  = True              two : five   =     48.5 : 1.0
               money on  = True              one : five   =     43.4 : 1.0
               waste of  = True              one : five   =     43.4 : 1.0
train on 8280 instances, test on 2760 instances
accuracy: 0.715507246377
Most Informative Features
              Save your  = True                n : y      =     33.7 : 1.0
            Don't waste  = True                n : y      =     29.4 : 1.0
                3 stars  = True                n : y      =     24.2 : 1.0
             excuse for  = True                n : y      =     22.9 : 1.0
          horror movie,  = True                n : y      =     22.9 : 1.0
      very disappointed  = True                n : y      =     22.9 : 1.0
            worst movie  = True                n : y      =     20.7 : 1.0
           worst movies  = True                n : y      =     20.7 : 1.0
               had high  = True                n : y      =     20.7 : 1.0
          absolutely no  = True                n : y      =     20.7 : 1.0
```


#### Using Uni-gram & Bi-gram
* Use them together
* bi-gram takes more seat
* Some repeat cases: 'Save' 'Save your'
* Overfit?

```
train on 8278 instances, test on 2762 instances
accuracy: 0.305635440701
Most Informative Features
                2 stars  = True              two : five   =     93.8 : 1.0
                    Save = True              one : five   =     63.8 : 1.0
                    Josh = True             thre : five   =     58.3 : 1.0
                    Bush = True             thre : five   =     56.8 : 1.0
              Save your  = True              one : five   =     53.6 : 1.0
                3 stars  = True             thre : five   =     51.2 : 1.0
             films were  = True              two : five   =     48.5 : 1.0
              comes off  = True              two : five   =     48.5 : 1.0
                 it two  = True              two : five   =     48.5 : 1.0
           the machines  = True              two : five   =     48.5 : 1.0
train on 8280 instances, test on 2760 instances
accuracy: 67219537219251
Most Informative Features
               horrible. = True                n : y      =     35.9 : 1.0
              Save your  = True                n : y      =     33.7 : 1.0
                 stupid. = True                n : y      =     31.6 : 1.0
                    Save = True                n : y      =     25.5 : 1.0
            Don't waste  = True                n : y      =     25.0 : 1.0
                3 stars  = True                n : y      =     24.2 : 1.0
             excuse for  = True                n : y      =     22.9 : 1.0
          horror movie,  = True                n : y      =     22.9 : 1.0
      very disappointed  = True                n : y      =     22.9 : 1.0
            worst movie  = True                n : y      =     20.7 : 1.0
```
#### Stop words 
Stopwords are words that are generally considered useless. Most search engines ignore these words because they are so common that including them would greatly increase the size of the index without improving precision or recall. NLTK comes with a stopwords corpus that includes a list of 128 english stopwords. Let’s see what happens when we filter out these words.

```
train on 8670 instances, test on 2210 instances
accuracy: 0.373484162896
Most Informative Features
                    Save = True              one : five   =     85.0 : 1.0
                   Damon = True              one : five   =     57.8 : 1.0
                  awful. = True              two : five   =     48.6 : 1.0
                  toilet = True              one : five   =     44.2 : 1.0
             pretentious = True              one : five   =     44.2 : 1.0
                   mess. = True              two : five   =     42.1 : 1.0
                 stupid. = True              two : five   =     42.1 : 1.0
                   steer = True              one : five   =     37.4 : 1.0
                   trite = True              one : five   =     37.4 : 1.0
train on 8280 instances, test on 2760 instances
accuracy: 0.730072463768
Most Informative Features
               horrible. = True                n : y      =     40.3 : 1.0
                    Save = True                n : y      =     25.5 : 1.0
                 stupid. = True                n : y      =     22.9 : 1.0
               McLintock = True                n : y      =     20.7 : 1.0
                  silly. = True                n : y      =     20.7 : 1.0
                  shoddy = True                n : y      =     18.5 : 1.0
               pathetic. = True                n : y      =     16.3 : 1.0
                 zombies = True                n : y      =     14.1 : 1.0
                conclude = True                n : y      =     14.1 : 1.0
                   swamp = True                n : y      =     14.1 : 1.0
                   
```
* Did not gain much but helps a little.

#### Make the dataset balanced
```
train on 4082 instances, test on 1361 instances
accuracy: 0.755326965467
Most Informative Features
                  Duvall = True                y : n      =     16.2 : 1.0
                   Count = True                n : y      =     15.1 : 1.0
                   Damon = True                n : y      =     14.3 : 1.0
                    Save = True                n : y      =     14.3 : 1.0
               horrible. = True                n : y      =     13.6 : 1.0
                   Haden = True                y : n      =     13.6 : 1.0
               contrived = True                n : y      =     12.9 : 1.0
                   Monte = True                n : y      =     12.1 : 1.0
                 Vampire = True                y : n      =     12.0 : 1.0
                      D
 = True                y : n      =     11.8 : 1.0
y precision: 0.849541284404
y recall: 0.648459383754
y F-measure: 0.735504368546
n precision: 0.692401960784
n recall: 0.873261205564
n F-measure: 0.772385509228
```
#### Using POS-tagging to find the JJ, JJS, VB. and only use these words
* when features are calculated, faster
* feature:

```
{'incorrect': True, 'graphic': True, 'atmospheric': True, 'cozy': True, 'hilarious': True, 'young': True, 'carefree': True, 'harmless': True, 'American': True, 'good': True, 'desperate': True, 'English': True, 'first': True}
``` 

```
train on 3368 instances, test on 1178 instances
accuracy: 0.395891341256
Most Informative Features
                   worst = True              one : four   =     17.9 : 1.0
                 average = True             thre : five   =     16.9 : 1.0
                   waste = True              one : four   =     16.7 : 1.0
                    Last = True             five : one    =     14.5 : 1.0
                     've = True              one : five   =     13.4 : 1.0
                    epic = True             five : one    =     13.1 : 1.0
                   awful = True              one : five   =     13.0 : 1.0
                terrible = True              one : four   =     12.6 : 1.0
               hilarious = True              two : five   =     11.4 : 1.0
                 classic = True             five : one    =     11.3 : 1.0


train on 4082 instances, test on 1361 instances
accuracy: 0.735488611315
Most Informative Features
                   worst = True                n : y      =     10.5 : 1.0
              delightful = True                y : n      =     10.0 : 1.0
             unwatchable = True                n : y      =      8.5 : 1.0
                 violent = True                y : n      =      8.2 : 1.0
                   waste = True                n : y      =      8.0 : 1.0
                     Bad = True                n : y      =      7.7 : 1.0
                  facial = True                y : n      =      6.3 : 1.0
                poignant = True                y : n      =      6.3 : 1.0
               skeptical = True                y : n      =      6.3 : 1.0
                  regret = True                y : n      =      6.3 : 1.0
y precision: 0.749295774648
y recall: 0.745098039216
y F-measure: 0.747191011236
n precision: 0.720430107527
n recall: 0.724884080371
n F-measure: 0.722650231125
```
**Look into the errors**

* "Not" cases: I know that it is cliche to say that the movie is not as good as the book. (1')
* Feeling changes: At first I was so excited to order this because I have heard so much about Tina Landon was eager to give this a try.  I found it so difficult to keep up with Tina you basically need to have some sort of training in choreography to understand how to do some of the moves. (1')
* Mismatch score:  I guess you get what you pay for.  Only $2 plus another $2-3 for shipping.  It's a DVD for the UK or Ireland.  It's printed in tiny letters on the DVD.  I obviously thought I was buying a DVD for the U.S. Bummer(1')
* Different Things: I had just finished reading the book and decided I'd like see how it was adapted to the big screen.  This version was the worst adaptation I've seen of a book made into a movie.  As I watched the film I wondered if the makers of the movie even bothered to read the book.  My girlfriend kept asking me during the film if "that happened in the book?"  At the end of the movie I told her that basically everything in the movie was not how it occurred in the book.  She enjoyed the movie until the end when it was like a "cheesy 80's montage".  The book is wonderful.  When I finished reading it, I felt like I had lost a good friend-I wished I could just keep reading it and reading it.  I've never read such an excellent novel.(1')
* No significant evidence: I recvd this video (DVD version) as a Christmas gift.  I put it on about 11 pm just to see what it was like, and finally got dragged to bed about 4 (5')

**Comparison**

* Make the dataset balanced will make a great contribution to the accuracy.
* Bi-gram improves the accuracy as it solves the 'No' case problem to some extent and involves many more valuable features.
* Uni-gram + Bi-gram might make the model overfit.
* Uni-gram without Stop Words can perform better than bi-gram only.
* Use part of the sentence after POS tagging is no worse than the Uni-gram or Bi-gram but faster when the text is pre-processed. 
* Use POS tagging helps a lot for ranking prediction.


### Aspect Extraction
* Tokenize
* POS tagging

```
[('If', 'IN'), ('you', 'PRP'), ('read', 'VBP'), ('and', 'CC'), ('loved', 'VBN'), ('the', 'DT'), ('book', 'NN'), (',', ','), ('then', 'RB'), ('most', 'RBS'), ('likely', 'JJ'), ('this', 'DT'), ('movie', 'NN'), ('is', 'VBZ'), ("n't", 'RB'), ('for', 'IN'), ('you', 'PRP'), ('The', 'DT'), ('only', 'JJ'), ('similarities', 'NNS'), ('between', 'IN'), ('the', 'DT'), ('two', 'CD'), ('being', 'VBG'), ('Dantes', 'NNS'), ('imprisonment', 'NN'), ('and', 'CC'), ('escape', 'NN'), ('I', 'PRP'), ('have', 'VBP'), ('yet', 'RB'), ('to', 'TO'), ('see', 'VB'), ('a', 'DT'), ('movie', 'NN'), ('version', 'NN'), ('of', 'IN'), ('the', 'DT'), ('Count', 'NNP'), ('of', 'IN'), ('Monte', 'NNP'), ('Cristo', 'NNP'), ('that', 'IN'), ('gets', 'NNS'), ('the', 'DT'), ('story', 'NN'), ('right', 'RB'), (',', ','), ('the', 'DT'), ('closest', 'JJS'), ('being', 'VBG'), ('the', 'DT'), ('1975', 'CD'), ('Richard', 'NNP'), ('Chamberlain', 'NNP'), ('version', 'NN'), (',', ','), ('but', 'CC'), ('even', 'RB'), ('that', 'IN'), ('one', 'CD'), ('had', 'VBD'), ('it', 'PRP'), ("'s", 'VBZ'), ('flaws', 'NNS'), ('A', 'DT'), ('summery', 'NN'), ('of', 'IN'), ('this', 'DT'), ('movie', 'NN'), ('would', 'MD'), ('be', 'VB'), ('Edmond', 'NNP'), ('Dantes', 'NNP'), ("'", 'POS'), ('life', 'NN'), ('is', 'VBZ'), ('ruined', 'VBN'), ('by', 'IN'), ('his', 'PRP$'), ('greedy', 'JJ'), ('friend', 'NN'), (',', ','), ('but', 'CC'), ('after', 'IN'), ('tweleve', 'JJ'), ('years', 'NNS'), ('in', 'IN'), ('prison', 'NN'), (',', ','), ('Dantes', 'NNP'), ('comes', 'VBZ'), ('back', 'RB'), (',', ','), ('gets', 'NNS'), ('his', 'PRP$'), ('vengence', 'NN'), (',', ','), ('and', 'CC'), ('Mercedes', 'NNP'), ('and', 'CC'), ('his', 'PRP$'), ('life', 'NN'), ('goes', 'VBZ'), ('back', 'RB'), ('to', 'TO'), ('how', 'WRB'), ('it', 'PRP'), ('was', 'VBD'), ('twelve', 'VB'), ('years', 'NNS'), ('ago', 'IN')]
```
* extract the NN and NNS which could be aspects
* seed for aspect

```
seed=["plot", "cast", "actor", "music", "story", "stereotype", "character", "acting", "director", "producer", "scene", "book", "adaptation"]
```
* wordnet propagation 
* define similarity using **Leacock-Chodorow Similarity**: Return a score denoting how similar two word senses are, based on the shortest path that connects the senses (as above) and the maximum depth of the taxonomy in which the senses occur. The relationship is given as -log(p/2d) where p is the shortest path length and d the taxonomy depth.

```
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
```
* Trial on a small set

```
['plot', 'cast', 'actor', 'music', 'story', 'stereotype', 'character', 'acting', 'director', 'producer', 'scene', 'book', 'adaptation', 'men', 'rapists', 'gangsters', 'bureaucrats', 'women', 'fools', 'types', 'liberal', 'female', 'reporter', 'characters', 'stereotypes', 'movie', 'parts', 'bit', 'home', 'owner', 'expression', 'watch', 'survival', 'person', 'wilderness', 'accident', 'exception', 'romance', 'part', 'girl', 'kisses', 'while', 'boy', 'affections', 'children', 'time', 'rabbit', 'fact', 'Classics', 'hundreds', 'years', 'universal', 'truths', 'audience', 'intelligence', 'works', 'line', 'man', 'prison', 'escapes', 'finds', 'seeks', 'homage', 'work', 'ends', 'changes', 'case', 'audacity', 'name', 'novel', 'adaptations', 'screenplay', 'beauty', 'power', 'burn', 'lot', 'atmosphere', 'web', 'revenge', 'wrongs', 'devices', 'entry', 'air', 'balloon', 'acrobats', 'ropes', 'plan', 'personages', 'sword', 'fights', 'scenes', 'device', 'son', 'screenwriters', 'sex', 'one', 'production', 'scenery', 'producers', 'ones', 'abomination', 'world', 'classics', 'getting', 'theater', 'version', 'better', 'film', 'similarities', 'Dantes', 'imprisonment', 'escape', 'gets', 'flaws', 'life', 'friend', 'fairy', 'tale', 'makes', 'feel', 'reading', 'screen', 'makers', 'girlfriend', 'end', 'montage', 'action', 'actors', 'job', 'roles', 'criticism', 'thing', 'source', 'generation', 'moviegoers', 'try', 'TV', 'main', 'ambition', 'night', 'engagement', 'treason', 'summation', 'chapter', 'relationship', 'prisoner', 'location', 'treasure', 'dozen', 'kings', 'details', 'intrigue', 'traps', 'enemies', 'sense', 'accomplishment', 'half', 'captivity', 'hour', 'imitation', 'master', 'books', 'movies', 'need', 'adventure', 'today', 'lifestyle', 'people', 'area', 'cellophane', 'con', 'trick', 'month', 'wrapping', 'kind', 'amazon', 'dvd', 'cover', 'popping', 'player', 'till', 'picture', 'friends', 'computers', 'error', 'place', 'copy', 'sellers', 'refund', 'elements', 'theme', 'names', 'set', 'century', 'mission', 'onset', 'finding', 'pirate', 'banker', 'months', 'loyalty', 'review', 'disc', 'problems', 'idea', 'success', 'hollywood', 'likes', 'art', 'screenwriter', 'brief', 'rundown', 'cow', 'letdown', 'pieces', 'transition', 'writer', 'dairy', 'rival', 'castle', 'satisfaction', 'illegitimate', 'child', 'duel', 'boyhood', 'pages', 'Man', 'chimp', 'sledgehammer', 'caricatures', 'fine', 'performance', 'young', 'entrance', 'sighs', 'party', 'eyes', 'coaster', 'nothing', 'annoyance', 'outrage', 'favor', 'script', 'way', 'cinematography', 'parameters', 'REGION', 'http', 'pleasure', 'region', 'cause', 'Guess', 'sailor', 'someone', 'times', 'criminals', 'aristocrats', 'secrets', 'turns', 'weaknesses', 'fiction', 'disservice', 'role', 'showing', 'deep', 'undercurrent', 'anger', 'drove', 'actions', 'bringing', 'depth', 'seconds', 'seller', 'favorites', 'things', 'point', 'one-liners', 'read', 'cliff', 'notes', 'themes', 'heart', 'similarity', 'share', 'travesty', 'somebody', 'series', 'depiction', 'bravo', 'flick', 'piece', 'garbage', 'feature', 'creations', 'crime', 'year', 'firmware', 'copies', 'perfect', 'condition', 'disk', 'events', 'formula', 'purchase', 'discs', 'filmmakers', 'novels', 'conceit', 'results', 'credit', 'eye', 'candy', 'seeing', 'means', 'substitute', 'recognition', 'worst', 'look', 'mystery', 'grand', 'hours', 'dialogue', 'slang', 'costs', 'theatre', 'pan', 'scan', 'release', 'star', 'rating', 'reason', 'films', 'red', 'coat', 'return', 'process', 'card', 'debt', 'mins', 'starts', 'economics', 'issues', 'consumers', 'symptom', 'households', 'incomes', 'policy', 'address', 'solutions', 'nation', 'level', 'issue', 'community', 'tangents', 'mention', 'documentary', 'career', 'student', 'proof', 'claims', 'opinions', 'waste', 'money', 'chance', 'cost', 'interest', 'mind', 'quality', 'image', 'videos', 'attributes', 'content', 'playing', 'artist', 'wall', 'rooms', 'viewer', 'asylum', 'viewers', 'imaginations', 'views', 'countryside', 'closeups', 'stage', 'mood', 'skills', 'minutes', 'lines', 'emotion', 'tone', 'amount', 'words', 'conflicts', 'budget', 'lacks', 'mannerisms', 'speech', 'patterns', 'conversations', 'monologues', 'stream', 'stopping', 'smooth', 'show', 'business', 'retrospect', 'Keyholes', 'features', 'woman', 'fighter', 'town', 'husband', 'culture', 'leader', 'fight', 'countrymen', 'family', 'battle', 'dead', 'uniform', 'love', 'sounds', 'race', 'outsiders', 'foreigners', 'subtlety', 'fan', 'trade', 'officers', 'army', 'soldiers', 'ways', 'force', 'reasons', 'rebel', 'divisions', 'Rifles', 'Government', 'clans', 'war', 'symbol', 'peasants', 'class', 'warriors', 'whims', 'modernization', 'rule', 'hands', 'wealth', 'fun', 'basis', 'history', 'spirit', 'dishonors', 'values']
```


### Make it aspect based by 
* POS tagging [done]
* Aspect extraction [done]
* Sentiment on each aspect 

### Possible problem
* There is no ground truth for each aspect: try to manually label into 'Good' and 'Not Good'
* nltk stemming

