#!/usr/bin/env python
# coding: utf-8

# In[1]:


def number_of_lines():
    fileh=open("/cxldata/datasets/project/mbox-short.txt","r")
    inp=fileh.read()
    fileh.close()
    count=len(inp.splitlines())
    return count


# In[2]:


nol=number_of_lines()
print(nol)


# In[3]:


def count_number_of_lines():
    fhand=open("/cxldata/datasets/project/mbox-short.txt")
    count=0
    for line in fhand:
        line=line.rstrip()
        if line.startswith("Subject:"):
            count+=1
    return count


# In[4]:


count=count_number_of_lines()
print(count)


# In[5]:


def average_spam_confidence():
    count=0
    summ=0.0
    fhand=open("/cxldata/datasets/project/mbox-short.txt")
    for line in fhand:
        line=line.rstrip()
        if line.startswith("X-DSPAM-Confidence:"):
            count+=1
            summ+=float(line.split(":")[1])
    return summ/count
        


# In[6]:


avg=average_spam_confidence()
print(avg)


# In[22]:


#Python Project - Churn Emails - Find Which Day of the Week the Email was sent
def find_email_sent_days():
    fhand=open("/cxldata/datasets/project/mbox-short.txt")
    dit={"Sat":0,"Sun":0,"Mon":0,"Tue":0,"Wed":0,"Thu":0,"Fri":0}
    count=0
    for line in fhand:
        if line.startswith("From "):
            count+=1
            value=line.split(" ")[2]
            dit[value]=dit[value]+1
    fhand.close()
    for k,v in dit.items():
        if (v==0):
            del dit[k]
        return dit


# In[23]:


dit=find_email_sent_days()
print(dit)


# In[ ]:




