# clinlog

[![PyPI version](https://badge.fury.io/py/clinlog.svg)](https://badge.fury.io/py/clinlog)
[![PyPI version](https://img.shields.io/github/license/salpreh/clinlog.svg)](https://img.shields.io/github/license/salpreh/clinlog.svg)

**Package to easily log styled messages on console using [colorama](https://github.com/tartley/colorama)**

---
## Basic usage
Create a `Logger` object and use his convenient methods to print styled messages in console. You can define a default tag for each kind of message on the `Logger` instance.

### Print style methods
- `confirm()`
- `error()`
- `warning()`
- `info()`
- `debug()`
- `print()`

The signature for all print methods are the same:
1. **message _(str)_**: Message to print.
2. **tag _(str)_**: (Optional) Prefix tag to print with the message. If `None` the default tag for this kind of messages is used. An empty string will remove the tag for this print.
3. **bold _(bool)_**: (Optional) `True` to use bright style to print the message (kind of bold font). By default `False`.
4. **highlight _(bool)_**: `True` to use the color on the background and a high contrast color for the message text.
5. **invert_color _(bool)_**: `True` to invert font color when highlight flag is on, this will switch between black and white. By default `False`.

### Default print tag attributes
When a `Logger` object is created all default tags are an empty string _(no tag)_
- `confirm_tag`
- `error_tag`
- `warn_tag`
- `info_tag`
- `print_tag`

### Log level param
You can provide a log level parameter to control the verbosity of the logger, this parameter can be provided during construction or via setter method. By default `Logger` class takes max verbosity level _(debug)_
```py
from clinlog import Logger

# Creating a Logger with warining log level
log = Logger(log_level='warning')

# Updating log level via setter
log.log_level = 'debug'

```


### Code Sample
```py
from clinlog import Logger

# Create the logger
log = Logger()

# Set default error tag
log.error_tag = '[ERROR]: '

# Print error styled message
log.error('Unable to access config file', bold=True)

# Print warning highlighted and bold
log.warning('The execution will continue with default configuration', None, True, True)

# Confirmation log with provided tag
log.confirm('Execution completed', '[SUCCESS]')

# Debug log with provided tag
log.debug('DB returned 8 entries for the user', '[DEBUG] ')
```

### Output
<img src="https://raw.githubusercontent.com/salpreh/clinlog/master/assets/output.png" alt="tree_output">

### Different styes sample
<img src="https://raw.githubusercontent.com/salpreh/clinlog/master/assets/sample.png" alt="tree_output">
