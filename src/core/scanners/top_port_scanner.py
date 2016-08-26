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

import nmap
import os,os.path
from src.utils.console_colors import *

def top_ports_scanner(CIDR,intensity,iface):

        print bcolors.OKGREEN + "      [ TOP TCP PORTS NETWORK SCANNER MODULE ]\n" + bcolors.ENDC

        if os.path.isfile('../Results/top_tcp'):
                print bcolors.WARNING + "[!] Top TCP Ports Results File Exists. Previous Results will be Overwritten" + bcolors.ENDC

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

        print "[+] Scanning Top 1000 TCP Ports in all hosts with %s intensity..." %intensity + "\n"
        arg = "-Pn " + intensity + " --top-ports 1000 --open -o ../Results/tcp_top -e " + iface
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
