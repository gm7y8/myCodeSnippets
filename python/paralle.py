#!/usr/bin/env python

from multiprocessing import Process, Pool
import requests
import time
import urllib2

def millis():
  return int(round(time.time() * 1000))

def byte_range_divide(l,n):
  len_seg=l/n
  #print len_seg
  rem=l%n
  #print rem
  lst=[]
  for i in range(0,n):
    min=len_seg*i
    max=len_seg*(i+1)
    if i==n-1:
      max+=rem
    lst.append([min,max])
  #print lst
  return lst

#print byte_range_divide(27945615,5)

def http_get(url):
  start_time = millis() 
  temp_url=url.split('|')
  req = urllib2.Request(temp_url[0])
  req.headers['Range'] = 'bytes=%s-%s' % (temp_url[1],temp_url[2])	
  result = {"url": url, "data": urllib2.urlopen(req, timeout=5).read()}
  print url + " took " + str(millis() - start_time) + " ms"
  return result


def create_urls(url):
  r=requests.head(url)
  length=int(r.headers['content-length'])
  #print length
  y=byte_range_divide(length,10)  
  lst=[];
  for i in range(0,len(y)-1):	
     	t=[url,y[i][0],y[i][1]]
        l='|'.join(str(e) for e in t)
        lst.append(l)
  print lst 	
  return lst

url="http://www-itec.uni-klu.ac.at/ftp/datasets/DASHDataset2014/BigBuckBunny/15sec/bunny_3748236bps/BigBuckBunny_15snonSeg.mp4"

#r=request.head(url);
#size=r.headers['content-length']

urls =create_urls(url)
print urls

pool = Pool(processes=5)

start_time = millis()
results = pool.map(http_get, urls)

print "\ntotal time to pull all the segments " + str(millis() - start_time) + " ms\n"

#for result in results:
#  print result

st=millis()
req=urllib2.Request(url)
temp=urllib2.urlopen(req, timeout=5).read()
print str(millis()-st)


