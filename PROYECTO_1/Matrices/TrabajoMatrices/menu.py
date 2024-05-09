from Input import *
import random


"""
Una empresa de colectivos tiene 3 líneas de 5 coches cada una. En total tiene 15 choferes 
(cada uno con un legajo distinto generado aleatoriamente).

Nos piden desarrollar un software que presente el siguiente menú  de usuarios:
Menú:

Cargar planilla. El chofer se debe identificar (el legajo debe existir dentro de una matriz de legajos). 
Si el chofer existe cargará la recaudación del viaje indicando línea y coche (no necesariamente un chofer 
está asignado a una única línea y coche), estos datos deben estar validados. Un chofer puede cargar más 
de una recaudación por día (para distintas líneas y distintos coches). Cada coche de cada línea puede 
tener varias recaudaciones diarias.
Mostrar la recaudación de cada coche y línea.
Calcular y mostrar recaudación por línea.
Calcular y mostrar recaudación por coche.
Calcular y mostrar la recaudación total.
Salir

Todo el desarrollo tiene que estar modularizado: ingreso de datos, validaciones de líneas y coches, 
generación y verificación de existencia de legajo, cálculos, etc.
"""


legajo_colectiveros = [
    [3014, 5451, 8745, 9854, 1496],
    [4758, 3625, 4561, 9874, 3219],
    [4758, 6958, 3625, 1425, 4510]
    ]


# Valido el legajo
def validar_legajo(legajo_colectiveros: list):
    ingrese_legajo = get_int("Ingrese su numero de legajo: ", "Ingrese su numero de legajo valido: ", 1000, 9999, 3)

    for i in range(len(legajo_colectiveros)):
        for j in range(len(legajo_colectiveros[i])):
            if ingrese_legajo == legajo_colectiveros[i][j]:
                return True


# Creo la matriz con las dimesiones correspondientes 
def matriz_lineas_coches(filas, columnas):
    matriz = [[0] * columnas for _ in range(filas)]
    return matriz


# Ingresar los datos necesarios 
def ingresar_datos(matriz):

    while True:
        columna = get_int("Ingrese el coche: ", "Error, ingrese un coche valido: ", 1, 5, 3)
        fila = get_int("Ingrese la linea: ", "Error, ingrese una linea valida: ", 1, 3, 3)

        if fila < 1 or fila > len(matriz) or columna < 1 or columna > len(matriz[0]):
            print("Fila o columna fuera de rango.")
            continue

        recaudacion = get_float("Ingrese la recaudacion: ", "Error, ingrese una recaudacion valida: ", 0, 999999, 3)
        matriz[fila - 1][columna - 1] += recaudacion

        continuar = input("¿Desea cargar otra recaudación? (S/N): ")
        print() 
        if continuar.upper() != 'S':
            break


# Mostrar la matriz con los datos
def mostrar_matriz(matriz):
    for fila in matriz:
        print(fila)


# Mostrar la recaudación de cada coche y línea
def mostrar_recaudacion_por_coche_y_linea(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(f"Línea {i+1}, Coche {j+1}: ${matriz[i][j]}")
        print() 


# Calcular y mostrar recaudacion por linea
def recaudacion_por_linea(matriz):
    
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            recaudacion_total_linea = 0
            recaudacion_total_linea += matriz[i][j]
        print(f"Recaudación total para la línea {i+1}: ${recaudacion_total_linea}")
    print() 


# Calcular y mostrar recaudacion por coche
def recaudacion_por_coche(matriz):

    for j in range(len(matriz[0])):
        for i in range(len(matriz)):
            recaudacion_total_coche = 0
            recaudacion_total_coche += matriz[i][j]
        print(f"Recaudación total para el coche {j+1}: ${recaudacion_total_coche}")
    print() 


# Calcular y mostrar el total de las recaudaciones
def recaudacion_total(matriz):
    total = 0
    for fila in matriz:
        for valor in fila:
            total += valor
    print(f"Recaudación total de todas las líneas y coches: ${total}")
    print() 

