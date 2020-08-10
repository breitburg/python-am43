# python-am43

AM43 blinds motor API implementation written on Python.

> **Warning**  
> Library supports only Linux, and all features was tested on the Raspberry Pi 4 (4GB)

## Usage

Code example:

```python
import am43

blind = am43.Blind(address='xx:xx:xx:xx:xx:xx')
blind.set_position(percentage=20)  # Sets blinds position
```

You can stop the blinds using `Blind.stop` method:

```python
blind.stop()  # Stops blinds
```

## Installation

To install the latest version you can use `pip` by executing that command:

```bash
$ pip install am43
```


## Requirements

Full list of all dependencies you can find in `setup.py` file:

- `bluepy` >= 1.3.0
- `munch` >= 2.5.0

And you need to have bluetooth module on your machine. On Raspberry Pi (>=3) one is already on the board.