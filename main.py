import argparse
from typing import List, Tuple

from smart_hub import SmartHub
from device import Device


def parse_cmd_line() -> Tuple[str, bytes]:
    parser = argparse.ArgumentParser()
    parser.add_argument("url")
    parser.add_argument("hub_address")
    args = parser.parse_args()
    return args.url, args.hub_address

if __name__ == '__main__':
    
    # Init Smart Hub
    url, hub_address = parse_cmd_line()
    hub = SmartHub(url, hub_address)
    
    # Getting devices list
    devices: List[Device] = hub.WHOISHERE()
    
    for device in devices:
        pass
