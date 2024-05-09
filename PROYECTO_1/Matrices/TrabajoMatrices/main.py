from menu import *

def menu_opciones():
    validar_legajo(legajo_colectiveros)
    matriz = matriz_lineas_coches(3, 5)


    ingresar_datos(matriz)

    while True:
        print("Menu:\n"
                "A. Mostrar la recaudación de cada coche y línea.\n"
                "B. Calcular y mostrar recaudación por línea.\n"
                "C. Calcular y mostrar recaudación por coche.\n"
                "D. Calcular y mostrar la recaudación total.\n"
                "E. Salir")
        
        opcion = input("Seleccione una opcion: ").upper()

        match opcion:

            case "A":
                mostrar_recaudacion_por_coche_y_linea(matriz)

            case "B":
                recaudacion_por_linea(matriz)
            
            case "C":
                recaudacion_por_coche(matriz)

            case "D":
                recaudacion_total(matriz)

            case "E":
                break


menu_opciones()