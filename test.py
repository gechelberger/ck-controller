"""
Title:
Description:
Usage:
Date Started:
Last Modified:
http://www.asymptoticdesign.org/
This work is licensed under a Creative Commons 3.0 License.
(Attribution - NonCommerical - ShareAlike)
http:#creativecommons.org/licenses/by-nc-sa/3.0/

In summary, you are free to copy, distribute, edit, and remix the work.
Under the conditions that you attribute the work to the author, it is for
noncommercial purposes, and if you build upon this work or otherwise alter
it, you may only distribute the resulting work under this license.

Of course, these permissions may be waived with permission from the author.

Description of Usage:
scottnla@faraday-cage:~/$ python readSerial.py [filename]
Reads serial information from an arduino circuit, writes it to file.
"""

import socket
import struct
import time
import numpy
import ckdmxlib
from numpy import *

def update_display(sockt, channel, lightArray):
    header = bytearray([0x04, 0x01, 0xdc, 0x4a, 0x01, 0x00, 0x08, 0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, channel, 0x00, 0x00, 0x00, 0x96, 0x00, 0xff, 0x0f])
    rgb_data = bytearray()
    for light in lightArray:
        rgb_data.append(light >> 16)
        rgb_data.append(light >> 8 & 0xff)
        rgb_data.append(light & 0xff)
    packetData = str(header) + str(rgb_data)
    sockt.send(packetData)

#Setup UDP Socket
destination_address = ('10.32.0.61', 6038)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.connect(destination_address)

#To set all lights to one color, then stop:
pixels = [0xAA00FF for i in range(0,50)]
update_display(sock, 0x01, pixels)
update_display(sock, 0x02, pixels)

time.sleep(5)

#Now to set a loop:

val = 0
sign = 1

while(True):
    if(val == 0x0000ff):
        sign = -1
        val += sign
    if (val == 0x000000):
        sign = 1
        val += sign
    else:
        val += sign
        pixels = [val for i in range(0,50)]
        update_display(sock, 0x01, pixels)
        update_display(sock, 0x02, pixels)
        time.sleep(0.01)
        