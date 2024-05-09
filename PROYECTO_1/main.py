def get_int(mensaje: str, minimo: int, maximo: int) -> int:
    numero = input(mensaje)
    numero = int(numero)

    while numero < minimo or numero > maximo:
        numero = input(f"Error. {mensaje}")
        numero = int(numero)

    return numero

# edad = get_init("Ingrese su edad: ", 18, 30)

# legajo = get_init("Ingrese su legajo: ", 1000, 2000)

# nota = get_init("Ingrese su nota: ", 1, 10)


def get_int_2(mensaje: str, mensaje_error: str, minimo: int, maximo: int, reintentos: int) -> int|None:
        numero = input(mensaje)
        numero = int(numero)

        while reintentos > 0 and (numero < minimo or numero > maximo):
            numero = input(mensaje_error)
            numero = int(numero)
        
            reintentos -= 1

        return numero

# pedir_numero = get_init_2("Ingrese un numero: ", "Error. Ingrese un numero: ", 20, 40, 3)



def get_float(mensaje: str, mensaje_error: str, minimo: float, maximo: float, reintentos: int) -> float|None:
        numero = input(mensaje)
        numero = float(numero)

        while reintentos > 0 and (numero < minimo or numero > maximo):
            numero = input(mensaje_error)
            numero = float(numero)
        
            reintentos -= 1

        return numero

# pedir_numero = get_float("Ingrese un numero: ", "Error. Ingrese un numero: ", 20.0, 40.0, 3)


def get_string(mensaje: str, mensaje_error: str, longitud: int, reintentos: int) -> int|None:
        string = input(mensaje)
        string = len(string)

        while reintentos > 0 and (string != longitud):
            string = input(mensaje_error)
            string = len(string)

            reintentos -= 1

        return string

# pedir_string = get_string("Escriba una string: ", "Error, no coicide con la cantidad de letras: ", 6, 3)


## RECURSIVIDAD ##

def cuenta_regresiva(iteracion):
      if iteracion != -1:
            print(iteracion)
            iteracion -= 1
            cuenta_regresiva(iteracion)


# cuenta_regresiva(100)

numero = 5
factorial = 0

for i in range(1, numero + 1):
      factorial = numero * i - 1

# print(factorial)


def factorial(numero):
      if numero == 0:
            return 1
      else:
            return numero * factorial(numero - 1)
      
# resultado = factorial(5)
# print(resultado)

# Mini parcilito

def calcular_precio_con_o_sin_descuento(precio: int|float, cantidad: int, porcentaje_descuento: int):

    if cantidad > 10:
        precio_total = precio * cantidad
        descuento = precio_total * (porcentaje_descuento / 100)
        precio_con_descuento = precio_total - descuento

        return precio_con_descuento
    
    else:
        return precio * cantidad
    
resultado = calcular_precio_con_o_sin_descuento(100, 80, 40)
print(resultado)
