# Define una función que encuentre el máximo de tres números. La función debe aceptar tres argumentos y devolver el número más grande.

def mayor_numero(numero_1, numero_2, numero_3):
    if numero_1 > numero_2 and numero_3:
        return numero_1
    else:
        if numero_2 > numero_3:
            return numero_2
        else:
            return numero_3


numero_1 = int(input("Ingrese un numero: "))
numero_2 = int(input("Ingrese otro numero: "))
numero_3 = int(input("Ingrese otro numero: "))

resultado = mayor_numero(numero_1, numero_2, numero_3)

print(f"El mayor numero de los ingresos es: {resultado}")