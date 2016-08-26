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
import threading
import subprocess
from src.utils.console_colors import *

class FullScanThread(threading.Thread):
    def __init__(self, ports, CIDR, index,pos,intensity,hostlist,iface):
        threading.Thread.__init__(self)
        self.ports = ports
        self.CIDR=CIDR
        self.index=index+1
        self.output=""
        self.resultPorts=[None]*1000
        self.pos=pos
        self.intensity=intensity
        self.hostlist=hostlist
        self.iface=iface

    def run(self):
        fullPorts_Scanning(self)
        for i in range(len(self.resultPorts)):
            if (len(self.resultPorts[i])!= 0):
                port = self.pos + i + 1
                print "TCP port: %d" % port
                print('----------------------------------------------------')
                for x in range(len(self.resultPorts[i])):
                    print bcolors.OKGREEN + ' [+] ' + bcolors.ENDC + '%s' %self.resultPorts[i][x]
                print "\n"


def fullPorts_Scanning(self):

    for i in range(len(self.resultPorts)):
        self.resultPorts[i]=[]


    nm = nmap.PortScanner()
    arg = "-Pn " + self.intensity + " -sT - sU -p%s" % self.ports + " --open -o ../Results/tcp_udp_scan%s" % self.index + " -e " + self.iface
    for h in self.hostlist:
        nm.scan(hosts=h, arguments=arg)
        for host in nm.all_hosts():
            hostname=host+nm[host].hostname()
            for proto in nm[host].all_protocols():
                lport = nm[host][proto].keys()
                lport.sort()
            for port in lport:
                pos=int(port)-self.pos-1
                self.resultPorts[pos].append(hostname)


class TCPFullThread(threading.Thread):
    def __init__(self, ports, CIDR, index,pos,intensity,hostlist,iface):
        threading.Thread.__init__(self)
        self.ports = ports
        self.CIDR=CIDR
        self.index=index+1
        self.output=""
        self.resultPorts=[None]*1000
        self.pos=pos
        self.intensity=intensity
        self.hostlist=hostlist
        self.iface=iface

    def run(self):
        TCPFull_scanning(self)
        for i in range(len(self.resultPorts)):
            if (len(self.resultPorts[i])!= 0):
                port = self.pos + i + 1
                print "TCP port: %d" % port
                print('----------------------------------------------------')
                for x in range(len(self.resultPorts[i])):
                    print bcolors.OKGREEN + ' [+] ' + bcolors.ENDC + '%s' %self.resultPorts[i][x]
                print "\n"

def TCPFull_scanning(self):

    for i in range(len(self.resultPorts)):
        self.resultPorts[i]=[]


    nm = nmap.PortScanner()
    arg = "-Pn " + self.intensity + " -p%s" % self.ports + " --open -o ../Results/tcp_full%s" % self.index + " -e " + self.iface
    for h in self.hostlist:
        nm.scan(hosts=h, arguments=arg)
        for host in nm.all_hosts():
            hostname=host+nm[host].hostname()
            for proto in nm[host].all_protocols():
                lport = nm[host][proto].keys()
                lport.sort()
            for port in lport:
                pos=int(port)-self.pos-1
                self.resultPorts[pos].append(hostname)


