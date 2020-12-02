import tkinter as tk

racine = tk.Tk()
racine.title('clic1')

canvas = tk.Canvas(racine, bg='black', height=500, width=500)

nb_clic = 0
co_x = []
co_y = []
def appui_touche1(event):
    global nb_clic
    global co_x
    global co_y
    X = event.x
    Y = event.y
    nb_clic +=1
    pixel = canvas.create_rectangle(X, Y, X+1, Y+1, fill = 'red', width=0)
    co_x.append(X)
    co_y.append(Y)
    print(co_x)
    if nb_clic == 1 or 0:
        return
    else:
        if ((co_x[-1] < 250 ) and (co_x[-2]< 250)):
            canvas.create_line((co_x[-1], co_y[-1]), (co_x[-2], co_y[-2]), fill='blue')
        elif ((co_x[-1]> 250) and (co_x[-2]> 250)):
            canvas.create_line((co_x[-1], co_y[-1]), (co_x[-2], co_y[-2]), fill='blue')
        elif (co_x[-1] < 250) and (co_x[-2] > 250):
            canvas.create_line((co_x[-1], co_y[-1]), (co_x[-2], co_y[-2]), fill='red')
        elif (co_x[-1] > 250) and (co_x[-2] < 250):
            canvas.create_line((co_x[-1], co_y[-1]), (co_x[-2], co_y[-2]), fill='red')
    

canvas.bind('<Button-1>', appui_touche1)

canvas.create_line((250, 0), (250, 500), fill='white')



canvas.grid()
racine.mainloop()
print(nb_clic, co_x, co_y)