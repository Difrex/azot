# Azot

Screen corners action in all WMs.

It's look like KWin or Compiz, e.t.c

## Configuration

By default it's stored in ~/.config/azot/config.json

* type must be ''exec'', ''notify'' or ''simple''
* exec: just show command
* notify: Show output from command
* simple: just execute command without notify
* command: command to execute
* corner: Screen corner 'left', 'right', 'top', 'bottom'
* position: 'left', 'right', 'middle'
* check_delay and after_exec_delay are set in seconds

### Depends

* X11
* libnotify-bin
* python-xlib

## In action

Youtube:

[![ScreenShot](https://raw.githubusercontent.com/Difrex/azot/master/screenshot/screen.png)](https://youtu.be/-qg1swICh4Y)

## Usage
```
  azot.py [-h] [-c CONFIG]
  optional arguments:
    -h, --help            show this help message and exit
    -c CONFIG, --config CONFIG
```

