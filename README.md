advancedremote
==============

just some tests for ipod in AIR mode.

Circut:

+5V ---------+                                                           #
             |                                                           #
             |            +------------------- pin 27 (data+)            # This
             |            |                                              # is
             |            |            +------ pin 16 (GND)              # for
             |            |            |                                 # charging.
             +--| 33k |---+---| 47k |--+                                 # Read
             |                                                           # more
             +--| 33k |---+---| 22k |--+                                 # at
             |            |            |                                 # http://pinouts.ru/PortableDevices/ipod_pinout.shtml
             |            |            +------ pin 15 (GND)              #
             |            |                                              #
             |            +------------------- pin 25 (data-)            #
             |                                                           #
             +-------------------------------- pin 23 (USB +5V in)       #

             +-------------------------------- pin 11 (Serial GND)
             |
             +--| 560k |---------------------- pin 21 (Dock identifier)
             |
GND ---------+


TX/RX on 13/12

Charging works with 6th gen ipod nano but not 7th gen ipod classic (120GB).
