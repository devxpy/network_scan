# network_scan
Periodically (10sec) calls `arp` command to check if the desired nodes are active

## Dependencies

- python 3.6
- net-tools

`sudo apt install python3.6 net-tools`


## Config

- Set the recognised devices in the `saved` list
- Set the interface. Run `ifconfig` to check all the network interfaces

## Usage

`python3 scan.py`
