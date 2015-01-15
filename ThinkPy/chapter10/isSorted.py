'''
Created on 3/11/2013

@author: rootmaster
'''
def is_sorted(t):
    isSorted = True
    sor = t[:]
    sor.sort()
    for i in range(len(t)):
        if t[i] == sor[i]:
            isSorted = True
            
        else:
            isSorted = False
        
    return isSorted

lista = [1, 2, 3, 4, 5, 6]
list2 = [3, 1, 7, 4, 2, 1]
list3 = [4, 4, 9, 12, 15]

print is_sorted(list2)