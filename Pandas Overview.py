#!/usr/bin/env python
# coding: utf-8

# # Pandas Overview

# In[1]:


#importing library using an alias name pd
import pandas as pd


# In[6]:


# Reading the file. pd.read_csv. Pass complete location as an argument or load file in jupyter
df=pd.read_csv("salaries.csv")

# writing variable name as such prints the contents in a variable. Here variable df is of dataframe type
df


# In[3]:


# type operator tells the datatype of the variable passed. df is a dataframe here
type(df)


# In[7]:


# print records from the begining of the table. By default it print 5 values
df.head()


# In[8]:


# print records from the begining of the table. The value in the brackets tells about how many values to print
df.head(6)


# In[9]:


# print records from the end of the table. By default it prints 5 values.
df.tail()


# In[10]:


# print records from the end of the table. The value in the brackets tells about how many values to print
df.tail(6)


# In[11]:


# dataframe.describe()- give statistical values like count, mean, standard deviation, minimum, quartile values(25%,50%,75%,100%) for each column holding numerical values
df.describe()


# In[18]:


# you can calculate individual statistical value using functions as wee
df['Age'].count()


# In[21]:


# The output of the df['Salary']>55000 is either true or false for all the persons in the table.


# In[20]:


# The rows having true as an answer for df['Salary']>55000 were printed
df[df['Salary']>55000]


# In[12]:


''' dataframe.info()- gives the information about the file
             - like number of enteries in each column, null values is a column, and data type of the values in a column
             - " not null" : no null enteries are present in that column
             - " int64"    : interger values are present in that column
             - " object"   : character values are present in that column'''

df.info()


# In[13]:


df


# In[14]:


# Printing individual column by passing column name in a dataframe: 
# here we are passing 'Name' in df(df is the name of dataframe where our table is present)
# 'Name' is a string
df['Name']


# In[15]:


# the name of the column is a string so we pass column name in apostophes or double quotes
df['Age']


# In[17]:


# Printing two columns together. The inner square brackets represent the passing of list as an argument
df[['Name','Salary']]


# In[ ]:




