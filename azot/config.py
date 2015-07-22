import ast
import argparse
import os
from X import get_geometry

# Globals
config_path = os.environ['HOME'] + '/.config/azot/config.json'

parser = argparse.ArgumentParser()
parser.add_argument('-c', '--config')
args = parser.parse_args()
if args.config:
	config_path = args.config


# Load configuration from file
def load():
    config = ''
    with open(config_path) as config_file:
        for line in config_file:
            config += line
    
    config_file.close()
    config = ast.literal_eval(config)
    config['corners'] = get_middle_areas()

    print config['corners']

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
                'right_corner': geometry['x'],
                'top_corner': 0,
                'bottom_corner': geometry['y'],
                'middle_x_start': middle_x_start,
                'middle_x_end': middle_x_end,
                'middle_y_start': middle_y_start,
                'middle_y_end': middle_y_end
              }

    return corners

