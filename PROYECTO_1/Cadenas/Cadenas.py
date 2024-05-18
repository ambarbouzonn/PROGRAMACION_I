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


def contador_vocales(cadena: str):
    cadena = cadena.lower()

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


def recibir_cadena(cadena: str, caracter: str):
    cadena = cadena.lower()

    for i in range(len(cadena)):
        if caracter == cadena[i]:
            resultado = f"Caracter {caracter}, encontrado en el primer indice de {i+1}" 
        else:
            resultado -1

    return resultado

# resultado = recibir_cadena()
# print(resultado)



###################### 3
# Crear una función que reciba como parámetro una cadena y determine si la misma es 
# o no un palíndromo. Deberá retornar un valor booleano indicando lo sucedido.

def cadena_palindromo(cadena: str):
    cadena = cadena.lower()
    
    if cadena == cadena[::-1]:
        return True
    else:
        return False
    
# resultado = cadena_palindromo()
# print(resultado)



###################### 4
# Crear una función que reciba como parámetro una cadena y suprima los caracteres repetidos.
# Ej: Si recibe como parámetro la cadena “Hooola” debe devolver “Hola”.

def eliminar_caracteres_repetidos(cadena: str):
    cadena_sin_repetidos = ""
    cadena = cadena.lower()

    for caracter in cadena:
        if caracter not in cadena_sin_repetidos:
            cadena_sin_repetidos += caracter
    return cadena_sin_repetidos

# resultado = eliminar_caracteres_repetidos("Hoooola")
# print(resultado)



###################### 5
# Crear una función que reciba una cadena por parámetro y suprima las vocales de la misma.
# Ej: Si recibe como parámetro la cadena “Hola” debe devolver “Hl”


def eliminar_vocales(cadena: str):
    cadena_sin_vocales = ""
    cadena = cadena.lower()

    for caracter in cadena:
        if caracter not in "aeiou":
            cadena_sin_vocales += caracter
        
    return cadena_sin_vocales


# resultado = eliminar_vocales("Hola")
# print(resultado)



###################### 6
# Crear una función para contar cuántas veces aparece una subcadena dentro de una cadena.
# Ej: Si recibe la cadena “El pan del panadero” y la subcadena “pan” deberá retornar el valor 2.

def hallar_subcadena(cadena: str, sub_cadena: str):
    cadena = cadena.lower()
    sub_cadena = sub_cadena.lower()
    contador = 0

    sub_cadena_len = len(sub_cadena)
    limite_cadena = len(cadena) - sub_cadena_len + 1

    for i in range(limite_cadena):
        if cadena[i:i + sub_cadena_len] == sub_cadena:
            contador += 1

    return contador


# resultado = hallar_subcadena("Hay varias manzanas en el arbol de manzanas", "manzanas")
# print(resultado)
            


###################### CSI UTN

def encontrar_sospechoso():

    numero_sospechosos = int(input("Ingrese la cantidad de sospechosos: "))

    adn_encontrado = input("Ingrese la muestra de adn encontrada: ")

    lista_sospechosos = {}

    for _ in range(numero_sospechosos):
        nombre_sospechoso = input("Ingrese el nombre del sospechoso: ")
        adn_sospechoso = input("Ingrese el adn del sospechoso: ")
        lista_sospechosos[nombre_sospechoso] = adn_sospechoso

    for nombre_sospechoso in lista_sospechosos:
        if adn_encontrado in lista_sospechosos[nombre_sospechoso]:
            return nombre_sospechoso
    return "Son todos inocentes"


resultado = encontrar_sospechoso()
print(resultado)