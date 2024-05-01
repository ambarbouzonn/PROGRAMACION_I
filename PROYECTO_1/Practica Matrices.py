def cargar_datos():
    M = int(input("Ingrese la cantidad de filas: "))
    N = int(input("Ingrese la cantidad de columnas: "))


    matriz_1 = [[0]*N for _ in range(M)]

    for i in range(len(matriz_1)):
        for j in range(len(matriz_1[i])):
            matriz_1[i][j] = int(input("Ingrese un número: "))
    
    for i in range(len(matriz_1)):
        for j in range(len(matriz_1[i])):
            print(f"{matriz_1[i][j]:5}", end = " ")
        print("")
    
    return matriz_1


matriz_1 = cargar_datos()
matriz_2 = cargar_datos()

def validar_dimensiones(matriz_1, matriz_2):
    
    if len(matriz_1[0]) != len(matriz_2):
        return False
    else:
        return True
    
resultado = validar_dimensiones(matriz_1, matriz_2)


def multiplicar_matrices(matriz_1, matriz_2):
    M = len(matriz_1)
    N = len(matriz_2[0])
    L = len(matriz_1[0])

    matriz_resultado = [[0]*N for _ in range(M)]

    for i in range(M):
        for j in range(N):
            for x in range(L):
                matriz_resultado[i][j] += matriz_1[i][x] * matriz_2[x][j]


    for i in range(len(matriz_resultado)):
        for j in range(len(matriz_resultado[i])):
            print(f"{matriz_resultado[i][j]:5}", end = " ")
        print("")
    
        
    return matriz_resultado
        

if resultado == False:
    print("Las matrices no se pueden multiplicar porque las columnas del primero no coinciden con las filas del segundo.")
else:
    resultado_multiplicacion = multiplicar_matrices(matriz_1, matriz_2)
    print(resultado_multiplicacion)

