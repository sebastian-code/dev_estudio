'''
Created on 10/11/2013

@author: rootmaster
'''
def sumAll(*args):
    dat = 0
    dat += args

#print sumAll(1, 3, 5)

# t = [('a', 0), ('b', 1), ('c', 2)]
# 
# for letter, number in t:
#     print number, letter

def sumaNumeros(num): 
    numCadena=str(num) 
    result=0 
    for i in numCadena: 
        result+=int(i)
        
    return result
    
#print sumaNumeros(275)

def sort_by_length(words):
    t = []
    for word in words:
        t.append((len(word), word))
        
    t.sort(reverse=True)
        
    res = []
        
    for length, word in t:
        res.append(word)
        
    return res
