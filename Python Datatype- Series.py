#!/usr/bin/env python
# coding: utf-8

# # Python Datatype- Series
# 
#     - We will see an overview of important methods in a Series
#     - You can consider Series as a column in a DataFrame
#     - We will also see how to convert Series to a DataFrame

# In[1]:


import pandas as pd


# In[2]:


# Creating a variable ser1 to create series
ser1 = pd.Series([100,200], index=['ab','cd'])
ser1


# In[3]:


# to delete all the values of ser1
ser1='NaN'
ser1


# In[4]:


# index method will display first column of Series datatype
ser2 = pd.Series([100,200], index=['ab','cd'])
ser2.index


# In[5]:


# loc method will give values associated with index values 
ser2.loc[['ab','cd']]


# In[6]:


# Note: we have pass values like [[]]. This is because we are passing list as an argument
# To perform operations row wise, we require index values


# In[7]:


ser2.loc[['ab']]


# In[9]:


# this will give all the values of all the index
ser2.loc[:]


# ### TypeCasting : Converting Series to a DataFrame

# In[13]:


#passing series as argument in a DataFrame
df= pd.DataFrame(ser2)
df


# In[14]:


# to pass multible series to DataFrame. This can be done by converting Series to Dictionary and then to DataFrame


# In[ ]:




