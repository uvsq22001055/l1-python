import tkinter as tk
import random

CANVAS_WIDTH, CANVAS_HEIGHT = 500, 500

# disque de diamètre 100 en bleu à un endroit choisi au hasard dans le canevas. Le cercle doit être inclu intégralement dans le canevas.
def Disque():
    x = random.randint(0, CANVAS_WIDTH-100)
    y = random.randint(0, CANVAS_HEIGHT-100)
    canvas.create_oval(x, y, x + 100, y +100, fill = 'blue')
    return

def Rectangle():
    x = random.randint(0, CANVAS_WIDTH-100)
    y = random.randint(0, CANVAS_HEIGHT-100)
    canvas.create_rectangle(x, y, x + 100, y +100, fill = 'red')
    return

def Croix():
    x = random.randint(0, CANVAS_WIDTH-100)
    y = random.randint(0, CANVAS_HEIGHT-100)
    canvas.create_line(x -20, y + 20, x + 20, y - 20, fill = 'yellow', width = '5')
    canvas.create_line(x-20, y -20 , x + 20, y + 20, fill = 'yellow', width = '5')
    
    return

racine = tk.Tk()
racine.title('Mon dessin')

bouton = tk.Button(racine, text="choisir une couleur", font = ("helvetica", "10"), activebackground = '#BBBBBB', overrelief = 'groove')
bouton1 = tk.Button(racine, text="cercle", command = Disque, font = ("helvetica", "10"), activebackground = '#A0AACC')
bouton2 = tk.Button(racine, text="carré", command = Rectangle, font = ("helvetica", "10"), activebackground = '#DFAAAA')
bouton3 = tk.Button(racine, text="croix", command = Croix, font = ("helvetica", "10"), activebackground = '#D8D0AA')

bouton.grid(column = 1, row= 0)
bouton1.grid(column = 0, row= 1)
bouton2.grid(column = 0, row= 2)
bouton3.grid(column = 0, row= 3)



canvas = tk.Canvas(racine, bg='white', height=CANVAS_HEIGHT, width=CANVAS_HEIGHT, borderwidth = '10', relief = 'sunken')
canvas.grid(column= 1, row = 1, rowspan = 3)

racine.mainloop() # Lancement de la boucle principale