nombre1 = input("Dime el nombre del primer usuario ")
edad1 = input("Dime su edad ")

nombre2 = input("Dime el nombre del segundo usuario ")
edad2 = input("Dime su edad ")

nombre3 = input("Dime el nombre del tercer usuario ")
edad3 = input("Dime su edad ")

print("Nombre \t\t Edad")
print(nombre1,"\t",edad1)
print(nombre2,"\t\t",edad2)
print(nombre3,"\t\t",edad3)

edad1b = int(edad1)
edad2b = int(edad2)
edad3b = int(edad3)

suma = edad1b + edad2b + edad3b
promedio = suma/3



print("Y el promedio de las edades de los usuarios es:",promedio)
