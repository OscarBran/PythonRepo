n = int(input("Ingresa el número de filas: "))
m = int(input("Ingresa el número de columnas: "))

matriz = []
for i in range(n):
    fila = []
    for j in range(m):
        valor = float(input(f"Elemento [{i}][{j}]: "))
        fila.append(valor)
    matriz.append(fila)

print("\nMatriz (vertical):")
for j in range(m):
    for i in range(n):
        print(matriz[i][j], end=" ")
    print()

print("\nSuma de columnas:")
for j in range(m):
    suma = sum(matriz[i][j] for i in range(n))
    print(f"Columna {j+1}: {suma}")
    if suma > 50:
        print(f"La columna {j+1} ha excedido la cantidad")
