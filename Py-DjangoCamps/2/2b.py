agenda = open("agendatelefonica.csv",'a')

##print(agenda.read())
##agenda.truncate()

nombre = input("Introduce el nombre de contacto: ")
telefono = input("Introduce su teléfono: ")

print("Se ha guardado en la agenda el contacto: ",nombre,"con el número de teléfono",telefono)

agenda.write(nombre)
agenda.write(",")
agenda.write(telefono)
agenda.write(",")
agenda.write("\n")


agenda.close()
