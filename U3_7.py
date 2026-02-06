dic1 = {"A": 1, "B": 2}
dic2 = {"A": 3}

resultado = {}

for clave, valor in dic1.items():
    resultado[clave] = [valor]

for clave, valor in dic2.items():
    if clave in resultado:
        resultado[clave].append(valor)
    else:
        resultado[clave] = [valor]

print(resultado)
