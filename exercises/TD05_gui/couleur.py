import tkinter as tk

CANVAS_WIDTH, CANVAS_HEIGHT = 400, 400

racine = tk.Tk()

def get_color(r, g, b):
    """ Retourne une couleur à partir de ses composantes r, g, b entre 0 et 255"""
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)

bouton1 = tk.Button(racine, text="Aléatoire", font = ("Courier", "30"), activebackground = '#BBBBBB', foreground='blue')
bouton2 = tk.Button(racine, text="Dégradé gris", font = ("Courier", "30"), activebackground = '#BBBBBB',foreground='blue')
bouton3 = tk.Button(racine, text="Dégradé 2D", font = ("Courier", "30"), activebackground = '#BBBBBB', foreground='blue')


bouton1.grid(column = 0, row= 0)
bouton2.grid(column = 0, row= 1)
bouton3.grid(column = 0, row= 2)


canvas = tk.Canvas(racine, bg='black', height=CANVAS_HEIGHT, width=CANVAS_HEIGHT, borderwidth = '10', relief = 'sunken')
canvas.grid(column= 1, row = 0, rowspan = 3)


racine.mainloop()