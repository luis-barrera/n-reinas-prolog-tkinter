import cairo

# WIDTH, HEIGHT = 512, 512
WIDTH, HEIGHT = 254, 254


class Tablero():

    # TODO: esta función debe regresar un string con el nombre del png
    def getImage(self, casillas, pos_reinas):
        surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
        # ctx.scale(WIDTH, HEIGHT)  # Normalizing the canvas
        ctx = cairo.Context(surface)
        CASILLAS = int(casillas)

        # TODO: poner las casillas con etiquetas a la izq y en la parte inferior
        tam_cuadrado = int(WIDTH / (CASILLAS + 1))

        pos_row = 0
        pos_col = 0

        for row in range(CASILLAS):
            # ctx.set_line_width(0.02)
            # ctx.set_source_rgb(0.3, 0.2, 0.5)  # Solid color
            pos_row = row * tam_cuadrado

            # TODO: agregar etiquetas a las col(abc...) y rows(123...)
            # Contadors de casillas
            casillas_counter = row % 2

            for col in range(CASILLAS):
                pos_col = col * tam_cuadrado

                if (casillas_counter % 2 == 0):
                    # TODO: cambiar los colores de las casillas
                    # PosX, PosY, TamX, TamY
                    ctx.rectangle(pos_col, pos_row, tam_cuadrado, tam_cuadrado)
                    ctx.set_source_rgba(0.53, 0.35, 0.41, 1)
                    ctx.fill()

                    ctx.rectangle(pos_col, pos_row, tam_cuadrado, tam_cuadrado)
                    ctx.set_source_rgba(0, 0, 0, 1)
                    ctx.set_line_width(0.01)
                    ctx.stroke()
                else:
                    # PosX, PosY, TamX, TamY
                    ctx.rectangle(pos_col, pos_row, tam_cuadrado, tam_cuadrado)
                    ctx.set_source_rgba(0.94, 0.67, 0.96, 1)
                    ctx.fill()

                    ctx.rectangle(pos_col, pos_row, tam_cuadrado, tam_cuadrado)
                    ctx.set_source_rgba(0, 0, 0, 1)
                    ctx.set_line_width(0.01)
                    ctx.stroke()

                if (pos_reinas[col] == (row + 1)):
                    queen = cairo.ImageSurface.create_from_png("chess-queen.png")
                    ctx.save()
                    ctx.translate(pos_col, pos_row)
                    queen_w = queen.get_width()
                    queen_h = queen.get_height()
                    ctx.scale(tam_cuadrado / queen_w, tam_cuadrado / queen_h)
                    ctx.set_source_surface(queen)
                    ctx.paint()
                    ctx.restore()

                if (col == CASILLAS - 1):
                    ctx.select_font_face("Courier",
                                         cairo.FONT_SLANT_NORMAL,
                                         cairo.FONT_WEIGHT_BOLD)
                    ctx.set_font_size(tam_cuadrado)

                    ctx.move_to(pos_col + tam_cuadrado + (tam_cuadrado * 0.2),
                                pos_row + (tam_cuadrado * 0.8))
                    ctx.set_source_rgb(1, 1, 1)
                    ctx.show_text(f'{CASILLAS - row}')
                    ctx.move_to(pos_col + tam_cuadrado + (tam_cuadrado * 0.2),
                                pos_row + (tam_cuadrado * 0.8))
                    ctx.set_source_rgb(0, 0, 0)
                    ctx.text_path(f'{CASILLAS - row}')
                    ctx.set_line_width(6 * (tam_cuadrado / WIDTH))
                    ctx.stroke()

                casillas_counter += 1

        label_horizontal = 'a'
        pos_row = CASILLAS * tam_cuadrado
        for col in range(CASILLAS):
            pos_col = col * tam_cuadrado
            ctx.select_font_face("Courier",
                                 cairo.FONT_SLANT_NORMAL,
                                 cairo.FONT_WEIGHT_BOLD)
            ctx.set_font_size(tam_cuadrado)

            ctx.move_to(pos_col + (tam_cuadrado * 0.2),
                        pos_row + (tam_cuadrado * 0.8))
            ctx.set_source_rgb(1, 1, 1)
            ctx.show_text(f'{label_horizontal}')
            ctx.move_to(pos_col + (tam_cuadrado * 0.2),
                        pos_row + (tam_cuadrado * 0.8))
            ctx.set_source_rgb(0, 0, 0)
            ctx.text_path(f'{label_horizontal}')
            ctx.set_line_width(6 * (tam_cuadrado / WIDTH))
            ctx.stroke()

            label_horizontal = chr(ord(label_horizontal) + 1)

        surface.write_to_png("chess.png")  # Output to PNG
