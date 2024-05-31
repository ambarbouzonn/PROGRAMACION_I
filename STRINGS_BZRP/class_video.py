from datetime import datetime

class Video:
    def __init__(self, titulo: str, vistas: int, tiempo: int, url_youtube: str, fecha_lanzamiento: str):
        self.titulo = titulo
        self.vistas = vistas
        self.tiempo = tiempo
        self.url_youtube = url_youtube
        self.fecha_lanzamiento = fecha_lanzamiento
        self.sesion = None
        self.colaborador = None
        self.codigo_url = None
        
    def mostrar_tema(self):
        #Agregar los datos pertinentes para que a la hora de mostrar se vean los datos completos del video
        print(f"Titulo: {self.titulo}")
        print(f"Vistas: {self.vistas}")
        print(f"Duración: {self.tiempo} segundos")
        print(f"URL de YouTube: {self.url_youtube}")
        print(f"Fecha de Lanzamiento: {self.fecha_lanzamiento.strftime("%d-%m-%Y")}")
        print("*"*30)

    def dividir_titulo(self):
        #Debe setear el atributo sesion y colaborador con los datos obtenidos del 
        #titulo del video
        partes = self.titulo.split(" | Sesión #")
        if len(partes) == 2:
            self.colaborador = partes[0]
            self.sesion = partes[1]

            print(f"Colaborador: {self.colaborador}")
            print(f"Sesión: {self.sesion}")
        
    
    def obtener_codigo_url(self):
        #Debe setear el atributo codigo_url con el codigo obtenido del atributo url_youtube
        #Por ej: si la url es https://www.youtube.com/watch?v=nicki13 
        #el codigo seria nicki13
        self.codigo_url = self.url_youtube.split("v=")[1]

    
    def formatear_fecha(self):
        #Necesitamos que la fecha de lanzamiento sea un objeto de la clase datetime (investigar).
        #Para ello deberán dividir la fecha (en formato string) en dia, mes y año y a partir de 
        #esos datos, crear la nueva fecha. 

        fecha_lanzamiento  = self.fecha_lanzamiento.split("-")
        self.fecha_lanzamiento = datetime(int(fecha_lanzamiento[0]), int(fecha_lanzamiento[1]), int(fecha_lanzamiento[2]))

    
    def normalizar_videos(videos):
        for video in videos:
            video.dividir_titulo()
            video.obtener_codigo_url()
            video.formatear_fecha()

    def mostrar_temas(videos):
        for video in videos:
            video.mostrar_tema()

    def obtener_sesion(self):
        pass
        


    def ordenar_sesion(videos):
        return sorted(videos, key=)
    


# video = Video("Trueno | Sesión #1", 25000000, 210, "https://www.youtube.com/watch?v=trueno1", "2020-06-05")
# video.dividir_titulo()
# video.obtener_codigo_url()
# video.formatear_fecha()
# video.mostrar_tema()
# print(f"Colaborador: {video.colaborador}")
# print(f"Sesión: {video.sesion}")
# print(f"Código URL: {video.codigo_url}")

