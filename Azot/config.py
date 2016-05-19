import ast
import argparse
import os
from Azot.X import get_geometry
from Azot.logger import info

# Globals
config_dir = os.environ['HOME'] + '/.config/azot/'
config_path = config_dir + "config.json"

default_config_paths = ['/usr/share/doc/azot/config.sample.json', './config.sample.json']

parser = argparse.ArgumentParser()
parser.add_argument('-c', '--config')
args = parser.parse_args()
if args.config:
    config_path = args.config

# Check config existence and copy if needed
if not os.path.exists(config_path):
    for default_path in default_config_paths:
        if os.path.exists(default_path):
            os.makedirs(config_dir)
            import shutil
            info("Config doesn't exist in " + config_path + "; copying...")
            shutil.copyfile(default_path, config_path)
            break

# Load configuration from file
def load():
    config = ''
    with open(config_path) as config_file:
        for line in config_file:
            config += line

    config_file.close()
    config = ast.literal_eval(config)
    config['corners'] = get_middle_areas()

    if not 'check_delay' in config.keys():
        config['check_delay'] = 0.3

    if not 'after_exec_delay' in config.keys():
        config['after_exec_delay'] = 1

    return config


# Calculate middle area
def get_middle_areas():
    geometry = get_geometry()

    # Middle X and Y activation area
    middle_x_area_pixels = int( ( geometry['x'] * 0.05 ) / 2 )
    middle_y_area_pixels = int( ( geometry['y'] * 0.05 ) / 2 )
    middle_x = int( geometry['x'] / 2 )
    middle_y = int( geometry['y'] / 2 )
    middle_x_start = int( middle_x - middle_x_area_pixels )
    middle_y_start = int( middle_y - middle_y_area_pixels )
    middle_x_end = int( middle_x + middle_x_area_pixels )
    middle_y_end = int( middle_y + middle_y_area_pixels )

    corners = { 'left_corner': 0,
                'right_corner': geometry['x'] - 1,
                'top_corner': 0,
                'bottom_corner': geometry['y'] - 1,
                'middle_x_start': middle_x_start,
                'middle_x_end': middle_x_end,
                'middle_y_start': middle_y_start,
                'middle_y_end': middle_y_end
              }

    return corners