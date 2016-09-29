
# coding: utf-8

# In[1]:

import sys
from bs4 import BeautifulSoup
import re
import nltk
from nltk.tree import Tree


# In[2]:

import os


# In[10]:

fp=open("/Users/annettechiu/Desktop/Transcript_PresidentialDebate.htm","rt")
html_doc=fp.read()
od = BeautifulSoup(html_doc, 'html.parser')

inline_content =od.find('article', attrs={'itemprop':'articleBody'})  


# In[13]:

sents=open("/Users/annettechiu/Desktop/obama_debate.html","rt")
html_doc=fp.read()
od = BeautifulSoup(html_doc, 'html.parser')


# In[14]:

for x in sents:
    print x
    #y=[z[1] for z in nltk.pos_tag(nltk.word_tokenize(x))]
    #print y
    y=nltk.pos_tag(nltk.word_tokenize(x))
    for i in range(len(y)-1):
        if y[i][1]=='JJ' and y[i+1][1]=='NN':
            print y[i], y[i+1]

