import tkinter as tk
from tkinter import PhotoImage
from juego import Juego
from mazo import *

class BlackjackGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Blackjack")

        self.canvas = tk.Canvas(root, width=800, height=600)
        self.canvas.pack()

        self.juego = Juego(MazoFrances())
        self.juego.iniciar_juego()

        self.cargar_imagenes()

        self.jugar_button = tk.Button(root, text="Jugar", command=self.jugar)
        self.jugar_button.pack()

        self.valorar_button = tk.Button(root, text="Valorar", command=self.valorar)
        self.valorar_button.pack()

    def cargar_imagenes(self):
        self.imagenes_cartas = []
        for carta in self.juego.jugador2.cartas:
            imagen = PhotoImage(file=f"carta_img/{carta.pinta}_{carta.valor}.png")
            self.imagenes_cartas.append(imagen)

        # Muestra las imágenes de las cartas del jugador en el canvas
        x, y = 100, 300
        for imagen in self.imagenes_cartas:
            self.canvas.create_image(x, y, image=imagen)
            x += 50  # Ajusta la posición de la siguiente carta

    def jugar(self):
        self.juego.jugar()
        self.cargar_imagenes()

    def valorar(self):
        self.juego.valorar_juego()

if __name__ == '__main__':
    root = tk.Tk()
    app = BlackjackGUI(root)
    root.mainloop()
