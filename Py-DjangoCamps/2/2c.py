agenda = open("agendatelefonica.csv")

##print(agenda.read())


##for i in range(1,25):
##    print(agenda.readline())

numero = 0

while numero < 25:
    print(agenda.readline())
    numero = numero + 1

print("Ya he terminado de leer el archivo")
