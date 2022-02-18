#!/usr/bin/env python
# coding: utf-8

# In[61]:


print("Hrishi and Suraj come %s in the class, "%'together' +
       "at 3 pm.")


# In[11]:


x = 'looked'

print("Hrishi %s and %s around"%('walked',x))


# In[16]:


print('The value of pi is: %6.3f' %(3.141592))


# In[24]:


print('Floating point numbers: %1.0f' %(20.725))


# In[26]:


variable = 25
string = "Variable as integer = %d \nVariable as float = %f" %(variable, variable)
print (string)


# In[28]:


print('We all are {}.'.format('champions'))


# In[31]:


print('{1} {0} {2} {3}.'.format('the','Solve', 'following' ,'equations'))


# In[34]:


print('a: {x}, b: {y}, c: {z}'.format(x = 7,y = 'five',z = 21.25))


# In[35]:


print('The first {o} was alright, but the {o} {m} was tough.'.format(o = 'third', m = 'second'))


# In[53]:


print('The area of rectangle is: %1.3f' %(50.625))

# vs.

print('The area of rectangle is: {0:2.3f}'.format(50.625))


# In[ ]:




