#!/usr/bin/python3

import subprocess
import re
import requests

# Store Mac address of all nodes here
saved = {
    'cc:fa:00:a7:73:ba': 'dev mob',
    '34:78:d7:84:93:d9': 'akshat mob',
    'fc:f8:ae:8d:b0:2b': 'akshat laptop',
    '50:8f:4c:80:65:3d': 'Karan mob',
    '78:02:f8:8d:9d:5d': 'Shubh mob',
}

# Set wireless interface using ifconfig
interface = "wlp4s0"

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
                    result.append((line[0], element))
    return result


def get_mac_vendor(devices):
    num=0
    for device in devices:
        try:
            url = f"http://api.macvendors.com/{device[1]}"
            vendor = requests.get(url).text
                
            device_name = saved[device[1]] if device[1] in saved else 'unrecognised !!'
            
            num+=1
            print(f'\n{num})', device_name,  '\nVendor:', vendor, '\nMac:', device[1], '\nIP: ',device[0])
        
        except Exception as e:
            print(e)

print('Retrieving connected devices ..')

devices = parse_arp()

if not devices:
    print('No devices found!')
    
else:
    print('Retrieving mac vendors ..')

    get_mac_vendor(devices)

