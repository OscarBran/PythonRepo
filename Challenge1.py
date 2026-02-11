import random
import os
import time

# ---------------
# GENERADOR DE MINAS (TEMPLATE)     
# -----------------
def generar_minas(filas_cols, num_minas):
    tablero = [True] * num_minas + [False] * (filas_cols ** 2 - num_minas)
    random.shuffle(tablero)
    return [tablero[i:i + filas_cols] for i in range(0, len(tablero), filas_cols)]

# -----------
# Funciones
# ---------
def limpiar():
    os.system("cls" if os.name == "nt" else "clear")

def crear_tablero_visible(n):
    return [["." for _ in range(n)] for _ in range(n)]

def imprimir_tablero(tablero):
    n = len(tablero)

    print("   ", end="")
    for i in range(1, n + 1):
        print(f"{i:2}", end=" ")
    print()

    for i in range(n):
        letra = chr(65 + i)
        print(f"{letra} ", end=" ")
        for j in range(n):
            print(f"{tablero[i][j]:2}", end=" ")
        print()

def parsear_coord(coord, n):
    try:
        fila = ord(coord[0].upper()) - 65
        col = int(coord[1:]) - 1
        if 0 <= fila < n and 0 <= col < n:
            return fila, col
    except:
        pass
    return None

# --------
# Estructura
# -------
def contar_minas(tablero_minas, f, c):
    n = len(tablero_minas)
    total = 0

    for i in range(f - 1, f + 2):
        for j in range(c - 1, c + 2):
            if 0 <= i < n and 0 <= j < n:
                if tablero_minas[i][j]:
                    total += 1

    return total

def revelar_casillas(tablero_minas, visible, f, c):
    n = len(tablero_minas)

    if not (0 <= f < n and 0 <= c < n):
        return

    if visible[f][c] != ".":
        return

    minas = contar_minas(tablero_minas, f, c)

    if minas > 0:
        visible[f][c] = str(minas)
        return

    visible[f][c] = " "

    for i in range(f - 1, f + 2):
        for j in range(c - 1, c + 2):
            if i != f or j != c:
                revelar_casillas(tablero_minas, visible, i, j)

def revelar_minas(tablero_minas, visible):
    n = len(tablero_minas)
    for i in range(n):
        for j in range(n):
            if tablero_minas[i][j]:
                visible[i][j] = "*"

def victoria(tablero_minas, visible):
    n = len(tablero_minas)
    for i in range(n):
        for j in range(n):
            if not tablero_minas[i][j] and visible[i][j] == ".":
                return False
    return True

# ------------
# Asegurar que la primera jugada no sea mina
# ------------
def asegurar_primera(tablero_minas, f, c, num_minas):
    n = len(tablero_minas)

    if not tablero_minas[f][c]:
        return tablero_minas

    libres = [(i, j) for i in range(n) for j in range(n) if not tablero_minas[i][j] and (i, j) != (f, c)]

    if libres:
        i2, j2 = random.choice(libres)
        tablero_minas[i2][j2] = True
        tablero_minas[f][c] = False

    return tablero_minas

# ----------------
# Ejecucion
# ----------
def jugar(n, num_minas):
    tablero_minas = generar_minas(n, num_minas)
    visible = crear_tablero_visible(n)

    primera = True

    while True:
        limpiar()
        imprimir_tablero(visible)

        coord = input("\nIngrese coordenada: ").strip()

        pos = parsear_coord(coord, n)
        if pos is None:
            print("Coordenada inválida")   #timer de reinicio
            time.sleep(1)
            continue

        f, c = pos

        if visible[f][c] != ".":
            print("Casilla ya revelada")
            time.sleep(1)
            continue

        if primera:
            tablero_minas = asegurar_primera(tablero_minas, f, c, num_minas)
            primera = False

        if tablero_minas[f][c]:
            revelar_minas(tablero_minas, visible)
            limpiar()
            imprimir_tablero(visible)
            print("\n¡Perdiste!")
            break

        revelar_casillas(tablero_minas, visible, f, c)

        if victoria(tablero_minas, visible):
            limpiar()
            imprimir_tablero(visible)
            print("\n¡Ganaste!")
            break

# ----------
# MENU
# ------------
def menu():
    while True:
        limpiar()
        print("BUSCAMINAS")
        print("1. Modo Normal (9x9, 10 minas)")
        print("2. Modo Avanzado (16x16, 25 minas)")
        print("3. Salir")

        op = input("Seleccione opción: ")

        if op == "1":
            jugar(9, 10)
            input("\nPresione Enter...")
        elif op == "2":
            jugar(16, 25)
            input("\nPresione Enter...")
        elif op == "3":
            break

menu()
