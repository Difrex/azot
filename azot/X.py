from Xlib import display

# Get screen resolution
def get_geometry():
    while 1:
        try:
            width = display.Display().screen().width_in_pixels
            height = display.Display().screen().height_in_pixels
            
            return {"x": width, "y": height}
        except:
            pass


# Get mouse cursor position
def get_cursor_position():
    while 1:
        try:
            data = display.Display().screen().root.query_pointer()._data

            return {'x': data['root_x'], 'y': data['root_y']}
        except:
            pass
