def get_color(r, g, b):
    """ Retourne une couleur à partir de ses composantes r, g, b entre 0 et 255"""
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)

import tkinter as tk 

racine = tk.Tk()

button1 = tk.Button(racine, text="aléatoire", font=("Courier", "26"))
button2 = tk.Button(racine, text = "dégradé gris", font=("Courier", "26"))
button3 = tk.Button(racine, text = "dégradé 2D", font=("Courier", "26"))

button1.grid(column=0, row=0)
button2.grid(column=0, row=1)
button3.grid(column=0, row=2)

racine.mainloop()