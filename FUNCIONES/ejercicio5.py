# Escribe una función que calcule el área de un círculo. La función debe recibir el radio como parámetro y devolver el área.

import math

def calcular_area_circulo(radio):
    area = math.pi * radio**2
    return area

radio = input("Ingrese el radio: ")
radio = int(radio)
resultado = calcular_area_circulo(radio)

print(f"El area de su circulo es: {resultado}")