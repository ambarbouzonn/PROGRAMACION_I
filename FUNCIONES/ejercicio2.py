# Crear una función que le solicite al usuario el ingreso de un número entero y lo retorne.

def pedir_numero_y_retornar(numero):
    return numero


numero = input("Ingrese un numero: ")
numero = int(numero)
resultado = pedir_numero_y_retornar(numero)

print(f"El numero que ingreso es: {resultado}")