from Alumno import *
from os import system

def mostrar_opciones():
    opcion = input("MENU\n 1. Cargar\n 2. Modificar\n 3. Eliminar\n 4. Mostrar\n 5. Salir\n Elija una opcion: ")
    return opcion

lista_alumnos = []

def menu():
    system("cls")
    while True:
        opcion = mostrar_opciones()
        match opcion:
            case "1":
                ingresar_alumno_lista(lista_alumnos)
            case "2": # Deben tener elementos de la lista
                dni = int(input("Ingrese el dni a modificar: "))
                modificar_alumno(lista_alumnos, dni)
            case "3":
                dni = int(input("Ingrese el dni a eliminar: "))
                elimiar_alumno(lista_alumnos, dni)
            case "4":
                mostrar_lista_alumnos(lista_alumnos)
            case "5":
                break

menu()