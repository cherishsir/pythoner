#!/usr/bin/python
#!coding:utf-8
import  os
from  urllib2  import *
from BeautifulSoup import BeautifulSoup
import sys
REDSTART="\033[91m"
REDEND="\033[0m"
def printall(end,titlelist):
	print "你将下载的视频如下:"
	for i in range(0,end):
		print str(i+1),titlelist[i]
	raw_input("按下任意键,开始下载")
	

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
            mp4url=str(i["href"]).strip()
            #print mp4url
            varlist.append(mp4url)
        
        
        	


def download(start,urllist,titlelist):
	number=1
	for i in range(start,len(urllist)):
		where="第"+str(number)+"课"
		filename=where+str(titlelist[i])+".mp4"
		if not os.path.isfile(filename): # do not have this file in local
			all="wget "+str(urllist[i])+" -O "+filename
			#print all
			os.system(all)
			number+=1
		
		else:
			print filename,"已经存在,skipping"
			number+=1

def dlone(url,filename):
    if  os.path.isfile(filename):
        print filename+" existed,skipping"
        return
    else:
        CHUNK=1000*1000
        try:
            req=urlopen(url,None,10)
            size=int(req.info()["Content-Length"])
            typefile=req.info()["Content-Type"]
            all=size/1000#kB
            now=0
            print filename+REDSTART+" 下载中"+REDEND,"\t",
            with open(filename,"wb") as fp:
                while True:
                    condition=float(now)*100*CHUNK/size
                    condition=float('%4.1f'% condition)
                    if(condition>=100):
                        condition=100
                        now=all/1000.0
		    tag="\033[91m[%"+str(condition)+"]"+str(now)+"MB\033[0m/"+"["+str(all/1000.0)+"MB]"
                    print tag,
                    sys.stdout.flush()
                    chunk=req.read(CHUNK)
                    if not chunk: break
                    fp.write(chunk)
		    print "\b"*(len(tag)-len(REDSTART+REDEND)+2),
                    now+=1
                #print "\n"  #download next
		print " "
        except  Exception,e:
            print e
            os.system("rm -rf  "+filename)
            return -1

           
                    
                    
                
            
def downloadopen(start,urllist,titlelist):
    number=1
    i=start
    while i<len(urllist):
        where="第"+str(number)+"课"
        filename=where+str(titlelist[i])+".mp4"
        url=urllist[i]
        if dlone(url,filename)==-1:
            print filename+" 下载失败"
        else:
            i+=1
            number+=1
        


##main function###########################################################
if __name__=="__main__":
    #url=raw_input("请输入你要下载的网页>:")
    url=str(sys.argv[1])
    #url="http://v.163.com/special/opencourse/classicalmechanics.html"
    mp4list=[] 				#save http://xx.mp4
    titlelist=[]				#save title
    geturl(url,mp4list,".mp4")
    gettitle(url,titlelist, "http://v.163.com/movie")
    #去掉重复的url and title,返回值为没有重复的url and title
    mp4list=getstart(mp4list)
    titlelist=getstart(titlelist)
    #下载对应的内容,通过mp4list找下载对应的视频，mp4list的len决定了视频的数量
    printall(len(mp4list),titlelist)
    downloadopen(0,mp4list,titlelist)

