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

import os, os.path, sys, socket
import subprocess
import nmap
from prettytable import PrettyTable
from src.utils.console_colors import *
from dns import resolver
from dns import reversename

class Hostname:
    def __init__(self):
        self.ips_gathered = []
        self.hostnames_gathered = []
        self.domains_gathered = []
        self.os_gathered = []
        self.hostnames = []
        self.live_ips = []

    def getLiveIPS(self):
        return self.live_ips
    
    def getIPsGathered(self):
        return self.ips_gathered

    def getHostnamesGathered(self):
        return self.hostnames_gathered

    def getDomainsGathered(self):
        return self.domains_gathered

    def getOSGathered(self):
        return self.os_gathered

    def gethostnames(self):
        return self.hostnames

    def findHostnames(self, int_ip, CIDR):

        print(bcolors.OKGREEN + "      [ HOSTNAMES ENUMERATION MODULE ]\n" + bcolors.ENDC)
        hostname = socket.gethostname()

        res_table = PrettyTable([bcolors.OKGREEN + '[IP]' + bcolors.ENDC, bcolors.OKGREEN + '[Hostname]' + bcolors.ENDC,
                                 bcolors.OKGREEN + '[Domain]' + bcolors.ENDC,
                                 bcolors.OKGREEN + '[Operating System]' + bcolors.ENDC], border=False, header=True)
        res_table.align = "l"
        print("Searching for hostnames in %s...\n" % CIDR)
        print("Current Hostname:" + bcolors.TITLE + " %s" % hostname + bcolors.ENDC)
        print(" ")
        
        try:
            subprocess.call('cme -t 50 --timeout 2 smb %s  > Results/hostnames' % CIDR, shell=True)
            #Discover live hosts
            nm=nmap.PortScanner()
            nm_arp=nm.scan(hosts=CIDR,arguments="-sn")
            for x in nm_arp.items()[1][1]:
                self.live_ips.append(x)
            
            self.live_ips.remove(int_ip)

            subprocess.call("strings Results/hostnames | grep '445' | awk '{print $2}' > Results/ips_gathered",shell=True)
            subprocess.call("strings Results/hostnames | grep '445' | awk '{print $4}' > Results/hostnames_gathered",shell=True)
            subprocess.call('strings Results/hostnames | grep ":" | cut -d ":" -f 3 | cut -d ")" -f 1 > Results/domains_gathered', shell=True)
            subprocess.call('strings Results/hostnames | grep ":" | cut -d "(" -f 1  > Results/operating_systems', shell=True)

            ips_gathered=[]
	    hostnames_gathered=[]
            domains_gathered=[]
            os_gathered=[]
   
	 # Read files into the lists
            with open("Results/ips_gathered", "r") as ips:
                ips_gathered = ips.readlines()
            with open("Results/hostnames_gathered", "r") as hostnames:
                hostnames_gathered = hostnames.readlines()
            with open("Results/domains_gathered", "r") as domains:
                domains_gathered = domains.readlines()
            with open("Results/operating_systems", "r") as oper:
                os_gathered = oper.readlines()

            subprocess.call("rm Results/ips_gathered", shell=True)
            subprocess.call("rm Results/hostnames_gathered", shell=True)
            subprocess.call("rm Results/domains_gathered", shell=True)
            subprocess.call("rm Results/operating_systems", shell=True)
  	    subprocess.call("rm Results/hostnames", shell=True)  

            # Get the array length for the loop
            length = len(ips_gathered)
	    
    	    for i in range(0, length):
        		self.ips_gathered.append(ips_gathered[i].strip())
        		self.hostnames_gathered.append(hostnames_gathered[i].strip())
        		self.domains_gathered.append(domains_gathered[i].strip())
                	os=os_gathered[i].replace("[0m"," ")
                	self.os_gathered.append(os.strip())
        	
            # Write the results on stdout and DB
            for i in range(0, length):
                if self.ips_gathered[i].strip() != int_ip.strip():
                    res_table.add_row([self.ips_gathered[i].strip(), self.hostnames_gathered[i].strip(),
                                       self.domains_gathered[i].strip(), self.os_gathered[i].strip()])
            print(res_table)
        except:
            print(bcolors.FAIL + "No Hostnames Found\n" + bcolors.ENDC)
        length = len(self.live_ips)
        if length != 0:
            print(bcolors.OKGREEN + "\n      [  SCOPE DEFINITION MODULE ]\n" + bcolors.ENDC)
            for ip in self.live_ips:
                if ip.strip() != int_ip.strip():
                    print(bcolors.TITLE + "[+] " + bcolors.ENDC + "%s " % ip.strip() + "added to scope!")
        else:
            print(
                    bcolors.WARNING + "NO LIVE IPS FOUND! THERE IS NO NEED TO CONTINUE! WARBERRY WILL NOW EXIT!" + bcolors.ENDC)
            sys.exit(1)
