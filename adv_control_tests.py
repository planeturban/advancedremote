#!/usr/bin/env python


import general
import serial
import time
import advanceddock
import struct
from general import *
serialPort = "/dev/tty.usbserial"

ser = serial.Serial(serialPort, baudrate=19200, timeout=1)

ser.write(general.mkcmd(0, "0104")) # Set iPod in AIR mode.
res = readResponse()


ser.write(advanceddock.set_pulling_mode(1))
ser.write(advanceddock.switch_to_type(5,0))

while True:
    if ser.inWaiting():
        res = readResponse(fullMessage=True)
        print res
