n = int(input("Ingresa la dimensión de la matriz: "))

matriz = []
for i in range(n):
    fila = []
    for j in range(n):
        if i == j:
            fila.append(1)
        else:
            fila.append(0)
    matriz.append(fila)

print("\nMatriz identidad:")
for fila in matriz:
    print(fila)
