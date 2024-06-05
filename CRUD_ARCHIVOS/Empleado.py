import json
from datetime import datetime
from Input import *
import csv


def crear_empleado(id: int, nombre: str, apellido: str, dni: int, puesto: str, salario: int):
    diccionario_empleado = {
        "id": id,
        "nombre": nombre,
        "apellido": apellido,
        "dni": dni,
        "puesto": puesto,
        "salario": salario
    }

    return diccionario_empleado


def obtener_puesto(mensaje: str, mensaje_error: str):
    puestos = ["Gerente", "Supervisor", "Analista", "Encargado", "Asistente"]

    while True:
        puesto = input(mensaje).strip().capitalize()
        if puesto in puestos:
            return puesto
        else:
            print(mensaje_error)


# Función para obtener el último ID desde Empleados.csv
def obtener_ultimo_id_desde_csv():
    try:
        with open("Empleados.csv", mode="r", newline='') as file: # Abre el archivo en modo lectrua ("r")
            reader = csv.DictReader(file) # Lee el archivo a tarves del DictReader que lo convierte cada fila en un diccionario, donda las claves son las columnas
            ids = [int(row['id']) for row in reader] # Itera sobre cada id de la columna y los mete en la lista IDS
            if not ids: # Si no hay id, retorna 0
                return 0
            
            ultimo_id = ids[0] # Se inicia con el primer elemento de la lista
            for id in ids: # Se recorren todos los id
                if id > ultimo_id: # Se establece el de mayor valor
                    ultimo_id = id
            return ultimo_id
        
    except FileNotFoundError: # En caso de no encontrar un archivo, retorna 0
        return 0

# Función para leer el último ID desde last_id.txt
def leer_ultimo_id():     
    try:    
        with open("last_id.txt", mode="r") as file:  # Abre el archivo en modo lectura ("r")
            contenido = file.read().strip()  # Leer y limpiar el contenido del archivo

            if contenido != "":  # Verificar si el contenido no está vacío
                return int(contenido)  # Convertir el contenido en un entero
            else:
                return 0  # Devolver 0 si el archivo está vacío
            
    except FileNotFoundError: # En caso de encontrar archivo, retorna 0
        return 0
    

# Función para escribir el último ID en last_id.txt
def escribir_ultimo_id(ultimo_id):
    with open("last_id.txt", mode="w") as file: # Abre el archivo en modo escritura ("w")
        file.write(str(ultimo_id)) # Se convierte en entero el ultido id, y se escribe en el archivo


# Función para inicializar el último ID
def inicializar_ultimo_id():
    ultimo_id_csv = obtener_ultimo_id_desde_csv() # Llamamos a la funcion para obtener el ultimo id del csv
    ultimo_id_txt = leer_ultimo_id() # Llamamos a la funcion para obetner el ultimo id del txt
    
    if ultimo_id_csv > ultimo_id_txt: # Se verifica si el ultimo id csv es mayor que el ultimo id guardado en el txt
        ultimo_id = ultimo_id_csv
    else:
        ultimo_id = ultimo_id_txt
    
    escribir_ultimo_id(ultimo_id) # Se escribe el ultimo id en el last_id.txt
    return ultimo_id # Se devuelve el ultimo id 


def ingresar_empleado_lista(lista_empleados: list[dict]):
    while True:
    
        ultimo_id = inicializar_ultimo_id() # A traves de la funcion se obtiene el ultimo id
        nuevo_id = ultimo_id + 1 # Al ultimo id obtenido, se le va incrementando 1 cada vez que se ingresa

        nombre = get_string_2("Ingrese su nombre/s: ", "Error al ingresar el nombre.", 20)
        apellido = get_string_2("Ingrese su apellido: ", "Error al ingresar el apellido.", 20)
        dni = get_int_3("Ingrese su DNI: ", "Error, ingrese un DNI valido: ", 5000000, 99999999)
        puesto = obtener_puesto("Ingrese su puesto: ", "Error al ingresar el puesto.")
        salario = get_int_2("Ingrese su salario: ", "Error, ingrese su salario correctamente.", 234315)

        diccionario_empleado = crear_empleado(nuevo_id, nombre, apellido, dni, puesto, salario) # Se guardan los datos dentro del diccionario

        lista_empleados.append(diccionario_empleado) # Se guarda el diccionario dentro de la lista

        seguir = input("Desea ingresar otro empleado? S/N").upper()
        if seguir != "S":
            escribir_ultimo_id(nuevo_id) # Se escribe el ultimo id utilizado en el txt
            break

 
