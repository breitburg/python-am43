# python-am43 ![](https://img.shields.io/pypi/dm/am43)

AM43 blinds motor protocol implementation written in Python.

> **Warning**  
> Library supports only Linux, and all features was tested on the Raspberry Pi 4

## Usage

To search for single blind use `am43.search` method:

```python
import am43

blind = am43.search('xx:xx:xx:xx:xx:xx')  # Returns single blind
blind.set_position(percentage=30)  # Sets blinds position
```

To use multiple blinds simply define the addresses in the `am43.search` method. It will return a list with a blinds:

```python
blinds = am43.search(
    'xx:xx:xx:xx:xx:xx',
    'xx:xx:xx:xx:xx:xx',
    'xx:xx:xx:xx:xx:xx'
)  # Returns multiple blinds instances
```

You can stop the blinds using `Blind.stop` method:

```python
blind.stop()  # Stops blinds
```

Also, you can access the motor properties:

```python
properties = blind.get_properties()

properties.battery  # 95 <int>
properties.position  # 100 <int>
properties.light  # 23 <int>
```

The light property will be zero if the sensor is not plugged in to the blind motor.

## Installation

To install the latest version you can use `pip` by executing that command:

```bash
$ pip install am43
```

All the requirements will be installed automatically.

## Requirements

Full list of all dependencies you can find in `setup.py` file:

- `bluepy` >= 1.3.0
- `munch` >= 2.5.0

And you need to have bluetooth module on your machine. On Raspberry Pi (>=3) one is already on the board.

