
# coding: utf-8

# In[1]:


import numpy as np
a = np.version
print(a)


# In[2]:


#How to create a 1D array?
b = np.arange(10)
print(b)


# In[6]:


# How to create a boolean array?
c = np.full((3,3),True,dtype=bool)
print(c)


# In[8]:


#How to extract items that satisfy a given condition from 1D array?
d = np.arange(10)
d[d%2 != 0]


# In[11]:


#How to replace items that satisfy a condition with another value in numpy array?
e  = np.arange(10)
e[e%2 != 0] = -1
e


# In[19]:


#How to replace items that satisfy a condition without affecting the original array?
d  = np.arange(10)
out = np.where(d%2 != 0, -1, d)
print(d)
print(out)


# In[20]:


#How to reshape an array?
arr = np.array([1,2,3])
print(arr.reshape(3,1))


# In[38]:


#How to stack two arrays vertically?
a = np.arange(10)
print(a.reshape(2,-1))
b = np.repeat(1,10).reshape(2,-1)
print(b)
c = np.tile(a, 1).reshape(2, -1)
c


# In[36]:


#How to stack two arrays horizontally?
a = np.arange(10).reshape(2, -1)
b = np.repeat(1, 10).reshape(2, -1)
print(np.hstack([a,b]))
print(np.concatenate([a, b], axis=1))
print(np.c_[a, b])


# In[45]:


#How to generate custom sequences in numpy without hardcoding?
a = np.array([1,2,3])
np.r_[np.repeat(a,3), np.tile(a,3)]


# In[50]:


#How to get the common items between two python numpy arrays?
a  = np.array([1,2,3,4,5,6])
b = np.array([5,6,7,8,9,10])
np.intersect1d(a, b)


# In[54]:


#How to remove from one array those items that exist in another?
a = np.array([1,2,3,4,5,6])
b = np.array([4,1,8,9,10])
np.setdiff1d(a, b)


# In[60]:


#how to the positions where the two elemnts of array matched
a = np.array([1,2,3,4,5,6])
b = np.array([7,8,9,1,10,11])
np.where(a == b)


# In[62]:


#How to extract all numbers between a given range from a numpy array?
a = np.arange(15)
a[(a >= 5) & (a <= 10)]


# In[68]:


#How to make a python function that handles scalars to work on numpy arrays?
def maxx(a,b):
    if a>b:
        return a
    else:
        b
pair_max =np.vectorize(maxx, otypes=[float])
a = np.array([6,7,9,8,9])
b = np.array([1,2,3,4,5])
pair_max(a,b)


# In[70]:


#How to swap two columns in a 2d numpy array?
a = np.arange(9).reshape(3,3)
a
a[:,[1,0,2]]

