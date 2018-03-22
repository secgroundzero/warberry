#!/usr/bin/python2

"""
This file is part of the WarBerry tool.
Copyright (c) 2018 Yiannis Ioannides (@sec_groundzero).
https://github.com/secgroundzero/warberry
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
"""
from optparse import OptionParser
from src.utils.console_colors import *
from src.warberrySetup.Warberry import *

def warberry():

    version = bcolors.TITLE + ( '''
 _    _  ___  ____________ ___________________   __
| |  | |/ _ \ | ___ \ ___ \  ___| ___ \ ___ \ \ / /
| |  | / /_\ \| |_/ / |_/ / |__ | |_/ / |_/ /\ V /
| |/\| |  _  ||    /| ___ \  __||    /|    /  \ /
\  /\  / | | || |\ \| |_/ / |___| |\ \| |\ \  | |
 \/  \/\_| |_/\_| \_\____/\____/\_| \_\_| \_| \_/

            TACTICAL EXPLOITATION

v5.1                              @sec_groundzero
                          secgroundzero@gmail.com
''') + bcolors.ENDC


    parser = OptionParser(usage= "usage: sudo %prog [options]",version=version)
    parser.add_option("-p", "--packets", action="store", dest="packets", default=20, type=int, help="# of Network Packets to capture" + bcolors.WARNING + " Default: 20" + bcolors.ENDC)
    parser.add_option("-x", "--expire", action="store", dest="expire", default=20, type=int,help="Time for packet capture to stop" + bcolors.WARNING + " Default: 20s" + bcolors.ENDC)
    parser.add_option("-I", "--interface", action="store", dest="iface", default="eth0",help="Network Interface to use." + bcolors.WARNING + " Default: eth0" + bcolors.ENDC, choices=['eth0', 'eth1', 'wlan0', 'wlan1', 'wlan2', 'at0'])
    parser.add_option("-N", "--name", action="store", dest="name", default="WarBerry",help="Hostname to use." + bcolors.WARNING + " Default: Auto" + bcolors.ENDC)
    parser.add_option("-i", "--intensity", action="store", dest="intensity", default="-T1", help="Port scan intensity." + bcolors.WARNING + " Default: T1" + bcolors.ENDC,choices=['-T1', '-T2', '-T3', '-T4'])
    parser.add_option("-P", "--poison", action="store_false",dest="poison",default=True, help="Turn Poisoning off."+ bcolors.WARNING + " Default: On" + bcolors.ENDC)
    parser.add_option("-t", "--time", action="store", dest="time", default=900, type=int, help="Responder Timeout Seconds")
    parser.add_option("-Q", "--quick", action="store_true", dest="fast", default=False, help="Scan using threads." + bcolors.WARNING + " Default: Off" + bcolors.ENDC)
    parser.add_option("-H", "--hostname", action="store_false", dest="hostname", default= True, help="Do not change WarBerry hostname" + bcolors.WARNING + " Default: Off" + bcolors.ENDC)
    parser.add_option("-e", "--enumeration", action="store_true",dest="enum", default=False, help="Disable enumeration mode." + bcolors.WARNING + " Default: Off" + bcolors.ENDC)
    parser.add_option("-M", "--malicious", action="store_true", dest="malicious", default=False, help="Enable Malicious only mode" + bcolors.WARNING + " Default: Off" + bcolors.ENDC)
    parser.add_option("-B", "--bluetooth", action="store_true", dest="btooth", default=False, help="Enable Bluetooth Scanning" + bcolors.WARNING + " Default: Off" + bcolors.ENDC)
    parser.add_option("-W", "--wifi", action="store_true", dest="wifi", default=False, help="Enable WiFi Scanning" + bcolors.WARNING + " Default: Off" + bcolors.ENDC)
    parser.add_option("-r", "--recon", action="store_true", dest="reconmode", default=False,help="Enable Recon only mode. " + bcolors.WARNING + " Default: Off" + bcolors.ENDC)
    parser.add_option("-C", "--clear", action="store_true", dest="clear", default=False, help="Clear previous output folders in ../Results")
    parser.add_option("-m", "--man", action="store_true", dest="manpage", default=False, help="Print WarBerry man pages")


    (options, args) = parser.parse_args()

    x = Warberry(options)




if __name__ == '__main__':

    warberry()