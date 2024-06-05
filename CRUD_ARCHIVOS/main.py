from Empleado import *

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
                        "8. Generar reporte por sueldo\n"
                        "9. Generar reporte por apellido\n"
                        "10. Salir\n\n"
                        "Elija una opcion: ")
        
        if opcion.isalpha() or opcion == "":
            print("Opcion invalida.\n")
            continue

        if opcion.isdigit() and 0 < int(opcion) <= 10:
            opcion = int(opcion)
            break

    return opcion


def menu():
    lista_empleados = cargar_empleados_csv("Empleados.csv")
    lista_empleados_eliminados = []

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
                sueldo = int(input("Ingrese el sueldo: "))
                generar_reporte_sueldo(lista_empleados, sueldo)
                print("")

            case 9:
                apellido = input("Ingrese el apellido: ")
                generar_reporte_apellido(lista_empleados, apellido)
                print("")

            case 10:
                guardar_empleados_csv(lista_empleados, "Empleados.csv")
                guardar_empleados_bajas_json(lista_empleados_eliminados, "Bajas.json")
                print("Saliendo...")
                break


menu()