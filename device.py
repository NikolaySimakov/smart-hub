from enum import Enum

# Available devices
class DeviceType(Enum):
    SmartHub: bytes = b'0x01'
    EnvSensor: bytes = b'0x02'
    Switch: bytes = b'0x03'
    Lamp: bytes = b'0x04'
    Socket: bytes = b'0x05'
    Clock: bytes = b'0x06'
    
    def __str__(self) -> str:
        return self.name

# Device model
class Device:
    def __init__(self, dev_name: DeviceType, dev_props: bytearray) -> None:
        self.dev_name = str(dev_name)
        self.dev_props = dev_props
