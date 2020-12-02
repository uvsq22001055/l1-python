import tkinter as tk

racine = tk.Tk()
racine.title('clic1')

canvas = tk.Canvas(racine, bg='black', height=500, width=500)

def appui_touche(event):
    X = event.x
    Y = event.y
    pixel = canvas.create_rectangle(X, Y, X+1, Y+1, fill = 'red', width=0)
    if X < 250:
        canvas.create_oval(X-25, Y-25, X+25, Y+25, fill='blue')
    elif X > 250:
        canvas.create_oval(X-25, Y-25, X+25, Y+25, fill='red')
    else:
        return


canvas.bind('<Button-1>', appui_touche)

canvas.create_line((250, 0), (250, 500), fill='white')



canvas.grid()
racine.mainloop()