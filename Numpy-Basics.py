#!/usr/bin/env python
# coding: utf-8

# ### Numpy Basics
# 
# 
# 

# In[1]:


# importing numpy file with an alias name as np
import numpy as np


# In[2]:


# creating a list as list1

list1=[1,2,3,4,5,6]
list1


# In[3]:


# creating an arrary as arr1 by passing list as argument

arr1=np.array(list1)
arr1


# In[4]:


# Note how an array is different in representation of list


# In[5]:


# Creating a 2 D array or matrix of zero'ss. It is also called as zero matrix
# ...pass number of rows=2 and number of columns=3 as arguments

arr2=np.zeros((2,3))
arr2


# In[6]:


# Creating a 2 D array or matrix of ones's. It is also called as one's matrix
# ...pass number of rows=2 and number of columns=3 as arguments

arr3= np.ones((2,3))
arr3


# In[7]:


# Arange function gives evenly spaced values.
# ...syntax= np.arrange(start value, stop value, step size)
# ...start value gives a starting value and stop value tells where to stop
# ...step size indicate the steps or increment/decrement between the values

arr4=np.arange(2,10)
print (arr4)
arr5=np.arange(0,6,2)
print (arr5)


# In[8]:


# linspace function behaves in a similar manner as arrange. 
# ...difference between both is: arrange uses step size to generate random values
# ...where as linspace uses fractional or decimal values as well along with step values
# ...linspace(start value, end value, number of values to generate)

arr6=np.linspace(2,30,5)
arr6


# In[9]:


# radom function generates random values from start values till stop values
#... syntax np.random.randint(start, stop)
#... randint will give integer values with random function to randomize values

var1=np.random.randint(0,7)
print(var1)
#var1 will return one random value from 0 to 7

arr7=np.random.randint(0,10,(2,2))
print(arr7)
#arr6 will give value in a 2X2 matrix from 0 to 10


# In[10]:


# seed functions ensures that also same set of values are used for randomization
#...for example: if in first rondomize value from 0 to 50 was selected
#...then in second randomize values from 0 to 50 will only be selected

np.random.seed(50)
arr8= np.random.randint(0,50,5)
print(arr8)


# In[11]:


arr9 = np.random.randint(0,50,10)
arr9


# ### Mathematical Operations

# In[12]:


# max operation: maximum value in an array or a list

print("max = ",arr9.max())


# In[13]:


# min operation: minimum value in an array or a list

print("min = ",arr9.min())


# In[14]:


# mean operation: mean of all the values present in a list or an array

print("mean= ",arr9.mean())


# In[15]:


# ...argmin operation: returns the indexof minimum value along a given axis. 
#...axis=0 means columnwize and axis=1 rowwize. 
#...by default it is axis=0

print("mimimum argument value= ",arr9.argmin())


# In[16]:


#argmax operation: returns the index of maximum value along a given axis

print("maximum argument value= ",arr9.argmax())


# In[17]:


# ...reshaping operation: change the shape i.e. from 1D to 2D and so on..
#...syntax reshape(row,column)

print("reshaping into 2X2 = ")
arr10= arr9.reshape(5,2)
print ("reshaped array is ",arr10)


# In[18]:


print("index of minimum value along rows",arr10.argmin(axis=1))

print("index of maximum value along columns",arr10.argmax(axis=0))


# ### Selected Selection or Slicing

# In[ ]:


# selecting particular values from an array 


# In[ ]:


# creating an array from list using random function.
# reshaping the array to 5X4 from 1X20


# In[21]:


list2=np.random.randint(2,50,20)
list2


# In[22]:


array1=np.array(list2)
array1


# In[24]:


array1=array1.reshape(5,4)
array1


# In[ ]:


# slicing syntax: [row1 : row nth, column1 : column nth]


# In[25]:


#printing all the values of array1
#here nothing is specified in rows and columns. and so it will print all the values of rows and columns
# note: values in python start with index 0 and end with index-1

print( array1[:,:])


# In[26]:


# print all the values of rows for first column
#this will print[all values of row, value of column[0] to column [1-1] i.e column 0]

print (array1[:,0:1])


# In[27]:


#print all the vlaues of columns for first row

print(array1[0:1,:])


# In[29]:


# print values of row=2,3 and column 1,3
# I am considering row 0 as 1st row and column 0 as first column

print(array1[2:4,1:4])


# In[ ]:




