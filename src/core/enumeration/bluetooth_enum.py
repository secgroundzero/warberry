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

from src.core.enumeration.bluetooth_enum import *
import subprocess
import os
from src.utils.console_colors import *
from bluetooth import *

def bluetooth_enum():

    subprocess.call("sudo cat /proc/cpuinfo | grep Revision | awk {'print $3'} > Results/model", shell=True)

    blues=[]
    with open('Results/model', 'r') as pi_model:
        for model in pi_model:
            if model.strip() == "a02082":
                print (" ")
                print (bcolors.OKGREEN + "      [ BLUETOOTH ENUMERATION MODULE ]\n" + bcolors.ENDC)
                length=0
                for i in range(10):
                    blues=discover()
                    length=length+len(blues)

    
    subprocess.call("rm Results/model", shell=True)
    if length == 0:
	print(bcolors.WARNING + "[-] No Bluetooth Devices Captured" + bcolors.ENDC)
    else:
	print(bcolors.TITLE + "[+] Done! Results saved in warberry.db" + bcolors.ENDC)
    return blues


def discover():
    bluef=[]
    blues = discover_devices()
    for device in blues:
        name = str(lookup_name(device))
        b={}
        b["name"]=str(name)
        b["device"]=str(device)
        bluef.append(b)

        print (bcolors.OKGREEN + "[+]" + bcolors.ENDC + " Found Bluetooth Device: " + str(name))
        print (bcolors.OKGREEN + "[+]" + bcolors.ENDC + " MAC address: " + str(device))
    return bluef
