#!/usr/bin/python
#!coding:utf-8
from urllib2 import *
from BeautifulSoup import BeautifulSoup
import os
import sys

def getlist(url,keywords):
    urllist=[]
    fid=urlopen(url)
    html=fid.read()
    soup=BeautifulSoup(html)
    for i in  soup.findAll("a"):
          if keywords in str(i):
            aurl=str(i["href"]).strip()
            #print mp4url
            urllist.append(aurl)   
    return urllist
            

def gettitle(url,keywords):
    titlelist=[]
    html=urlopen(url).read()
    soup=BeautifulSoup(html,fromEncoding="gb18030")
    for i in  soup.findAll("a"):
     if keywords in str(i):
        titleurl=str(i.string).strip()
        titleurl=titleurl.replace(" ","")
        titlelist.append(titleurl.replace(" - ","").strip())	
    return titlelist
        

def getstart(alist):
    i=0
    first=alist[i]
    while first=="None":
        #print "haha"
        i+=1
        first=alist[i]
    newlist=[]
    b=i
    for i in range(b+1,len(alist)):
        if first==alist[i]:
            break
    #print i
    for a in range(i,len(alist)):
        #print "*inside getstart*",alist[a]
        newlist.append(alist[a])

    return newlist
url="http://v.163.com/special/opencourse/lectureroncomputerscience.html"
if __name__=="__main__":
    url=str(sys.argv[1])
    keywords="http://v.163.com/movie/"
    urllist=getlist(url,keywords)
    urllist=getstart(urllist)
    cmd="you-get %s"
    for  aurl in urllist:
        #print cmd %aurl
        os.system(cmd %aurl)
