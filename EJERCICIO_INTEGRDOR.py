
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


for ingresos in range(1, 11):

    # Solicitar nombre
    nombre_empleado = input("Ingrese su nombre: ")

    # Solicitar edad
    edad = input("Ingrese su edad: ")
    edad = int(edad)

    while edad < 18:
        edad = input("Ingrese su edad correspondiente: ")
        edad = int(edad)

    # Solicitar genero
    genero = input("Ingrese la primera letra de su genero (Femenino, Masculino, Otro): ")

    while genero != "F" and genero != "M" and genero != "O":
        genero = input("Ingrese su genero: ")

    # Solicitar tecnologia (IA, RV/RA, IOT)
    tecnologia = input("Ingrese la tecnologia que utiliza (IA, RV/RA, IOT): ")

    while tecnologia != "IA" and tecnologia != "RV" and tecnologia != "RA" and tecnologia != "IOT":
        tecnologia = input("Ingrese la tecnologia que utiliza (IA, RV/RA, IOT): ")

        
    
    print(nombre_empleado)
    print(edad)
    print(genero)
    print(tecnologia)


            
                



    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()

        
            