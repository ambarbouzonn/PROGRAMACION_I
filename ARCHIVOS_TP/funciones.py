"""
1. Crear una función que reciba como parámetros una lista de números y 
el path de un archivo. La misma deberá guardar la lista en un archivo de texto.

2. Crear una función que reciba como parámetro el path de un archivo. La misma
deberá leer el archivo del ejercicio anterior, solo dejando pasar a la lista los 
números múltiplos de 2.

3. Crear una función que reciba como parámetros dos paths: uno correspondiente a un 
archivo de origen y otro correspondiente a un archivo de destino. La función debe 
leer el contenido del archivo de origen y luego transcribirlo en el archivo de destino. 
En caso de error la función retornará algún tipo de código de error indicando que paso.

4. Crear una función llamada contar_elementos que recibe como parámetro el path de un 
archivo de texto que contiene un poema. La función deberá contar la cantidad de líneas, 
la cantidad de palabras y la cantidad de caracteres que contiene el poema. La función 
retornará un diccionario con los datos obtenidos.

"""



###### 1
def guardar_lista_en_archivo(lista_numeros, path_archivo):
    with open(path_archivo, 'w') as file:
        for numero in lista_numeros:
            file.write(f"{numero}\n")

###### 2
def leer_multiplos_en_archivo(path_archivo):
    multiplos = []
    
    with open(path_archivo, "r") as file:
        for linea in file:
            numero = int(linea.strip())
            if numero % 2 == 0:
                multiplos.append(numero)
    return multiplos

def mostrar_miltiplos(multiplos, path_destino):
    with open(path_destino, "w") as file:
        for numero in multiplos:
            file.write(f"{numero}\n")


def guardar_multiplos(path, lista_numeros: list):
    with open(path, "w") as archivo:
        for numero in lista_numeros:
            if numero % 2 == 0:
                (archivo.write(f"{numero}\n"))

    
###### 3
def transferir_datos(path_origen, path_destino):
    try:
        with open(path_origen, 'r') as archivo_origen:
            contenido = archivo_origen.read()

        with open(path_destino, 'w') as archivo_destino:
            archivo_destino.write(contenido)

    
    except Exception as error:
        error_encontrado = print(f"Error: {error}")

        return error_encontrado
        

###### 4
def contar_elementos(path_archivo):
    diccionario = {
        'lineas': 0,
        'palabras': 0,
        'caracteres': 0
    }

    with open(path_archivo, 'r') as file:
        for linea in file:
            if linea.strip(): 
                diccionario['lineas'] += 1
                diccionario['palabras'] += len(linea.split())
            diccionario['caracteres'] += len(linea)


    return diccionario

            
                   