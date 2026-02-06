octantes = {(1,1,1):1, (-1,1,1):2, (-1,-1,1):3, (1,-1,1):4, 
            (1,1,-1):5, (-1,1,-1):6, (-1,-1,-1):7, (1,-1,-1):8}

n = int(input("¿Cuántos puntos deseas introducir? "))
puntos = []

for i in range(n):
    x = float(input(f"Punto {i+1} - x: "))
    y = float(input(f"Punto {i+1} - y: "))
    z = float(input(f"Punto {i+1} - z: "))
    
    signo = (1 if x > 0 else -1, 1 if y > 0 else -1, 1 if z > 0 else -1)
    octante = octantes.get(signo, None)
    puntos.append((x, y, z, octante))

print("\n" + "=" * 50)
for x, y, z, octante in puntos:
    print(f"El punto ({x}, {y}, {z}) pertenece al octante {octante}")
