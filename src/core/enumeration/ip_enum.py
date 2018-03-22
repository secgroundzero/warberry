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


from src.utils.utils import *
from scapy.all import *


def iprecon(ifname, netmask):

        print(bcolors.OKGREEN + "      [ IP ENUMERATION MODULE ]\n" + bcolors.ENDC)

        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            int_ip = socket.inet_ntoa(fcntl.ioctl(s.fileno(), 0x8915, struct.pack('256s', ifname[:15]))[20:24])
        except:
            subprocess.call('clear', shell=True)
            banner_full()
            print(bcolors.FAIL + "Interface %s seems to be down. Try Running with -I to specify an interface" %ifname + bcolors.ENDC)
            exit()

        if not ip_validate(int_ip) and int_ip != "169.254.253.251":
            print('[+] Internal IP obtained on ' + bcolors.TITLE + '%s:' % ifname + bcolors.ENDC + bcolors.OKGREEN + " %s" % int_ip + bcolors.ENDC + ' netmask ' + bcolors.OKGREEN + '%s' % netmask + bcolors.ENDC)
            external_IP_recon()
            return int_ip
        else:

            print(bcolors.FAIL + "[!] Invalid IP obtained." + bcolors.ENDC + " Checking if we can bypass with static IP.\n")
            return (static_bypass(ifname))


