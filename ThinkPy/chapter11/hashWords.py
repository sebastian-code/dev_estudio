'''
Created on 3/11/2013

@author: rootmaster
'''
def hashingList():
    d = dict()
    i = 0
    arch = open('words.txt')
    for line in arch:
        d[line] = i
        i += 1

    print d

def histogram1(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1

    return d

def histogram(s):
    d = dict()

    return d

#print histogram('Brontosauropouduolipiduos')

'''
A solution to keep track of values that have already been computed is storing them in a dictionary.
A previously computed value that is stored for later use is called a memo.
Each time a calculation is made, the function searchs for the proper memo, if it's there, it returns it,
if not, the function calcultes it, stores it and returns it.
Here is an implementation of fibonacci using memos:
'''
k = {0:0, 1:1}


def calc_Fibonacci(n):
    if n in k:
        return k[n]

    else:
        res = calc_Fibonacci(n - 1) + calc_Fibonacci(n - 2)
        k[n] = res
        return res
