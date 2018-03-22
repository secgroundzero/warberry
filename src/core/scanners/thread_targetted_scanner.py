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

import os, os.path
import nmap
import threading
from src.utils.console_colors import *
from src.utils.port_obj_Read import port_obj_reader
from src.warberrySetup.WarberryDB import *


class ScanThread(threading.Thread):

    #CONSTRUCTOR
    def __init__(self, name,  port, message, CIDR, intensity, type, hostlist, iface, session):
        threading.Thread.__init__(self)
        self.name = name
        self.port=port
        self.message=message
        self.CIDR=CIDR
        self.intensity=intensity
        self.output=""
        self.hosts=[]
        self.type=type
        self.hostlist=hostlist
        self.iface=iface
        self.session=session
	self.lock=threading.Lock()

    def run(self):
        self.scan_targetted()

    def scan_targetted(self):
        self.output = self.output+ bcolors.TITLE + "[+] " + bcolors.ENDC + "Scanning for " + self.name + " ..."
        self.scanning()

    def scanning(self):
        nm = nmap.PortScanner()
        if (self.type == "y"):
            arg = "-Pn -sU -p" + str(self.port) + " " + self.intensity + " --open"
        elif (self.type == "n"):
            arg = "-Pn -p" + str(self.port) + " " + self.intensity + " --open"
        elif (self.type == "yn"):
            arg = "-Pn -p -sS -sU" + str(self.port) + " " + self.intensity + " --open"
        arg += " -e " + self.iface
        for h in self.hostlist:
            nm.scan(hosts=h, arguments=arg)
            for host in nm.all_hosts():
                self.output += "\n----------------------------------------------------\n"
                self.hosts.append(host)
                #x=WarberryDB()
		#self.lock.acquire()
                #x.insertScannerQ(self.session,self.name,host)
		#self.lock.release()
                self.output = self.output + bcolors.OKGREEN + "*** " + self.name + " Found : %s via port " % host + self.port + " ***" + bcolors.ENDC
                self.output = self.output + "\n" + bcolors.TITLE + self.message + "\n"+ bcolors.ENDC
                #self.output = self.output + bcolors.TITLE + "\n[+] Done! Results saved in warberry.db"  "\n" + bcolors.ENDC

class ThreadPortScanner:

    def __init__(self):
        self.scanners = {}

    def thread_port_scanner(self, CIDR, intensity, iface,hostlist,session):
        print(" ")
        print(bcolors.OKGREEN + " [ TARGETTED SERVICES NETWORK SCANNER MODULE ]\n" + bcolors.ENDC)
        print(bcolors.TITLE + "[*] Beginning Scan of live IPs in scope in subnet %s with %s intensity." % (CIDR, intensity) + bcolors.ENDC)
        print(" ")
        threads = []
        ports_list = port_obj_reader("portlist_config")
        for i in ports_list:
            temp = []
            count = 0
            for key, value in vars(i).iteritems():
                temp.append(value)
                count += 1
            for i in range(0, len(temp[5])):
                t = ScanThread(str(temp[0]), str(temp[5][i]), str(temp[4]), CIDR, intensity,str(temp[1]),hostlist, iface, session)
            t.start()
            threads.append(t)

        for t in threads:
            t.join()
            self.scanners[t.name] = t.hosts
	    x=WarberryDB()
	    for i in t.hosts:
            	x.insertScannerQ(session,t.name,i)
            print(t.output)

