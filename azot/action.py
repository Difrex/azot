import os
import subprocess
import azot.config


# Globals
config = azot.config.load()


# Execute command
def do(cmd):
    print string


# Get shell command output
def get_cmd(cmd):
	out = os.popen(cmd).read()
	
	return out



