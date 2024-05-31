from Input import *

# C
def crear_alumno(dni: int, nombre: str, apellido: str, nota: int) -> dict:
    dicionario_alumno = {
        "dni": dni,
        "nombre": nombre,
        "apellido": apellido,
        "nota": nota
    }

    return dicionario_alumno

def ingresar_alumno_lista(lista_alumnos: list[dict]):
    dni = int(input("Ingrese su DNI: ")) # Usar get string
    nombre = input("Ingrese su nombre: ").capitalize() # Usar get string
    apellido = input("Ingrese su apellido: ").capitalize() # Usar get string
    nota = int(input("Ingrese su nota de forma numerica: ")) # Usar get int

    dicionario_alumno = crear_alumno(dni, nombre, apellido, nota)

    lista_alumnos.append(dicionario_alumno)


# R
def mostrar_lista_alumnos(lista_alumnos: list[dict]):
    for alumno in lista_alumnos:
        mostrar_un_almuno(alumno)

def mostrar_un_almuno(un_alumno: dict):
    print(f"{un_alumno["dni"]} - {un_alumno["nombre"]} - {un_alumno["apellido"]} - {un_alumno["nota"]}")


# U
def modificar_alumno(lista_alumnos: list[dict], dni: int): # Generar mas validaciones, si encontro o no, y si puedo modificar o no
    for alumno in lista_alumnos:
        if alumno["dni"] == dni:
            print("Alumno encontrado")
            nueva_nota = int(input("Ingrese la nuena nota: "))
            alumno["nota"] = nueva_nota
            break
        
# D
def elimiar_alumno(lista_alumnos: list[dict], dni: int): # No hay que sacarlo del sistema, solo de la lista
    eliminado = None
    for alumno in lista_alumnos:
        if alumno["dni"] == dni:
            mostrar_un_almuno(alumno)
            eliminado = alumno
            break

    if eliminado != None:
        lista_alumnos.remove(eliminado)


