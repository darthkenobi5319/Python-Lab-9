# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 10:15:32 2017

@author: ZHENGHAN ZHANG
"""
import statistics

f=open('dragons.csv', 'r')
#average length of name
key=f.readline().strip().split(',')
m=0
y=[]
for i in f:
    x={}
    a=i.strip().split(',')
    for l in range(len(key)):
        k=key[l]
        v=a[l]
        x[k]=v        
    m+=len(x['name'])
    y.append(x)    
avg=m/len(y)
print('the average length of the dragon name is:', format(avg, '.2f'))

#other statistical data
age=[]
for i in range(len(y)):
    age.append(y[i]['age'])
maximum=max(age)
print('The maximum age is:',maximum)
minimum=min(age)
print('The minimum age is:',minimum)
mode=statistics.mode(age)
print('The mode is:',mode)
f.close()