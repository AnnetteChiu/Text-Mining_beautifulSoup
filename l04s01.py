import sys
import urllib2
import nltk

from bs4 import BeautifulSoup
import re


fp=open("obama_list.txt","rt")
fout=open("obama_corpus.txt","wt")
for line in fp.read().split("\n"):
    if len(line)>10:
        html_link="http://americanrhetoric.com/"+line.rstrip()
        print html_link
        html_doc=urllib2.urlopen(html_link).read()
        od = BeautifulSoup(html_doc,'html.parser')
        all_corpus=""
        for x in  od.find_all('font',attrs={'face':'Verdana'}):
            all_corpus += x.get_text().encode('ascii','ignore')
        all_corpus=all_corpus.replace("\n"," ").replace("\r"," ")
        all_corpus=re.sub(r'\s+',' ',all_corpus)
        if len(all_corpus)>100:
            fout.write(all_corpus+"\n")
fout.close()

