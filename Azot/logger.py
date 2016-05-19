import sys


# Print to STDERR
def warning(msg):
    print("WARNING: ", msg, file=sys.stderr)


# Print to STDOUT
def info(msg):
    print("INFO: ", msg, file=sys.stdout)