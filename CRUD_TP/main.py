from Empleado import *

lista_empleados = []

lista_empleados_eliminados = []

def mostrar_opciones():
    while True:
        opcion = input("Menu\n\n"
                        "1. Ingresar empleado\n"
                        "2. Modificar empleados\n"
                        "3. Eliminar empleados\n"
                        "4. Mostrar empleados\n"
                        "5. Calcular salario promedio\n"
                        "6. Buscar empleado por DNI\n"
                        "7. Ordenar empleados\n"
                        "8. Salir\n\n"
                        "Elija una opcion: ")
        
        if opcion.isalpha() or opcion == "":
            print("Opcion invalida.\n")
            continue

        opcion = int(opcion)

        if opcion < 1 or opcion > 8:
            print("Opción invalida.\n")
            continue
        
        break

    return opcion
    

def menu():
    while True:
        opcion = mostrar_opciones()
        match opcion:

            case 1:
                ingresar_empleado_lista(lista_empleados)
                print("")

            case 2:
                modificar_empleado(lista_empleados)
                print("")

            case 3:
                eliminar_empleado(lista_empleados, lista_empleados_eliminados)
                print("")

            case 4:
                mostrar_lista_empleados(lista_empleados)
                print("")

            case 5:
                calcular_promedio(lista_empleados)
                print("")

            case 6:
                buscar_empleado(lista_empleados)
                print("")

            case 7:
                ordenar_empleados(lista_empleados)
                print("")

            case 8:
                break


menu()