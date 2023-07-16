
class Payload:
    def __init__(self, src: int, dst: int, serial: int, dev_type: bytes, cmd: bytes, cmd_body: bytearray) -> None:
        self.src = src
        self.dst = dst
        self.serial = serial
        self.dev_type = dev_type
        self.cmd = cmd
        self.cmd_body = cmd_body
    
    def to_bytearray(self) -> bytearray:
        # For integers, we'll use 'to_bytes' with big endian byte order
        src_bytes = self.src.to_bytes(4, 'big') 
        dst_bytes = self.dst.to_bytes(4, 'big') 
        serial_bytes = self.serial.to_bytes(4, 'big')

        # Assuming 'dev_type' is a string, we'll convert it into bytes
        dev_type_bytes = self.dev_type.encode('utf-8')

        # cmd and cmd_body are already bytes, so no need to convert them

        # Now that all attributes are bytes, we can concatenate them into one byte array 
        return bytearray(src_bytes + dst_bytes + serial_bytes + dev_type_bytes + self.cmd + self.cmd_body)
    