def mostrar_lista_empleados(lista_empleados: list[dict]):
    print(f"{'ID':<5}{'Nombre':<15}{'Apellido':<15}{'DNI':<10}{'Puesto':<15}{'Salario':<15}") # Se muestra la lista con forma de tabla
    print("-" * 75)

    for empleado in lista_empleados: # Se itera por cada empleado y se muestra en una linea
        mostrar_empleado(empleado)

def mostrar_empleado(un_empleado): # Se muestra las caracteristicas del empleado en una linea
    print(f"{un_empleado['id']:<5}{un_empleado['nombre']:<15}{un_empleado['apellido']:<15}{un_empleado['dni']:<10}{un_empleado['puesto']:<15}{un_empleado['salario']:<15,}")



def modificar_empleado(lista_empleados: list[dict]):
    while True:
        id = input("Ingrese el ID del empleado que desea modificar ('q' para salir): ").lower()

        if id == "q": # La opcion "q" para salir de la opcion
            print("Saliendo...")
            return
        
        if id.isdigit() and int(id) > 0:
            id = int(id)

        else:
            print("ID inválido. Ingrese un ID válido o 'q' para salir.\n")
            continue
        
        id = int(id) # Si ya paso ambas validaciones, se convierte en entero y rompe el bucle
        break

    empleado_encontrado = False # Una bandera para la busqueda de un empleado

    for empleado in lista_empleados:
        if empleado["id"] == id: # Si el ID ingresado es correcto entra
            empleado_encontrado = True # Se cambia la bandera
            print("Se encontro empleado.\n\n")

            while empleado_encontrado == True:
                opcion = input("Indique que es lo que desea modificar (0 'q' para salir): ").strip().lower() # El strip elemina si es hay caracteres

                if opcion == "q": # Sale de la funcion
                    return
                
                if opcion != "dni" and opcion != "nombre" and opcion != "apellido" and opcion != "puesto" and opcion != "salario": # Si la opcion es diferente a las opcines 
                    print("Esa categoría no existe.")
                    continue

                else:
                    break

            match opcion: # Si la opcion es valida, agarra el caso y pide confirmacion de la modificacion 
                case "dni":
                    dni_nuevo = get_int_3("Ingrese el nuevo dni modificado: ", "Error, DNI invalido.", 5000000, 99999999)
                    confirmacion = input("Esta seguro que quiere realizar ese cambio? S/N: ").upper()
                    if confirmacion != "S":
                        print("No se realizo el cambio.")
                    else:
                        empleado["dni"] = dni_nuevo

                case "nombre":
                    nombre_nuevo = get_string_2("Ingrese su nombre modificado: ", "Error al ingresar el nombre.", 20)
                    confirmacion = input("Esta seguro que quiere realizar ese cambio? S/N: ").upper()
                    if confirmacion != "S":
                        print("No se realizo el cambio.")
                    else:
                        empleado["nombre"] = nombre_nuevo

                case "apellido":
                    apellido_nuevo = get_string_2("Ingrese su apellido modificado: ", "Error al ingresar el apellido.", 20)
                    confirmacion = input("Esta seguro que quiere realizar ese cambio? S/N: ").upper()
                    if confirmacion != "S":
                        print("No se realizo el cambio.")
                    else:
                        empleado["apellido"] = apellido_nuevo

                case "puesto":
                    puesto_nuevo = obtener_puesto("Ingrese su puesto modificado: ", "Error al ingresar el puesto.")
                    confirmacion = input("Esta seguro que quiere realizar ese cambio? S/N: ").upper()
                    if confirmacion != "S":
                        print("No se realizo el cambio.")
                    else:
                        empleado["puesto"] = puesto_nuevo

                case "salario":
                    salario_nuevo = get_int_2("Ingrese su salario modificado: ", "Error, ingrese su salario correctamente.", 234315)
                    confirmacion = input("Esta seguro que quiere realizar ese cambio? S/N: ").upper()
                    if confirmacion != "S":
                        print("No se realizo el cambio.")
                    else:
                        empleado["salario"] = salario_nuevo

    if empleado_encontrado == False: # Si no se pudo validar el ID con uno existente retorna el print
        print("No se encontro empleado.\n\n")



