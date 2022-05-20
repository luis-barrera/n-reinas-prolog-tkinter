# n-reinas-prolog-tkinter

Aplicación en [python-tkinter](https://docs.python.org/3/library/tkinter.html) que muestra las soluciones obtenidas de [Prolog](https://www.swi-prolog.org/) para el problema de [N-Reinas](https://es.wikipedia.org/wiki/Problema_de_las_ocho_reinas).
Las soluciones se obtienen de un programa de Prolog.
La aplicación principal es en Python y se conecta a un [servidor de Prolog](https://www.swi-prolog.org/pldoc/man?section=socket) a través de socket para enviar y obtener soluciones.
Se usa [pycairo](https://pycairo.readthedocs.io/en/latest/) para generar las soluciones en una imagen.
