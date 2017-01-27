
# coding: utf-8

# ### Crawler Pratice

# In[2]:

import pandas
import os 
dflist = []
for f in os.listdir('/Users/wulala/Documents/lvrdata2'):
    path = '/Users/wulala/Documents/lvrdata2/{}/A_lvr_land_A.CSV'
    df = pandas.read_csv('/Users/wulala/Documents/lvrdata/A_lvr_land_A.CSV', encoding = 'big5')
    dflist.append(df)
#df.head


# In[3]:

len(dflist)


# ### pandas.concat 合併資料

# In[5]:

dfall = pandas.concat(dflist)


# * head 前五行資料

# In[6]:

dfall.head()


# ### 敘述性資料

# In[7]:

dfall.describe()


# In[8]:

dfall.to_excel('lvr_data.xlsx')


# In[ ]:



