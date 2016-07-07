"""
This file is part of the WarBerry tool.
Copyright (c) 2016 Yiannis Ioannides (@sec_groundzero).
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
import os, os.path
from src.utils.console_colors import *
from bluetooth import *

def bluetooth_enum():

    subprocess.call("sudo cat /proc/cpuinfo | grep Revision | awk {'print $3'} > ../Results/model", shell=True)

    with open('../Results/model', 'r') as pi_model:
        for model in pi_model:
            if model.strip() == "a02082":
                print " "
                print bcolors.OKGREEN + "      [ BLUETOOTH ENUMERATION MODULE ]\n" + bcolors.ENDC

                def discover():
                    blues = discover_devices()
                    for device in blues:
                        name = str(lookup_name(device))
                        with open('../Results/blues','a') as bluesfile:
                            bluesfile.write(str(name) + " " + str(device)+ "\n")

                        print bcolors.OKGREEN + "[+]" + bcolors.ENDC + " Found Bluetooth Device: " + str(name)
                        print bcolors.OKGREEN + "[+]" + bcolors.ENDC + " MAC address: " + str(device)

                for i in range(10):
                    discover()
            else:
                return
    if os.path.isfile('../Results/blues'):
        if os.stat('../Results/blues').st_size != 0:
            print bcolors.TITLE + "[+] Done! Results saved in /Results/blues" + bcolors.ENDC
    else:
        print bcolors.WARNING + "[-] No Bluetooth Devices Captured" + bcolors.ENDC
