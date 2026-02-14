class Persona:
    def __init__(self, nombres, apellidos):
        self.nombres = nombres
        self.apellidos = apellidos


lista_estudiantes = []

archivo = open("estudiantes_practica.txt", "r")

for linea in archivo:
    datos = linea.strip().split(",")

    nombres = datos[0]
    apellidos = datos[1]

    estudiante = Persona(nombres, apellidos)
    lista_estudiantes.append(estudiante)

archivo.close()

for e in lista_estudiantes:
    print(e.nombres, e.apellidos)
