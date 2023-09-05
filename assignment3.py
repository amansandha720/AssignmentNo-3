#!/usr/bin/env python
# coding: utf-8

# In[8]:


import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import seaborn as sns

data=pd.read_csv("ToyotaCorolla.csv")
data


# In[9]:


plt.plot(data["Price"],data["HP"])


# In[11]:


plt.hist(data['Price'],label='Price')
plt.hist(data['HP'],label='HP')

plt.show()


# In[15]:


plt.scatter(data['HP'], data['Price'], label= 'red')
plt.show()


# In[16]:


sns.boxplot(y = data['Price'], x = data['Fuel_Type'], hue = data['Automatic'])


# In[ ]:




