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


#!/usr/bin/python
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
logging.info("finished")
logging.captureWarnings(True)
#Suppress Scapy IPv6 Warnings
import requests.packages.urllib3
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()


from optparse import OptionParser
import subprocess
import os, os.path
import sys, getopt
import socket
import fcntl
import struct
import urllib,urllib2
import re
import httplib
from scapy.all import *
import nmap
from socket import inet_aton
import socket
import json
from urllib import urlopen
import ftplib
import time
from netaddr import *
#External modules
from src.utils.info_banners import *
from src.core.scanners.targetted_scanner import *
from src.core.scanners.targetted_thread_scanner import *
from src.core.scanners.top_port_scanner import *
from src.core.scanners.full_port_scanner import *
from src.core.enumeration.services_enum import *
from src.core.enumeration.nameservers import *
from src.core.bypass import *
from src.core.scanners.full_thread_scanner import *
from src.core.enumeration.bluetooth_enum import *
from src.core.enumeration.ip_enum import *
from src.core.enumeration.network_packets import *
from src.core.enumeration.os_enum import *
from src.core.enumeration.services_enum import *
from src.core.enumeration.wifi_enum import *
from src.core.exploits.responder_poison import *
from src.utils.info_banners import *
from src.utils.console_colors import *
from src.utils import *


