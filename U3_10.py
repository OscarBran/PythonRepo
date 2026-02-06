def crear_lista(n):
    lista = []
    print(f"\nLista {n} (escribe 'fin' para terminar):")
    while True:
        e = input("Elemento: ").strip()
        if e.lower() == 'fin': break
        if e: lista.append(e)
    return lista

def analizar(l1, l2):
    s1, s2 = set(l1), set(l2)
    return {
        'comun': s1 & s2,
        'solo_una': s1 ^ s2,
        'resto_l1': s1 - s2,
        'resto_l2': s2 - s1
    }

print("COMPARADOR DE LISTAS\n")
l1 = crear_lista(1)
l2 = crear_lista(2)
r = analizar(l1, l2)

print(f"\n{'='*40}")
print(f"1. En ambas: {len(r['comun'])} - {r['comun']}")
print(f"2. Solo en una: {len(r['solo_una'])} - {r['solo_una']}")
print(f"3. Solo en Lista1: {len(r['resto_l1'])} - {r['resto_l1']}")
print(f"4. Solo en Lista2: {len(r['resto_l2'])} - {r['resto_l2']}")
print(f"{'='*40}")
