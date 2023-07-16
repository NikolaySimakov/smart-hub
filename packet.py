from payload import Payload

class Packet:
    def __init__(self, payload: Payload) -> None:
        self.payload: bytearray = payload.to_bytearray()
        self.length: bytes = len(self.payload)
        self.crc8: bytes = self._calculate_crc8()
        
    def _calculate_crc8(self):  
        """Calculate 8-bit Cyclic Redundancy Check."""
        # You'll replace this with the actual calculation.
        return 0
    
    def get_data(self):
        return {
            "length" : self.length,
            "payload" : self.payload,
            "crc8" : self.crc8,
        }