def main():

    version = bcolors.TITLE + ( '''
 _    _  ___  ____________ ___________________   __
| |  | |/ _ \ | ___ \ ___ \  ___| ___ \ ___ \ \ / /
| |  | / /_\ \| |_/ / |_/ / |__ | |_/ / |_/ /\ V /
| |/\| |  _  ||    /| ___ \  __||    /|    /  \ /
\  /\  / | | || |\ \| |_/ / |___| |\ \| |\ \  | |
 \/  \/\_| |_/\_| \_\____/\____/\_| \_\_| \_| \_/

            TACTICAL EXPLOITATION

v4.0                              @sec_groundzero
                          secgroundzero@gmail.com
''') + bcolors.ENDC


    parser = OptionParser(usage= "usage: sudo %prog [options]",version=version)
    parser.add_option("-a", "--attack", action="store", dest="attacktype", default="-A", help="Attack Mode."+ bcolors.WARNING + " Default: --attack" + bcolors.ENDC,choices=['-A','--attack','-T','--toptcp', '-B','--topudp', '-F', '--fulltcp'])
    parser.add_option("-p", "--packets", action="store", dest="packets", default=20, type=int, help="Number of Network Packets to capture")
    parser.add_option("-I", "--interface", action="store", dest="iface", default="eth0",help="Network Interface to use." + bcolors.WARNING + " Default: eth0" + bcolors.ENDC, choices=['eth0', 'eth1', 'wlan0', 'wlan1', 'wlan2', 'at0'])
    parser.add_option("-N", "--name", action="store", dest="name", default="WarBerry",help="Hostname to use." + bcolors.WARNING + " Default: Auto" + bcolors.ENDC)
    parser.add_option("-i", "--intensity", action="store", dest="intensity", default="-T1", help="Port scan intensity." + bcolors.WARNING + " Default: T1" + bcolors.ENDC,choices=['-T1', '-T2', '-T3', '-T4'])
    parser.add_option("-P", "--poison", action="store_false",dest="poison",default=True, help="Turn Poisoning off."+ bcolors.WARNING + " Default: On" + bcolors.ENDC)
    parser.add_option("-Q", "--quick", action="store_true", dest="fast", default=False, help="Scan using threads." + bcolors.WARNING + " Default: Off" + bcolors.ENDC)
    parser.add_option("-H", "--hostname", action="store_false", dest="hostname", default= True, help="Do not change WarBerry hostname" + bcolors.WARNING + " Default: Off" + bcolors.ENDC)
    parser.add_option("-e", "--enumeration", action="store_true",dest="enum", default=False, help="Disable enumeration mode." + bcolors.WARNING + " Default: Off" + bcolors.ENDC)
    parser.add_option("-M", "--malicious", action="store_true", dest="malicious", default=False, help="Enable Malicious only mode" + bcolors.WARNING + " Default: Off" + bcolors.ENDC)
    parser.add_option("-B", "--bluetooth", action="store_true", dest="btooth", default=False, help="Enable Bluetooth Scanning" + bcolors.WARNING + " Default: Off" + bcolors.ENDC)
    parser.add_option("-W", "--wifi", action="store_true", dest="wifi", default=False, help="Enable WiFi Scanning" + bcolors.WARNING + " Default: Off" + bcolors.ENDC)
    parser.add_option("-r", "--recon", action="store_true", dest="reconmode", default=False,help="Enable Recon only mode. " + bcolors.WARNING + " Default: Off" + bcolors.ENDC)
    parser.add_option("-S", "--sniffer", action="store_true", dest="sniffer", default=False,help="Enable Sniffer only mode." + bcolors.WARNING + " Default: Off" + bcolors.ENDC)
    parser.add_option("-C", "--clear", action="store_true", dest="clear", default=False, help="Clear previous output folders in ../Results")
    parser.add_option("-m", "--man", action="store_true", dest="manpage", default=False, help="Print WarBerry man pages")


    (options, args) = parser.parse_args()
    #set globals from options
    packets = options.packets
    iface = options.iface
    host_name = options.name
    attacktype=options.attacktype
    intensity=options.intensity

    def statusWrite(message):
        """Write a status message"""
        with open('../Results/running_status', 'a') as status:
            status.write(message)
    def setupAttack():
        """Sets Up Attack"""
        subprocess.call('clear',shell=True)
        banner()
        int_ip=iprecon(iface)
        if (int_ip == None)
            exit
        netmask = netmask_recon(iface)
        statusWrite("Completed IP Recon\n")
        CIDR = subnet(int_ip,netmask)
    #clear previous output folders                
    if options.clear == True:
        clear_output()
    #display man page
    if options.manpage == True:
        subprocess.call('clear', shell=True)
        banner_full_help()
    #hostname operations
    if host_name != "WarBerry":
        manual_namechange(host_name)
    if options.hostname == True and host_name == "WarBerry":
        namechange()
    
    #attack
    if attacktype == "-A" or attacktype == '--attack':
        if not os.geteuid() == 0:
            print bcolors.FAIL + '*** You are not running as root and some modules will fail ***\nRun again with sudo.' + bcolors.ENDC
            sys.exit(-1)
        dhcp_check()
        setupAttack()
        if options.malicious == True:
            statusWrite("Entering poisoning mode\n")
            poison(iface)
        else:
            ##external_IP_recon()
            sniffer(iface, packets)
            statusWrite("Completed sniffing network packets\n")
            pcap_parser()
            ##scope_definition(iface, CIDR)
            hostnames(CIDR)
            statusWrite("Completed hostnames search\n")
            nbtscan(CIDR)
            statusWrite("Completed NBTScan\n")
            
            #end recon mode
            if options.reconmode == False:
                if options.fast == False:
                    single_port_scanner(CIDR, intensity)
                else:
                    thread_port_scanner(CIDR, intensity)
                statusWrite("Completed Port Scanning\n")
                if options.enum == False:
                    shares_enum()
                    statusWrite("Completed Enumerating Shares\n")
                    smb_users()
                    statusWrite("Completed Enumerating Users\n")
                    domains_enum()
                    statusWrite("Completed Enumerating Domains\n")
                    webs_prep()
                    http_title_enum()
                    statusWrite("Completed Enumerating HTTP Titles\n")
                    nfs_enum()
                    statusWrite("Completed NFS Enumeration\n")
                    waf_enum()
                    statusWrite("Completed WAF Enumeration\n")
                    mysql_enum()
                    statusWrite("Completed MYSQL Enumeration\n")
                    mssql_enum()
                    statusWrite("Completed MSSQL Enumeration\n")
                    ftp_enum()
                    statusWrite("Completed FTP Enumeration\n")
                    snmp_enum()
                    statusWrite("Completed SNMP Enumeration\n")
                    clamav_enum()
                    statusWrite("Completed ClamAV Enumeration\n")
                    informix_enum()
                    statusWrite("Completed Informix DB Enumeration\n")
                    informix_tables()
                    statusWrite("Completed Informix Tables Enumeration\n")
                    sip_methods_enum()
                    statusWrite("Completed SIP Methods Enumeration\n")
                    sip_users_enum()
                    statusWrite("Completed SIP Users Enumeration\n")
                    os_enum(CIDR)
                    statusWrite("Completed OS Enumeration\n")
                if options.btooth == True:
                    bluetooth_enum()
                    statusWrite("Completed bluetooth scan\n")
                if options.wifi == True:
                    wifi_enum()
                    statusWrite("Completed wifi networks scan\n")
                print ""
            print bcolors.TITLE + "All scripts completed. Check the /Results directory" + bcolors.ENDC
            print " "
            if options.poison == True:
                statusWrite("Entering poisoning mode\n")
                    poison(iface)

    elif attacktype == '-T' or attacktype == '--toptcp':
        setupAttack()
        external_IP_recon()
        ##scope_definition(iface, CIDR)
        top_ports_scanner(CIDR, intensity)
        print bcolors.TITLE + "All scripts completed. Check the /Results directory" + bcolors.ENDC

    elif attacktype == '-B' or attacktype == '--tcpudp':
        setupAttack()
        external_IP_recon()
        ##scope_definition(iface, CIDR)
        if options.fast == True:
            tcpudp_thread_scanner(CIDR,intensity)
        else:
            tcpudp_scanner(CIDR,intensity)
        print bcolors.TITLE + "All scripts completed. Check the /Results directory" + bcolors.ENDC
    
    elif attacktype == '-F' or attacktype == '--fulltcp':
        setupAttack()
        external_IP_recon()
        ##scope_definition(iface, CIDR)
        if options.fast == True:
            full_thread_scanner(CIDR,intensity)
        else:
            full_scanner(CIDR,intensity)
        print bcolors.TITLE + "All scripts completed. Check the /Results directory" + bcolors.ENDC
    
    elif attacktype == '-S' or attacktype == '--sniffer':
        subprocess.call('clear', shell=True)
        sniffer(iface, packets)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        subprocess.call("sudo mkdir ../Results/Responder_logs", shell=True)
        subprocess.call("sudo mv ../Tools/Responder/logs/* ../Results/Responder_logs/",shell=True)
        subprocess.call('clear', shell=True)
        banner_full()
