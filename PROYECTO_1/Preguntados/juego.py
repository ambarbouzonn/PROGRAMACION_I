import random
from preguntas import preguntas

class JuegoPreguntados:
    def __init__(self):
        self.categorias = list(preguntas.keys())
        self.puntos_por_categoria = {categoria: 0 for categoria in self.categorias}
        self.preguntas_utilizadas = []

    def obtener_pregunta(self):
        categoria = random.choice(self.categorias)
        preguntas_categoria = preguntas[categoria]
        pregunta = random.choice(preguntas_categoria)
        while pregunta in self.preguntas_utilizadas:
            pregunta = random.choice(preguntas_categoria)
        pregunta["categoria"] = categoria  # Añadir la categoría a la pregunta
        self.preguntas_utilizadas.append(pregunta)
        return pregunta

    def verificar_respuesta(self, pregunta, respuesta_usuario):
        es_correcta = respuesta_usuario == pregunta["respuesta"]
        if es_correcta:
            self.puntos_por_categoria[pregunta["categoria"]] += 1
        else:
            self.puntos_por_categoria[pregunta["categoria"]] = max(0, self.puntos_por_categoria[pregunta["categoria"]] - 1)
        return es_correcta