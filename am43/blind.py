from bluepy import btle
from munch import Munch
import time


class Blind:
    def __init__(self, device: object = None, auto_connect: bool = True, retry: bool = True):
        self.retry = retry
        self.device = device
        self.identifiers = Munch(move=0x0d, stop=0x0a, battery=0xa2, light=0xaa, position=0xa7)
        self.blind = None
        self._battery = self._position = self._light = None

        if auto_connect:
            self.connect()

    def connect(self, service: str = 'fe50', characteristic: str = 'fe51') -> None:
        while True:
            try:
                self.blind = btle.Peripheral(self.device)

                delegate = btle.DefaultDelegate()
                delegate.handleNotification = lambda handle, data: self._update_data(data=data)
                self.blind.setDelegate(delegate)

                self.characteristic = self.blind.getServiceByUUID(service).getCharacteristics(characteristic)[0]
                return
            except btle.BTLEDisconnectError as error:
                self.disconnect()
                if not self.retry:
                    raise error
                else:
                    time.sleep(1)
    
    def disconnect(self):
        if self.blind:
            self.blind.disconnect()
            self.blind = None

    def send(self, data: any, identifier: bytearray, wait_notification: bool = False) -> dict:
        while True:
            try:
                if not self.blind:
                    self.connect()

                message = bytearray({0x9a}) + bytearray({identifier}) + bytearray({len([data])}) + bytearray([data])
                message += self._calculate_checksum(data=message)

                if wait_notification and self.blind.waitForNotifications(10):
                    pass

                return self.characteristic.write(message)
            except btle.BTLEDisconnectError as error:
                self.disconnect()
                if not self.retry:
                    raise error
                else:
                    self.connect()

    def _update_data(self, data: bytearray) -> None:
        identifier = data[1]

        if identifier == self.identifiers.battery:
            self._battery = data[7]
        elif identifier == self.identifiers.position:
            self._position = data[5]
        elif identifier == self.identifiers.light:
            self._light = data[4] * 12.5

    def get_properties(self) -> Munch:
        self.send(data=0x01, identifier=self.identifiers.battery, wait_notification=True)
        self.send(data=0x01, identifier=self.identifiers.position, wait_notification=True)
        self.send(data=0x01, identifier=self.identifiers.light, wait_notification=True)

        return Munch(battery=self._battery, position=self._position, light=self._light)

    def set_position(self, percentage: int) -> None:
        self.send(data=percentage, identifier=self.identifiers.move)

    def stop(self) -> None:
        self.send(data=0xcc, identifier=self.identifiers.stop)

    @staticmethod
    def _calculate_checksum(data: bytearray) -> bytearray:
        checksum = 0
        for byte in data:
            checksum = checksum ^ byte

        return bytearray({checksum})
