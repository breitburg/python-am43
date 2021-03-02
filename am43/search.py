from .blind import Blind
from bluepy import btle


def search(*addresses: list, auto_connect: bool = True, retry: bool = True, device: int = 0) -> any:
    blinds = [Blind(device=device, auto_connect=auto_connect, retry=retry) for device in btle.Scanner(device).scan() if
              device.addr in addresses]

    if not blinds:
        raise IndexError('there is no blinds were found')

    return blinds[0] if len(blinds) == 1 else blinds
