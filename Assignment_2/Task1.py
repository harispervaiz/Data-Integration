
# coding: utf-8

# In[47]:


import pandas as pd
import numpy as np

import re
from __future__ import division


# In[142]:


import requests
RESULTS = list();
def evaluate(csv):
    url = "http://gorilla.bigdama.tu-berlin.de:8001/DataCleaningEvaluator/"
    r = requests.post(url, data={"value": csv})
    if r.status_code != 200:
            print "There is an error! The error code:", r.status_code
    print r.text
    RESULTS.append(r.text)
    return r.text


# # Task 1
# ## Error Detection
# 
# Here, we want to only detect data errors. To mark a cell as data error, you just need to
# change its value into something else.
# - Which of the mentioned data quality constraints can help you to detect data errors?
# How?
# - Report your best error detection precision, recall, and F1.

# There are some desired data quality constraints for the dataset:
# 1. All alphabetical characters in all columns should be capitalized.
# 2. Address data should be compatible to the standard in https://tools.usps.com/go/ZipLookupAction!input.action
# 3. The State column should contain the correct two character US state code.
# 4. City column should contain real city names.
# 5. ZIP column should be formatted as a 5 digit value.
# 6. SSN column should contain an 8-10 digit value.
# Note that, you do not need to fix the DOB, POBox, and POCityStateZip columns.

# In[ ]:


df = pd.read_csv("./inputDB.csv")
print df.shape
f = open('us_cities.txt', 'r')
c = f.readlines()
cities = [str(city).rstrip().upper() for city in c]
reZIP = re.compile('[A-Z a-z]*(\d{5})')
reSSN = re.compile('^(\d{3}-\d{2}-\d{4})|(\d{3}\d{2}\d{4})|\d{8}|\d{9}|\d{10}$')




# In[ ]:


#Rule 4 5 6 What if the City,SSN or ZIP is NaN ? Is this an error ?
#df['City'] =df['City'].fillna('ERROR')
#df['SSN'] =df['SSN'].fillna('ERROR')
#df['ZIP'] =df['ZIP'].fillna('ERROR')
reSSN.match("23334245")


# In[ ]:


states_list = ( 'AL', 'AK', 'AS', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'DC', 'FM', 'FL', 'GA', 'GU', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MH', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'MP', 'OH', 'OK', 'OR', 'PW', 'PA', 'PR', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VI', 'VA', 'WA', 'WV', 'WI', 'WY' )
df = pd.read_csv("./inputDB.csv")

is_capitalized = lambda x: x if str(x).upper() in str(x) else "ERROR"
is_properStateCode = lambda x: x if str(x).upper()  in states_list else "ERROR"
is_properCity = lambda x: x if str(x).upper()  in cities else "ERROR"
is_properZIP = lambda x: x if  reZIP.match(str(x)) else "ERROR"
is_properSSN = lambda x: x if  reSSN.match(str(x)) else "ERROR"

df['FirstName'] = df['FirstName'].map(is_capitalized)
df['MiddleName'] = df['MiddleName'].map(is_capitalized)
df['LastName'] = df['LastName'].map(is_capitalized)

df['SSN'] = df['SSN'].map(is_properSSN)
df['City'] = df['City'].map(is_properCity).map(is_capitalized)
df['ZIP'] = df['ZIP'].map(is_properZIP)
df['Address'] = df['Address'].map(is_capitalized)


df['State'] = df['State'].map(is_properStateCode).map(is_capitalized)





test = df.to_csv(index=False)
df.sample(100)


# In[ ]:


evaluate(test)


# In[ ]:


print(RESULTS)


# In[ ]:





# In[ ]:





# In[ ]:




