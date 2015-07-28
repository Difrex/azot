from Xlib import display
from time import sleep

# Get screen resolution
def get_geometry():
    while 1:
        try:
            width = display.Display().screen().width_in_pixels
            height = display.Display().screen().height_in_pixels
            
            return {"x": width, "y": height}
        except Exception, e:
            print e
            print "Spleep for 10 second"
            sleep(10)


# Get mouse cursor position
def get_cursor_position():
    while 1:
        try:
            data = display.Display().screen().root.query_pointer()._data

            return {'x': data['root_x'], 'y': data['root_y']}
        except Exception, e:
            print e
            print "Spleep for 10 second"
            sleep(10)
