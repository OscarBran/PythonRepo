numeros = []

while True:
    entrada = input("Introduce un número complejo (ej: 3+4j) o 'fin' para terminar: ").strip()
    if entrada.lower() == 'fin':
        break
    
    try:
        complejo = complex(entrada)
        opuesto = -complejo
        conjugado = complejo.conjugate()
        tupla = (complejo, opuesto, conjugado)
        numeros.append(tupla)
        print(f"✓ Guardado\n")
    except ValueError:
        print("Formato inválido. Intenta de nuevo.\n")

print("\n" + "=" * 60)
print("NÚMEROS COMPLEJOS:")
print("=" * 60)

for complejo, opuesto, conjugado in numeros:
    print(f"Número: {complejo} | Opuesto: {opuesto} | Conjugado: {conjugado}")
