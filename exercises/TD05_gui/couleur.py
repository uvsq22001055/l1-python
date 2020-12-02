import tkinter as tk

CANVAS_WIDTH, CANVAS_HEIGHT = 256, 256

racine = tk.Tk()

canvas = tk.Canvas(racine, bg='black', height=CANVAS_HEIGHT, width=CANVAS_HEIGHT, borderwidth = '10', relief = 'sunken')


def get_color(r, g, b):
    """ Retourne une couleur à partir de ses composantes r, g, b entre 0 et 255"""
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)

def draw_pixel(i, j, color):
    pixel = canvas.create_rectangle(i, i, j, j, fill = color, width=0)
    return pixel

draw_pixel(128, 129, 'white')

bouton1 = tk.Button(racine, text="Aléatoire", font = ("Courier", "20"), activebackground = '#BBBBBB', foreground='blue')
bouton2 = tk.Button(racine, text="Dégradé gris", font = ("Courier", "20"), activebackground = '#BBBBBB',foreground='blue')
bouton3 = tk.Button(racine, text="Dégradé 2D", font = ("Courier", "20"), activebackground = '#BBBBBB', foreground='blue')


bouton1.grid(column = 0, row= 0)
bouton2.grid(column = 0, row= 1)
bouton3.grid(column = 0, row= 2)
canvas.grid(column= 1, row = 0, rowspan = 3)




racine.mainloop()