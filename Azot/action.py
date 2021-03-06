import os
import Azot.config
from Azot.X import get_cursor_position
from time import sleep

# Globals
config = Azot.config.load()
corners = {
            'top': config['corners']['top_corner'],
            'right': config['corners']['right_corner'],
            'bottom': config['corners']['bottom_corner'],
            'left': config['corners']['left_corner']
        }


# Execute command
def do():
    def task_exec():
        msg = type_exec(action)
        notify(msg)
        sleep(config['after_exec_delay'])

    position = get_cursor_position()
    for action in config['actions']:

        # angles
        if action['position'] != 'middle':
            if action['corner'] == 'top' or action['corner'] == 'bottom':
                if position['y'] == corners[ action['corner'] ] and position['x'] == corners[action['position']]:
                    task_exec()
            elif action['corner'] == 'left' or action['corner'] == 'right':
                if position['x'] == corners[ action['position'] ] and position['y'] == corners[ action['corner'] ]:
                    task_exec()

        # middles
        elif action['position'] == 'middle':
            if action['corner'] == 'top' or action['corner'] == 'bottom':
                if position['y'] == corners[ action['corner'] ] and position['x'] > config['corners']['middle_x_start'] and position['x'] < config['corners']['middle_x_end']:
                    task_exec()
            elif action['corner'] == 'left' or action['corner'] == 'right':
                if position['x'] == corners[ action['corner'] ] and position['y'] > config['corners']['middle_y_start'] and position['y'] < config['corners']['middle_y_end']:
                    task_exec()
    sleep(config['check_delay'])


# Detect type and execute
def type_exec(action):
    if action['type'] == 'notify':
        out = get_cmd(action['command'])
        return out
    elif action['type'] == 'exec':
        get_cmd(action['command'])
        return action['command']
    elif action['type'] == 'simple':
        get_cmd(action['command'])
        return None
    else:
        return 'Unknown type!'


# Get shell command output
def get_cmd(cmd):
    out = os.popen(cmd).read()
    return out


# Show notify message
def notify(msg):
    if msg is not None:
        get_cmd( "notify-send 'azot event' \"{0}\"".format(msg) )