mi_lista = [-1] * 5

for i in range(len(mi_lista)):
    mi_lista[i] = int(input("Ingrese un numero: "))


for i in range(len(mi_lista)):
    print(mi_lista[i])
################################################################

bandera_salida = True

while bandera_salida == True:
    index = int(input("Ingrese la posicion: "))
    while index < 1 or index > len(mi_lista):
        index = int(input("Reingrese la posicion: "))

    numero = int(input("Ingrese un numero: "))

    mi_lista[index-1] = numero

    seguir = input("Continua? ")
    if seguir == "no":
        bandera_salida = False


for i in range(len(mi_lista)):
    if mi_lista[i] != -1:
        print(f"{i+1} -- {mi_lista[i]}")

##################################################################
lista = [45, 9, 3, -3, 100, -2, 3]


bandera_maximo = True

for i in range(len(lista)):
    if bandera_maximo == True or lista[i] > numero_maximo:
        numero_maximo = lista[i]
        bandera_maximo = False

print(f"El maximo numero de la lista es: {numero_maximo}")

#################################################################
lista = [45, 9, 3, -3, 100, -2, 3]

numero_buscado = 3
reemplazo = 1000

for i in range(len(lista)):
    if lista[i] == numero_buscado:
        lista[i] = reemplazo

for i in range(len(lista)):
    print(lista[i])

##################################################################

def sumar_positivos(lista: list) -> int|float:
    if type(lista) == list and len(lista) > 0:
        suma = 0
        for i in range(len(lista)):
            if lista[i] > 0:
                suma += lista[i]