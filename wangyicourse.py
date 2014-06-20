#!/usr/bin/python
#!coding:utf-8
import  os
from  urllib2  import *
from BeautifulSoup import BeautifulSoup
import sys



url=raw_input("请输入你要下载的网页>:")
#url="http://v.163.com/special/opencourse/learningfromdata.html"

mp4list=[ ] 		#save http://xx.mp4
titlelist=[]		#save title


def gettitle(url,varlist):
	html=urlopen(url).read()
	soup=BeautifulSoup(html,fromEncoding="gb18030")
	for i in  soup.findAll("a"):
	 if "http://v.163.com/movie" in str(i):
		titleurl=str(i.string)
		varlist.append(titleurl)	

def getmp4(url,varlist):
	html=urlopen(url).read()
	soup=BeautifulSoup(html)
	for i in  soup.findAll("a"):
	 if "mp4" in str(i):
		mp4url=str(i["href"]).strip()
		mp4list.append(mp4url)	
if  len(sys.argv)==2:
	os.makedirs(sys.argv[1]) #mdir a dir
	savedir=sys.argv[1]
getmp4(url,mp4list)
gettitle(url,titlelist)

number=0

for i in range(0,len(mp4list)):
	where="第"+str(number)+"课"
	filename=where+str(titlelist[i])+".mp4"
	if not os.path.isfile(filename): # do not have this file in local
		all="wget "+str(mp4list[i])+" -O "+filename
		#print all
		os.system(all)
		
	else:
		print filename,"已经存在,skipping"

	if  len(sys.argv)==2:
		os.system("mv "+filename+" "+sys.argv[1])
	number+=1
	






