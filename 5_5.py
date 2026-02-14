class Usuario:
    def __init__(self, usuario, password, saldo=0):
        self._usuario = usuario
        self._password = password
        self._saldo = saldo

    def abonar(self, monto):
        self._saldo += monto

    def retirar(self, monto):
        if monto <= self._saldo:
            self._saldo -= monto
            return True
        return False


def cargar():
    lista = []
    try:
        archivo = open("usuarios.csv", "r")
        for linea in archivo:
            u, p, s = linea.strip().split(",")
            lista.append(Usuario(u, p, float(s)))
        archivo.close()
    except:
        pass
    return lista


def guardar(lista):
    archivo = open("usuarios.csv", "w")
    for u in lista:
        archivo.write(u._usuario + "," + u._password + "," + str(u._saldo) + "\n")
    archivo.close()


usuarios = cargar()

print("1. Registro")
print("2. Login")
op = input("Opción: ")

if op == "1":
    u = input("Usuario: ")
    p = input("Password: ")
    usuarios.append(Usuario(u, p))
    guardar(usuarios)

elif op == "2":
    u = input("Usuario: ")
    p = input("Password: ")

    actual = None
    for x in usuarios:
        if x._usuario == u and x._password == p:
            actual = x

    if actual:
        print("1. Abonar")
        print("2. Retirar")
        op2 = input("Opción: ")
        monto = float(input("Monto: "))

        if op2 == "1":
            actual.abonar(monto)
        elif op2 == "2":
            if not actual.retirar(monto):
                print("Fondos insuficientes")

        guardar(usuarios)
