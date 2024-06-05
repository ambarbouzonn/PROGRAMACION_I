class Bolígrafo:
    def __init__(self, color, grosor_punta):
        self.capacidad_tinta_maxima = 100
        self.cantidad_tinta = 80
        self.color = color
        self.grosor_punta = grosor_punta

    def escribir(self, texto):
        tinta_necesaria = len(texto)
        if self.grosor_punta.lower() == 'grueso':
            tinta_necesaria *= 2

        if tinta_necesaria <= self.cantidad_tinta:
            self.cantidad_tinta -= tinta_necesaria
            return texto
        else:
            return "No alcanza la tinta"

    def recargar(self, cantidad):
        if self.cantidad_tinta + cantidad <= self.capacidad_tinta_maxima:
            self.cantidad_tinta += cantidad
            return "Lapicera recargada"
        else:
            sobrante = (self.cantidad_tinta + cantidad) - self.capacidad_tinta_maxima
            self.cantidad_tinta = self.capacidad_tinta_maxima
            return f"Se recargó la lapicera y sobró {sobrante} cantidad de tinta"
