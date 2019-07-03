#!/usr/bin/env python
# coding: utf-8

# In[2]:


### Lists


# In[10]:


#Create an empty list called as list1
list1=[]
list1


# In[9]:


#create a list with random values: string, character, integer, float, complex numbers, Boolean values
list2=["abc",1,3.14]
list2
list3=[1+2j,True]
list3


# In[16]:


#concatenating two lists
list1=list2+list3
list1


# In[25]:


#print first value of list
print(list1[0])


# In[29]:


#print length of the list
len(list1)


# In[28]:


#to see the datatype of a list
type(list1)


# In[21]:


#slicing of a list: picking up values from the lsit
print(list1[:])
#List3 has 2 values i.e.list[0] and list[1]. It will print all the values from 0 to 1


# In[22]:


#last three items will be removed from list
print(list1[:-3])


# In[24]:


#it will print list elements from second to last 4th element
print(list1[1:-3])


# In[31]:


#It will print elements after ignoring 2 elements from start and till length of list1 ie.list[2,3]
list1[2: len(list2)]


# In[34]:


#update a value in a list. replaced 3.14 by "rep"
list1[2]="rep"
list1


# In[35]:


#creating 2D List. List5 is a mtrix of 3 rows and 3 columns
list4=[[]]
list5=[[1,2,3],[4,5,6],[7,8,9]]
list5


# In[36]:


#selecting a value from 2D list. Printing row1 column3
list5[0][2]


# In[37]:


## Append List : adds a new value in the end of the list
list1.append(1234)
list1


# In[39]:


#Here we append the value of the variable in the end of the list.
#executing this code 2 times will append 1.35 two times in a list
i=1.35
list1.append(i)
list1


# In[40]:


# Copy command- copy the elements of one list into another list
list6=list1.copy()
list6


# In[42]:


#clear command - clear all the elements of the list
list6.clear()
list6


# In[43]:


#del command- deletes all the memory alocated to a list. i.e. deletes a list
del(list6)
list6


# In[45]:


#count command- cound the number of times an element is present is a list
list1.count(1.35)


# In[46]:


#index command- returns the index value of the element present in a list
#in case of duplicates, the index value of first element will be returned
list1.index(1.35)


# In[47]:


#insert command: insert a value in a list at a given position
#list.index(position, new element)
list1.insert(0,"value0")
list1


# In[48]:


#pop command: delete a particular value in a list by passing the index.
list1.pop(0)
list1


# In[49]:


#pop the value at index1 of list1 as True returns 1
list1.pop(True)
list1


# In[51]:


#remove command- remove element passed as argument
list1.remove(1.35)
list1


# In[54]:


#reverse command-reverses the element of the list
list1.reverse()
list1


# In[67]:


#sort command- sort the values in a list.
# the values dhould be of same datatype -int,float,char,string
list6=[3,2,4,3,7,6,1]
list6.sort()
print(list6)
list6.sort(reverse=True)
print(list6)
list7=['k','p','a']
list7.sort()
print(list7)
list8=["air","wind","fire","friend","fish"]
list8.sort()
print(list8)


# In[ ]:




