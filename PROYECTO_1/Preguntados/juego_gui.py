import tkinter as tk
from tkinter import messagebox
from juego import JuegoPreguntados
import random

class JuegoGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Preguntados")
        self.juego = JuegoPreguntados()
        self.pregunta_label = tk.Label(root, text="")
        self.pregunta_label.pack()
        self.respuesta_var = tk.StringVar()
        self.respuesta_entry = tk.Entry(root, textvariable=self.respuesta_var)
        self.respuesta_entry.pack()
        self.respuesta_button = tk.Button(root, text="Responder", command=self.responder)
        self.respuesta_button.pack()
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
        self.pregunta_label.config(text=f"{self.pregunta['pregunta']}\n\n{''.join([f'{i+1}. {opcion}\n' for i, opcion in enumerate(self.pregunta['opciones'])])}")

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