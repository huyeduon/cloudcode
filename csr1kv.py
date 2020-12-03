# Check on-prem tunnel status
# POC Quality
# Author: Huyen Duong

import sys, os
from netmiko import ConnectHandler
from countKeyWord import *

csr1k = {
    'device_type': 'cisco_ios',
    'host':   '13.239.93.113',
    'username': 'cisco',
    'password': '123Cisco123!',
    'port' : 22,          # optional, defaults to 22
}

net_connect = ConnectHandler(**csr1k)
tun1 = net_connect.send_command('show interfaces tunnel1')

with open('tun1_file.txt','w') as writer:
    writer.write(tun1)

net_connect.disconnect()

firstLine = ''
with open('tun1_file.txt','r') as reader:
    lines = reader.readlines()
    firstLine = lines[0]
    firstLine.split()

key_word = 'up'
up_count = 0
up_count = countKeyWord(key_word, firstLine)
if up_count == 2:
    print("onprem tunnel is up")