from Input import *

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


def ingresar_empleado_lista(lista_empleados: list[dict]):
    while True:
        if len(lista_empleados) >= 20:
            print("La lista de empleados esta completa.")
            break

        if len(lista_empleados) < 20:
            id = len(lista_empleados) + 1

            nombre = get_string_2("Ingrese su nombre/s: ", "Error al ingresar el nombre.", 20)

            apellido = get_string_2("Ingrese su apellido: ", "Error al ingresar el apellido.", 20)

            dni = get_int_3("Ingrese su DNI: ", "Error, ingrese un DNI valido: ", 5000000, 99999999)

            puesto = obtener_puesto("Ingrese su puesto: ", "Error al ingresar el puesto.")

            salario = get_int_2("Ingrese su salario: ", "Error, ingrese su salario correctamente.", 234315)

            diccionario_empleado = crear_empleado(id, nombre, apellido, dni, puesto, salario)

            lista_empleados.append(diccionario_empleado)

            seguir = input("Desea ingresar otro empleado? S/N").upper()
            if seguir != "S":
                break

 
def mostrar_lista_empleados(lista_empleados: list[dict]):
    print(f"{'ID':<5}{'Nombre':<15}{'Apellido':<15}{'DNI':<10}{'Puesto':<15}{'Salario':<15}")
    print("-" * 75)

    for empleado in lista_empleados:
        mostrar_empleado(empleado)

def mostrar_empleado(un_empleado: dict):
    print(f"{un_empleado['id']:<5}{un_empleado['nombre']:<15}{un_empleado['apellido']:<15}{un_empleado['dni']:<10}{un_empleado['puesto']:<15}{un_empleado['salario']:<15,}")


def modificar_empleado(lista_empleados: list[dict]):
    while True:
        id = input("Ingrese el ID del empleado que desea modificar (q para salir): ").lower()
        if id == "q":
            print("Saliendo...")
            return
        if id.isalpha():
            print("ID invalido. Ingrese un ID valido o ¨q¨ para salir.\n")
            continue
        
        id = int(id)
        break

    empleado_encontrado = False

    for empleado in lista_empleados:
        if empleado["id"] == id:
            empleado_encontrado = True
            print("Se encontro empleado.\n\n")
            while empleado_encontrado == True:
                opcion = input("Indique que es lo que desea modificar: ").lower()
                if opcion == "q":
                    return
                if opcion not in ["dni", "nombre", "apellido", "puesto", "salario"]:
                    print("Esa categoria no exite.")
                else:
                    break

            match opcion:
                case "dni":
                    dni_nuevo = get_int_3("Ingrese el nuevo dni modificado: ", "Error, DNI invalido.", 5000000, 99999999)
                    empleado["dni"] = dni_nuevo
                case "nombre":
                    nombre_nuevo = get_string_2("Ingrese su nombre modificado: ", "Error al ingresar el nombre.", 20)
                    empleado["nombre"] = nombre_nuevo
                case "apellido":
                    apellido_nuevo = get_string_2("Ingrese su apellido modificado: ", "Error al ingresar el apellido.", 20)
                    empleado["apellido"] = apellido_nuevo
                case "puesto":
                    puesto_nuevo = obtener_puesto("Ingrese su puesto modificado: ", "Error al ingresar el puesto.")
                    empleado["puesto"] = puesto_nuevo
                case "salario":
                    salario_nuevo = get_int_2("Ingrese su salario modificado: ", "Error, ingrese su salario correctamente.", 234315)
                    empleado["salario"] = salario_nuevo

    if empleado_encontrado == False:
        print("No se encontro empleado.\n\n")


def eliminar_empleado(lista_empleados: list[dict], lista_empleados_eliminados: list[dict]):
    while True: 
        id_a_eliminar = input("Ingrese el ID del empleado (o ´q´ para salir): ").lower()
        eliminado = None

        if id_a_eliminar == "q":
            print("Saliendo...")
            break

        id_a_eliminar = int(id_a_eliminar)
        for empleado in lista_empleados:
            if empleado["id"] == id_a_eliminar:
                mostrar_empleado(empleado)
                eliminado = empleado
                break
        
        if eliminado != None:
            lista_empleados.remove(eliminado)
            lista_empleados_eliminados.append(eliminado)


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
    while True:
        dni_buscado = input("Ingrese el DNI a buscar (o ´q´ para salir): ").lower()
        empleado_encontrado = False

        if dni_buscado == "q":
            print("Saliendo...")
            break
        
        for empleado in lista_empleados:
            if empleado["dni"] == dni_buscado and empleado_encontrado == False:
                empleado_encontrado = True
                print(f"Empleado encontrado!")
                print(f"Nombre y apellido: {empleado["nombre"]} {empleado["apellido"]}\n"
                    f"ID: {empleado["id"]}\n"
                    f"Puesto: {empleado["puesto"]}\n"
                    f"Salario: {empleado["salario"]}")
            
        if empleado_encontrado == False:
            print("No se encontro ningun empleado con ese DNI.")



def ordenar_empleados(lista_empleados: list[dict]):
    while True:
        menu_opciones = input("Indique por que desea ordenar a los empleados (o ´q´ para salir):\n"
                            "1. Nombre\n"
                            "2. Apellido\n"
                            "3. Salario\n"
                            "Elija una opcion: ")
        
        if menu_opciones == "q":
            print("Saliendo...")
            break

        if menu_opciones.isalpha():
            print("Opcion invalida.")
            continue

        menu_opciones = int(menu_opciones)
        break


    match menu_opciones:
        case 1:
            lista_empleados.sort(key=lambda x: x["nombre"].lower())
            print("Lista de empleados ordenada por nombre.")
        case 2:
            lista_empleados.sort(key=lambda x: x["apellido"].lower())
            print("Lista de empleados ordenada por apellido.")
        case 3:
            lista_empleados.sort(key=lambda x: x["salario"])
            print("Lista de empleados ordenada por salario.")


    print(f"{'ID':<5}{'Nombre':<15}{'Apellido':<15}{'DNI':<10}{'Puesto':<15}{'Salario':<15}")
    print("-" * 75)
    for empleado in lista_empleados:
        print(f"{empleado['id']:<5}{empleado['nombre']:<15}{empleado['apellido']:<15}{empleado['dni']:<10}{empleado['puesto']:<15}{empleado['salario']:<15,}")
    print("\n")


