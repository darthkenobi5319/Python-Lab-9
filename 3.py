# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 10:52:46 2017

@author: ZHENGHAN ZHANG
"""

f=open('dragons.csv', 'r')
key=f.readline().strip().split(',')
y=[]
for i in f:
    x={}
    a=i.strip().split(',')
    for l in range(len(key)):
        k=key[l]
        v=a[l]
        x[k]=v        
    y.append(x)
#importantttttttttt!!!!!!!!!!!!!!!!!!!!!!!
counts={}    
for i in range(len(y)):
    if y[i]['breed'] not in counts:
        counts[y[i]['breed']]=0
    counts[y[i]['breed']] += 1
for i in counts:
    print('The number of dragons in breed',i,'is',counts[i])
    
#find the largest size first, and then identify its parameters
index={}
m=0
#giving the netire dragon dict as a value for index dict avoids the problem of having to find the index for the largest dragon
for i in range(len(y)):
    if y[i]['breed'] not in index:
        index[y[i]['breed']]=y[i]
    if int(y[i]['size'])>=int(index[y[i]['breed']]['size']):
        index[y[i]['breed']]=y[i]
for i in index:
    print('The largest dragon in breed',i,'is',index[i])       
    
f.close()      