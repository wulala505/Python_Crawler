
# coding: utf-8

# In[46]:

import json
import urllib2
import requests
from bs4 import BeautifulSoup
#11450
for i in range(0,100,50):
    url=("https://business.591.com.tw/home/search/rsList?is_new_list=1&storeType=1&type=1&kind=5&searchtype=1&region=1&shType=clinch&firstRow="+"i"+"&totalRows=11478")
    data = json.load(urllib2.urlopen(url),encoding="utf-8")
    d=data["data"]["data"]
    for k in d:
        house_id = k["houseid"]
        
        url2="https://rent.591.com.tw/rent-detail-"+str(house_id)+".html"
        r=requests.get(url2)
        r.encoding = 'utf8'
        soup=BeautifulSoup(r.text,"lxml")
        try:
            price=soup.find('div','price clearfix').find('i').text.encode("utf-8")
            s=soup.find('ul','attr').find('li').text.encode("utf-8")
            location=soup.find('span','addr').text.encode("utf-8")
            hid = k["houseid"] 
            print price,s,location,hid
        except:
            print k["houseid"]

