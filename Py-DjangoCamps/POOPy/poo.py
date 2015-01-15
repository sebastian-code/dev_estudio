##### Clases
# class Persona:
# 	def inicializar(self, nombre):
# 		self.nombre = nombre
# 		edad = 12

# 	def obtener_nombre(self):
# 		print(self.nombre)

# persona1 = Persona()
# persona1.inicializar('Carlos')
# persona1.obtener_nombre()

# persona2 = Persona()
# persona2.inicializar('Samuel')
# persona2.obtener_nombre()


##### Estructuras
# class Entrada:
# 	pass

# nueva_entrada = Entrada()
# nueva_entrada.nombre = 'Bienvenidos'
# nueva_entrada.fecha = '06-03-2013'

# otra_entrada = Entrada()
# otra_entrada.nombre = 'Otra entrada'
# otra_entrada.fecha = '07-03-2013'
# print(nueva_entrada.nombre)
# print(otra_entrada.nombre)


##### Modificar atributos
# class Animal:
# 	def inicializar(self, nombre, tipo):
# 		self.nombre = nombre
# 		self.tipo = tipo

# animal = Animal()
# animal.inicializar('Elefante', 'Mamifero')
# animal.tipo = 'Anfibio'
# animal.edad = 123
# print(animal.tipo)
# print(animal.edad)


##### Herencia
# class Persona:
# 	def hablar(self, texto):
# 		print(texto)

# 	def decir_algo(self):
# 		self.hablar('Decir algo')

# class Juan(Persona):
# 	def decir_hola(self):
# 		self.hablar('Hola Mundo!')

# 	def decir_algo(self):
# 		super(Juan, self).decir_algo()

# juan = Juan()
# juan.decir_hola()
# juan.decir_algo()


##### Polimorfismo
# class ClaseA:
# 	def inicializar(self):
# 		self.numero = 1

# 	def avanzar(self):
# 		self.numero += 1
# 		print(self.numero)

# class ClaseB:
# 	def inicializar(self):
# 		self.numero = 3

# 	def avanzar(self):
# 		self.numero += 1
# 		print(self.numero)

# instanciaA = ClaseA()
# instanciaA.inicializar()

# instanciaB = ClaseB()
# instanciaB.inicializar()

# def caminar(objeto):
# 	objeto.avanzar()

# caminar(instanciaA)
# caminar(instanciaB)


##### Name Mangling
# class Ejemplo:
# 	def inicializar(self):
# 		self.__numero = 5 # _Ejemplo__numero - _OtraClase__numero

# 	def obtener_numero(self): # _Ejemplo__obtener_numero()
# 		print(self.__numero)

# ejemplo = Ejemplo()
# ejemplo.inicializar()
# ejemplo.obtener_numero()
# print(ejemplo._Ejemplo__numero)


##### Metodos Magicos
class Animal:
	def __init__(self, nombre): # NO ES CONSTRUCTOR
		self.nombre = nombre

	# def __new__()
	# def __add__(x) -> Animal + 12
	# def __call__(x, y) -> Animal(12, 34)
	# def __eq__(x) -> Animal == OtraClase

	def obtener_nombre(self):
		print(self.nombre)

animal = Animal('Elefante')
# animal.inicializar('Elefante')
animal.obtener_nombre()

# int()
# str()
# list()
# dict()
# bool()