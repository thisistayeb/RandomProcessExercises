#!/usr/bin/env python
# coding: utf-8



NAME = '1-B'


import numpy as np
import random
from math import sqrt
import nepzeb


n = 1000

mu = 1/4 #mean not rate

t = 0

ni = n//2

T = 30

ar = sorted(np.random.exponential(mu,10000))[2000]
br = sorted(np.random.exponential(mu,10000))[8000]

pr = 0.9


ns = ni
nh = n - ns
nd = 0
nu = 0
nr = 0
nu = 0

society = ['sick' for i in range(ns)] + ['healthy' for j in range(nh)]
random.shuffle(society)


tu_list = []



recoverd = np.zeros(n)

def NewCase_occur():
    
    fall_ill_chance = []
    for every_person in range(len(society)):
        
        
        if (society[every_person] == 'healthy'):
                   
            fall_ill_chance.append(np.random.exponential(mu))

        #sick or dead
        else:
            fall_ill_chance.append(float('inf'))

    return(min(fall_ill_chance),fall_ill_chance.index(min(fall_ill_chance)))



def NewCase(tt, index):
    global t
    global ns
    global nh
    
    t += tt
    ns += 1
    nh -= 1
    
    society[index] = 'sick'


def tr_occur():
    
    v = []
    for ill in range(len(society)):
        if society[ill] == 'sick':
            v.append(np.random.uniform(ar,br))

        else:
            v.append(float('inf'))
    return(min(v),v.index(min(v)))


def tr(tt,index):
    
    global nd
    global nh
    global nr
    global nu
    global ns
    global t
    
    t += tt
    
    if random.random() < pr:
        
        nh += 1
        nr += 1
        nu += 1
        ns -= 1
        
        tu_list.append( (t+(np.random.uniform(0.1,1))) )

        society[index] = 'healthy'
        recoverd[index] = 1
        
    else:
        
        nd += 1
        ns -= 1
        society[index] = 'dead'



fileName = NAME + '-n:{},ni:{},mu:{},ar:{},br:{},pr:{}'.format(n,ni,mu,ar,br,pr)




f = open('{}.csv'.format(fileName), 'w')
f.write('Event,Time,Healthy People,Ill People,Recoverd people,RIP,\n')



while (t < T):
    
    
    #check if one or more people's convalescence time have been over
    tu_list.sort()
    if (len(tu_list) > 0):
        if (tu_list[0] <= t):
            count = 0
            for i in range(len(tu_list)):
                if tu_list[i] <= t:
                    count += 1
            nu -= count
            tu_list = tu_list[count:]
            

    X = NewCase_occur()
    Y = tr_occur()
    
    
    #check if both are inf then Break
    if X[0] == Y[0] == float('inf'):
        break
    
    if X[0] <= Y[0]:
        NewCase(X[0],X[1])
        f.write('[sick],{},{},{},{},{}, \n'.format(t,nh,ns,int(sum(recoverd)),nd))
        
    if Y[0] < X[0]:
        tr(Y[0], Y[1])
        f.write('[heal/dead],{},{},{},{},{}, \n'.format(t,nh,ns,int(sum(recoverd)),nd))
    
f.close()


nepzeb.plotter('{}.csv'.format(fileName))





