'''
Created on 8/09/2013
@author: Sebastian Reyes Espinosa
@version: 0.1
'''

texto_plano = ''
_Equivaliencias = [('M', 1000),
                   ('D', 500),
                   ('C', 100),
                   ('L', 50),
                   ('X', 10),
                   ('V', 5),
                   ('I', 1),
                   ('', 0)
                   ]
texto_plano = 'MMMCMIX'


def Calcula_valor(texto_a_buscar):
    for romano, decimal in _Equivaliencias:
        if romano == texto_a_buscar:
            break
    return decimal


def RomanoADecimal(texto):
    _procesado = 0
    valor_anterior = 0
    for caracter in texto:
        valor = Calcula_valor(caracter)
        if valor > valor_anterior:
            _procesado = _procesado + valor - (valor_anterior * 2)

        else:
            _procesado = _procesado + valor

        print(valor, valor_anterior, _procesado)
        valor_anterior = valor

    return _procesado

print("Resultado ->", RomanoADecimal(texto_plano))
