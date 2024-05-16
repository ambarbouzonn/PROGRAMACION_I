class Personaje:
    # ATRIBUTOS



    # METODOS
    def __init__(self, nombre: str, nano: bool, vuela: bool, poder: str, pelea: int):
        self.nombre = nombre
        self.usa_nanotecnologia = nano
        self.puede_volar = vuela
        self.super_poder = poder
        self.pelea = pelea
    
    def describerse(self):
        cadena = f"{self.nombre}-{self.super_poder}-{self.pelea}"
        if self.usa_nanotecnologia == True:
            cadena += "- Usa nanotecnologia"
        else:
            cadena += "- No usa nanotecnologia"
        
        return cadena
    
    def volar(self, altura, velocidad):
        if self.puede_volar:
            print(f"Estoy volando a {altura} mts de altura, a una velocidad de {velocidad} km/h")
        else:
            print(f"{self.nombre} usted no puede volar")


    def atacar(self, enemigo: "Personaje"):
        if self.pelea > enemigo.pelea:
            print(f"Gano {self.nombre}")
            self.pelea -= enemigo.pelea
            enemigo.pelea = 0

        elif self.pelea < enemigo.pelea:
            print(f"Gano {enemigo.nombre}")
            enemigo.pelea -= self.pelea
            self.pelea = 0

        else:
            print("Empataron.")