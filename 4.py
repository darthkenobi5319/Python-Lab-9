# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 11:14:27 2017

@author: ZHENGHAN ZHANG
"""

f=open('dragons.csv', 'r')
key=f.readline().strip().split(',')
y=[]
dragon={}
for i in f:
    x={}
    a=i.strip().split(',')
    for l in range(len(key)):
        k=key[l]
        v=a[l]
        x[k]=v        
    y.append(x)    
    breed=x['breed']
    if breed not in dragon:
        dragon[breed]=[]
    dragon[breed].append(x)
f.close()
'''
This should look like this:
breed1--[d1,d14,d23]
breed2--[d5,d10,d22]
......
......
......    
'''
f=open('newdragons.csv','w')
print('name','age','size','color','breed',sep=',',file=f)
for i in dragon:
    for j in dragon[i]:
        print(j['name'],j['age'],j['size'],j['color'],j['breed'],sep=',',file=f)
f.close()