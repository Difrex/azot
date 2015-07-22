from Xlib import display
import azot.action

azot.action.do("TRATATA")

width = display.Display().screen().width_in_pixels
height = display.Display().screen().height_in_pixels

root = display.Display().screen().root.display

# print data["root_x"], data["root_y"]
#print width, height 
#print root.__dict__
