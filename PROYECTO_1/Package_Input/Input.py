# Realizar un paquete denominado Package_Input, el mismo deberá contener los siguientes módulos:
# Input.py
# get_int()
# get_float()
# get_string()

# Validate.py
# validate_number()
# validate_length()

# Nota: estas funciones las tendrán que desarrollar en el módulo Validate y utilizar en el módulo Input.py para realizar las validaciones necesarias.


def get_int(mensaje: str, mensaje_error: str, minimo: int, maximo: int, reintentos: int) -> int|None:
        numero = input(mensaje)
        numero = int(numero)

        while reintentos > 0 and (numero < minimo or numero > maximo):
            numero = input(mensaje_error)
            numero = int(numero)
        
            reintentos -= 1

        return numero

def get_float(mensaje: str, mensaje_error: str, minimo: float, maximo: float, reintentos: int) -> float|None:
        numero = input(mensaje)
        numero = float(numero)

        while reintentos > 0 and (numero < minimo or numero > maximo):
            numero = input(mensaje_error)
            numero = float(numero)
        
            reintentos -= 1

        return numero

def get_string(mensaje: str, mensaje_error: str, longitud: int, reintentos: int) -> int|None:
        string = input(mensaje)
        string = len(string)

        while reintentos > 0 and (string != longitud):
            string = input(mensaje_error)
            string = len(string)

            reintentos -= 1

        return string   

