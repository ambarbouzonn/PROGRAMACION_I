import tkinter as tk
from tkinter import messagebox, font
from juego import JuegoPreguntados
import random

class JuegoGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Preguntados")
        self.root.geometry("400x300")
        self.juego = JuegoPreguntados()
        self.font = font.Font(family="Helvetica", size=12)
        self.colores = {"Arte": "red", "Historia": "yellow", "Geografía": "blue", "Química": "green"}
        self.pregunta_label = tk.Label(root, text="", font=self.font, wraplength=380, justify="center")
        self.pregunta_label.pack(pady=10)
        self.respuestas_frame = tk.Frame(root)
        self.respuestas_frame.pack(pady=10)
        self.respuesta_var = tk.StringVar()  # Se crea la variable de respuesta
        self.root.protocol("WM_DELETE_WINDOW", self.mostrar_puntos)
        self.siguiente_pregunta()

    def responder(self):
        respuesta_usuario = self.respuesta_var.get()
        if respuesta_usuario.lower() == "q":
            self.mostrar_puntos()
        elif respuesta_usuario.isdigit() and 1 <= int(respuesta_usuario) <= len(self.pregunta["opciones"]):
            if self.juego.verificar_respuesta(self.pregunta, self.pregunta["opciones"][int(respuesta_usuario)-1]):
                messagebox.showinfo("Respuesta", "¡Respuesta correcta!")
            else:
                messagebox.showinfo("Respuesta", f"Respuesta incorrecta. La respuesta correcta es: {self.pregunta['respuesta']}")
            self.respuesta_var.set("")  # Limpiar el cuadro de entrada
            self.siguiente_pregunta()
        else:
            messagebox.showerror("Error", "Opción inválida.")

    def siguiente_pregunta(self):
        self.pregunta = self.juego.obtener_pregunta()
        categoria = self.pregunta['categoria']
        self.pregunta_label.config(text=f"{self.pregunta['pregunta']}\n", fg="black", bg=self.colores.get(categoria, "white"))
        for widget in self.respuestas_frame.winfo_children():
            widget.destroy()  # Limpiar las opciones de respuesta anteriores
        # Mostrar opciones de respuesta
        for i, opcion in enumerate(self.pregunta['opciones']):
            respuesta_btn = tk.Button(self.respuestas_frame, text=f"{i+1}. {opcion}", font=self.font, bg=self.colores.get(categoria, "white"), fg="black", command=lambda opcion=opcion: self.responder_opcion(opcion))
            respuesta_btn.pack(side=tk.TOP, padx=10, pady=5)

    def responder_opcion(self, opcion):
        respuesta_index = self.pregunta['opciones'].index(opcion) + 1
        self.respuesta_var.set(str(respuesta_index))
        self.responder()

    def mostrar_puntos(self):
        puntos_por_categoria = self.juego.puntos_por_categoria
        puntos_texto = "\n".join([f"{categoria}: {puntos}" for categoria, puntos in puntos_por_categoria.items()])
        messagebox.showinfo("Puntos por categoría", puntos_texto)
        self.root.quit()

def main():
    root = tk.Tk()
    juego_gui = JuegoGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()