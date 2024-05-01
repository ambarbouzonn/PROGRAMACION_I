from Input import *

def validate_number(numero: int, mensaje_error: str,  minimo: int, maximo: int, reintentos: int) -> int:
    numero = int(numero)

    while reintentos > 0 and (numero < minimo or numero > maximo):
        numero = input(mensaje_error)
        numero = int(numero)

        reintentos -= 1

    return numero
# mensaje = validate_number(f"Ingrese un numero: ", "Error, ingrese otro numero: ", 20, 50, 3)

def validate_lenght(mensaje: str, mensaje_error: str, longitud: int, reintentos: int) -> str | None:
    string = input(mensaje)
    string = len(string)

    if string == longitud:
        return string
    else:
        while reintentos > 0:
            string = input(mensaje_error)

            reintentos -= 1

# validacion = get_string("Ingrese un string: ", "La longitud de caracter ingresada es incorrcta, vuelva a ingresarlo: ", 6, 3)


