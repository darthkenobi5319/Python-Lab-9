# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 11:40:49 2017

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
    age=x['age']
    if age not in dragon:
        dragon[age]=[]
    dragon[age].append(x)
f.close()
x=[]
for i in dragon:
    #INTEGER WARNING!
    #RETARD ALERT!
    x.append(int(i))
    x.sort()

f=open('newdragons.csv','w')
print('name','age','size','color','breed',sep=',',file=f)
for i in x:
    for j in dragon[str(i)]:
        print(j['name'],j['age'],j['size'],j['color'],j['breed'],sep=',',file=f)
f.close()