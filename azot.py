import azot.action
from azot.X import get_geometry, get_cursor_position
import azot.config


geometry = get_geometry()
position = get_cursor_position()

azot.config.load()

print geometry['x'], geometry['y']
print position['x'], position['y']
