#!/usr/bin/env python
# coding: utf-8

# ___________________________________________________________________________________________________________________

# # 5
# Consider a single-server queueing model in which customers arrive accordin to a nonhomogeneous Poisson process. Upon arriving they either enter service if the server is free or else they join the queue. Suppose, however, that each customer will only wait a random amount of time, having distribution F, in queue before leaving the system. Let G denote the service distribution. Define variables and events so as to analyze this model, and give the updating procedures. Suppose we are interested in estimating the average number of lost customers by time T , where a customer that departs before entering service is considered lost.

# ___________________________________________________________________________________________________________________

# In[1]:


import numpy as np


#  We Assume: $\lambda: 3 + t$, [0,11]
#  
#  
#  and $ \lambda_{0} = 11$

# F ~ each customer stand in queue a "unifrom random time" between 2 times "lam_zero" and 5 times "lam_zero".

# In[2]:


T = 80

lam_zero = 11 #lambda_{0}
nl = 0 #customer who left the queue
sigma = 1/80
t = 0
na = 0
nd = 0
ss = 0
td = float('inf')
n = 0
arrivals = []
departures = []
def next_dep():
    return(max(0, np.random.normal(lam_zero, sigma)))


# In[3]:


def non_homogeneous_poission(lam_zero,t,T):

    while t<T:
        I = np.random.exponential(1/lam_zero)
        u = np.random.random()
        
        #lambda(t) = 3 + t
        if (u <= (3+t)/lam_zero):
            t += I
            return(t)
            
    
#print("Time Out, na is {}, nd is {}, nl is {}".format(na,nd,nl))


# In[4]:


ta = non_homogeneous_poission(lam_zero,t,T)


# In[5]:


nsim = 10000
people_out = []
people_arr = []
people_dep = []

for i in range(nsim):
    while (min(ta, td) < T):
        if (ta <= td):

            t = ta
            na += 1
            n += 1


            #ta += non_homogeneous_poission(lam_zero,t,T)
            ta += np.random.exponential(1/lam_zero)

            if (n==1):
                td = t + next_dep()

            #service isn't empty
            if (n > 1):
                F = np.random.uniform(2*lam_zero, 5* lam_zero)

                if F > td:
                    #Client Bored and left the queue
                    n -= 1
                    nl += 1

        else:
            t = td
            n -= 1
            nd += 1
            td += next_dep()


    while (n>0):

        t = td
        n -= 1
        nd += 1
        td = td + next_dep()
    
    people_out.append(nl)
    people_arr.append(na)
    people_dep.append(nd)


# ___________

# In[6]:


np.mean(people_arr)


# In[7]:


np.mean(people_dep)


# In[8]:


np.mean(people_out)


# _____________________________________________________________________________________________________________________________________________
