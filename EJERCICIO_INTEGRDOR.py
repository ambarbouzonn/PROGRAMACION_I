
"""
Para ello, la empresa realiza entre sus empleados una encuesta, con el propósito de conocer ciertas métricas.

A) Los datos a ingresar por cada empleado encuestado son:
nombre del empleado
edad (no menor a 18)
género (Masculino - Femenino - Otro)
tecnologia (IA, RV/RA, IOT)  
B) Cargar por terminal 10 encuestas.
C) Determinar:
Cantidad de empleados de género masculino que votaron por IOT o IA, cuya edad esté entre 25 y 50 años inclusive.
Porcentaje de empleados que no votaron por IA, siempre y cuando su género no sea Femenino o su edad se encuentre entre los 33 y 40.
Nombre y tecnología que votó, de los empleados de género masculino con mayor edad de ese género.
"""

contador_masc_ia_iot = 0
contador_emp_no_IA = 0
total_empleados = 0
mayor_edad_masc = 150
nombre_mayor_edad_masc = ""
tecno_mayor_edad_masc = ""

for ingresos in range(1, 11):

    # Solicitar nombre
    nombre_empleado = input("Ingrese su nombre: ").capitalize()

    # Solicitar edad
    edad = input("Ingrese su edad: ")
    edad = int(edad)

    while edad < 18:
        edad = input("Ingrese su edad correspondiente: ")
        edad = int(edad)

    # Solicitar genero
    genero = input("Ingrese la primera letra de su genero (Femenino, Masculino, Otro): ").capitalize()

    while genero != "F" and genero != "M" and genero != "O":
        genero = input("Ingrese su genero: ")

    # Solicitar tecnologia (IA, RV/RA, IOT)
    tecnologia = input("Ingrese la tecnologia que utiliza (IA, RV/RA, IOT): ").upper()

    while tecnologia != "IA" and tecnologia != "RV" and tecnologia != "RA" and tecnologia != "IOT":
        tecnologia = input("Ingrese la tecnologia que utiliza (IA, RV/RA, IOT): ")


    # Contador de masculinos entre 25 y 50 años, y tecnologias IA o IOT
    if genero == "M" and tecnologia == "IA" and 25 <= edad <= 50:
        contador_masc_ia_iot += 1
    else:
        if genero == "M" and tecnologia == "IOT" and 25 <= edad <= 50:
            contador_masc_ia_iot += 1

    # Cantidad de empleados que no votaron por IA, su género no sea Femenino o su edad se encuentre entre los 33 y 40
    if (genero != "F" and edad <= 33 or edad >= 40 ) and tecnologia != "IA":
        contador_emp_no_IA += 1
    
    total_empleados += 1


    # Empleado de género masculino con mayor edad
    if genero == "M" and edad < mayor_edad_masc:
        mayor_edad_masc = edad
        nombre_mayor_edad_masc = nombre_empleado
        tecno_mayor_edad_masc = tecnologia
    else:
        if genero == "M" and edad > mayor_edad_masc:
            mayor_edad_masc = edad
            nombre_mayor_edad_masc = nombre_empleado
            tecno_mayor_edad_masc = tecnologia


# Porcentaje de empleados que no votaron por IA
if total_empleados > 0:
    porcentaje_emp_no_ia = (contador_emp_no_IA / total_empleados) * 100 
else: 
    porcentaje_emp_no_ia = 0

        
    

print(f"La cantidad de empleados que votaron por IA o por IOT, entre 25 y 50 años son: {contador_masc_ia_iot}")

print("El pocentaje de empleados que no votaron por IA, expluyendo si\n"
    f"son de genero Femenino o tienen entre 33 y 40 años: {porcentaje_emp_no_ia}")

print(f"El empleado de genero masculino de mayor edad\n"
      f"es: {nombre_mayor_edad_masc} de {mayor_edad_masc}, utilizando la tecnologia {tecno_mayor_edad_masc}")


    


        
        
            