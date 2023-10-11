import tkinter as tk
from tkinter import PhotoImage
from juego import Juego
from mazo import *

class BlackjackGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Blackjack")

        self.canvas = tk.Canvas(root, width=1500, height=950)
        self.canvas.pack()

        self.juego = Juego(MazoFrances())
        self.juego.iniciar_juego()

        self.texto_valor_jugador = self.canvas.create_text(200, 900, text="", anchor='w')
        self.texto_valor_casa = self.canvas.create_text(200, 470, text="", anchor='w')

        self.cargar_imagenes()
        
        self.jugar_button = tk.Button(root, text="Jugar", command=self.jugar)
        self.jugar_button.pack()
        
        self.valorar_button = tk.Button(root, text="Valorar", command=self.valorar)
        self.valorar_button.pack()

    def cargar_imagenes(self):
        self.canvas.delete(self.texto_valor_jugador)
        self.canvas.delete(self.texto_valor_casa)

        self.imagenes_cartas_jugador = []
        self.imagenes_cartas_casa = []
        for carta in self.juego.jugador2.cartas:
            imagen = PhotoImage(file=f"carta_img/{carta.pinta}_{carta.valor}.png")
            self.imagenes_cartas_jugador.append(imagen)

        for carta in self.juego.jugador1.cartas:
            imagen = PhotoImage(file=f"carta_img/{carta.pinta}_{carta.valor}.png")
            self.imagenes_cartas_casa.append(imagen)

        # Muestra las imágenes de las cartas del jugador en el canvas
        x, y = 100, 700
        for imagen in self.imagenes_cartas_jugador:
            self.canvas.create_image(x, y, image=imagen)
            x += 50  # Ajusta la posición de la siguiente carta

        # Muestra las imágenes de las cartas de la casa en el canvas
        x, y = 100, 300
        for imagen in self.imagenes_cartas_casa:
            self.canvas.create_image(x, y, image=imagen)
            x += 50

        # Muestra el valor de la mano del jugador
        valor_jugador = self.juego.jugador2.obtener_valor_mazo()
        self.texto_valor_jugador = self.canvas.create_text(200, 900, text=f"Valor del Jugador: {valor_jugador}", anchor='w')

        # Muestra el valor de la mano de la casa
        valor_casa = self.juego.jugador1.obtener_valor_mazo()
        self.texto_valor_casa = self.canvas.create_text(200, 470, text=f"Valor de la Casa: {valor_casa}", anchor='w')

    def jugar(self):
        self.juego.jugar()
        self.cargar_imagenes()

    def valorar(self):
        self.juego.valorar_juego()
        ganador = self.determinar_ganador()
        self.canvas.create_text(800, 400, text=f"Ganador: {ganador}", font=("Helvetica", 24))

    def determinar_ganador(self):
        valor_jugador = self.juego.jugador2.obtener_valor_mazo()
        valor_casa = self.juego.jugador1.obtener_valor_mazo()

        if valor_jugador > 21:
            return "Casa"
        elif valor_casa > 21:
            return "Jugador"
        elif valor_jugador > valor_casa:
            return "Jugador"
        elif valor_casa > valor_jugador:
            return "Casa"
        else:
            return "Empate"

if __name__ == '__main__':
    root = tk.Tk()
    app = BlackjackGUI(root)
    root.mainloop()
