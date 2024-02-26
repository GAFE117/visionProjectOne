import curses

def main(stdscr):
    # Limpiar la pantalla
    stdscr.clear()

    # Obtener dimensiones de la pantalla
    height, width = stdscr.getmaxyx()

    # Definir las opciones del menú
    options = ["Option 1", "Option 2", "Option 3", "Exit"]

    # Inicializar el cursor en la primera opción
    cursor_y = 0
    cursor_x = 0

    # Imprimir las opciones del menú
    while True:
        stdscr.clear()
        for i, option in enumerate(options):
            x = width // 2 - len(option) // 2
            y = height // 2 - len(options) // 2 + i
            if i == cursor_y:
                stdscr.attron(curses.color_pair(1))
                stdscr.addstr(y, x, option)
                stdscr.attroff(curses.color_pair(1))
            else:
                stdscr.addstr(y, x, option)
        stdscr.refresh()

        # Obtener entrada del usuario
        key = stdscr.getch()

        # Mover el cursor hacia arriba
        if key == curses.KEY_UP and cursor_y > 0:
            cursor_y -= 1

        # Mover el cursor hacia abajo
        elif key == curses.KEY_DOWN and cursor_y < len(options) - 1:
            cursor_y += 1

        # Salir del programa si se presiona Enter en "Exit"
        elif key == curses.KEY_ENTER or key in [10, 13]:
            if cursor_y == len(options) - 1:
                break

curses.wrapper(main)

