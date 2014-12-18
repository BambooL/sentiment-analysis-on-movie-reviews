#!/usr/bin/env python

import csv
from collections import defaultdict
from iqap import IqapReader

######################################################################

def get_all_imdb_scores(src_filename):
    """
    Turns the imdb-assess.csv data into a dictionary mapping 
    (word, tag) pairs to dictionaries of values.
 
    Argument: the file imdb-lemmas-assess.csv as the R function VocabAssess
 
    Value: vals -- a mapping from (word, tag) pairs to dictionaries 
    {'Word':word, 'Tag':tag, 'ER':float, 'Coef':float: 'P':float}
    """
    vals = {}
    csvreader = csv.reader(file(src_filename))
    header = csvreader.next()
    for row in csvreader:
       d = dict(zip(header, row))
       for label in ('ER', 'Coef', 'P'):
          d[label] = float(d[label])
       vals[(d['Word'], d['Tag'])] = d
    return vals

