# Diseña una función que calcule la potencia de un número. La función debe recibir la base y 
# el exponente como argumentos y devolver el resultado.



def calcular_potencia(base_numero, potencia_numero):
    cuenta_potencia = base_numero ** potencia_numero

    return cuenta_potencia


base_numero = int(input("Ingrese la base del numero: "))
potencia_numero = int(input("Ingrese la potencia del numero: "))
resultado = calcular_potencia(base_numero, potencia_numero)

print(f"El resultado de la cuenta es: {resultado}")