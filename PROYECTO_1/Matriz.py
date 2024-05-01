################### Recorrer matrices
matriz = [
    [5,4.9],
    [9,8,7],
    [3,1,5]
]

for i in range(3):
    for j in range(3):
        print(matriz[i][j], end = " ")
    print("")



################### Por filas
M = 3
N = 3

matriz = [[0] * N for _ in range(M)]


for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        matriz[i][j] = int(input("Ingrese un numero: "))

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        print(f"{matriz[i][j]:5}", end = " ")
    print("")



################### Por columnas
matriz = [[5,4,9,10],
          [9,8,7,15],
          [3,1,5,11]]

for j in range(len(matriz[0])):
    for i in range(len(matriz)):
        print(f"{matriz[i][j]:4}", end = " ")
    print("")



################## Escalar
matriz = [[5,4.9],
          [9,8,7],
          [3,1,5]]

escalar = 5
M = len(matriz) # Filas
N = len(matriz[0]) # Columnas

matriz_resultado = [[0]* N for _ in range(M)]

for i in range(M):
    for j in range(N):
        matriz_resultado[i][j] = matriz[i][j] * escalar

for i in range(M): 
    for j in range(N): 
        print(f"{matriz_resultado[i][j]:5}", end = " ")
    print("")



################## Suma de matricez
matriz_a = [
    [5,4.9],
    [9,8,7],
    [3,1,5]
]

matriz_b = [
    [54,84,79],
    [19,68,57],
    [32,31,45]
]

M = len(matriz_a) # Filas
N = len(matriz_b[0]) # Columnas

matriz_resultado = [[0]* N for _ in range(M)]

for i in range(M):
    for j in range(N):
        matriz_resultado[i][j] = matriz_a[i][j] + matriz_b[i][j]

for i in range(M): 
    for j in range(N): 
        print(f"{matriz_resultado[i][j]:5}", end = " ")
    print("")

