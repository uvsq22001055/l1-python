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


def ecran_aleatoire():
    for i in range(0, 258):
        for j in range(0, 258):
            list_color = ['white', 'black', 'red', 'green', 'blue', 'cyan', 'yellow', 'magenta']
            color = rd.choice(list_color)
            draw_pixel(i, j, color)

def degrade_gris():
    c = 0    
    for i in range(0, 258):
        color = get_color(c, c, c)
        for j in range(0, 258):
            draw_pixel(i, j, color)
        c += 1

def degrade_2D():
    r = 0
    b = 0
    for i in range(0, 255):
        color = get_color(r, 0, b)
        for j in range(255, 0, -1):
            draw_pixel(j, j, color)
        
        
        r += 1
        b += 1





bouton1 = tk.Button(racine, text="Aléatoire", font = ("Courier", "20"), command = ecran_aleatoire , activebackground = '#BBBBBB', foreground='blue')
bouton2 = tk.Button(racine, text="Dégradé gris", command = degrade_gris , font = ("Courier", "20"), activebackground = '#BBBBBB',foreground='blue')
bouton3 = tk.Button(racine, text="Dégradé 2D", command = degrade_2D, font = ("Courier", "20"), activebackground = '#BBBBBB', foreground='blue')


bouton1.grid(column = 0, row= 0)
bouton2.grid(column = 0, row= 1)
bouton3.grid(column = 0, row= 2)
canvas.grid(column= 1, row = 0, rowspan = 3)




racine.mainloop()