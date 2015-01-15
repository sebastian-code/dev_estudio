# -*- coding:utf-8 -*-

'''
Created on 14/10/2013

@author: rootmaster
'''
def check_fermat(a, b, c, n):
    if a**n + b**n == c**n:
        print 'Holy smokes, Fermat was wrong!'
    
    else:
        print 'No, that doesn’t work.'

def call_fermat():
    a = int(raw_input('Valor de a: '))
    b = int(raw_input('Valor de b: '))
    c = int(raw_input('Valor de c: '))
    n = int(raw_input('Valor de n: '))
    check_fermat(a, b, c, n)

call_fermat()