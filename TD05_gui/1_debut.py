import tkinter as tk

CANVAS_WIDTH, CANVAS_HEIGHT = 600, 400


root = tk.Tk()

canvas = tk.Canvas(root, width = CANVAS_WIDTH, height = CANVAS_HEIGHT)

# Début de votre code
x = CANVAS_WIDTH //2 #ligne imaginaire vertical en x = 100unité depuis le bord gauche(centre du premier cercle a gauche)
y1 = 100 #hauteur du centre de la feuille
y2=CANVAS_HEIGHT - 100
canvas.create_line((x, y1), (x, y2))
canvas.create_oval(x - 50, y1 + 50, x + 50, y1 - 50) #creation ovale -> cerlce, de diametre 100 (cercle de gauche) de centre x0
canvas.create_oval(x - 50, y2 + 50, x + 50, y2 - 50) #creation ovale -> cerlce, de diametre 100 (cercle de droite)de centre x1
canvas.create_oval((x - 50 , (y1 + y2) // 2 + 50, x + 50, (y1 + y2) // 2-50))
canvas.grid()

root.mainloop()
