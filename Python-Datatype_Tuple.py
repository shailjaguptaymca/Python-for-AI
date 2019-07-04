#!/usr/bin/env python
# coding: utf-8

# ### Python Datatype- Tuple

# In[2]:


# Create an empth tuple
tuple1=()
tuple2=()


# In[7]:


#Insert values in tuple1 and tuple2
tuple1=(12,13,18,1+4j,"a","abc")
tuple2=(True, 4.56,"data1",-3.45)
print(tuple1)
print(tuple2)


# In[8]:


#Concatenating tuples into new tuple: tuple3
tuple3=tuple1+tuple2
print(tuple3)


# In[9]:


#Slicing a tuple- Selecting all the tuple excluding last three
print(tuple3[:-3])


# In[12]:


# Updating index=0 value of a tuple : This will generate error.
# update,replace,remove operations are not performed on a tuple
# Tuple cannot be modified
tuple3[0]="ab"


# In[13]:


# Count method- Count number of times an element is present in a tuple
tuple3.count(12)


# In[14]:


#Index method -returns the index of a particular value in a list
tuple3.index(12)


# In[ ]:




