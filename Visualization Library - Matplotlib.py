#!/usr/bin/env python
# coding: utf-8

# # Visualization Library - matplotlib
# 
#     We will be covering bar-graph, line-plot, scatter-plot, histogram, pie chart.
#     We will also learn to draw multiple graph in a figure or a plot

# In[ ]:


#importing pyplot package of matplotlib library with an alias name as plt
import matplotlib.pyplot as plt


# ### 1. Bar Graph

# In[3]:


# creating list of input for x and y axis
x=[1,2,3]
y=[30,43,12]

# plotting a bar graph using bar method
plt.bar(x,y)

# displaying graph using show method
plt.show()


# In[4]:


'''Color attributes can be defined as
    1. By using alpabets for colors: k = black, b = blue, r= red, y = yellow, g = green
    2. By using complete names: "darkgreen", "pink", "red", "margenta"
    3. By using hash codes for colors
'''
plt.bar(x, y, color="red")
plt.show()


# In[7]:


plt.bar(x,y)
# Providing title to a graph using title method
plt.title("Bar-Graph")

# Providing labels to x and y axis using xlabel and ylabel method
plt.xlabel("x-values")
plt.ylabel("y-values")
plt.show()


# In[18]:


# Two Bar Graph in one plot

x1= [1, 3, 4, 7, 9]
x2= [2, 5, 6, 8, 10, 13]
y1= [12, 15, 30, 45, 25]
y2= [23, 43, 45, 24, 10, 12]

# Note: shape i.e 1X5 here should be same for x and y

plt.bar(x1, y1, color= 'black')

# width defines the breadth of the bar)
plt.bar(x2, y2, color= 'cyan', width=0.2)

plt.show()
''' You can use titles, labels in the graph 
    You can store multiple graph together by defining x3,x4,y3,y4....
    and display them together by writing .show() at the end


# ### 2. Scatter Plot
# 
#         It plots the points on the graph as dots
#         

# In[19]:


x1= [1, 3, 4, 7, 9]
x2= [2, 5, 6, 8, 10, 13]
y1= [12, 15, 30, 45, 25]
y2= [23, 43, 45, 24, 10, 12]


# In[22]:


plt.scatter(x1, y1, color= "orange")
plt.scatter(x2, y2, color= "blue")
plt.show()


# In[31]:


# figure method change the outline of the figure. figsize(shape of the graph ie. length and breadth of figure)
# Note: modification in figure should be done before defining scatter
plt.figure(figsize=(5,5))

# s defines the size of the dot
# alpha defines gradient of the color. Value Near to 1 gives darkest gradient and the color is lightest at 0
# markers can be '^', 'o', '.', '*', 's'=square and so on
plt.scatter( x1, y1, s= 60, alpha= 0.7, marker = '*')
plt.scatter( x2, y2, s= 40, alpha= 1.0, marker = 's')


plt.show()


# ### 3. Line Plot
# 
#         Generally use for regression problem where the data is continuous. Example: sensex data..

# In[32]:


x1= [1, 3, 4, 7, 9]
x2= [2, 5, 6, 8, 10, 13]
y1= [12, 15, 30, 45, 25]
y2= [23, 43, 45, 24, 10, 12]


# In[34]:


plt.plot(x1, y1, label="line1")
plt.plot(x2, y2, label="line2")

# to display the labels: line1 with blue colour indication , line2 with orange colour indication, we have to write legend method
# try deleting the plt.legend() line
plt.legend()

plt.show()


# ### 4. Pie Chart
# 
#      - To calculate the percentage according to 360 degrees
#      - Pie chart create slices according to the data

# In[39]:


x=[20,15,25,30,10,5]

# label names that will be given to each portion of a pie
label_names=["talking", "study", "eating", "sleeping", "cooking", "playing"]

# colors given to each portion of a pie
cols= ['violet','red','blue','green','yellow','orange']

#startangle position of start of a pie chart . It is given from 360 degree
#explode =1 will show which portion of pie will be pop out
#autopct calculates the percentage where 1 represent integer and 2 represent upto two decimal places. '%'is to show percentage values

plt.pie(x, labels=label_names, colors=cols, startangle=0, explode=(0,0,0,1,0,0), autopct='%1.2f%%')


# ### 5. Histogram

# In[42]:


# Gives twenty random numbers between 0 to 100
import numpy as np
x= np.random.randint(0,100,20)

#hist method draws a histogram. 
# bins are the divisions between division on x axis i.e 10,20,30. There is a gap of 10 units between each unit on x axis
plt.hist(x,bins=10, width=0.5)


# ### 6. Combination of graphs

# In[50]:


x1= [1, 3, 4, 7, 9]
x2= [1, 3, 4, 7, 9]

y1= [12, 15, 30, 45, 25]
y2= [13, 16, 31, 46, 26]

#plotting a bar graph, line plot and scatter plot together)
plt.bar(x1, y1, label='bar', width=0.25)
plt.plot(x2, y2, label='line-plot')
plt.scatter(x2, y2, label='scatter-plot')

plt.xlabel("x-values")
plt.ylabel("y-values")

plt.legend()

plt.show()


# In[53]:


# use plt.barh to plot graph horizontally
x1= [1, 3, 4, 7, 9]
y1= [12, 15, 30, 45, 25]

#plotting a bar graph horizontly
plt.barh(x1, y1)
plt.show()


# In[ ]:




