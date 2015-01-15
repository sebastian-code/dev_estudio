# Agenda telefónica
# v0.1 por Jose Vicente Carratala

import modulos

modulos.bienvenidos()

opcion = input("> ")

print("Has seleccionado la opción", opcion)

if opcion == "1":
    modulos.escribir()
elif opcion == "2":
    print("Dime cuantos registros quieres ver:")
    registros = input("> ")
    registrosnumero = int(registros)
    modulos.listar((registrosnumero + 1))
else:
    modulos.mierror()
