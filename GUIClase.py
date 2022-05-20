# Para correr esta aplicación:
# Primero: Correr el servidor de swipl con el comando:
# swipl -l Servi.pl -g true -g servidor
# Luego ejecutar la gui:
# python GUIClase.py

import tkinter as tk             # Crear ventanas
from PIL import Image, ImageTk   # Insertar imagenes en las ventanas
import os                        # Poder acciones del sistema operativo
import time                      # Librería de tiempo para esperar

import cliente as con            # Propia: conexión a socket prolog
import draw_sol                  # Crea un png con la solución

# Inicia el servidor con el socket de prolog
prolog = con.Conecta()
# Inicia la clase que va crear png de la solución
Tablero = draw_sol.Tablero()

# Crear ventana principal y le ponemos un nombre
ven = tk.Tk(className="Problemas de las N Reinas")
# Dimensines y posición inicial de la ventana
ven.geometry("600x400+100+100")


# Hacer un query a prolog para obtener la solución
def imp():
    # Elimina soluciones previas
    try:
        os.remove("chess.png")
    # Exception si el archivo no existe
    except FileNotFoundError:
        print("No existe el archivo chess.png")

    # Obtiene el texto dentro del cuadro de input
    reinas = t1.get()

    # Excepciones a la entrada de usuarios
    # No introdujo un número
    try:
        int(reinas)
    except ValueError:
        return
    # Introdujo un valor que no tiene solución
    if (reinas == "" or reinas == "3" or reinas == "2" or int(reinas) <= 0):
        return

    # Hace la consulta en el servidor de prolog
    res = prolog.query(reinas)

    # Generar el png del tablero con la solución obtenida
    Tablero.getImage(reinas, res)

    # Intentar leer el archivo png donde está la solución
    while True:
        try:
            with open("chess.png", 'rb') as _:
                break
        # Exception si el archivo aún no está generado
        except IOError:
            time.sleep(3)
            print(".", end="")

    # Cargar la imagen generada
    tablero = Image.open("chess.png")
    # Poner un label en la ventana
    sol = ImageTk.PhotoImage(tablero)
    # Insertar imagen en el label de la ventana
    label_sol = tk.Label(image=sol)
    label_sol.image = sol
    # Posición del label con la imagen
    label_sol.grid(row=1, column=0)


# Agrupamos el texto, el cuadro de input y el botón en uno solo
# Le damos un padding del borde de 10px
frame1 = tk.Frame(ven, padx=10, pady=10)
# Hacemos que estos tres elementos sean parte del grid
# Al hacerlos parte del grid su posición se determina automáticamente
frame1.grid()
# Creamos el label de texto y la agregamos al frame
tk.Label(frame1, text="Número de Reinas").grid(row=0, column=0)
# Agregamos el cuadro de input y lo agregamos al frame
t1 = tk.Entry(frame1)
t1.grid(row=0, column=1)
# Creamos el botón y lo agregamos al frame
ok = tk.Button(frame1,
               text='Mostrar Solución',
               # Le decimos que función correr al pulsar el botón
               command=imp).grid(row=0, column=2)
# Agregamos un padding a cada elemento
for child in frame1.winfo_children():
    child.grid_configure(padx=10, pady=10)


# Función para cerrar la ventana
def cierra():
    print("Cierro ventana")
    ven.destroy()


# Cerrar ventana
ven.protocol('WM_DELETE_WINDOW', cierra)

# Mostrarla ventana
ven.mainloop()
