import tkinter as tk

racine = tk.Tk()
racine.title('clic1')

canvas = tk.Canvas(racine, bg='black', height=500, width=500)

def appui_touche(event):
    print("Tu as appuyé sur la touche", event.char)
    X = event.x
    Y = event.y
    pixel = canvas.create_rectangle(X, Y, X+1, Y+1, fill = 'red', width=0)

canvas.bind('<Button-1>', appui_touche)




canvas.grid()
racine.mainloop()