def eliminar_empleado(lista_empleados: list[dict], lista_empleados_eliminados: list[dict]):
    while True: 
        id_a_eliminar = input("Ingrese el ID del empleado (o 'q' para salir): ").lower()
        empelado_eliminado = None

        if id_a_eliminar == "q":
            print("Saliendo...")
            return

        if id_a_eliminar.isdigit and id_a_eliminar > 0:
            id_a_eliminar = int(id_a_eliminar)
            break

        else:
            print("ID inválido. Ingrese un ID válido o 'q' para salir.\n")
            continue

        
    for empleado in lista_empleados: 
        if empleado["id"] == id_a_eliminar:
            mostrar_empleado(empleado)
            empelado_eliminado = empleado # El empleado pasa a ser como empleado eliminado
            break

        
    if empelado_eliminado != None:
        confirmacion = input("¿Está seguro que desea eliminar este empleado? S/N: ").upper() # Se pide la confimacion

        if confirmacion == "S":
            lista_empleados.remove(empelado_eliminado) # Se elimina de la lista al empleado
            lista_empleados_eliminados.append(empelado_eliminado) # Se incorpora el la lista de empleados eliminados 
            print("Empleado eliminado.")

        else:
            print("Operación cancelada.")

    else:
        print("No se encontró empleado con ese ID.\n")


def calcular_promedio(lista_empleados: list[dict]):
    suma = 0
    total = 0

    for empleado in lista_empleados:
        suma += empleado["salario"]
        total += 1

    if total == 0:
        print("No hay empleados en la lista para calcular el promedio.")
    
    promedio = suma / total
    print(f"El salario promedio es de: {promedio:.2f}")



def buscar_empleado(lista_empleados: list[dict]):
    empleado_encontrado = False # Bandera para la busqueda del empleado

    while True:
        dni_buscado = input("Ingrese el DNI a buscar (o 'q' para salir): ").lower()

        if dni_buscado == "q":
            print("Saliendo...")
            return

        if dni_buscado.isdigit() and int(dni_buscado) > 0: # Se valida que sea un numero
            dni_buscado = int(dni_buscado)
            break

        else:
            print("DNI inválido.")
            continue

    for empleado in lista_empleados: # Se itera sobre los empleados
        if empleado["dni"] == dni_buscado: # Si un dni se iguala al buscado entra
            empleado_encontrado = True
            print(f"Empleado encontrado!")

            print(f"Nombre y apellido: {empleado['nombre']} {empleado['apellido']}\n"
                f"ID: {empleado['id']}\n"
                f"Puesto: {empleado['puesto']}\n"
                f"Salario: {empleado['salario']}")
            
        
    if empleado_encontrado == False:
        print("No se encontró un empleado con ese DNI.")


def bubble_sort_descendente(arr, key): # Ordenamiento estilo bubble sort de mayor a menor
    n = len(arr)
    
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j][key] < arr[j+1][key]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


def bubble_sort_ascendente(arr, key): # Ordenamineto estilo bubble sort de menor a mayor
    n = len(arr)
    
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j][key] > arr[j+1][key]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


