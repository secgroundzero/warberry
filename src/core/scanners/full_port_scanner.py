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
import nmap
from src.utils.console_colors import *


def tcpudp_scanner(CIDR,intensity, iface):

        print bcolors.OKGREEN + "      [ TCP/UDP NETWORK SCANNER MODULE ]\n" + bcolors.ENDC

        if os.path.isfile('../Results/tcp_udp_scan'):
                print bcolors.WARNING + "[!] TCP/UDP Results File Exists. Previous Results will be Overwritten " + bcolors.ENDC

        hostlist = []
        if os.path.isfile('../Results/live_ips'):
                with open('../Results/live_ips', 'r') as h:
                        hosts = h.readlines()
                        for host in hosts:
                                hostlist.append(host.strip())
        else:
                with open('../Results/ips_discovered', 'r') as h:
                        hosts = h.readlines()
                        for host in hosts:
                                hostlist.append(host.strip())

        print "Beginning Scanning Subnet %s" %CIDR

        print " "
        nm = nmap.PortScanner()

        print "[+] Scanning TCP/UDP Ports in all hosts..."
        arg = "-Pn " + intensity + " -sT -sU --open -o ../Results/tcp_udp_scan -e " + iface
        for h in hostlist:
                nm.scan(hosts=h, arguments=arg)
                for host in nm.all_hosts():
                        print('----------------------------------------------------')
                        print host + nm[host].hostname() + " open TCP/UDP ports: "
                        for proto in nm[host].all_protocols():
                                lport = nm[host][proto].keys()
                                lport.sort()
                        for port in lport:
                                print bcolors.OKGREEN + ' [+] ' + bcolors.ENDC + '%s' % port



def full_scanner(CIDR,intensity, iface):

        print bcolors.OKGREEN + "      [ FULL TCP NETWORK SCANNER MODULE ]\n" + bcolors.ENDC

        if os.path.isfile('../Results/tcp_full'):
                print bcolors.WARNING + "[!] Full TCP Results File Exists. Previous Results will be Overwritten" + bcolors.ENDC

        print "Beginning Scanning Subnet %s" %CIDR

        print " "
        nm = nmap.PortScanner()
        hostlist = []
        if os.path.isfile('../Results/live_ips'):
                with open('../Results/live_ips', 'r') as h:
                        hosts = h.readlines()
                        for host in hosts:
                                hostlist.append(host.strip())
        else:
                with open('../Results/ips_discovered', 'r') as h:
                        hosts = h.readlines()
                        for host in hosts:
                                hostlist.append(host.strip())

        print "[+] Scanning All TCP Ports in all hosts..."
        arg = "-Pn " + intensity + " -p1-65535 --open -o ../Results/tcp_full -e " + iface
        for h in hostlist:
                nm.scan(hosts=h, arguments=arg)
                for host in nm.all_hosts():
                        print('----------------------------------------------------')
                        print host + nm[host].hostname() + " open TCP ports: "
                        for proto in nm[host].all_protocols():
                                lport = nm[host][proto].keys()
                                lport.sort()
                        for port in lport:
                                print bcolors.OKGREEN + ' [+] ' + bcolors.ENDC + '%s' %port