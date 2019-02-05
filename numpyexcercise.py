
# coding: utf-8

# In[5]:


import numpy as np
a = np.array([1,2,3])
b = np.r_[np.repeat(a, 3), np.tile(a, 3)]
print(b)


# In[15]:


a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])
np.intersect1d(a,b)


# In[16]:


# How to remove from one array those items that exist in another?
a = np.array([1,2,3,4,5])
b = np.array([4,5,6,7,8])
np.setdiff1d(a,b)


# In[17]:


#How to get the positions where elements of two arrays match?
a = np.array([1,2,3,4,5])
b = np.array([1,2,3,4,6])
np.where(a==b)


# In[25]:


#How to extract all numbers between a given range from a numpy array?
# Get all items between 1 and 10 from a.
a = np.array([1,2,3,10,52,30])
print(a[(a >= 1) & (a <= 10)])
index = np.where((a >= 1) & (a <= 10))
print(index)


# In[3]:


import numpy as np
a = np.array([1,2,3])
b = np.r_[np.repeat(a,3), np.tile(a,3)]
print(b)


# In[4]:


import numpy as np
print(np.version)


# In[ ]:



#creating 1D array
import numpy as np
a = np.arange(10)
print(a)

