#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pickle


# In[ ]:


fv_load = pickle.load(open('./saves/favorite_save.pkl','rb'))
print(fv_load)


# In[ ]:


type(fv_load)


# In[ ]:


print(fv_load['tiger'])


# In[ ]:


autompg_lr = pickle.load(open('./saves/autompg_lr.pkl','rb'))
print(autompg_lr)


# In[ ]:


type(autompg_lr)


# In[ ]:


print(autompg_lr.predict([[3504.0,8]]))


# In[ ]:




