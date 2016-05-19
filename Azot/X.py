from Xlib import display
from time import sleep
from Azot.logger import warning

working_display = display.Display()
working_screen = working_display.screen()
root_window = working_screen.root

# Get screen resolution
def get_geometry():
    while 1:
        try:
            width = working_screen.width_in_pixels
            height = working_screen.height_in_pixels

            return {"x": width, "y": height}
        except Exception as e:
            warning(str(e) + '\n' + 'Spleep for 10 second')
            sleep(10)


# Get mouse cursor position
def get_cursor_position():
    while 1:
        try:
            data = root_window.query_pointer()._data

            return {'x': data['root_x'], 'y': data['root_y']}
        except Exception as e:
            warning(str(e) + '\n' + 'Spleep for 10 second')
            sleep(10)