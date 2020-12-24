# python-am43

AM43 blinds motor API implementation written on Python.

> **Warning**  
> Library supports only Linux, and all features was tested on the Raspberry Pi 4 (4GB)

## Usage

Code example:

```python
import am43

blind = am43.search('xx:xx:xx:xx:xx:xx')
blind.set_position(percentage=20)  # Sets blinds position
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

Light property will be always return zero if the sensor don't plugged into the blind motor.

To use multiple blinds simply define the addresses in the `am43.search` method. It will return a list with a blinds:

```python
import am43
blinds = am43.search('xx:xx:xx:xx:xx:xx', 'xx:xx:xx:xx:xx:xx', 'xx:xx:xx:xx:xx:xx')

for blind in blinds:
    blind.set_position(percentage=10)
```

## Installation

To install the latest version you can use `pip` by executing that command:

```bash
$ pip install am43
```

All requirements will be installed automatically.

## Requirements

Full list of all dependencies you can find in `setup.py` file:

- `bluepy` >= 1.3.0
- `munch` >= 2.5.0

And you need to have bluetooth module on your machine. On Raspberry Pi (>=3) one is already on the board.

