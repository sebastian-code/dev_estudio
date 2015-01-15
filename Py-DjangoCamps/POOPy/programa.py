class Persona:
	def __init__(self):
		self.documento = int(input('Documento: '))
		self.nombre = input('Nombre: ')
		self.edad = int(input('Edad: '))

	# dict() -> __setitem__ y __getitem__
	def __setitem__(self, name, value): # instancia['atributo'] = 'valor'
		self.__setattr__(name, value) # instancia.atributo = 'valor'

	def __getitem__(self, name):
		return self.__getattribute__(name) # instancia.atributo

	def obtener_datos(self):
		print('Documento: %d \nNombre: %s \nEdad: %d' % (self.documento, self.nombre, self.edad) )

class Estudiante(Persona):
	def __init__(self):
		super(Estudiante, self).__init__()
		self.colegio = input('Colegio: ')

estudiante = Estudiante()
estudiante.obtener_datos()
estudiante['documento'] = 123
estudiante['nuevo'] = True
estudiante.obtener_datos()
print(estudiante.nuevo)
print(estudiante['nombre'])