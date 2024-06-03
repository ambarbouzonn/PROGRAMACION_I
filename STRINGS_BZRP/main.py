"""
Consigna:
1. IMPLEMENTAR LOS METODOS VACIOS DE LA CLASE VIDEO

2. CREAR UN MENU DE USUARIO CON LAS SIGUIENTES OPCIONES:

A. NORMALIZAR OBJETOS: para cada video de la lista, se deberá llamar a los métodos de instancia: dividir_titulo, 
obtener_codigo_url y formatear_fecha, dado que la lista de objetos que nos pasan no cumple con las normas de estandarización 
de videos que nos solicitan.
B. MOSTRAR TEMAS: se deberá mostrar la lista de todos los temas
C. ORDENAR TEMAS: los temas se ordenarán por número de sesión de menor a mayor.
D. PROMEDIO DE VISTAS: mostrar el promedio de vistas expresado en k.
E. MAXIMA REPRODUCCION: mostrar el o los videos con mayor cantidad de vistas.
F. BUSQUEDA POR CODIGO: mostrar los videos cuyo código comiencen con la palabra "nick"
G. LISTAR POR COLABORADOR: el usuario ingresa el nombre de un colaborador y el programa deberá listar todos los videos de 
ese colaborador.
H. LISTAR POR MES: el usuario ingresa un mes, y se deberán listar todos los temas lanzados en ese mes (sin importar el año)
I. SALIR 

NOTA: 
1. Las opciones BCDEFG no serán accesibles si no se normalizan previamente los datos.
2. Todas las opciones tienen que estar resueltas en metodos de la clase Video que reciban una lista de videos sumado a los
parametros necesarios para lograr el objetivo y mantener independencia de código. 
"""
from data import *


def menu():
    bandera_seguir = False
    while bandera_seguir == False:
        opcion = input("""
    A. NORMALIZAR OBJETOS
    B. MOSTRAR TEMAS
    C. ORDENAR TEMAS
    D. PROMEDIO DE VISTAS
    E. MAXIMA REPRODUCCION
    F. BUSQUEDA POR CODIGO
    G. LISTAR POR COLABORADOR
    H. LISTAR POR MES
    I. SALIR

    Elija una opción: """).upper()


        match opcion:
            case "A":
                Video.normalizar_videos(lista_videos)
            case "B":
                Video.mostrar_temas(lista_videos)
            case "C":
                Video.ordenar_sesion(lista_videos)
                Video.mostrar_temas(lista_videos)
            case "D":
                Video.promedio_vistas(lista_videos)
            case "E":
                Video.max_vistas(lista_videos)
            case "F":
                Video.buscar_codigo(lista_videos, "nick")
            case "G":
                Video.listar_por_colaborador(lista_videos)
            case "H":
                Video.listar_por_mes(lista_videos)
            case "I":
                seguir = input("Seguro que quiere salir?")
                if seguir == "si":
                    bandera_seguir = True


menu()