#!/usr/bin/python
#!coding:utf-8
import  os
from  urllib2  import *
from BeautifulSoup import BeautifulSoup
import sys
<<<<<<< HEAD
def printall(start,titlelist):
	print "你将下载的视频如下:"
	for i in range(start,len(titlelist)):
		print titlelist[i]
	raw_input("按下任意键,开始下载")
	

def getstart(titlelist):
	first=titlelist[1]
	for i in range(2,len(titlelist)):
		if first==titlelist[i]:
			return i
	return 0
=======


>>>>>>> 864a8bd1632c40b3ed36c586abd03e10826e3057
def gettitle(url,varlist):
	html=urlopen(url).read()
	soup=BeautifulSoup(html,fromEncoding="gb18030")
	for i in  soup.findAll("a"):
	 if "http://v.163.com/movie" in str(i):
<<<<<<< HEAD
		titleurl=str(i.string).strip()
		titleurl=titleurl.replace(" ","")
		varlist.append(titleurl.replace(" - ","").strip())	
=======
		titleurl=str(i.string)
		varlist.append(titleurl)	
>>>>>>> 864a8bd1632c40b3ed36c586abd03e10826e3057

def getmp4(url,varlist):
	html=urlopen(url).read()
	soup=BeautifulSoup(html)
	for i in  soup.findAll("a"):
<<<<<<< HEAD
	 if ".mp4" in str(i):
		mp4url=str(i["href"]).strip()
		varlist.append(mp4url)	


def download(start,varlist,titlelist):
	number=1
	for i in range(start,len(varlist)):
		where="第"+str(number)+"课"
		filename=where+str(titlelist[i])+".mp4"
		if not os.path.isfile(filename): # do not have this file in local
			all="wget "+str(varlist[i])+" -O "+filename
			#print all
			os.system(all)
			number+=1
		
		else:
			print filename,"已经存在,skipping"
			number+=1

##main function###########################################################
if __name__=="__main__":
	url=raw_input("请输入你要下载的网页>:")
	#url="http://v.163.com/special/opencourse/classicalmechanics.html"
	mp4list=[" ",] 				#save http://xx.mp4
=======
	 if "mp4" in str(i):
		mp4url=str(i["href"]).strip()
		mp4list.append(mp4url)	



if __name__=="__main__":
	url=raw_input("请输入你要下载的网页>:")
	#url="http://v.163.com/special/opencourse/learningfromdata.html"
	mp4list=[ ] 				#save http://xx.mp4
>>>>>>> 864a8bd1632c40b3ed36c586abd03e10826e3057
	titlelist=[]				#save title
	if  len(sys.argv)==2:
		os.makedirs(sys.argv[1]) 	#mdir a dir
		savedir=sys.argv[1]
<<<<<<< HEAD
	getmp4(url,mp4list)	
	gettitle(url,titlelist)
	start=getstart(titlelist)
	printall(start,titlelist)

	number=1
	for i in range(start,len(mp4list)):
=======
	getmp4(url,mp4list)
	gettitle(url,titlelist)
	number=0
	for i in range(0,len(mp4list)):
>>>>>>> 864a8bd1632c40b3ed36c586abd03e10826e3057
		where="第"+str(number)+"课"
		filename=where+str(titlelist[i])+".mp4"
		if not os.path.isfile(filename): # do not have this file in local
			all="wget "+str(mp4list[i])+" -O "+filename
			#print all
			os.system(all)
<<<<<<< HEAD
			number+=1
		
		else:
			print filename,"已经存在,skipping"
			number+=1

		if  len(sys.argv)==2:
			os.system("mv "+filename+" "+sys.argv[1])
		

=======
		
		else:
			print filename,"已经存在,skipping"

		if  len(sys.argv)==2:
			os.system("mv "+filename+" "+sys.argv[1])
		number+=1
	
>>>>>>> 864a8bd1632c40b3ed36c586abd03e10826e3057






