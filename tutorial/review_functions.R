#!/usr/bin/env R

## Functions for working with the review data described at
## http://compprag.christopherpotts.net/reviews.html
##
## author: Christopher Potts
## copyright: Copyright 2011, Christopher Potts
## credits: []
## license: Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License: http://creativecommons.org/licenses/by-nc-sa/3.0/
## version: 1.0
## maintainer: Christopher Potts
## email: See the author's website

######################################################################
## This function does a basic plot of the sort that we will
## want to do a lot, with Tufte-inspired axis labels.
## Arguments:
## x: the x-axis data vector
## y: the y-axis data vector
## digits: rounding for the y-axis (default: 2)
## ylim: limits for the y-axis, as a vector (default: c(min(y), max(y)))
## log: log-scale axis (default: '' means no log-scale; options are y, x, xy)
## main: a string to use as the main (plot title) argument (default: '')
## xlab: a string to label the x-axis (default: 'Category')
## ylab: a string to label the y-axis (default: '')
WordPlot = function(x, y, digits=2, ylim=c(min(y), max(y)), log='', 
                    main='', xlab='Category', ylab=''){
  plot(x, y,
       ylim=ylim,
       log=log,
       main=main, xlab=xlab, ylab=ylab,
       pch=19, type='b', axes=FALSE)
  axis(1, at=x)
  axis(2, at=y, labels=round(y, digits), las=1)
}

######################################################################
## Get the subframe for a word and add RelFreq and Pr values.
## Arguments:
## df: a data-frame in the format of imdb-words.csv
## word: any string
## tag: any string (but should be a, n, r, or v)
## Value: the word frame with new distribution values.
WordFrame = function(df, word, tag){
  pf = subset(df, Word==word & Tag==tag)
  ## Exit if the word isn't in df:
  if(nrow(pf)==0){
    print(paste('Ack: (', word, ',', tag, ') not in database', sep=''))
    return()
  }
  ## Add the values:
  pf$RelFreq = pf$Count / pf$Total
  pf$Pr = pf$RelFreq / sum(pf$RelFreq)
  ## Return the augmented frame:
  return(pf)
}

BigramFrame = function(df, word1, tag1, word2, tag2){
  pf = subset(df, Word1==word1 & Tag1==tag1 & Word2==word2 & Tag2==tag2)
  ## Exit if the word isn't in df:
  if(nrow(pf)==0){
    print(paste('Ack: (', word1, ',', tag1, ') not in database', sep=''))
    return()
  }
  ## Add the values:
  pf$RelFreq = pf$Count / pf$Total
  pf$Pr = pf$RelFreq / sum(pf$RelFreq)
  ## Return the augmented frame:
  return(pf)
}

######################################################################
## Expected ratings for words.
## Argument:
## pf: a phrase frame produced by WordFrame
## Value: The expected rating for pf
ExpectedRating = function(pf){
  sum(pf$Category * pf$Pr)
}

######################################################################
## Prevent R from printing '0' for a p value, which is impossible.
## Input: a model fit produced by WordLogit.
## Output: a string representing the p value as an equality or inequality (if it is tiny).
ExtractPrintableP = function(fit){
  p = summary(fit)$coef[2,4]
  pp = ''
  if (p < 0.001){ pp = 'p < 0.001' }
  else { pp = paste('p =', round(p, 3)) }
  return(pp)
}

######################################################################
## Fit a model for a word's frame.
## Argument: a phrase frame of the sort produced by WordFrame
## Output: the fitted model
WordLogit = function(pf){
  fit = glm(cbind(pf$Count, pf$Total-pf$Count) ~ Category, family=quasibinomial, data=pf)
  return(fit)
}

######################################################################
## Arguments:
## df: a dataframe like imdb
## word: any string
## tag: any string, but should be one of a, n, v, r
## ylim: allows the user to specify the y-axis limits (default: c(0, 0.3))
WordDisplay = function(df, word, tag, ylim=c(0,0.3)){
  pf = WordFrame(df, word, tag)
  ## Basic plotting:
  title = paste('(', word, ',', tag, ') -- ', sum(pf$Count), ' tokens', sep= '')
  WordPlot(pf$Category, pf$Pr, main=title, ylim=ylim)
  ## Get the expected rating:
  er = ExpectedRating(pf)
  abline(v=er, col='red')
  ## Try to avoid having the text we add overlap the data:
  textx = 10
  textpos = 2
  if(max(er > 6)){ textx = 1; textpos=4 }
  text(textx, max(ylim), paste('ER = ', round(er,2), sep=''), col='red', pos=textpos)
  ## Fit the model:
  fit = WordLogit(pf)
  ## Add the fitted values:
  points(fit$fitted/sum(pf$RelFreq), col='blue', pch=18)
  ## Interpolate a curve through the fitted values.
  curve(plogis(fit$coef[1] + fit$coef[2]*x)/sum(pf$RelFreq), col='blue', add=TRUE)
  ## The text annotation.
  pp = ExtractPrintableP(fit)
  text(textx, max(ylim)*0.9,
       paste('Category coef. = ', round(fit$coef[2], 2), ' (', pp, ')', sep=''),
       col='blue', pos=textpos)
}

######################################################################
## This subfunction calculates assesment values for a word based on a subframe.
## Argument: A Word's subframe directly from the main CSV source file.
## (Pr and RelFreq are added as part of this function.)
## Value: a vector (er, coef, coef.p).
WordAssess = function(pf){
  ## Build up the subframe as usual:
  pf$RelFreq = pf$Count/pf$Total
  pf$Pr = pf$RelFreq / sum(pf$RelFreq)
  ## ER value.
  er = ExpectedRating(pf)
  ## Logit and the coefficient values. (We don't need the intercept values.)
  fit = WordLogit(pf)
  coef = fit$coef[2]
  coef.p = summary(fit)$coef[2,4]
  ## Return a vector of assessment values, which ddply will add to its columns:
  return(cbind(er, coef, coef.p))
}

######################################################################
## Load the library for the ddply function.
library(plyr)
VocabAssess = function(df){
  ## ddply takes care of grouping into words and
  ## then applying WordAssess to those subframes.
  ## It will also display a textual progress bar.
  vals = ddply(df, c('Word', 'Tag'), WordAssess, .progress='text')
  ## Add intuitive column names.
  colnames(vals) = c('Word', 'Tag', 'ER', 'Coef', 'P')
  return(vals)
}