def ordenar_empleados(lista_empleados: list[dict]):
    while True:
        menu_opciones = input("Indique por que desea ordenar a los empleados (o 'q' para salir):\n"
                            "1. Nombre ascedente\n"
                            "2. Nombre descendente\n"
                            "3. Apellido ascedente\n"
                            "4. Apellido descendente\n"
                            "5. Salario ascedente\n"
                            "6. Salario ascedente\n"
                            "Elija una opcion: ")
        
        
        if menu_opciones == "q":
            print("Saliendo...")
            return

        if menu_opciones.isdigit() and 0 < int(menu_opciones) <= 6: # Valida si es un numero y esta dentro del rango
            menu_opciones = int(menu_opciones)
            break

        else:
            print("Opcion invalida.")
            continue

    match menu_opciones: # Busca la opcion en los case y genera el ordenamiento de la lista
        case 1:
            bubble_sort_ascendente(lista_empleados, "nombre")
            print("Lista de empleados ordenada por nombre de forma ascendente.")
            mostrar_lista_empleados(lista_empleados)

        case 2:
            bubble_sort_descendente(lista_empleados, "nombre")
            print("Lista de empleados ordenada por nombre de forma descendente.")
            mostrar_lista_empleados(lista_empleados)

        case 3:
            bubble_sort_ascendente(lista_empleados, "apellido")
            print("Lista de empleados ordenada por apellido de forma ascendente.")
            mostrar_lista_empleados(lista_empleados)

        case 4:
            bubble_sort_descendente(lista_empleados, "apellido")
            print("Lista de empleados ordenada por apellido de forma descendente.")
            mostrar_lista_empleados(lista_empleados)

        case 5:
            bubble_sort_ascendente(lista_empleados, "salario")
            print("Lista de empleados ordenada por salario de forma ascendente..")
            mostrar_lista_empleados(lista_empleados)

        case 6:
            bubble_sort_ascendente(lista_empleados, "salario")
            print("Lista de empleados ordenada por salario de forma ascendente..")
            mostrar_lista_empleados(lista_empleados)




def guardar_empleados_csv(lista_empleados: list[dict], nombre_archivo: str):

    with open(nombre_archivo, mode="w", newline="") as file: # Abre el archivo en modo escritura, el newline establece
        writer = csv.writer(file) # Escribe los datos de un archivo CSV (file) a un escritor 
        
        writer.writerow(["id", "nombre", "apellido", "dni", "puesto", "salario"]) # Se escribe una fila con los titulos de las columnas
        

        for empleado in lista_empleados: # Se itera sobre cada empleado de la lista
            writer.writerow([empleado["id"], empleado["nombre"], empleado["apellido"], empleado["dni"], empleado["puesto"], empleado["salario"]]) # Se escribe una fila en el archivo por cada empleado 
    
    print(f"Datos guardados en {nombre_archivo}")



def cargar_empleados_csv(nombre_archivo: str) -> list[dict]:
 
    lista_empleados = []

    try:
        with open(nombre_archivo, mode="r") as file: # Se abre el archivo en modo lectura ("r") 
            reader = csv.DictReader(file) # Se leen las filas del archivo CSV, asi obteniendo las claves de la primera fila como columnas
            for fila in reader:
                empleado = {
                    "id": int(fila["id"]),
                    "nombre": fila["nombre"],
                    "apellido": fila["apellido"],
                    "dni": int(fila["dni"]),
                    "puesto": fila["puesto"],
                    "salario": int(fila["salario"])
                } # Se crea un diccionario que contiene las filas del archivo, donde las claves son los nombres de la columna

                lista_empleados.append(empleado) # Se carga el empleado a la lista de empleados 

    except FileNotFoundError: # Printea el error en caso de encontrar un archivo
        print(f"El archivo {nombre_archivo} no existe. Se creará uno nuevo al guardar.")
    except KeyError as error: # Printea el error en caso de que falte una clave en una fila del CSV
        print(f"Error en el archivo CSV: campo {error} no encontrado.")
    except Exception as error: # Printea en caso general de algun otro error
        print(f"Error al leer el archivo CSV: {error}")

    return lista_empleados


def guardar_empleados_bajas_json(lista_empleados_eliminados: list[dict], nombre_archivo: str):
    with open(nombre_archivo, mode="w") as file: # Se abre el archivo en modo escritura ("w")
        json.dump(lista_empleados_eliminados, file) # Convierte la lista de empleados eliminados a formato JSON y los escribe en el archivo file
    print(f"Empleados dados de baja guardados en {nombre_archivo}")


def generar_reporte_sueldo(lista_empleados: list[dict], sueldo: int):
    empelados_con_sueldo = []
    for empleado in lista_empleados:
        if empleado["salario"] > sueldo:
            empelados_con_sueldo.append(empleado)
    fecha_reporte = datetime.now().strftime("%d/%m/%Y")
