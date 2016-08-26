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
from src.utils.console_colors import *
from src.core.enumeration.services_enum import *
from src.core.scanners.port_list import *


def scanner(name,path_file, port, message,result_file,CIDR, intensity,type,hostlist, iface):
        if os.path.isfile(path_file):
                print bcolors.WARNING + "[!] " + bcolors.ENDC + name + " Results File Exists. New results will be appended"
        print "[+] Scanning for " + name + " ..."
        nm = nmap.PortScanner()
        if (type == "y"):
                arg = "-Pn -sU -p" + port + " " + intensity + " --open"
        elif(type=="n"):
                arg = "-Pn -p" + port + " " + intensity + " --open"
        elif (type == "yn"):
                arg = "-Pn -p -sT -sU" + port + " " + intensity + " --open"
        arg += " -e " + iface
        for h in hostlist:
                nm.scan(hosts=h, arguments=arg)
                for host in nm.all_hosts():
                        writeFile = path_file
                        with open(writeFile, 'a') as hosts:
                                print ("----------------------------------------------------")
                                hosts.write('%s\n' % host)
                                print bcolors.OKGREEN + "*** " + name + " Found : %s via port " % host + port + " ***" + bcolors.ENDC
                                print bcolors.TITLE + message + bcolors.ENDC
        if (os.path.isfile(path_file)):
                print bcolors.TITLE + "\n[+] Done! Results saved in /Results/" + result_file + "\n" + bcolors.ENDC


def single_port_scanner(CIDR, intensity, iface):
        print " "
        print bcolors.OKGREEN + " [ TARGETTED SERVICES NETWORK SCANNER MODULE ]\n" + bcolors.ENDC
        print "\n[*] Beginning Scanning Subnet %s" % CIDR
        print " "
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

        for i in range(len(path_file)):
                scanner(name[i], path_file[i], port[i], message[i], result_file[i], CIDR, intensity, scan_type[i],hostlist, iface=iface)




