#!/usr/bin/env python
# coding: utf-8

# # Average cost of undergraduate student by state USA

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


x=pd.read_csv('C:/My python files/nces330_20.csv')



# In[3]:


x.info()


# In[14]:


x=pd.read_csv('C:/My python files/nces330_20.csv')
x.head(10)


# In[54]:


x=pd.read_csv('C:/My python files/nces330_20.csv')
x=x[x["State"]=="Alabama"]["Value"].mean()
print("The Average cost of undergraduate student in Alabama is",x)


# In[10]:


x=pd.read_csv('C:/My python files/nces330_20.csv')
x=x[x["State"]=="Alabama"]["Value"].mean()


# In[13]:


x=pd.read_csv('C:/My python files/nces330_20.csv')
x.tail(10)


# In[17]:


x=pd.read_csv('C:/My python files/nces330_20.csv')
x.groupby("State")["Value"].mean()


# In[18]:


x=pd.read_csv('C:/My python files/nces330_20.csv')
x.groupby("State")["Type"].agg(pd.Series.mode)


# In[58]:


x=pd.read_csv('C:/My python files/nces330_20.csv')
x=x["Expense"].agg(pd.Series.mode)
print("Most undergraduate students prefer spending on ",x)


# In[62]:


x=pd.read_csv('C:/My python files/nces330_20.csv')
x=x[x["State"]=="Texas"]["Value"].max()
print("The maximum amount one can spend in Texas is ",x)


# In[28]:


x=pd.read_csv('C:/My python files/nces330_20.csv')
max_value=x["Value"].max()
x=x[x["Value"]==max_value]
print(x)


# In[45]:


import matplotlib.pyplot as plt


# In[63]:



x=pd.read_csv('C:/My python files/nces330_20.csv')
x=x.groupby("Year")["Value"].mean().plot()
x


# In[68]:


x=pd.read_csv('C:/My python files/nces330_20.csv')
x=x.groupby("Length")["Value"].mean()
print(x)
y=x.plot(kind="pie")
print(y)


# In[67]:


x=pd.read_csv('C:/My python files/nces330_20.csv')
x.groupby("State")["Value"].mean().plot(kind="bar")


# In[ ]:




