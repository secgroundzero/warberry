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
from src.core.enumeration.services_enum import *
from src.utils.port_obj_Read import port_obj_reader


def scanner(name, path_file, port, message, result_file, CIDR, intensity, type, hostlist, iface):
    port = str(port).translate(None,'\'\"][ ')
    port =port.split(',')
    if os.path.isfile(path_file):
        print bcolors.WARNING + "[!] " + bcolors.ENDC + name + " Results File Exists. New results will be appended"
    print "[+] Scanning for " + name + " ..."
    nm = nmap.PortScanner()
    for i in range(0,len(port)):
        if (type == "y"):
            arg = "-Pn -sU -p:" + str(port[i]).translate(None, '\'][ ') + " " + intensity + " --open"
        elif (type == "n"):
            arg="-Pn -p"+str(port[i]).translate(None, '\'][ ') + " " + intensity + " --open"
        elif (type == "yn"):
            arg ="-Pn -p -st -sU"+str(port[i]).translate(None, '\'][ ') + " " + intensity + "--open"
        arg += " -e " + iface
        for h in hostlist:
            nm.scan(hosts=h, arguments=arg)
            for host in nm.all_hosts():
                    writeFile = path_file
                    with open(writeFile, 'a') as hosts:
                        print ("----------------------------------------------------")
                        hosts.write('%s\n' % host)
                        print bcolors.OKGREEN + "*** " + name + " Found : %s via port " % host + str(port) + " ***" + bcolors.ENDC
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

        #port_obj_reader reads portlist_config file and creates a list with port_objects for scalability.
        #port list input filename is as below.
        ports_list=port_obj_reader("portlist_config")
        for i in ports_list:
            temp=[]
            count=0
            for key, value in vars(i).iteritems():
                temp.append(value)
                count=count+1
            scanner(str(temp[0]),str(temp[2]),str(temp[5]).split('.'),str(temp[4]),str(temp[3]),CIDR,intensity,str(temp[1]),hostlist,iface=iface)
        return "Completed Port Scanning\n"