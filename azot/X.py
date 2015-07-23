from Xlib import display

# Get screen resolution
def get_geometry():
    try:
        width = display.Display().screen().width_in_pixels
        height = display.Display().screen().height_in_pixels
        
        return {"x": width, "y": height}
    except:
        get_geometry()


# Get mouse cursor position
def get_cursor_position():
    data = display.Display().screen().root.query_pointer()._data

    return {'x': data['root_x'], 'y': data['root_y']}
