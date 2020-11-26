import tkinter as tk

CANVAS_WIDTH, CANVAS_HEIGHT = 600, 400


root = tk.Tk()

canvas = tk.Canvas(root, width = CANVAS_WIDTH, height = CANVAS_HEIGHT)

# Début de votre code
x0 = 100 #ligne imaginaire vertical en x = 100unité depuis le bord gauche(centre du premier cercle a gauche)
x1 = CANVAS_WIDTH - 100 #ligne imaginaire vertical en x = -100unité depuis le bord droit(centre du premier cercle a droite)
y = CANVAS_HEIGHT / 2 #hauteur du centre de la feuille
canvas.create_line(x0, y, x1, y)  #ligne du point 1(x0, y) au point 2(x1, y)
canvas.create_oval(x0 - 50, y + 50, x0 + 50, y - 50) #creation ovale -> cerlce, de diametre 100 (cercle de gauche) de centre x0
canvas.create_oval(x1 - 50, y + 50, x1 + 50, y - 50) #creation ovale -> cerlce, de diametre 100 (cercle de droite)de centre x1
canvas.create_oval((x0 + x1) / 2 - 50, y + 50, (x0 + x1) / 2 + 50, y - 50) #creation ovale -> cerlce, de diametre 100 (cercle du mileu) centre milieu[x0, x1]
canvas.grid()
# Fin de votre code

root.mainloop()
