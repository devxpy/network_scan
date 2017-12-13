#!/usr/bin/python3

import subprocess
import re
from time import time

# Store Mac address of all nodes here
saved = [
    'cc:fa:00:a7:73:ba',
    '34:78:d7:84:93:d9',
    'fc:f8:ae:8d:b0:2b',
    '50:8f:4c:80:65:3d',
    '78:02:f8:8d:9d:5d',
]

# Set wireless interface using ifconfig
interface = "wlan0"

mac_regex = re.compile(r'([a-zA-Z0-9]{2}:){5}[a-zA-Z0-9]{2}')


def parse_arp():
    arp_out = subprocess.check_output(f'arp -e -i {interface}', shell=True).decode('utf-8')
    if 'no match found' in arp_out:
        return None
    
    result = []
    for lines in arp_out.strip().split('\n'):
        line = lines.split()
        if interface in line and '(incomplete)' not in line:
            for element in line:
                # If its a mac addr
                if mac_regex.match(element):
                    result.append({'Address' : line[0], 'mac' : element})
    return result



if __name__ == '__main__':
    while True:
        devices = parse_arp()
            
        if not devices:
            print('No devices found!')
            
        else:
            macs = []
            for device in devices:
                if device['mac'] not in saved:
                    print('Unkown Device', device)
                else:
                    print('Found Device', device)
                
                macs.append(device['mac'])
            
            count = 0
            for saved_device in saved:
                if saved_device not in macs:
                    print('Device Missing', saved_device)
                    count += 1
            print(f'\n{count} missing devices')
        
        sleep(10)
