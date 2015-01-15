'''
Created on 13/10/2013
@summary: Aplicacion creada a manera de ejercicio para afianzar conocimientos.
@author: Sebastian Reyes Espinosa.
@version: v1
'''
def print_title():
    secuence = '----'
    print '+', secuence, '+', secuence, '+'

def print_row():        
    secuence = '    '
    print '|', secuence, '|', secuence, '|'
    
def print_grid():
    print_title()
    print_row()
    print_row()
    print_row()
    print_row()
    print_title()
    print_row()
    print_row()
    print_row()
    print_row()
    print_title()

print_grid()