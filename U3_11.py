palabras = []

while True:
    palabra = input("Introduce una palabra (vacío para terminar): ")
    if not palabra:
        break
    palabras.append(palabra)

palabras_tupla = tuple(palabras)

if len(palabras_tupla) >= 2:
    primera, *_, ultima = palabras_tupla
    print(f"\nPalabras guardadas: {palabras_tupla}")
    print(f"Primera palabra: {primera}")
    print(f"Última palabra: {ultima}")
elif len(palabras_tupla) == 1:
    primera, = palabras_tupla
    print(f"\nPalabras guardadas: {palabras_tupla}")
    print(f"Solo hay una palabra: {primera}")
else:
    print("No se ingresó ninguna palabra.")
