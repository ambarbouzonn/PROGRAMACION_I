from juego import JuegoPreguntados
import random

def main():
    while True:
        juego = JuegoPreguntados()
        puntos_por_categoria = {categoria: 0 for categoria in juego.categorias}
        print("¡Bienvenido a Preguntados!")
        while len(juego.preguntas_utilizadas) < len(juego.categorias):
            pregunta = juego.obtener_pregunta()
            print("Categoría:", pregunta["categoria"])
            print(pregunta["pregunta"])
            print()  # Espacio adicional
            for i, opcion in enumerate(pregunta["opciones"], start=1):
                print(f"{i}. {opcion}")
            print()  # Espacio adicional
            respuesta_usuario = input("Ingrese el número de la opción correcta (o 'q' para salir): ")
            print()  # Espacio adicional
            if respuesta_usuario.lower() == "q":
                break
            if respuesta_usuario.isdigit():
                if int(respuesta_usuario) >= 1 and int(respuesta_usuario) <= len(pregunta["opciones"]):
                    if juego.verificar_respuesta(pregunta, pregunta["opciones"][int(respuesta_usuario)-1]):
                        print("¡Respuesta correcta!")
                    else:
                        print("Respuesta incorrecta. La respuesta correcta es:", pregunta["respuesta"])
                else:
                    print("Opción inválida.")
            else:
                print("Opción inválida.")
            print()  # Espacio adicional
        for pregunta in juego.preguntas_utilizadas:
            puntos_por_categoria[pregunta["categoria"]] = juego.puntos_por_categoria[pregunta["categoria"]]
        print("Puntos por categoría:")
        for categoria, puntos in puntos_por_categoria.items():
            print(f"{categoria}: {puntos}")
        if respuesta_usuario.lower() == "q":
            break

if __name__ == "__main__":
    main()