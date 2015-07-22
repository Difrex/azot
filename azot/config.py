import ast
import argparse
import os
from pprint import pprint

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
   
    config = ast.literal_eval(config)
    
    return config

