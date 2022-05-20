import tkinter as tk
from PIL import Image, ImageTk
import os
import time

import cliente as con
import draw_sol

prolog = con.Conecta()
Tablero = draw_sol.Tablero()

ven = tk.Tk(className="Problemas de las N Reinas")
ven.geometry("600x400+100+100")


def imp():
    print('Di click al botón')

    try:
        os.remove("chess.png")
    except FileNotFoundError:
        print("No existe el archivo chess.png")

    reinas = t1.get()
    res = prolog.query(reinas)

    print("Generando solución")
    Tablero.getImage(reinas, res)

    while True:
        try:
            with open("chess.png", 'rb') as _:
                break
        except IOError:
            time.sleep(3)
            print(".", end="")

    tablero = Image.open("chess.png")
    sol = ImageTk.PhotoImage(tablero)
    label_sol = tk.Label(image=sol)
    label_sol.image = sol
    label_sol.grid(row=3, column=0)


frame1 = tk.Frame(ven, padx=10, pady=10)
frame1.grid()
tk.Label(frame1, text="Número de Reinas").grid(row=0, column=0)
t1 = tk.Entry(frame1)
t1.grid(row=0, column=1)
ok = tk.Button(frame1, text='Mostrar Solución', command=imp).grid(row=0, column=2)
for child in frame1.winfo_children():
    child.grid_configure(padx=10, pady=10)
# ok = tk.Button(frame1, text='Mostrar Solución', command=imp()).grid(row=0, column=2)



def cierra():
    print("Cierro ventana")
    ven.destroy()


ven.protocol('WM_DELETE_WINDOW', cierra)

# ven.tk.call('tk', 'scaling', 4.0)
ven.mainloop()
