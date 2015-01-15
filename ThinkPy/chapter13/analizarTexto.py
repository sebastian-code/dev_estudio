'''
Created on 10/11/2013
# -*- coding:utf-8 -*-
@note:  Se puede especificar tipo de encoding con la finalidad de no eliminar caracteres acentuados,
        al no haberse hecho, se descomenta en la funcion analizeLine() para eliminarse.
@author: rootmaster
'''
import string

def analizeText(text):
    data = open(text, 'r')
    arch = data.read()
    arch = arch.replace('-', ' ')
    histograma = {}
    for word in arch.split():
        word = word.strip(string.whitespace + string.punctuation)
        #elimina caracteres del tipo Non-ASCII de cada palabra
        word = "".join([x for x in word if ord(x)<128]) 
        word = word.lower()
        histograma[word] = histograma.get(word, 0) + 1
    
    cont = sum(histograma.values())
    masComun = []
    for key, value in histograma.items():
        masComun.append((value, key))
    
    masComun.sort()
    masComun.reverse()
    
    masComunes = []
    for i in range(0, 10):
        masComunes.append(masComun[i])
    
    data.close()
        
    print 'Cantidad de palabras en el texto:',cont
    print 'Cantidad de palabras distintas usadas en el texto:',len(histograma)
    print 'Las 25 palabras mas comunes usadas en el texto:',masComunes
    print 'Palabras mas comunes usadas en el texto:',masComun
#    print histograma

# Por algun motivo por determinar, el analisis del archivo genera un error de repeticion de la instruccion 'print histograma'
# limpiando la consola y comenzando de nuevo, aunque ofrece el resultado igual.
# analizeText('emma.txt')
analizeText('textoPrueba.txt')