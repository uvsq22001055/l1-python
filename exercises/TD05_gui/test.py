import tkinter as tk
import random as rd

CANVAS_WIDTH, CANVAS_HEIGHT = 256, 256

racine = tk.Tk()

canvas = tk.Canvas(racine, bg='black', height=CANVAS_HEIGHT, width=CANVAS_HEIGHT)


def get_color(r, g, b):
    """ Retourne une couleur à partir de ses composantes r, g, b entre 0 et 255"""
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)

def draw_pixel(i, j, color):
    pixel = canvas.create_rectangle(i, j, i, j, fill = color, width=0)
    return pixel





degrade_gris()

canvas.grid()




racine.mainloop()