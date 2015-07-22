# Azot

Screen corners actions in all WM.

## Configuration

Edit config.sample.json and put it into ~/.config/azot/config.json

* type must be ''exec'' or ''notify''
  exec: just show command
  notify: Show output from command
* command: command to execute
* corner: Screen corner 'left', 'right', 'top', 'bottom'
* position: 'left', 'right', 'middle'

## Usage
```
  azot.py [-h] [-c CONFIG]
  optional arguments:
    -h, --help            show this help message and exit
    -c CONFIG, --config CONFIG
```

