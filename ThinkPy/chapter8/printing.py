'''
Created on 20/10/2013

@author: rootmaster
'''
prefixes = 'JKLMNOPQ'
suffix = 'ack'

for letter in prefixes:
    if letter == "O" or letter == "Q":
        print(letter + "u" + suffix)
    else:
        print(letter + suffix)
