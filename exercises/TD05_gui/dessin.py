import tkinter as tk



racine = tk.Tk()
racine.title('Mon dessin')

bouton = tk.Button(racine, text="choisir une couleur", font = ("helvetica", "10"), activebackground = '#BBBBBB')
bouton1 = tk.Button(racine, text="cercle", font = ("helvetica", "10"), activebackground = '#D8D0AA')
bouton2 = tk.Button(racine, text="carré", font = ("helvetica", "10"), activebackground = '#A0AACC')
bouton3 = tk.Button(racine, text="croix", font = ("helvetica", "10"), activebackground = '#DFAAAA')

bouton.grid(column = 1, row= 0)
bouton1.grid(column = 0, row= 1)
bouton2.grid(column = 0, row= 2)
bouton3.grid(column = 0, row= 3)



canvas = tk.Canvas(racine, bg='black', height=500, width=500)
canvas.grid(column= 1, row = 1, rowspan = 3)

racine.mainloop() # Lancement de la boucle principale