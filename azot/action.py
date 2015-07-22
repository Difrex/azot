import os
import subprocess
import azot.config
from X import get_cursor_position
from time import sleep

# Globals
config = azot.config.load()
corners = {
            'top': config['corners']['top_corner'],
            'right': config['corners']['right_corner'],
            'bottom': config['corners']['bottom_corner'],
            'left': config['corners']['left_corner']
        }


# Execute command
def do():
    position = get_cursor_position()
    for action in config['actions']:

        # angles
        if action['position'] != 'middle':
            if action['corner'] == 'top' or action['corner'] == 'bottom':
                if position['y'] == corners[ action['corner'] ] and position['x'] == corners[action['position']]:
                    print action
                    print position
                    print 'Get position: {0} and corner {1}'.format(action['position'], action['corner'])
                    sleep(1) 
            elif action['corner'] == 'left' or action['corner'] == 'right':
                if position['x'] == corners[ action['position'] ] and position['y'] == corners[ action['corner'] ]:
                    print action
                    print position
                    print 'Get position: {0} and corner {1}'.format(action['position'], action['corner'])
                    sleep(1)

        # middles
        elif action['position'] == 'middle':
            if action['corner'] == 'top' or action['corner'] == 'bottom':
                if position['y'] == corners[ action['corner'] ] and position['x'] > config['corners']['middle_x_start'] and position['x'] < config['corners']['middle_x_end']:
                    print action
                    print position
                    print 'Get position: {0} and corner {1}'.format(action['position'], action['corner'])
                    sleep(1) 
            elif action['corner'] == 'left' or action['corner'] == 'right':
                if position['x'] == corners[ action['corner'] ] and position['y'] > config['corners']['middle_y_start'] and position['y'] < config['corners']['middle_y_end']:
                    print action
                    print position
                    print 'Get position: {0} and corner {1}'.format(action['position'], action['corner'])
                    sleep(1)


# 


# Get shell command output
def get_cmd(cmd):
    out = os.popen(cmd).read()
    
    return out


# Show notify message
def notify(msg):

