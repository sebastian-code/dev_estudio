datos = {} # Diccionario que contendra toda la informacion que el usuario ingrese

while True: # Bucle "infinito" para pedir varios datos al usuario, cantidad indefinida de veces
	nombre = input('Nombre: ') # Pedimos en nombre, de tipo str
	edad = int(input('Edad: ')) # Pedimos la edad y la volvemos a entero (int)
	gustos = input('Gustos (separados por coma): ') # Pedimos los gustos separados por coma para volverlo una lista despues
	datos[nombre] = (edad, gustos.split(',')) # Almacenamos el nuevo valor en el diccionario datos y volvemos los gustos una lista, separandolos por coma
	opcion = input('\nSalir? [s/n]: ') # Preguntamos si el usuario quiere salir
	if opcion.lower() == 's': # Volvemos lo que haya introducido el usuario a minuscula y preguntamos si es 's' para salir
		break # Rompemos el bucle para terminar su ejecución

for item in datos.items(): # Recorremos el diccionario datos obteniendo sus .items() para así poder acceder a sus elementos como si fueran tuplas
	print('%s tiene %d años y sus gustos son: %s' % (item[0], item[1][0], ','.join(item[1][-1]))) # Imprimimos los datos del usuario, convirtiendo los gustos en un string separando con una coma sus elementos mediante el metodo .join() de 'str'