'''
Created on 8/09/2013
@author: Sebastian Reyes Espinosa
@contact: sebaslander@yahoo.es
@version: 0.1
'''


def transNumArabigos(numero):
    '''
    @requires: El valor asignado a la variable numero debe ser del tipo String.
    @return: La transformacion del String numero en codificacion romana a
    codificacion decimal arabiga.
    '''
    resultado = 0
    val_ant = 0
    val_act = 0
    # Acudo al uso de un diccionario porque facilita la forma en que se
    # comparan valores.
    valores = {'M': 1000,
               'D': 500,
               'C': 100,
               'L': 50,
               'X': 10,
               'V': 5,
               'I': 1
               }
    if len(numero) > 0:
        val_ant = numero[0]  # Con este condicional asigno el primer valor
                             # de numero.

    for letra in numero:
        '''Recorro el String numero a lo largo de todos sus componentes. Si la
        letra se encuentra en el diccionario asigno su valor a val_act de lo
        contrario, la letra suministrada es invalida.'''
        if letra in valores:
            val_act = valores[letra]

        else:
            print('Valor suministrado invalido:', letra)
            return 'NaN'
        # Si el valor anterior es mayor o igual que el valor actual
        # se suman, de lo contrario se restan
        if val_ant >= val_act:
            resultado += val_act

        else:
            resultado += val_act - (2 * val_ant)
        val_ant = val_act

    return resultado

# Se usa upper() para garantizar la lectura del valor asignado gracias a
# estar en mayusculas
numero = raw_input("Introduzca un Numero Romano: ").upper()
print("Numero Arabigo:", transNumArabigos(numero))
