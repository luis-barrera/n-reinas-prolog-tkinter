import cairo
import cliente

CASILLAS = 3
WIDTH, HEIGHT = 1024, 1024

surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
ctx = cairo.Context(surface)

# ctx.scale(WIDTH, HEIGHT)  # Normalizing the canvas

# TODO: poner las casillas con etiquetas a la izq y en la parte inferior
tam_cuadrado = int(WIDTH / (CASILLAS + 1))

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

        queen = cairo.ImageSurface.create_from_png("chess-queen.png")
        ctx.save()
        ctx.translate(pos_col, pos_row)
        queen_w = queen.get_width()
        queen_h = queen.get_height()
        ctx.scale(tam_cuadrado / queen_w, tam_cuadrado / queen_h)
        ctx.set_source_surface(queen)
        ctx.paint()
        ctx.restore()

        casillas_counter += 1

# ctx = cairo.Context(surface)
# ctx.rectangle(0, 0, WIDTH, HEIGHT)
# ctx.set_source_rgba(1, 1, 1, 1)
# ctx.set_line_width(0.01)
# ctx.stroke()


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

# ctx.set_source_surface(queen, 1, 1)
# ctx.paint()

# wi = queen.get_width()
# he = queen.get_height()
# queen = queen.scale(tam_cuadrado, tam_cuadrado)  # Normalizing the canvas
# reina = cairo.ImageSurface(cairo.FORMAT_ARGB32, tam_cuadrado, tam_cuadrado)
# reina_ctx = cairo.Context(reina)


surface.write_to_png("chess.png")  # Output to PNG

