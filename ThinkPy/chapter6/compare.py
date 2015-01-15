'''
Created on 19/10/2013

@author: rootmaster
'''

'''
Function compares x & y and returns a value in correpondence
according to the following sentences.
1 if x > y, 0 if x == y, and -1 if x < y

'''

def compare(x, y):
    if x > y:
        return 1
    if x == y:
        return 0
    if x < y:
        return -1

def factorial (n):
    if not isinstance(n, int):
        print 'Factorial is only defined for integers.'
        return None
    
    elif n < 0:
        print 'Factorial is not defined for negative integers.'
        return None
    
    elif n == 0:
        return 1
    
    else:
        return n * factorial(n-1)

    
print factorial(-5)
