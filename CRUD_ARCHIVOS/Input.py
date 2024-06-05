import Validate as validate 


# Con intentos, max y min
def get_int(mensaje:str, mensaje_error:str, minimo:int, maximo:int, reintentos:int) -> int|None:
    
    number = int(input(f"{mensaje}"))

    for i in range(0, reintentos+1):
        
        if validate.validate_number(number, minimo, maximo):
            return number

        elif i+1 == reintentos:
            return None
        else:
            number = int(input(f"{mensaje_error}"))


# Con minimo
def get_int_2(mensaje: str, mensaje_error: str, minimo: int) -> int:
    while True:
        numero = input(mensaje)

        if numero.isalpha() or numero == "":
            print(mensaje_error)
            continue

        numero = int(numero)

        if numero > minimo:
            return numero
        else:
            print(mensaje_error)

# Con min y max
def get_int_3(mensaje: str, mensaje_error: str, minimo: int, maximo: int) -> int:
    while True:
        numero = input(mensaje)

        if numero.isalpha() or numero == "":
            print(mensaje_error)
            continue

        numero = int(numero)

        if maximo > numero > minimo:
            return numero
        else:
            print(mensaje_error)

        

def get_float(mensaje:str, mensaje_error:str, minimo:float, maximo:float, reintentos:int) -> float|None:
    
    number = float(input(f"{mensaje}"))

    for i in range(0, reintentos+1):
        
        if validate.validate_number(number, minimo, maximo):
            return number

        elif i+1 == reintentos:
            return None
        else:
            number = float(input(f"{mensaje_error}"))

def get_string(mensaje:str, mensaje_error:str, longitud:int, reintentos:int) -> str|None:

    string = input(f"{mensaje}")

    for i in range(0, reintentos+1):
    
        if validate.validate_length(string, longitud):
            return string
        
        elif i+1 == reintentos:
            return None
        
        else:
            string = input(f"{mensaje_error}")


def get_string_2(mensaje: str, mensaje_error: str, longuitud_max: int) -> str:
    while True:
        caracteres = input(mensaje).strip().capitalize()
        if len(caracteres) <= longuitud_max and caracteres.isalpha():
            return caracteres
        else:
            print(mensaje_error)


