#!/usr/bin/env python
# coding: utf-8

# In[1]:


import subprocess


# In[2]:


print(subprocess.check_output(['echo' ,'%cd%'],shell=True).decode('utf-8'))


# ## Git Clone

# In[4]:


def clone(path):
    subprocess.call(['git','clone',path])


# In[28]:


clone("https://github.com/adarsh62656/PHPapp.git")


# ## Git Add

# In[29]:


def addtostage(path):
    """path -   Add Path of file to Move on staging area"""
    subprocess.call(['git','add',path])


# ## Git rm

# In[36]:


def rmstage(path):
    """path -   Add Path of file to remove from staging area"""
    subprocess.call(['git','rm',path])


# ## Git Commit

# In[30]:


def commit(message):
    """message -   Enter Commit Message"""
    subprocess.call(['git','commit','-m',message])


# ## Git INIT

# In[51]:


def gitinit(path=""):
    """path -   Enter Path to initialize empty repozitory"""
    if path=="":
        subprocess.call(['git','init'])
    else:
        subprocess.call(['git','init',path])


# ## Git log

# In[52]:


import os
def log(path=""):
    """path -   Enter Path to see logs of repozitory"""
    os. chdir(path)
    print(subprocess.check_output(['git' ,'log'],shell=True).decode('utf-8'))


# In[53]:





# In[61]:





# In[ ]:





# In[ ]:




