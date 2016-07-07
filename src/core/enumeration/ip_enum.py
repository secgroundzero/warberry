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
from scapy.all import *

def iprecon(ifname):

        print bcolors.OKGREEN + "      [ IP ENUMERATION MODULE ]\n" + bcolors.ENDC

        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            int_ip = socket.inet_ntoa(fcntl.ioctl(s.fileno(),0x8915, struct.pack('256s', ifname[:15]))[20:24])

        except:
            subprocess.call('clear', shell=True)
            banner_full()
            print bcolors.FAIL + "Interface %s seems to be down. Try Running with -I to specify an interface" %ifname + bcolors.ENDC

        netmask = socket.inet_ntoa(fcntl.ioctl(socket.socket(socket.AF_INET, socket.SOCK_DGRAM), 35099, struct.pack('256s', ifname))[20:24])

        if not ip_validate(int_ip) and int_ip!="169.254.253.251":
            print '[+] Internal IP obtained on '+ bcolors.TITLE + '%s:' % ifname + bcolors.ENDC + bcolors.OKGREEN + " %s" % int_ip + bcolors.ENDC + ' netmask ' + bcolors.OKGREEN + '%s' % netmask + bcolors.ENDC
            netmask = netmask_recon(ifname)
            external_IP_recon()
            CIDR = subnet(int_ip, netmask)
            scope_definition(ifname, CIDR)
            return int_ip
        else:

            print bcolors.FAIL + "[!] Invalid IP obtained." + bcolors.ENDC + " Checking if we can bypass with static IP.\n"
            return (static_bypass(ifname))

def scope_definition(ifname, CIDR):

    print ifname+"\n"
    print CIDR
    print bcolors.OKGREEN + "      [  SCOPE DEFINITION MODULE ]\n" + bcolors.ENDC

    print "Finding live IPs in order to include only those in the scans to minimize footprint\n"

    conf.verb = 0
    ans, unans = srp(Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=CIDR), iface=ifname, timeout=10)
    print bcolors.TITLE + "IP Addresses Found " + bcolors.ENDC
    print bcolors.TITLE + "--------------------" + bcolors.ENDC
    ips = []
    for snd, rcv in ans:
        print rcv.sprintf(r" %ARP.psrc%")
        ip_result = rcv.sprintf(r"%ARP.psrc%")
        ips.append(ip_result)
    with open('../Results/live_ips', 'w') as ip_addresses:
        for ip in ips:
            ip_n=ip+"\n"
            ip_addresses.write(ip_n)
