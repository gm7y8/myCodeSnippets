#!/usr/bin/env python
import requests
import time
import urllib2
import sys
import urlparse
import csv
def get_size(url):
  r=requests.head(url)
  length=int(r.headers['content-length'])
  return length


base_url="http://www-itec.uni-klu.ac.at/ftp/datasets/DASHDataset2014/BigBuckBunny/10sec/"
"""
bit_rate=['bunny_982168bps','bunny_88563bps','bunny_769540bps','bunny_565835bps','bunny_500530bps','bunny_45351bps','bunny_3748236bps',
		'bunny_365887bps','bunny_3464259bps','bunny_3222578bps','bunny_315047bps','bunny_2863389bps','bunny_252582bps','bunny_2372196bps'
		,'bunny_215976bps','bunny_2061491bps','bunny_176031bps','bunny_1419205bps','bunny_127052bps','bunny_1165885bps']
"""

bit_rate=['bunny_987061bps','bunny_88482bps','bunny_771359bps',
'bunny_568500bps',
'bunny_503270bps',
'bunny_45373bps',
'bunny_3792491bps',
'bunny_368912bps',
'bunny_3493765bps',
'bunny_3245900bps',
'bunny_317328bps',
'bunny_2884382bps',
'bunny_252988bps',
'bunny_2384387bps',
'bunny_216536bps',
'bunny_2070985bps',
'bunny_176780bps',
'bunny_1431232bps',
'bunny_127412bps',
'bunny_1174238bps']



nof=60
with open('10sec.csv', 'w') as csvfile:
    fieldnames = ['url', 'file_name','segment_number','bit_rate','file_size']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for i in bit_rate:
	for j in range(n):
                file_name="BigBuckBunny_10s"+str(j)+".m4s"
		temp=str(i)+"/"+file_name
		url_temp=urlparse.urljoin(base_url,temp)
                fsize=get_size(url_temp) 
 		writer.writerow({'url':url_temp, 'file_name':file_name,'segment_number':j,'bit_rate':i,'file_size':fsize})
                		
			
