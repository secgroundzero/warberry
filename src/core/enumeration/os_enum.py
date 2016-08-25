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

import os, os.path
import subprocess
from src.utils.console_colors import *

def os_enum(CIDR,iface):

        subprocess.call("nmap -sP %s -e %s -oG - | awk '/Up$/{print $2}' >> ../Results/live_ips" % (iface, CIDR), shell=True)

        if os.stat('../Results/live_ips').st_size != 0:
                print " "
                print bcolors.OKGREEN + "      [ OS ENUMERATION MODULE ]\n" + bcolors.ENDC
        else:
                return

        if os.path.isfile('../Results/os_enum'):
                print bcolors.WARNING + "[!] OS Enum Results File Exists. Previous Results will be Overwritten\n " + bcolors.ENDC

        subprocess.call("sudo sort ../Results/live_ips | uniq > ../Results/liveip_hosts", shell=True)
        with open('../Results/liveip_hosts') as alive:
                for live in alive:
                        print "[*] Enumerating OS on %s" %live.strip()
                        subprocess.call('sudo xprobe2 -D 11 %s 2>/dev/null | grep -A 1 "Primary guess:" >> ../Results/os_enum' %live.strip(), shell=True)

        print bcolors.TITLE + "[+] Done! Results saved in /Results/os_enum" + bcolors.ENDC
