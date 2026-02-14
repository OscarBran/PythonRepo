class Usuario:
    def __init__(self, id_usuario, nombres, apellidos, facultad):
        self.id_usuario = id_usuario
        self.nombres = nombres
        self.apellidos = apellidos
        self.facultad = facultad


class Estudiante(Usuario):
    pass


class Profesor(Usuario):
    pass


def guardar_usuario(usuario, tipo):
    archivo = open("usuarios.csv", "a")
    linea = tipo + "," + usuario.id_usuario + "," + usuario.nombres + "," + usuario.apellidos + "," + usuario.facultad + "\n"
    archivo.write(linea)
    archivo.close()


# Crear usuarios
id_usuario = input("Ingrese carnet o usuario: ")
nombres = input("Ingrese nombres: ")
apellidos = input("Ingrese apellidos: ")
facultad = input("Ingrese facultad: ")

tipo = input("¿Es estudiante o profesor?: ")

if tipo == "estudiante":
    u = Estudiante(id_usuario, nombres, apellidos, facultad)
    guardar_usuario(u, "estudiante")

elif tipo == "profesor":
    u = Profesor(id_usuario, nombres, apellidos, facultad)
    guardar_usuario(u, "profesor")

else:
    print("Tipo no válido")

print("Usuario guardado en archivo.")
