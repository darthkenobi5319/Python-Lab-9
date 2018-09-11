# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 09:54:10 2017

@author: ZHENGHAN ZHANG
"""

#THIS block of codes is the basis for all else to come
#It gives a list of dragons, expressed by dictionaries
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
print(y)
f.close()    