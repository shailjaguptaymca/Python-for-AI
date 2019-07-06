#!/usr/bin/env python
# coding: utf-8

# # Visualization Library - Seaborn
# 
#     -The library seaborn is used to plot relational graphs.
#     -These graphs describes the statistics of the data
#     

# In[1]:


#importing libraries
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt


# ### SwarmPlot 
#     
#     - For Categorial Data
#     - Creating SwarmPlot using iris dataset

# In[2]:


# reading Titanic.csv file
df=pd.read_csv("iris.csv")

print(df.head())

# the information about, number of rows in each column, null enteries and datatype of coluns
df.info()

# Statistical values of individual columns like number of enteries, mean, std deviation, minimum, maximum, quartile values
df.describe()


# In[3]:


# statistical values using formulas
print(df['sepal_length'].min())
print(df['sepal_length'].max())
print(df['sepal_length'].std())
print(df['sepal_length'].mean())


# In[4]:


# plotting swarmplot for petal length(y) of different species of flowers(x)
sns.swarmplot(y="petal_length",x="species",data=df)
plt.plot()


# ### Regression Plot

# In[5]:


sns.regplot(x='petal_length',y='sepal_width',data=df,color='orange')
plt.show()


# ### BoxPlot

# In[6]:


''' BoxPlot is used for regression problems
    The line B,C,D are the quartiles
    The line B is the mid of A 
'''
bx=sns.boxplot(x='petal_length',data=df)
bx.set_title("box_plot")
plt.show()


# ### Violin Plot

# In[7]:


#ax =axis on which the graph will be drawn i.e where the graph start
#fig are the boundaries of figure ie. the lenght and breadth of graph
# subplot: multiple type of graph in a graph
fig,ax=plt.subplots()

#vert= False : the graph should not be vertical. Remove and see what happens
ax.violinplot(df["sepal_length"],vert=False)
plt.show()


# ### Factor Plot
# 
#     -using Titanic_Data.csv file

# In[8]:


# We are doing categorial plotting in bar graph
# kind: denotes the kind of graph we wish to make
#palette: color shadings in the graph
#x: Pclass
#y: Survived
#label: sex
# It will draw a graph between Pclass and Survived using Sex as category
df=pd.read_csv('Titanic_Data.csv')
g=sns.factorplot("Pclass","Survived","Sex",data=df,kind="bar", palette='muted',legend=True)


# In[9]:


# the above graph shows the probablity of a person being male or female from different classes in Titanic survival


# ### Facet Grid
#     
#     -Facet Grid is used for the scatter plotting in a grid form
#     -Every grid will have one graph
#     

# In[11]:


tips=pd.read_csv("tips.csv")

# the grid is divided into rows and columns
# margin_titles =True display the margins
g=sns.FacetGrid(tips,col="sex",row="smoker",margin_titles=True)

#plotting a scatter plot: x=total_bill and y=tip
g.map(plt.scatter,"total_bill","tip")

#suptitle: title of the figure
g.fig.suptitle("Facet Grid")

#savefig : save the figure in the working directory. You can give location as well to save a file
plt.savefig("fig.png")
plt.show()


# In[ ]:




