# Números
	# Enteros
	# Flotantes

# Booleanos

# Secuencias
	# Listas
	# Tuplas
	# Cadenas

# Mapeados
	# Diccionarios

# Type Casting

#······································

# Enteros
entero = 12
entero_negativo = -12
print(type(entero_negativo))
print(type(type))

# Flotantes
flotantes = 12.34
print(type(flotantes))

# Booleanos
booleano1 = True
booleano2 = False
print(type(booleano1))
print(type(entero == flotantes))

# Listas
lista = ['Hola', 12, 12.34, True, ['hola', False]]
lista2 = [False, 45.34, 12, 'cadena']
print(type(lista))
print(lista + lista2)
print('hola' in lista)
print('Hola' not in lista)
print(lista[-3])
print(lista[1:5:3])
print(lista[1:-1:2])

# Tuplas
tupla = ('cadena',)
tupla2 = (False, 34, 'cadena2')
print(type(tupla))
print(tupla + tupla2)
print('cadena' in tupla)
print('cadena' not in tupla)
print(tupla[1:-1:2])

# lista[0] = True
# print(lista)
# tupla[0] = False
# print(tupla)

lista.append(456)
print(lista)

# Cadenas
cadena = 'Hola Mundo!'
cadena2 = 'Otro valor'
print(type(cadena))
print(cadena + cadena2)
print(cadena * 4)
print('a' in cadena)
print('a' not in cadena)
print(cadena[1:5:2])

# Diccionarios
diccionario = {'clave':'valor', True:False, 12:45}
diccionario2 = {45:21}
print(type(diccionario))

print(diccionario.__dir__())
print(diccionario.items())
diccionario['nueva'] = 123
print(diccionario.keys())



print(cadena)
print(cadena.find('a'))
print(cadena.startswith('a'))
print(cadena.endswith('a'))
print(cadena.__dir__())
print(cadena.upper())



print(type(lista))
print(list(tupla))
print(tuple(lista))
print(tuple(cadena))
print(int(flotantes))
print(float(entero))

lista_dict = ([True, False], (12, 'cadena'))
print(dict(lista_dict))