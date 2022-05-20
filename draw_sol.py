# Para correr esta aplicación:
# Primero: Correr el servidor de swipl con el comando:
# swipl -l Servi.pl -g true -g servidor
# Luego ejecutar la gui:
# python GUIClase.py

# Generar imagenes SVG y exportarlas a PNG
import cairo

# Tamaño de la imagen
# WIDTH, HEIGHT = 512, 512
WIDTH, HEIGHT = 254, 254


class Tablero():
    # Función que dibuja la solución a partir de las reinas y la solución
    def getImage(self, casillas, pos_reinas):
        # Creamos un espacio de trabajo con las medidas
        surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
        # Agregamos el espacio de trabajo a un contexto para poder trabajar
        ctx = cairo.Context(surface)

        # Cantidad de reinas, y por tanto, casillas por lado
        CASILLAS = int(casillas)

        # Tamaño del cuadrado a partir de la cantidad de casillas
        # También dejamos un espacio para poner leyendas en los bordes
        tam_cuadrado = int(WIDTH / (CASILLAS + 1))

        # Posición en la que nos encontramos dibujando
        # El dibujo se hace trabajando por renglones y luego columnas
        pos_row = 0  # Renglón
        pos_col = 0  # Columna

        # Recorrer por renglones
        for row in range(CASILLAS):
            # Borde a las casillas
            # ctx.set_line_width(0.02)
            # ctx.set_source_rgb(0.3, 0.2, 0.5)

            # Actualizar el renglón que estamos
            pos_row = row * tam_cuadrado

            # Contadors de casillas, para poner colores
            casillas_counter = row % 2

            # Recorrer por columans
            for col in range(CASILLAS):
                # Actualizamos la columna
                pos_col = col * tam_cuadrado

                # Dibujar una casilla oscura
                if (casillas_counter % 2 == 0):
                    # Dibujamos un rectángulo
                    # Argumentos: PosX, PosY, TamX, TamY
                    ctx.rectangle(pos_col, pos_row, tam_cuadrado, tam_cuadrado)
                    # Ponemos un color oscuro
                    ctx.set_source_rgb(13/15, 3/5, 7/51)
                    # Llenamos el rectángulo con el color
                    ctx.fill()
                # Dibujar una casilla clara
                else:
                    # PosX, PosY, TamX, TamY
                    ctx.rectangle(pos_col, pos_row, tam_cuadrado, tam_cuadrado)
                    # Cambiar color a claro
                    ctx.set_source_rgb(13/15, 4/5, 35/51)
                    # Llenamos el rectángulo con el color
                    ctx.fill()

                # Dibujar reinas según la solución de prolog
                if (pos_reinas[col] == (row + 1)):
                    # Lee una imágen png con un dibujo de reina
                    queen = (cairo
                             .ImageSurface
                             .create_from_png("chess-queen.png"))
                    # Guarda el contexto para liberar memoria
                    ctx.save()
                    # No movemos a la posición en la que insertar
                    ctx.translate(pos_col, pos_row)
                    # Obtenemos ancho y largo del dibujo de la reina
                    queen_w = queen.get_width()
                    queen_h = queen.get_height()
                    # Cambiamos el tamaño de la reina según su tamaño
                    #   y el tamaño del dibujo
                    ctx.scale(tam_cuadrado / queen_w, tam_cuadrado / queen_h)
                    # Ponemos la imagen en el contexto
                    ctx.set_source_surface(queen)
                    # Lo dibujamos
                    ctx.paint()
                    # Regresamos al estado anterior del contexto
                    ctx.restore()

                # Dibujar las leyendas al lado izquierdo
                if (col == CASILLAS - 1):
                    # Seleccionamos una fuente y la ponemos en negritas
                    ctx.select_font_face("Courier",
                                         cairo.FONT_SLANT_NORMAL,
                                         cairo.FONT_WEIGHT_BOLD)
                    # El tamaño de la fuente es el mismo que las casillas
                    ctx.set_font_size(tam_cuadrado)

                    # Nos movemos al lugar en el cual escribir
                    ctx.move_to(pos_col + tam_cuadrado + (tam_cuadrado * 0.2),
                                pos_row + (tam_cuadrado * 0.8))
                    # Color del texto, blanco
                    ctx.set_source_rgb(1, 1, 1)
                    # Contenido del texto es el número de renglón
                    ctx.show_text(f'{row + 1}')

                    # Dibujar contorno de letras
                    # Nos movemos al lugar en el cual escribir
                    ctx.move_to(pos_col + tam_cuadrado + (tam_cuadrado * 0.2),
                                pos_row + (tam_cuadrado * 0.8))
                    # Color del contorno, negro
                    ctx.set_source_rgb(0, 0, 0)
                    # Contenido del texto es el número de renglón
                    ctx.text_path(f'{row + 1}')
                    # Ancho de la linea del contorno
                    ctx.set_line_width(6 * (tam_cuadrado / WIDTH))
                    # Dibujar el contorno
                    ctx.stroke()

                # Actualizar el contador para dibujar la casilla
                #   siguiente del otro color
                casillas_counter += 1

        # Leyendas de la parte inferior
        # Son letras minúsculas
        label_horizontal = 'a'
        # Movernos al último renglón
        pos_row = CASILLAS * tam_cuadrado
        # Recorrer las columnas del renglón
        for col in range(CASILLAS):
            # Actualizar el renglón
            pos_col = col * tam_cuadrado

            # Seleccionamos una fuente y la ponemos en negritas
            ctx.select_font_face("Courier",
                                 cairo.FONT_SLANT_NORMAL,
                                 cairo.FONT_WEIGHT_BOLD)
            # El tamaño de la fuente es el mismo que las casillas
            ctx.set_font_size(tam_cuadrado)

            # Nos movemos al lugar en el cual escribir
            ctx.move_to(pos_col + (tam_cuadrado * 0.2),
                        pos_row + (tam_cuadrado * 0.8))

            # Color del texto, blanco
            ctx.set_source_rgb(1, 1, 1)
            # Contenido del texto es el una letra
            ctx.show_text(f'{label_horizontal}')

            # Dibujar contorno de letras
            # Nos movemos al lugar en el cual escribir
            ctx.move_to(pos_col + (tam_cuadrado * 0.2),
                        pos_row + (tam_cuadrado * 0.8))
            # Color del contorno, negro
            ctx.set_source_rgb(0, 0, 0)
            # Contenido del texto es el una letra
            ctx.text_path(f'{label_horizontal}')
            # Ancho de la linea del contorno
            ctx.set_line_width(6 * (tam_cuadrado / WIDTH))
            # Dibujar el contorno
            ctx.stroke()

            # Actualizar el character según el abecedario
            label_horizontal = chr(ord(label_horizontal) + 1)

        # Guardar a archivo PNG
        surface.write_to_png("chess.png")
