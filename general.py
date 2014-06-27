#!/usr/bin/python
#!coding:utf-8
import  os
from  urllib2  import *
from BeautifulSoup import BeautifulSoup
import sys
def printall(end,titlelist):
	print "你将下载的视频如下:"
	for i in range(0,end):
		print str(i+1),titlelist[i]
	raw_input("按下任意键,开始下载")
	

def getstart(alist):
	i=0
	first=alist[i]
	while first=="None":
		print "haha"
		i+=1
		first=alist[i]
	newlist=[]
	b=i
	for i in range(b+1,len(alist)):
		if first==alist[i]:
			break
	print i
	for a in range(i,len(alist)):
		#print "*inside getstart*",alist[a]
		newlist.append(alist[a])

	return newlist
def gettitle(url,varlist,keywords):
	html=urlopen(url).read()
	soup=BeautifulSoup(html,fromEncoding="gb18030")
	for i in  soup.findAll("a"):
	 if keywords in str(i):
		#print i
		titleurl=str(i.string).strip()
		titleurl=titleurl.replace(" ","")
		varlist.append(titleurl.replace(" - ","").strip())	

def geturl(url,varlist,keywords):
	html=urlopen(url).read()
	soup=BeautifulSoup(html)
	for i in  soup.findAll("a"):
	 if keywords in str(i):
		#print str(i);
		mp4url=str(i["href"]).strip()
		varlist.append(mp4url)	


def download(start,urllist,titlelist):
	number=1
	for i in range(start,len(urllist)):
		where="第"+str(number)+"课"
		filename=where+str(titlelist[i])
		if not os.path.isfile(filename): # do not have this file in local
			all="wget "+str(urllist[i])+" -O "+filename
			#print all
			os.system(all)
			number+=1
		
		else:
			print filename,"已经存在,skipping"
			number+=1

def downloadopen(start,urllist,titlelist):
	number=1
	for i in range(start,len(urllist)):
		where="第"+str(number)+"课"
		filename=where+str(titlelist[i])
		if not os.path.isfile(filename): # do not have this file in local    
		        CHUNK=1024*1024
			req=urlopen(urllist[i])
			size=int(req.info()["Content-Length"])
			ALL=size/CHUNK+1
			now=0
			print "下载中 "+filename+"["+str(size/1000)+"KiB]"
			with open(filename,"wb") as fp:
			   while True:
				condition=int(float(now)*100/ALL)
				if condition >100:
					condition=100
				print "\033[91m\r[%"+str(condition)+"]\033[0m",
				sys.stdout.flush()
				chunk=req.read(CHUNK)
				if not chunk: break
				fp.write(chunk)
				now+=1
				
			   print "\n"
			number+=1
		
		else:
			print filename,"已经存在,skipping"
			number+=1


##main function###########################################################
if __name__=="__main__":
	url=raw_input("请输入你要下载的网页>:")
	#url="http://v.163.com/special/opencourse/classicalmechanics.html"
	pdflist=[] 				#save http://xx.mp4
	titlelist=[]				#save title
	geturl(url,pdflist,".pdf")
	pdflist=[url+i for i in pdflist]
	gettitle(url,titlelist,".pdf")
	printall(len(pdflist),titlelist)
	downloadopen(0,pdflist,titlelist)

