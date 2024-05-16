###################### 1
# Crear una función que reciba como parámetro una cadena y determine la cantidad de 
# vocales que hay de cada una (individualmente). La función retornará una matriz indicando
# en la columna 1 cada vocal, y en la columna 2 la cantidad.
# Por ej:
# cadena = “murcielaguito”
# “a” 1
# “e” 1
# “i” 2
# “o” 1
# “u” 2

# cadena = input("Ingrese una cadena: ").lower()

def contador_vocales(cadena: str):

    matriz_vocales = [["a", 0],
                      ["e", 0],
                      ["i", 0],
                      ["o", 0],
                      ["u", 0]]

    for i in cadena:
        if i in "a" or "e" or "i" or "o" or "u":
            for j in matriz_vocales:
                if j[0] == i:
                    j[1] += 1

    return matriz_vocales

# resultado = contador_vocales() 
# print(resultado)



###################### 2
# Crear una función que reciba una cadena y un caracter. La función deberá devolver 
# el índice en el que se encuentre la primera incidencia de dicho caracter, o -1 en caso de que no esté.

# cadena = input("Ingrese una cadena: ").lower()
# caracter = input("Ingrese un caracter: ").lower()

def recibir_cadena():
    for i in range(len(cadena)):
        if caracter == cadena[i]:
            return f"Caracter {caracter}, encontrado en el primer indice de {i+1}" 
        
    return -1

# resultado = recibir_cadena()
# print(resultado)



###################### 3
# Crear una función que reciba como parámetro una cadena y determine si la misma es 
# o no un palíndromo. Deberá retornar un valor booleano indicando lo sucedido.

# cadena = input("Ingrese una cadena: ").lower()

def cadena_palindromo():
    if cadena == cadena[::-1]:
        return True
    else:
        return False
    

# resultado = cadena_palindromo()
# print(resultado)



###################### 4
# Crear una función que reciba como parámetro una cadena y suprima los caracteres repetidos.
# Ej: Si recibe como parámetro la cadena “Hooola” debe devolver “Hola”.

cadena = input("Ingrese una cadena: ").lower()

def eliminar_caracteres_repetidos():
    for i in range(len(cadena)):
        caracter = cadena[i]
        if caracter == i:
            caracter