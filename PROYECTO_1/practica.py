from Package_Input.Input import get_int

def pedir_numeros():
    lista_numero = []

    for i in range(10):
        numero = get_int(f"{i+1}.Ingrese un numero: ", "Error!, Ingrese nuevamente un numero: ", -1000, 1000, 3)

        if -1000 <= numero <= 1000:
            lista_numero.append(numero)
        
    return lista_numero

lista_numeros = pedir_numeros()

def sumar_positivos_y_negativos(lista: list):
    positivos = 0
    negativos = 0
    for i in lista_numeros:
        if i > 0:
                positivos += i
        else:
            negativos += i

    print(f"La suma de los numeros positivos es: {positivos}")
    print(f"La suma de los numeros negativos es: {negativos}")
    
# sumatoria = sumar_positivos_y_negativos(lista_numeros)

def sumar_pares(lista: list):
    suma = 0
    for i in lista_numeros:
          if i % 2 == 0:
               suma += i

    print(f"La suma de los numeros pares es: {suma}")

# resultado = sumar_pares(lista_numeros)

def mayor_impar(list):
    numero_mayor_impar = 0

    for i in lista_numeros:
        if i % 2 != 0:
            numero_mayor_impar = i
        elif  i % 2 != 0 and i > numero_mayor_impar:
            numero_mayor_impar = i
    
    print(f"El numero mayor de los impares es: {numero_mayor_impar}")

# mayor_de_impares = mayor_impar(lista_numeros)

def listar_pares(list):
    lista_numero_pares = []

    for i in lista_numeros:
        if i % 2 == 0:
            numero_par = i
            lista_numero_pares.append(numero_par)

    print(f"Lista de los numeros pares ingresados: {lista_numero_pares}")

# lista_par = listar_pares(lista_numeros)

def listar_posicion_impar(list):
    for i in range(len(lista_numeros)):
        if i % 2 != 0: 
            lista_impar = lista_numeros[i]
            print(f"Numero: {lista_impar}. Posicion: {i}")

# lista_impar = listar_posicion_impar(lista_numeros)


def menu_opciones():

    while True:
        print("- Menu de opciones -\n"
              "B. Mostrar la cantidad de números positivos y negativos.\n"
              "C. Mostrar la sumatoria de los números pares.\n"
              "D. Informar el mayor de los números impares.\n"
              "E. Listar todos los números ingresados.\n"
              "F. Listar todos los números pares.\n"
              "G. Listar los números de las posiciones impares.\n"
              "H. Salir\n")
        
        opcion = input("Seleccione una opcion: ").upper()
        

        match opcion:
            case "B":
                sumar_positivos_y_negativos(lista_numeros)

            case "C":
                sumar_pares(lista_numeros)
            
            case "D":
                mayor_impar(lista_numeros)

            case "E":
                print(lista_numeros)
            
            case "F":
                listar_pares(lista_numeros)

            case "G":
                listar_posicion_impar(lista_numeros)

            case "H":
                break

            
menu_opciones()
            
