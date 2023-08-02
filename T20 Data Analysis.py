#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import necessary libraries
import pandas as pd
import json


# In[3]:


with open('t20_json_files/t20_wc_match_results.json') as f:
    data = json.load(f)
data


# In[4]:


df_match = pd.DataFrame(data[0]['matchSummary'])
df_match.head()


# In[5]:


df_match.shape


# In[6]:


df_match.rename({'scorecard': 'match_id'}, axis = 1, inplace = True)
df_match.head()


# In[18]:


match_ids_dict = {}

for index, row in df_match.iterrows():
    key1 = row['team1'] + ' Vs ' + row['team2']
    key2 = row['team2'] + ' Vs ' + row['team1']
    
    match_ids_dict[key1] = row["match_id"]
    match_ids_dict[key2] = row["match_id"]
    
match_ids_dict


# In[ ]:


{
    "Namibia Vs Sri Lanka": "T20I # 1823",
    "Sri Lanka Vs Namibia": "T20I # 1823",
    "Netherlands Vs U.A.E": "T20I # 1825",
    "U.A.E Vs Netherlands": "T20I # 1825",
    ...
}


#  **batting summary**

# In[10]:


with open('t20_json_files/t20_wc_batting_summary.json') as f:
    data = json.load(f)
    
    all_records = []
    
    for rec in data:
        all_records.extend(rec['battingSummary'])
        
data


# In[11]:


df_batting = pd.DataFrame(all_records)
df_batting.head(11)


# In[12]:


df_batting = pd.DataFrame(all_records)
df_batting.tail(11)


# In[14]:


df_batting["out/not_out"] = df_batting.dismissal.apply(lambda x: "out" if len(x) > 0 else "not_out")
df_batting.head(11)


# In[15]:


df_batting.drop(columns=["dismissal"], inplace=True)
df_batting.head(10)


# In[17]:


df_batting['batsmanName'] = df_batting['batsmanName'].apply(lambda x: x.replace('â€', ''))
df_batting.head(15)


# In[20]:


df_batting["match_id"] = df_batting["match"].map(match_ids_dict)

match_ids_dict["Namibia Vs Sri Lanka"]


# In[21]:


df_batting.head()


# In[22]:


df_batting.to_csv('t20_csv_files/temp.csv', index = False)

