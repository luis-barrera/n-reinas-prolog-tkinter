import cairo

CASILLAS = 8
WIDTH, HEIGHT = 1024, 1024

surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
ctx = cairo.Context(surface)
ctx.set_line_width(0.02)
ctx.set_source_rgb(0.3, 0.2, 0.5)  # Solid color

ctx.scale(WIDTH, HEIGHT)  # Normalizing the canvas

# TODO: poner las casillas con etiquetas a la izq y en la parte inferior
tam_cuadrado = 1 / (CASILLAS + 1)

for row in range(CASILLAS):
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
            ctx.set_source_rgba(1, 0, 0, 1)
            ctx.fill()

            ctx.rectangle(pos_col, pos_row, tam_cuadrado, tam_cuadrado)
            ctx.set_source_rgba(0, 0, 0, 1)
            ctx.set_line_width(0.01)
            ctx.stroke()
        else:
            # PosX, PosY, TamX, TamY
            ctx.rectangle(pos_col, pos_row, tam_cuadrado, tam_cuadrado)
            ctx.set_source_rgba(0, 0, 1, 1)
            ctx.fill()

            ctx.rectangle(pos_col, pos_row, tam_cuadrado, tam_cuadrado)
            ctx.set_source_rgba(0, 0, 0, 1)
            ctx.set_line_width(0.01)
            ctx.stroke()

        casillas_counter += 1


        # # PosX, PosY, TamX, TamY
        # ctx.rectangle(pos_row, pos_col, tam_cuadrado, tam_cuadrado)
        # ctx.set_source_rgba(1, 0, 0, 1)
        # ctx.fill()

        # ctx.rectangle(pos_row, pos_col, tam_cuadrado, tam_cuadrado)
        # ctx.set_source_rgba(0, 0, 0, 1)
        # ctx.set_line_width(0.01)
        # ctx.stroke()

# ctx.stroke()
# ctx.set_source_rgb(0, 0, 0)
# ctx.stroke()

surface.write_to_png("chess.png")  # Output to PNG

