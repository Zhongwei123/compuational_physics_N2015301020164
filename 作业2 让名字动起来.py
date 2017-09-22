# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 15:10:33 2017

@author: 钟伟
"""

import sys, time

def interface_show(**kwargs):
    lineTmpla = ' '*5 + kwargs['title'] + kwargs['artist'] + kwargs['rate'] + " %-3s"
    print(time_remain(lineTmpla, kwargs['minutes'])),

def time_remain(lineTmpla, mins):
    count = 0 
    while (count < mins):
        count += 1
        n = mins - count
        time.sleep(1)
        sys.stdout.write("\r" + lineTmpla %(n),)
        sys.stdout.flush()
        if not n:
            return '开始无节操表演'

interface_show(title="感谢观看", artist="这么矬的", rate="大boss来了", minutes=6)

import time
a1=[" ","#","#","#"," ","#","#","#"," "]
a2=[" ","#"," ","#"," ","#"," ","#"," "]
a3=[" ","#"," ","#"," ","#"," ","#"," "]
a4=["{","——","——","——","——","——","——","——","}"]
a5=["#","  ","  ","  ","  ","  ","  ","  "," #"]
a6=["#","  ","  "," @ ","  ","@  ","  ","  "," #"]
a7=[" #","  ","  ","  "," ** ","  ","  ","  ","# "]
a8=["  #"," ","  "," ( "," *** "," ) ","  ","  "," #"]
a9=["  "," ——","—— ","—— ","- ","——","——","——","——"]
 
t=0
while t<10:
    
    for i1 in a1:
        print(i1,end='')
    print("\n")
    for i2 in a2:
        print(i2,end='')
    print("\n")
    for i3 in a3:
        print(i3,end='')
    print("\n")
    for i4 in a4:
        print(i4,end='')
    print("\n")
    for i5 in a5:
        print(i5,end='')
    print("\n")
    for i6 in a6:
        print(i6,end='')
    print("\n")
    for i7 in a7:
        print(i7,end='')
    print("\n")
    for i8 in a8:
        print(i8,end='')
    print("\n")
    for i9 in a9:
        print(i9,end='')
    print("\n")
    for j in (a1,a2,a3,a4,a5,a6,a7,a8,a9):
        j.insert(0,"   ")
    time.sleep(1)
    t+=1
    print(" ")
    
