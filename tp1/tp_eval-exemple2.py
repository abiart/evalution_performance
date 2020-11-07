#!/usr/bin/env python
# coding: utf-8

# ## Importation des bibliothéques
#         

# In[10]:


import random
import matplotlib.pyplot as plt
import math
import numpy as np


# ##  Fonction pour calculer la moyenne empérique

# In[11]:


def Xn(t,n):
    x=0
    for j in t:
        x=x+j
    return x/n
    


# ## Déclaration de fonction qui va générer les valeurs xn

# In[12]:


def alea_table(n,lamda):
    t=np.random.exponential(1/lamda,n)
    return(t)


# ##  Fonction pour calculer la variance empérique

# In[13]:


def variance(t,n,xn):
    tita=0
    for i in t:
        tita=tita+(i-xn)**2
        return tita/n


# ## coder la distibution uniforme continu sur l'intervalle [0,1]

# In[36]:


n=[10,100,1000,10000,100000,1000000]
tita_table=[]
xn=[]
lamda=2
for i in n:
    t=alea_table(i,lamda)
    xn.append(Xn(t,i))
    tita_table.append(variance(t,i,Xn(t,i)))
plt.plot(n,xn,color='g',label="moyenne empérique")
plt.plot(n,tita_table ,color='r',label="variance empérique")
plt.legend()
plt.xlabel("Nombre d'echantillon")
plt.ylabel("Variables aléatoires")
plt.title(" la moyenne empérique et la variance empérique")
plt.grid()
plt.show()

for i in range(len(n)):
    print(" pour{} valeurs aléatoires :la moyenne empérique ={}, la varience emprique={} ".format(n[i],xn[i],t[i]))


# ## N est proportionnelle à la valeur moyenne et  inversement proportionnelle à la variance mathématique pour une distribution exponentielle.

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




