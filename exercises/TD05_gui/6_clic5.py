import tkinter as tk

racine = tk.Tk()
racine.title('clic5')

canvas = tk.Canvas(racine, bg='black', height=500, width=500)

nb_clic = 0
co_x = []
co_y = []


def appui_touche1(event):
    global nb_clic
    nb_clic +=1
    X = event.x
    Y = event.y
    co_x.append(X)
    co_y.append(Y)
    
    if nb_clic <= 8:
        co_pi = (X, Y), (X+1, Y+1)
        pixel = canvas.create_rectangle(co_pi, fill = 'red', width=0)
        cercle = canvas.create_oval(X-25, Y-25, X+25, Y+25, fill='red')
    elif nb_clic == 9:
        for item in canvas.find_all():
            if canvas.type(item) == 'oval':
                canvas.itemconfig(item, fill='yellow')

canvas.bind('<Button-1>', appui_touche1)




canvas.grid()
racine.mainloop()
print(nb_clic, co_x, co_y)