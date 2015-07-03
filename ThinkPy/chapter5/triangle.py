'''
Created on 16/10/2013

@author: rootmaster
'''
def is_triangle(a, b, c):
    if a > b and a > c:
        if b + c > a:
            print ("Yes!")

        else:
            print ("No!")

    elif b > a and b > c:
        if a + c > b:
            print ("Yes!")

        else:
            print ("No!")

    elif c > a and c > b:
        if a + b > c:
            print ("Yes!")

        else:
            print ("No!")

def call_it():
    a = int(input("Primer lado"))
    b = int(input("Segundo lado"))
    c = int(input("Tercer lado"))
    is_triangle(a, b, c)

call_it()
