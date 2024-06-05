from class_boligrafo import Bolígrafo

# Función para obtener entrada del usuario
def obtener_datos_boligrafo():
    color = input("Ingrese el color del bolígrafo: ")
    grosor_punta = input("Ingrese el grosor de la punta (Fino/Grueso): ")
    return color, grosor_punta

# Crear bolígrafos a partir de la entrada del usuario
color_azul, grosor_azul = obtener_datos_boligrafo()
color_rojo, grosor_rojo = obtener_datos_boligrafo()

boligrafo_azul = Bolígrafo(color_azul, grosor_azul)
boligrafo_rojo = Bolígrafo(color_rojo, grosor_rojo)

# Mostrar estado inicial
print(f"Bolígrafo {color_azul} - Tinta: {boligrafo_azul.cantidad_tinta}, Grosor: {boligrafo_azul.grosor_punta}")
print(f"Bolígrafo {color_rojo} - Tinta: {boligrafo_rojo.cantidad_tinta}, Grosor: {boligrafo_rojo.grosor_punta}")

# Escribir con ambos bolígrafos
texto = input("Ingrese el texto a escribir: ")
resultado_azul = boligrafo_azul.escribir(texto)
resultado_rojo = boligrafo_rojo.escribir(texto)

# Mostrar resultados de escritura
print(f"Resultado de escribir con bolígrafo {color_azul}: {resultado_azul}")
print(f"Resultado de escribir con bolígrafo {color_rojo}: {resultado_rojo}")

# Mostrar estado de tinta después de escribir
print(f"Bolígrafo {color_azul} - Tinta restante: {boligrafo_azul.cantidad_tinta}")
print(f"Bolígrafo {color_rojo} - Tinta restante: {boligrafo_rojo.cantidad_tinta}")

# Recargar bolígrafos
cantidad_recarga_azul = int(input(f"Ingrese la cantidad de tinta para recargar el bolígrafo {color_azul}: "))
cantidad_recarga_rojo = int(input(f"Ingrese la cantidad de tinta para recargar el bolígrafo {color_rojo}: "))

recarga_azul = boligrafo_azul.recargar(cantidad_recarga_azul)
recarga_rojo = boligrafo_rojo.recargar(cantidad_recarga_rojo)

# Mostrar resultados de recarga
print(f"Resultado de recargar bolígrafo {color_azul}: {recarga_azul}")
print(f"Resultado de recargar bolígrafo {color_rojo}: {recarga_rojo}")

# Mostrar estado final
print(f"Bolígrafo {color_azul} - Tinta final: {boligrafo_azul.cantidad_tinta}")
print(f"Bolígrafo {color_rojo} - Tinta final: {boligrafo_rojo.cantidad_tinta}")