def full_thread_scanner(CIDR,intensity, iface):

    print bcolors.OKGREEN + "      [ FULL TCP NETWORK SCANNER MODULE ]\n" + bcolors.ENDC

    if os.path.isfile('../Results/tcp_full'):
        print bcolors.WARNING + "[!] Full TCP Results File Exists. Previous Results will be Overwritten" + bcolors.ENDC

    print "Beginning Scanning Subnet %s" % CIDR +"\n"
    threads = []
    ports = ['1-1000', '1001-2000','2001-3000','3001-4000','4001-5000','5001-6000','6001-7000','7001-8000','8001-9000','9001-10000','10001-11000','11001-12000','12001-13000','13001-14000','14001-15000', '15001-16000','16001-17000','17001-18000','18001-19000','19001-20000', '20001-21000', '21001-22000', '22001-23000', '23001-24000','24001-25000','25001-26000','26001-27000','27001-28000','28001-29000','29001-30000', '30001-31000','31001-32000','32001-33000','330001-34000','34001-35000', '35001-36000', '36001-37000','37001-38000','38001-39000','39001-40000','40001-41000','41001-42000','42001-43000','43001-44000','44001-45000','45001-46000','46001-47000','47001-48000', '48001-49000', '49001-50000','50001-51000','51001-52000','52001-53000','53001-54000', '54001-55000','55001-56000','56001-57000','57001-58000','58001-59000','60001-61000', '61001-62000','62001-63000','63001-64000','64001-65000', '65001-65535']
    pos = [0, 1000, 2000,3000, 4000,5000,6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000, 16000, 17000, 18000, 19000, 20000, 21000, 22000, 23000, 24000, 25000, 26000, 27000, 28000, 29000, 30000,31000, 32000, 33000, 34000, 35000, 36000, 37000, 38000, 39000, 40000,41000, 42000, 43000, 44000, 45000, 46000, 47000, 48000, 49000, 50000,51000, 52000, 53000, 54000, 55000, 56000, 57000,58000, 59000, 60000, 61000, 62000, 63000, 64000, 65000, 65000]

    print "[+] Scanning All TCP Ports in all hosts with %s intensity..." %intensity+"\n"

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

    for i in range(len(ports)):
        t = TCPFullThread(ports[i],CIDR,i,pos[i],intensity,hostlist, iface=iface)
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    with open('../Results/tcp_full', 'w') as full_tcp:
        for i in range(len(ports)):
            index=i+1
            file="../Results/tcp_full%d" %index
            with open(file, 'r') as tcp:
                    h=tcp.readlines();
                    for x in h:
                        full_tcp.write(x)
            subprocess.call("sudo rm -rf %s" % file, shell=True)



def tcpudp_thread_scanner(CIDR,intensity, iface):

    print bcolors.OKGREEN + "      [ TCP/UDP NETWORK SCANNER MODULE ]\n" + bcolors.ENDC

    if os.path.isfile('../Results/tcp_udp_scan'):
        print bcolors.WARNING + "[!] TCP/UDP Results File Exists. Previous Results will be Overwritten " + bcolors.ENDC


    print "Beginning Scanning Subnet %s" % CIDR +"\n"
    threads = []
    ports = ['1-1000', '1001-2000','2001-3000','3001-4000','4001-5000','5001-6000','6001-7000','7001-8000','8001-9000','9001-10000','10001-11000','11001-12000','12001-13000','13001-14000','14001-15000', '15001-16000','16001-17000','17001-18000','18001-19000','19001-20000', '20001-21000', '21001-22000', '22001-23000', '23001-24000','24001-25000','25001-26000','26001-27000','27001-28000','28001-29000','29001-30000', '30001-31000','31001-32000','32001-33000','330001-34000','34001-35000', '35001-36000', '36001-37000','37001-38000','38001-39000','39001-40000','40001-41000','41001-42000','42001-43000','43001-44000','44001-45000','45001-46000','46001-47000','47001-48000', '48001-49000', '49001-50000','50001-51000','51001-52000','52001-53000','53001-54000', '54001-55000','55001-56000','56001-57000','57001-58000','58001-59000','60001-61000', '61001-62000','62001-63000','63001-64000','64001-65000', '65001-65535']
    pos = [0, 1000, 2000,3000, 4000,5000,6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000, 16000, 17000, 18000, 19000, 20000, 21000, 22000, 23000, 24000, 25000, 26000, 27000, 28000, 29000, 30000,31000, 32000, 33000, 34000, 35000, 36000, 37000, 38000, 39000, 40000,41000, 42000, 43000, 44000, 45000, 46000, 47000, 48000, 49000, 50000,51000, 52000, 53000, 54000, 55000, 56000, 57000,58000, 59000, 60000, 61000, 62000, 63000, 64000, 65000, 65000]

    print "[+] Scanning TCP/UDP Ports in all hosts with %s intensity..." %intensity + "\n"

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

    for i in range(len(ports)):
        t = FullScanThread(ports[i],CIDR,i,pos[i],intensity,hostlist, iface=iface)
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    with open('../Results/tcp_udp_scan', 'w') as full_tcp:
        for i in range(len(ports)):
            index=i+1
            file="../Results/tcp_udp_scan%d" %index
            with open(file, 'r') as tcp:
                    h=tcp.readlines();
                    for x in h:
                        full_tcp.write(x)
            subprocess.call("sudo rm -rf %s" % file, shell=True)



