# Programa que verifica si la entrada es de tipo entero

entrada = input("Ingresa un valor: ")

# Verificar si es de tipo entero
try:
    numero = int(entrada)
    print(numero)
except ValueError:
    pass

print("Fin de la ejecución")
