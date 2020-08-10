from bluepy import btle
from munch import munchify


class Blind:
    def __init__(self, address: bytes, auto_connect: bool = True, reconnect: bool = True):
        self.address = address
        self.device = [device for device in btle.Scanner().scan() if device.addr == address][0]
        self.identifiers = munchify(dict(move=0x0d, stop=0x0a, battery=0xa2, light=0xaa, position=0xa7))
        self.reconnect = reconnect

        if auto_connect:
            self.connect(retry=True)

    def connect(self, retry: bool = False, service: str = 'fe50', characteristic: str = 'fe51') -> None:
        while True:
            try:
                self.blind = btle.Peripheral(self.device)
                self.characteristic = self.blind.getServiceByUUID(service).getCharacteristics(characteristic)[0]
            except btle.BTLEDisconnectError:
                if retry:
                    continue
            break

    def send(self, data: any, identifier: bytearray) -> dict:
        if self.reconnect: self.connect()

        message = bytearray({0x9a}) + bytearray({identifier}) + bytearray({len([data])}) + bytearray([data])
        message += self.calculate_checksum(data=message)
        result = self.characteristic.write(message)

        if self.reconnect: self.blind.disconnect()
        return result

    def set_position(self, percentage: int) -> None:
        self.send(data=percentage, identifier=self.identifiers.move)

    def stop(self) -> None:
        self.send(data=0xcc, identifier=self.identifiers.stop)

    @staticmethod
    def calculate_checksum(data: bytearray) -> bytearray:
        checksum = 0
        for byte in data:
            checksum = checksum ^ byte

        return bytearray({checksum})
