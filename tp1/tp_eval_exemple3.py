#!/usr/bin/env python
# coding: utf-8

# ## Importation des bibliothéques
#         

# In[42]:


from scipy.stats import randint
import matplotlib.pyplot as plt
import numpy as np
import math
import random


# ##  Fonction pour calculer la moyenne empérique

# def uniforme(a,b):
#     return(a+(b-a)*random())
# 

# In[43]:


def Xn(t,n):
    x=0
    for j in t:
        x=x+j
    return x/n
    


# ## Déclaration de fonction qui va générer les valeurs xn

# In[54]:


def alea_table(n):
    t=[]
    for i in range(n+1):
        t.append(random.uniform(a,b))#
    return(t)
   


# ##  Fonction pour calculer la variance empérique

# In[55]:


def variance(t,n,xn):
    tita=0
    for i in t:
        tita=tita+(i-xn)**2
        return tita/n


# ## coder la distibution uniforme continu sur l'intervalle [0,1]

# In[59]:


n=[100,1000,10000,100000]

tita_table=[]
xn=[]
a=5
b=100
for i in n:
    t=alea_table(i)
    xn.append(Xn(t,i))
    tita_table.append(variance(t,i,Xn(t,i)))
plt.plot(n,tita_table ,color='r',label="variance empérique")
plt.plot(n,xn,color='g',label="moyenne empérique")
plt.legend()
plt.xlabel("Nombre d'echantillon")
plt.ylabel("Variables aléatoires")
plt.title(" la moyenne empérique et la variance empérique")
plt.grid()
plt.show()



for i in range(len(n)):
    print(" pour{} valeurs aléatoires :la moyenne empérique ={}, la varience emprique={} ".format(n[i],xn[i],t[i]))


# ## le nombre d’échantillons N est inversement proportionnelle de valeur moyenne et la variance mathématique

# In[ ]:





# In[ ]:




