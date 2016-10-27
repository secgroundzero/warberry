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

import os
import socket
from src.utils.info_banners import *
import fcntl
import struct
from netaddr import *
from src.utils.console_colors import *
from src.core.bypass.static import *
from src.core.bypass.nac import *
from src.core.bypass.mac import *
from src.utils.utils import *



def zone_transfers(CIDR, iface):

        if os.path.isfile('../Results/zones'):
                if os.stat('../Results/dns').st_size != 0:
                        print " "
                        print bcolors.OKGREEN + "      [ ZONE TRANSFER MODULE ]\n" + bcolors.ENDC
                else:
                        return

        if os.path.isfile('../Results/zones'):
                print bcolors.WARNING + "[!] Zone Transfer Results File Exists. Previous Results will be overwritten\n " + bcolors.ENDC
                with open('../Results/dns') as dns:
                        for host in dns:
                                print bcolors.WARNING + "[*] Attempting Zone Transfer on %s" %host.strip() + bcolors.ENDC
                                subprocess.call('sudo nmap -Pn -e' + iface + '--script=dns-zone-transfer %s -O ../Results/domains' %host, shell = True)
                print bcolors.TITLE + "[+] Done! Results saved in /Results/zones" + bcolors.ENDC
        else:
                return


