import tkinter as tk

racine = tk.Tk()
racine.title('clic1')

canvas = tk.Canvas(racine, bg='black', height=500, width=500)

def appui_touche(event):
    X = event.x
    Y = event.y
    if X < 250:
        color = 'blue'
    elif X > 250:
        color = 'red'
    else:
        return
    canvas.create_oval(X-25, Y-25, X+25, Y+25, fill=color)


canvas.bind('<Button-1>', appui_touche)

canvas.create_line((250, 0), (250, 500), fill='white')



canvas.grid()
racine.mainloop()