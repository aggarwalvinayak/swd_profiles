import hashlib 
import urllib.request
from urllib.parse import urlparse
import ssl
import os
import timeit

start = timeit.default_timer()

ssl._create_default_https_context = ssl._create_unverified_context

url='https://swd.bits-goa.ac.in/media/'
number='9120273977'
data=list()
file=open('list.txt')
os.mkdir('Images')
for line in file:
    data.append(line.rstrip())
for item in data:
    hash=((hashlib.md5((number+item).encode()).hexdigest()))
    try:
        urllib.request.urlretrieve((url+hash+'.jpg').rstrip(), os.path.join(os.getcwd(),'Images', str(item+'.jpg')))
        print('Retreiving:',item,end='\r')
    except:
        continue
stop = timeit.default_timer()
print('/r')
print('Time taken:',stop-start)