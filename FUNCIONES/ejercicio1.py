# Reciba un numero y determine si ese numero es par o no.

def es_par_o_impar(numero):
    if numero % 2 == 0:
        mensaje = "Par"
    else:
        mensaje = "Impar"
    return  mensaje

numero = input("Ingrese un numero: ")
numero = int(numero)
resultado = es_par_o_impar(numero)
print(f"El numero es {numero} y es {resultado}")