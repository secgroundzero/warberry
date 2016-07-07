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

import subprocess
import os, os.path
from src.utils.console_colors import *

def wifi_enum():

    subprocess.call("sudo cat /proc/cpuinfo | grep Revision | awk {'print $3'} > ../Results/model", shell=True)

    with open('../Results/model', 'r') as pi_model:
        for model in pi_model:
            if model.strip() == "a02082":
                print " "
                print bcolors.OKGREEN + "      [ Wi-Fi ENUMERATION MODULE ]\n" + bcolors.ENDC

                subprocess.call("sudo iwlist wlan0 scan | grep ESSID | awk {'print $1'} > ../Results/wifis", shell = True)
                if os.path.isfile('../Results/wifis'):
                    with open('../Results/wifis', 'r') as wifis:
                        if os.stat('../Results/wifis').st_size != 0:
                            for wifi in wifis:
                                print bcolors.OKGREEN + "[+] " + bcolors.ENDC + "Found Wireless Network: %s" %wifi.strip() + bcolors.ENDC
                        else:
                            print bcolors.WARNING + "[-] No Wireless Networks Captured" + bcolors.ENDC
                else:
                    return
            else:
                return
