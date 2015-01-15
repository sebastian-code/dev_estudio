'''
Created on 11/11/2013
@author: rootmaster
'''
import os

def buscarDup(dirS):
    dato = []
    try:
        for item in os.listdir(dirS):
            path = os.path.join(dirS, item)
            if os.path.isfile(path):
                dato.append(path)
            
            else:
                pass

    except:
        return 'Monda, ocurrio un error y no tengo ni puta idea que fue lo que paso'