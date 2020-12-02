import tkinter as tk

racine = tk.Tk()
racine.title('clic4')

canvas = tk.Canvas(racine, bg='black', height=500, width=500)

nb_clic = 0

def appui_touche1(event):
    global nb_clic
    nb_clic +=1
    if nb_clic == 10:
        racine.destroy()
    elif nb_clic % 2 != 0:
        canvas.itemconfigure(carre, fill='black')
    elif nb_clic % 2 == 0:
        canvas.itemconfigure(carre, fill='white')

canvas.bind('<Button-1>', appui_touche1)
carre = canvas.create_rectangle((150, 150), (350, 350),  fill='white')




canvas.grid()
racine.mainloop()
print(nb_clic, co_x, co_y)