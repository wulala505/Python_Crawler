
# coding: utf-8

# In[5]:

import requests
from bs4 import BeautifulSoup
url="http://data.gcis.nat.gov.tw/od/data/api/A1B4CBFF-2D3A-409B-8A78-2AD94F63AE4A?$format=json&$filter=Business_Name like 咖啡 and Agency eq 379100000G and Business_Current_Status eq 01"
r = requests.get(url)
soup = BeautifulSoup(r.text)

data=soup.p.text
print data


# In[11]:

import json

dd=json.loads(data)
for no in dd:
    #print no["President_No"]
    url_base="http://data.gcis.nat.gov.tw/od/data/api/7E6AFA72-AD6A-46D3-8681-ED77951D912D?$format=json&$filter=President_No eq "
    url_middle=no["President_No"]
    url_end=" and Agency eq 379100000G"
    url2=url_base+url_middle+url_end
    try:
        r2 = requests.get(url2)
        soup = BeautifulSoup(r2.text)
        data2=soup.p.text
        dd2=json.loads(data2)
        try:
            for add in dd2:
                print add["Business_address"]   
        except ValueError:
            print no["President_No"]
    except ValueError:
        print no["President_No"]
    
#dd2=json.loads(data2)
#for add in dd2:
#    print add["Business_address"]    
    

