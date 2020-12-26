from .blind import Blind
from bluepy import btle

def search(*addresses: list, auto_connect: bool = True, retry: bool = True) -> any:
    blinds = [Blind(device=device, auto_connect=auto_connect, retry=retry) for device in btle.Scanner().scan() if device.addr in addresses]
    return blinds[0] if len(addresses) == 1 else blinds
