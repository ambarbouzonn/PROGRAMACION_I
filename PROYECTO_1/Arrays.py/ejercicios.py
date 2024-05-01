# Escribir una función que reciba una lista de enteros, la misma calculará y devolverá el promedio de todos los números.

# lista = [1, 2, 3, 4, 5, 6]
def calcular_promedio_enteros(lista: list):
    for i in range(len(lista)):
        suma = sum(lista)
        cantidad = len(lista)

        return suma / cantidad
    
# resultado = calcular_promedio_enteros(lista)
# print(f"El promedio de la suma es: {resultado}")


# Escribir una función parecida a la anterior, pero la misma deberá calcular y devolver el promedio de los números positivos.

# lista = [-3, 6, 8, 9, -4, -9, 10, 7]
def calcular_promedio_positivos(lista: list):
    for i in range(len(lista)):
        if lista[i] > 0:
            suma = sum(lista)
            cantidad = len(lista)

            return suma / cantidad

# resultado = calcular_promedio_positivos(lista)
# print(f"El promedio de la suma de los numeros positivos es: {resultado}")


# Escribir una función que calcule y retorne el producto de todos los elementos de la lista que recibe como parámetro.

# lista = [1, 2, 3, 4, 5, 6]

def calcular_producto(lista: list):
    producto = 1
    for i in lista:
        producto *= i
    return producto

# resultado = calcular_producto(lista)
# print(f"El resultado de el producto de todos los elementos es: {resultado}")


# Escribir una función que reciba como parámetros una lista de enteros y retorne la posición del valor máximo encontrado.

# lista = [11, 12, 8, 25]

def encontrar_posicion(lista: list) -> int:
    bandera_maximo = True
    posicion_maximo = 0

    for i in range(len(lista)):
        if bandera_maximo == True:
            numero_maximo = lista[i]
            bandera_maximo = False
            posicion_maximo = i

        elif numero_maximo < lista[i]:
            numero_maximo = lista[i]
            posicion_maximo = i

    return print(f"{posicion_maximo} -- {numero_maximo}")

# encontrar_posicion(lista)


# Escribir una función que reciba como parámetros una lista de enteros y muestre la/las 
# posiciones en donde se encuentra el valor máximo hallado.


# Escribe una función llamada reemplazar_nombres que reciba como parámetros una lista de 
# nombres, un nombre a reemplazar y su correspondiente reemplazo. La función debe reemplazar 
# cada ocurrencia del nombre a reemplazar en la lista con su correspondiente reemplazo y luego 
# retornar la cantidad total de reemplazos realizados.


# lista = ["Lucia", "Sofia", "Micaela", "Sofia", "Joaquin", "Sofia"]

def reemplazar_nombres(lista: list):
    nombre = "Sofia"
    remplazo = "Maria"
    cantidad_remplazos = 0

    for i in range(len(lista)):
        if lista[i] == nombre:
            lista[i] = remplazo
            cantidad_remplazos += 1

    return cantidad_remplazos

# resultado = reemplazar_nombres(lista)
# print(resultado)


