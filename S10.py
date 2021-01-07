#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup
r=requests.get("https://m.aflc.com.cn/sports/6435.html")

soup = BeautifulSoup(r.text,"html.parser")

sel1s = soup.select("table")


for sel1 in sel1s:
        datas=list(sel1.stripped_strings)      
        datas.pop(0)
        datas.pop(0)
        datas.pop(25)
        datas.pop(25)
        datas.pop(25)
        datas.pop(25)
        datas.pop(25)
        datas.pop(25)
        datas.pop(45)
        datas.pop(45)
        datas.pop(45)
        datas.pop(45)
        datas.pop(45)
        datas.pop(45)
        datas.pop(65)
        datas.pop(65)
        datas.pop(65)
        datas.pop(65)
        datas.pop(65)
        datas.pop(65)
print(datas)


# In[2]:


x=[ ]

for j in range(0,5):
    x.append(datas[j])

print(x)


# In[3]:


a=[ ]
b=[ ]
c=[ ]
d=[ ]
e=[ ]
for i in range(5,85,1):
        if i %5==1:
            a.append(datas[i])
        elif i %5==2:
            b.append(int(datas[i]))
        elif i %5==3:
            c.append(int(datas[i]))
        elif i %5==4:
            d.append(int(datas[i]))
        elif i %5==0:
            e.append(int(datas[i]))

            
print(a ,'\n',b ,'\n' ,c,'\n' ,d ,'\n' ,e)


# In[4]:


num=[
    a,
    b,
    c,
    d,
    e,
]
print(num)


# In[5]:


dict={
    x[0]:num[4],
    x[1]:num[0],
    x[2]:num[1],
    x[3]:num[2],
    x[4]:num[3]
}


# In[6]:


import pandas as pd
df=pd.DataFrame(dict)
df


# In[12]:


import matplotlib.pyplot as plt

plt.rcParams["font.sans-serif"]="Microsoft JhengHei"

plt.tick_params(axis='both')


listx1 = df['胜']
listy1 = df['战队']

listx2 = df['负']
plt.ylim(0,8)
plt.grid(lw=1,alpha=0.1)

plt.plot(listy1, listx1, 'k-s', ms=10, label="win")
plt.plot(listy1, listx2, 'r--s',ms=10, label="lose")

plt.legend()

plt.xlabel("战队",fontsize=16)
plt.ylabel("勝敗",fontsize=16)
plt.show()


# In[16]:


import matplotlib.pyplot as plt

listx1 = df['积分']
listy1 = df['战队']
plt.bar(listy1, listx1 )

plt.xlabel("战队",fontsize=16)
plt.ylabel("积分",fontsize=16)
plt.show()


# In[9]:


import matplotlib.pyplot as plt
separeted = (0.1, 0, 0.1, 0.2, 0,0, 0, 0, 0.1, 0,0.1, 0, 0, 0, 0,0) 
sizes = df['积分']
labels = df['战队']
plt.pie(sizes,
        labels = labels,
        radius = 2, 
        autopct = "%1.1f%%",
        explode = separeted, 
       pctdistance = 0.8,
       textprops = {"fontsize" : 12})

plt.title("積分", {"fontsize" : 16})
plt.show()


# In[10]:


import sqlite3
conn= sqlite3.connect("C:/Users/USER/Desktop/302.db")
df.to_sql('s10',conn,if_exists='replace')


# In[ ]:




