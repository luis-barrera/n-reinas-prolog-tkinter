import tkinter as tk
import cliente as con

prolog = con.Conecta()

e1: tk.Entry
e2: tk.Entry

ven = tk.Tk(className="Interfaz Gráfica")
ven.geometry("600x400+100+100")

ok = tk.Button(ven, text='OK')
ok.place(x=100, y=100)

tk.Label(ven, text="Lista").grid(row=0)
t1 = tk.Entry(ven)
t1.grid(row=0, column=1)
tk.Label(ven, text="Elemento").grid(row=1)
t2 = tk.Entry(ven)
t2.grid(row=1, column=1)


def imp(event):
    print('Di click al botón')
    lista = t1.get()
    elem = t2.get()
    print(f'Busca {elem} en {lista}')
    res = prolog.query(lista, elem)
    l_res = tk.Label(text=f'La respuesta fue {res}')
    l_res.grid(row=2, column=2)


ok.bind('<Button-1>', imp)


def cierra():
    print("Cierro ventana")
    ven.destroy()


ven.protocol('WM_DELETE_WINDOW', cierra)

ven.tk.call('tk', 'scaling', 4.0)
ven.mainloop()
