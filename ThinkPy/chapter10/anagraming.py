# -*- coding:utf-8 -*-
'''
Created on 3/11/2013

@author: rootmaster
'''
def is_anagram(x , y):
    a = list(x)
    b = list(y)
    a.sort()
    b.sort()
    isSort = True
    for i in range(len(a)):
        if a[i] == b [i]:
            isSort = True
        else:
            isSort = False
    
    return isSort

pal1 = "abcdefg"
pal2 = "zlkoipñ"
pal3 = "gfzdcba"

print is_anagram(pal1, pal3)