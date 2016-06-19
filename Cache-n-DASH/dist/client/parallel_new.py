#!/usr/bin/env python

from multiprocessing import Process, Pool
import requests
import time
import urllib2
import sys
from collections import defaultdict

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
      max+=rem+1
    lst.append([min,max])
  print lst
  return lst

#print byte_range_divide(27945615,5)

def http_get(url):
  start_time = millis() 
  temp_url=url.split('|')
  req = urllib2.Request(temp_url[0])
  req.headers['Range'] = 'bytes=%s-%s' % (temp_url[1],temp_url[2])	
  result = {"url": url, "data": urllib2.urlopen(req).read()}
  #print url + " took " + str(millis() - start_time) + "ms"
  return result


def create_urls(url):
  r=requests.head(url)
  length=int(r.headers['content-length'])
  print length
  y=byte_range_divide(length,10)  
  lst=[];
  for i in range(0,len(y)):	
     	t=[url,y[i][0],y[i][1]-1]
        l='|'.join(str(e) for e in t)
        lst.append(l)
  print lst 	
  return lst

def main(arg1,arg2):
    # print command line arguments
    

    #url="http://www-itec.uni-klu.ac.at/ftp/datasets/DASHDataset2014/BigBuckBunny/4sec/bunny_45226bps/BigBuckBunny_4snonSeg.mp4"
    url=arg1 
	#r=request.head(url);
	#size=r.headers['content-length']
    file_name=arg2 
    urls =create_urls(url)
    #print urls

    pool = Pool(processes=5)
     
    start_time = millis()
    results = pool.map(http_get, urls)
    tib=millis() - start_time
    print "\ntotal time to pull all the segments " + str(tib) + " ms\n"
    #print results
    result=defaultdict(list)
    #file_name=url.split('/')[-1]
    #print(file_name)
    segment_file= open(file_name, 'wb')
    for d in results:
       for key, value in d.iteritems():
            result[key].append(value)
    #print("".join(result['data']))
    file_size=len("".join(result['data']))
    segment_file.write("".join(result['data'])) 
    segment_file.close() 	
    st=millis()
    req=urllib2.Request(url)
    temp=urllib2.urlopen(req, timeout=5).read()
    tis=millis()-st
    print "time to download  complete chunck"+str(tis)+"ms\n"
    print "\n time saved="+str(tis-tib)+"ms\n"
    return file_size
if __name__ == "__main__":
    sys.exit(main(sys.argv[1],sys.argv[2]))

