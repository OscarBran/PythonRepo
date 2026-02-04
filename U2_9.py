# Ejercicio 9

entrada = input("Ingresa un valor: ")

# Verificar si es de tipo entero
try:
    numero = int(entrada)
    print(numero)
except ValueError:
    pass

print("Fin de la ejecución")

