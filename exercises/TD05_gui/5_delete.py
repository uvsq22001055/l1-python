import tkinter as tk
import random

CANVAS_WIDTH, CANVAS_HEIGHT = 500, 500


objets = []


# disque de diamètre 100 en bleu à un endroit choisi au hasard dans le canevas. Le cercle doit être inclu intégralement dans le canevas.
def Disque():
    global objets
    x = random.randint(0, CANVAS_WIDTH-99)
    y = random.randint(0, CANVAS_HEIGHT-99)
    cercle = canvas.create_oval(x, y, x + 100, y +100, fill = color)
    objets.append(cercle)
    

def Rectangle():
    global objets
    x = random.randint(0, CANVAS_WIDTH-99)
    y = random.randint(0, CANVAS_HEIGHT-99)
    rect = canvas.create_rectangle(x, y, x + 100, y +100, fill = color)
    objets.append(rect)

def Croix():
    global objets
    x = random.randint(0, CANVAS_WIDTH-99)
    y = random.randint(0, CANVAS_HEIGHT-99)
    line1 =canvas.create_line((x, y), (x+100, y+100), fill = color)
    line2 =canvas.create_line((x+100, y), (x, y +100), fill = color)
    objets.append(line1)
    objets.append(line2)
    

def Choisir_couleur():
    global color
    color = input("choisis une couleur:")

def Undo():
    global objets
    if not(objets):
        return
    else:
        if canvas.type(objets[-1]) == 'line':
            canvas.delete(objets[-1])
            canvas.delete(objets[-2])
            del objets[-1]
            del objets[-1]
        else:
            canvas.delete(objets[-1])
            del objets[-1]

racine = tk.Tk()
racine.title('Mon dessin')



bouton = tk.Button(racine, text="choisir une couleur", command = Choisir_couleur, font = ("helvetica", "10"), activebackground = '#BBBBBB', overrelief = 'groove')
bouton_u=tk.Button(racine, text='Undo', command=Undo, font = ("helvetica", "10"), activebackground = '#BBBBBB', overrelief = 'groove')
bouton1 = tk.Button(racine, text="cercle", command = Disque, font = ("helvetica", "10"), activebackground = '#A0AACC')
bouton2 = tk.Button(racine, text="carré", command = Rectangle, font = ("helvetica", "10"), activebackground = '#DFAAAA')
bouton3 = tk.Button(racine, text="croix", command = Croix, font = ("helvetica", "10"), activebackground = '#D8D0AA')



bouton.grid(column = 1, row= 0)
bouton_u.grid(column=2, row=0)
bouton1.grid(column = 0, row= 1)
bouton2.grid(column = 0, row= 2)
bouton3.grid(column = 0, row= 3)


canvas = tk.Canvas(racine, bg='black', height=CANVAS_HEIGHT, width=CANVAS_HEIGHT, borderwidth = '10', relief = 'sunken')
canvas.grid(column= 1, row = 1, rowspan = 3, columnspan =2)

racine.mainloop() # Lancement de la boucle principale
print(objets)