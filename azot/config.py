import argparse
import os


# Globals
config_path = os.environ['HOME'] + '.config/azot/config.json'
parser = argparse.ArgumentParser()
parser.add_argument('-c', '--config')
args = parser.parse_args()
if args.config:
	config_path = args.config


# Load configuration from file
def load():
    print config_path


