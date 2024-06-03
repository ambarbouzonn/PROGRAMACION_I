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

    # A
    def normalizar_videos(videos):
        for video in videos:
            video.dividir_titulo()
            video.obtener_codigo_url()
            video.formatear_fecha()


    # B
    def mostrar_temas(videos):
        for video in videos:
            video.mostrar_tema()
        

    # C
    def ordenar_sesion(videos):
        videos.sort(key=lambda video: int(video.sesion))
        print("Sesiones ordenadas por número:")


    # D
    def promedio_vistas(videos):
        total_videos = len(videos)

        if total_videos == 0:
            print("No hay videos en la lista.")
            return
        
        suma = sum(video.vistas for video in videos)
        promedio = suma / total_videos
        
        print(f"El promedio de vistas es: {promedio:,}")

    
    # E
    def max_vistas(videos):
        if not videos:
            print("No hay videos en la lista.")
            return
        
        max_video = videos[0]
        for video in videos[1:]:
            if video.vistas > max_video.vistas:
                max_video = video
        
        print("El video con más vistas es:")
        max_video.mostrar_tema()

    
    # F
    def buscar_codigo(videos, codigo_inicio: str):
        resultados = [video for video in videos if video.codigo_url.startswith(codigo_inicio)]
        if not resultados:
            print(f"No se encontraron videos cuyo código comiencen con '{codigo_inicio}'")
        else:
            print(f"Videos cuyo código comienzan con '{codigo_inicio}':")
            for video in resultados:
                video.mostrar_tema()


    # G
    def listar_por_colaborador(videos):
        colaborador = input("Ingrese el nombre del colaborador: ").capitalize()
        resultados = [video for video in videos if video.colaborador and video.colaborador.lower() == colaborador.lower()]
        if not resultados:
            print(f"No se encontraron videos del colaborador '{colaborador}'")
        else:
            print(f"Videos del colaborador '{colaborador}':")
            for video in resultados:
                video.mostrar_tema()

    # H
    def listar_por_mes(videos):
        mes = int(input("Ingrese el mes que desea buscar: "))
        resultados = [video for video in videos if video.fecha_lanzamiento.month == mes]
        if not resultados:
            print(f"No se encontraron videos lanzados en el mes {mes}.")
        else:
            print(f"Videos lanzados en el mes {mes}:")
            for video in resultados:
                video.mostrar_tema()
        

