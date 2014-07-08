#!/usr/bin/env python2
# vim: set fileencoding=utf8

import base64
import requests
import time
import os
import sys
import argparse
import random
from HTMLParser import HTMLParser
import select
from  urllib2  import *

s = '\x1b[%d;%dm%s\x1b[0m'       # terminual color template
parser = HTMLParser()

############################################################
# wget exit status
wget_es = {
    0: "No problems occurred.",
    2: "User interference.",
    1<<8: "Generic error code.",
    2<<8: "Parse error - for instance, when parsing command-line optio.wgetrc or .netrc...",
    3<<8: "File I/O error.",
    4<<8: "Network failure.",
    5<<8: "SSL verification failure.",
    6<<8: "Username/password authentication failure.",
    7<<8: "Protocol errors.",
    8<<8: "Server issued an error response."
}
############################################################

headers = {
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Encoding":"text/html",
    "Accept-Language":"en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4,zh-TW;q=0.2",
    "Content-Type":"application/x-www-form-urlencoded",
    "User-Agent":"Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1700.77 Safari/537.36"
}

wget_template = 'wget -q -c -nv -O "%s" "%s"'
api = 'http://api.flvxz.com/jsonp/purejson/url/%s'

def download(infos):
    #if not os.path.exists(infos['dir_']):
    #   os.mkdir(infos['dir_'])

    #else:
        #if os.path.exists(infos['filename']):
            #return 0

    num = random.randint(0, 7) % 7
    col = s % (2, num + 90, os.path.basename(infos['filename']))
    print '\n  ++ 正在下载:', '#', s % (1, 97, infos['n']), '/', s % (1, 97, infos['amount']), '#', col

    cmd = wget_template % (infos['filename'], parser.unescape(infos['durl']))
    status = os.system(cmd)

    if status != 0:     # other http-errors, such as 302.
        wget_exit_status_info = wget_es[status]
        print('\n\n ----###   \x1b[1;91mERROR\x1b[0m ==> \x1b[1;91m%d (%s)\x1b[0m   ###--- \n\n' % (status, wget_exit_status_info))
        print s % (1, 91, '  ===> '), cmd
        sys.exit(1)

def downloads(infos):
	#if not os.path.exists(infos['dir_']):
	#   os.mkdir(infos['dir_'])

	#else:
	#if os.path.exists(infos['filename']):
	    #return 0

	num = random.randint(0, 7) % 7
	col = s % (2, num + 90, os.path.basename(infos['filename']))
	#print '\n  ++ 正在下载:', '#', s % (1, 97, infos['n']), '/', s % (1, 97, infos['amount']), '#', col
	flvurl=str(parser.unescape(infos['durl']))
	flvname=str(infos['filename'])
	req=urlopen(flvurl,None,10)
	size=int(req.info()["Content-Length"])
        CHUNK=1024*1024*2
	ALL=size/CHUNK
	now=0
	print "下载中 "+flvname+"["+str(size/1000/1000)+"MB]"
	with open(flvname,"wb") as fp:
		while True:
			condition=float(now)*100/ALL
			condition=float('%4.1f'% condition)
			if condition >100:
				condition=100
				now=size/1000/1000
			print "\r"+" "*20,
			print "\033[91m\r[%"+str(condition)+"]"+str(now)+"MB\033[0m/"+"["+str(size/1000/1000)+"MB]",
			sys.stdout.flush()
			chunk=req.read(CHUNK)
			if not chunk: break
			fp.write(chunk)
			now+=1
	print "\n"
	    



def play(infos):
    num = random.randint(0, 7) % 7
    col = s % (2, num + 90, os.path.basename(infos['filename']))
    print '\n  ++ play:', '#', s % (1, 97, infos['n']), '/', s % (1, 97, infos['amount']), '#', col

    cmd = 'mpv --really-quiet --cache 8140 --cache-default 8140 ' \
        '"%s"' % parser.unescape(infos['durl'])
        #'--http-header-fields "User-Agent:%s" ' \
        #'"%s"' % (headers['User-Agent'], infos['durl'])

    status = os.system(cmd)
    timeout = 1
    ii, _, _ = select.select([sys.stdin], [], [], timeout)
    if ii:
        sys.exit(0)
    else:
        pass

def pickup(j):
    print s % (1, 97, '  ++ pick a quality:')
    for i in xrange(len(j)):
        print s % (1, 91, '  %s' % (i+1)), j[i]['quality']

    #p = raw_input(s % (1, 92, '  Enter: '))
    p="3"
    if p.isdigit():
        p = int(p)
        if p <= len(j):
            return j[p-1]
        else:
            print s % (1, 91, '  !! enter error')
            sys.exit()
    else:
        print s % (1, 91, '  !! enter error')
        sys.exit()

def main(url):
    encode_url = base64.b64encode(url.replace('://', ':##'))
    url = api % encode_url

    r = requests.get(url)
    j = r.json()
    if j:
        j = pickup(j)
    else:
        print s % (1, 91, '  !! Can\'t get videos')
        sys.exit()
    print s % (2, 92, '  -- %s' % j['quality'].encode('utf8'))

    yes = True if len(j['files']) > 1 else False
    dir_ = os.path.join(os.getcwd(), j['title'].encode('utf8')) if yes else os.getcwd()

    n = 1
    amount = len(j['files'])
    j['title']=j['title'].replace(" ","")
    for i in j['files']:
        infos = {
            'filename': os.path.join("", '%s_%s.%s' % (j['title'].encode('utf8'), n, i['ftype'].encode('utf8'))),
            'durl': i['furl'].encode('utf8'),
            'dir_': dir_,
            'amount': amount,
            'n': n
        }
        if args.play:
            play(infos)
        else:
            downloads(infos)
        n += 1

if __name__ == '__main__':
    p = argparse.ArgumentParser(description='flvxz')
    p.add_argument('url', help='site url')
    p.add_argument('-p', '--play', action='store_true', \
                help='play with mpv')
    args = p.parse_args()
    main(args.url)
