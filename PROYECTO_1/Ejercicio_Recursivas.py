from Package_Input.Input import get_int

# Realizar una función recursiva que calcule la suma de los primeros números naturales:
def sumar_naturales(numero: int) -> int|None:
        if numero <= 0:
            resultado = 0
        else:
            resultado = numero + sumar_naturales(numero - 1)
        
        return resultado

print(sumar_naturales(5))

# Realizar una función recursiva que calcule la potencia de un número:
def calcular_potencia(numero: int, potencia: int) -> int:
        if numero <= 0:
            resultado = 0
        else:
            resultado = numero ** potencia

        return resultado

print(calcular_potencia(2, 3))

# Realizar una función recursiva que la suma de los dígitos de un número:
def sumar_digitos(numero: int) -> int:
        if numero <= 0:
            resultado = 0
        else:
            suma = 0
            for digito in str(numero):
                suma += int(digito)
            resultado = suma
        
        return resultado

print(sumar_digitos(12))

# Realizar una función para calcular el número de Fibonacci de un número ingresado por consola.
def calcular_fibonacci(numero: int) -> int:
        if numero <= 0:
            return numero
        
        elif numero == 1 or numero == 2:
            resultado = 1

        else:
            suma_fibonacci = calcular_fibonacci(numero - 1) + calcular_fibonacci(numero - 2)
            resultado = suma_fibonacci
        
        return resultado

mensaje = get_int("Ingrese un numero: ", "Error, ingrese un numero positivo: ", 1, 50, 3)
mensaje = int(mensaje)

resultado = calcular_fibonacci(mensaje)
print(resultado)

