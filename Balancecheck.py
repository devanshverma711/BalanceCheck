#!/usr/bin/env python
# coding: utf-8

# In[82]:


def balancecheck(s):
    
    if len(s)%2 != 0:
        return False
    
    opening=set("([{")
    
    match=set([("(", ")"),("[","]"),("{","}")])
    
    stack=[]
    
    for i in s:
        
        if i in opening:
            stack.append(i)
            
        else:
            if len(stack)==0: 
                return False
            
            last=stack.pop()
        
            if (last,i) not in match:
                return False
    return len(stack)==0
        


# In[83]:


{'key1','key2','key3'}


# In[84]:


balancecheck("[]")


# In[85]:


{1,2,(3,2),5}


# In[86]:


balancecheck("[]")


# In[87]:


balancecheck("[]")


# In[88]:


{1}
balancecheck("[]")


# In[ ]:




