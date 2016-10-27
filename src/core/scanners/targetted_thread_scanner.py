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
import nmap 
import threading 
import time
from src.core.scanners.port_list import *
from src.utils.console_colors import *

class ScanThread(threading.Thread):
    def __init__(self,name, path_file,port, message, file,CIDR, intensity, type,hostlist,iface):
        threading.Thread.__init__(self)
        self.name = name
        self.path_file = path_file
        self.port=port
        self.message=message
        self.result_file=file
        self.CIDR=CIDR
        self.intensity=intensity
        self.output=""
        self.type=type
        self.hostlist=hostlist
        self.iface=iface

    def run(self):
        file=self.path_file
        if os.path.isfile(file):
            self.output=self.output + bcolors.WARNING + "[!] " + bcolors.ENDC + self.name + " Results File Exists. New results will be appended\n"
        scan_targetted(self)
        return self.output

def scan_targetted(self):
    self.output=self.output+ "[+] Scanning for "+ self.name + " ..."
    scanning(self)
    if (os.path.isfile(self.path_file)):
        self.output = self.output + bcolors.TITLE + "\n[+] Done! Results saved in /Results/"+self.result_file+"\n" + bcolors.ENDC


def scanning(self):
    nm=nmap.PortScanner()
    if (self.type=="y"):
        arg="-Pn -sU -p"+self.port + " " + self.intensity + " --open"
    elif(self.type=="n"):
        arg="-Pn -p"+self.port + " " + self.intensity + " --open"
    elif(self.type=="yn"):
        arg ="-Pn -p -sT -sU" + self.port + " " + self.intensity + " --open"
    #nm.scan(hosts=h, arguments=arg)
    arg += " -e " + self.iface
    for h in self.hostlist:
        nm.scan(hosts=h, arguments=arg)
        for host in nm.all_hosts():
            writeFile = self.path_file
            with open(writeFile, 'a') as hosts:
                self.output = self.output + "\n----------------------------------------------------\n"
                hosts.write('%s\n' % host)
                self.output = self.output + bcolors.OKGREEN + "*** " + self.name + " Found : %s via port " % host + self.port + " ***" + bcolors.ENDC
                self.output = self.output + "\n" + bcolors.TITLE + self.message + bcolors.ENDC


def thread_port_scanner(CIDR, intensity, iface):
    
    print " "
    print bcolors.OKGREEN + " [ TARGETTED SERVICES NETWORK SCANNER MODULE ]\n" + bcolors.ENDC
    print "\n[*] Beginning Scanning Live IPs in Subnet %s with %s intensity." %(CIDR, intensity)
    print " "
    threads=[]
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
        t = ScanThread(name[i],path_file[i],port[i],message[i], result_file[i],CIDR,intensity, scan_type[i],hostlist, iface=iface)
        t.start()
        threads.append(t)

    for t in threads:
        t.join()
        print t.output

