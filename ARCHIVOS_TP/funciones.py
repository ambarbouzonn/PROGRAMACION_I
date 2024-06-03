def guardar_lista_en_archivo(lista_numeros, path_archivo):
    with open(path_archivo, 'w') as file:
        for numero in lista_numeros:
            file.write(f"{numero}\n")


def leer_multiplos_en_archivo(path_archivo):
    multiplos = []
    with open(path_archivo, "r") as file:
        for linea in file:
            numero = int(linea.strip())
            if numero % 2 == 0:
                file.write(f"{numero}-")

    

        


