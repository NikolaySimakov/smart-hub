import time
import requests
from typing import List

from device import Device, DeviceType
from packet import Packet
from payload import Payload


class SmartHub:
    
    def __init__(self, url: str, hub_address: bytes) -> None:
        self.url = url
        self.hub_address = hub_address
        self.serial = 1
    
    def WHOISHERE(self) -> List[Device]:
        '''
        Getting device type
        '''
        payload = Payload(src=self.hub_address,
                          dst=b'0x3FFF',
                          serial=self.serial,
                          dev_type=...,
                          cmd=DeviceType.SmartHub,
                          
                          )
        packet = Packet(payload)
        resp = self.post_request(packet.get_data())
        
    
    def GETSTATUS(self):
        pass
    
    def SETSTATUS(self):
        pass
    
    
    def post_request(self, data):
        resp = requests.post(url=self.url, data=data)
        self.serial += 1
        return resp
