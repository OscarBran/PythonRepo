class Vehiculo:
    def __init__(self, marca, modelo, tarifa_diaria):
        self.marca = marca
        self.modelo = modelo
        self.tarifa_diaria = tarifa_diaria

    def imprimir_info(self):
        print("Marca:", self.marca)
        print("Modelo:", self.modelo)
        print("Tarifa diaria:", self.tarifa_diaria)


class Auto(Vehiculo):
    def __init__(self, marca, modelo, tarifa_diaria, puertas):
        super().__init__(marca, modelo, tarifa_diaria)
        self.puertas = puertas

    def calcular_alquiler(self, dias):
        return self.tarifa_diaria * dias


class Camioneta(Vehiculo):
    def __init__(self, marca, modelo, tarifa_diaria):
        super().__init__(marca, modelo, tarifa_diaria)

    def calcular_alquiler(self, dias):
        return (self.tarifa_diaria * dias) + 10


def guardar_vehiculo(tipo, vehiculo):
    archivo = open("vehiculos.csv", "a")

    if tipo == "auto":
        linea = "auto," + vehiculo.marca + "," + vehiculo.modelo + "," + str(vehiculo.tarifa_diaria) + "," + str(vehiculo.puertas) + "\n"
    else:
        linea = "camioneta," + vehiculo.marca + "," + vehiculo.modelo + "," + str(vehiculo.tarifa_diaria) + "\n"

    archivo.write(linea)
    archivo.close()


while True:
    print("\n1. Registrar Auto")
    print("2. Registrar Camioneta")
    print("3. Calcular alquiler")
    print("4. Salir")

    op = input("Seleccione: ")

    if op == "1":
        marca = input("Marca: ")
        modelo = input("Modelo: ")
        tarifa = float(input("Tarifa diaria: "))
        puertas = int(input("Puertas: "))

        auto = Auto(marca, modelo, tarifa, puertas)
        guardar_vehiculo("auto", auto)
        print("Auto guardado")

    elif op == "2":
        marca = input("Marca: ")
        modelo = input("Modelo: ")
        tarifa = float(input("Tarifa diaria: "))

        camioneta = Camioneta(marca, modelo, tarifa)
        guardar_vehiculo("camioneta", camioneta)
        print("Camioneta guardada")

    elif op == "3":
        tipo = input("Tipo (auto/camioneta): ")
        dias = int(input("Días de alquiler: "))

        if tipo == "auto":
            tarifa = float(input("Tarifa diaria: "))
            auto = Auto("temp", "temp", tarifa, 4)
            print("Costo:", auto.calcular_alquiler(dias))

        elif tipo == "camioneta":
            tarifa = float(input("Tarifa diaria: "))
            camioneta = Camioneta("temp", "temp", tarifa)
            print("Costo:", camioneta.calcular_alquiler(dias))

    elif op == "4":
        break
