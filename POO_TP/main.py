# Archivo: main.py

from class_boligrafo import Bolígrafo

# Crear bolígrafos
boligrafo_azul = Bolígrafo("Azul", "Fino")
boligrafo_rojo = Bolígrafo("Rojo", "Grueso")

# Mostrar estado inicial
print(f"Bolígrafo Azul - Tinta: {boligrafo_azul.cantidad_tinta}, Grosor: {boligrafo_azul.grosor_punta}")
print(f"Bolígrafo Rojo - Tinta: {boligrafo_rojo.cantidad_tinta}, Grosor: {boligrafo_rojo.grosor_punta}")

# Escribir con ambos bolígrafos
resultado_azul = boligrafo_azul.escribir("Hola Mundo")
resultado_rojo = boligrafo_rojo.escribir("Hola Mundo")

# Mostrar resultados de escritura
print(f"Resultado de escribir con bolígrafo azul: {resultado_azul}")
print(f"Resultado de escribir con bolígrafo rojo: {resultado_rojo}")

# Mostrar estado de tinta después de escribir
print(f"Bolígrafo Azul - Tinta restante: {boligrafo_azul.cantidad_tinta}")
print(f"Bolígrafo Rojo - Tinta restante: {boligrafo_rojo.cantidad_tinta}")

# Recargar bolígrafos
recarga_azul = boligrafo_azul.recargar(30)
recarga_rojo = boligrafo_rojo.recargar(50)

# Mostrar resultados de recarga
print(f"Resultado de recargar bolígrafo azul: {recarga_azul}")
print(f"Resultado de recargar bolígrafo rojo: {recarga_rojo}")

# Mostrar estado final
print(f"Bolígrafo Azul - Tinta final: {boligrafo_azul.cantidad_tinta}")
print(f"Bolígrafo Rojo - Tinta final: {boligrafo_rojo.cantidad_tinta}")
