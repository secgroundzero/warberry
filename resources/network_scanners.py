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
import sys, getopt
import socket
import fcntl
import struct
import re
import nmap
from socket import inet_aton
from info_banners import *
from services_enum import *
from console_colors import bcolors



def scanner_full(CIDR):

        print bcolors.OKGREEN + "      [ TCP/UDP NETWORK SCANNER MODULE ]\n" + bcolors.ENDC

        if os.path.isfile('../Results/tcp_udp_scan'):
                print bcolors.WARNING + "[!] TCP/UDP Results File Exists. Previous Results will be Overwritten " + bcolors.ENDC

        print "Beginning Scanning Subnet %s" %CIDR

        print " "
        nm = nmap.PortScanner()

        print "[+] Scanning TCP/UDP Ports in all hosts..."
        nm.scan(hosts=CIDR, arguments='-Pn -T4 -sT -sU --open -o ../Results/tcp_udp_scan')
        for host in nm.all_hosts():
                print('----------------------------------------------------')


def scanner_tcp_full(CIDR):

        print bcolors.OKGREEN + "      [ FULL TCP NETWORK SCANNER MODULE ]\n" + bcolors.ENDC

        if os.path.isfile('../Results/tcp_full'):
                print bcolors.WARNING + "[!] Full TCP Results File Exists. Previous Results will be Overwritten" + bcolors.ENDC

        print "Beginning Scanning Subnet %s" %CIDR

        print " "
        nm = nmap.PortScanner()

        print "[+] Scanning All TCP Ports in all hosts..."
        nm.scan(hosts=CIDR, arguments='-Pn -T4 -p1-65535 --open -o ../Results/tcp_full')
        for host in nm.all_hosts():
                print('----------------------------------------------------')
                print host + nm[host].hostname() + " open TCP ports: "
                for proto in nm[host].all_protocols():
                        lport = nm[host][proto].keys()
                        lport.sort()
                for port in lport:
                        print bcolors.OKGREEN + ' [+] ' + bcolors.ENDC + '%s' %port


def scanner_top(CIDR):

        print bcolors.OKGREEN + "      [ TOP TCP PORTS NETWORK SCANNER MODULE ]\n" + bcolors.ENDC

        if os.path.isfile('../Results/top_tcp'):
                print bcolors.WARNING + "[!] Top TCP Ports Results File Exists. Previous Results will be Overwritten" + bcolors.ENDC

        print "Beginning Scanning Subnet %s" %CIDR
        print " "
        nm = nmap.PortScanner()

        print "[+] Scanning TOP 1000 TCP Ports in all hosts..."
        nm.scan(hosts=CIDR, arguments='-Pn -T4 --top-ports 1000 --open -o ../Results/tcp_top')
        for host in nm.all_hosts():
                print('----------------------------------------------------')
                print host + nm[host].hostname() + " open TCP ports: "
                for proto in nm[host].all_protocols():
                        lport = nm[host][proto].keys()
                        lport.sort()
                for port in lport:
                        print bcolors.OKGREEN + ' [+] ' + bcolors.ENDC + '%s' %port

