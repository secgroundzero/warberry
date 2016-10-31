#!/usr/bin/python

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
from src.core.enumeration.mailowner import *
from src.core.enumeration.os_enum import *
from src.core.enumeration.services_enum import *
from src.core.enumeration.wifi_enum import *
from src.core.exploits.responder_poison import *
from src.core.enumeration.zones import *
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
    parser.add_option("-p", "--packets", action="store", dest="packets", default=20, type=int, help="# of Network Packets to capture" + bcolors.WARNING + " Default: 20" + bcolors.ENDC)
    parser.add_option("-x", "--expire", action="store", dest="expire", default=20, type=int,help="Time for packet capture to stop" + bcolors.WARNING + " Default: 20s" + bcolors.ENDC)
    parser.add_option("-I", "--interface", action="store", dest="iface", default="eth0",help="Network Interface to use." + bcolors.WARNING + " Default: eth0" + bcolors.ENDC, choices=['eth0', 'eth1', 'wlan0', 'wlan1', 'wlan2', 'at0'])
    parser.add_option("-N", "--name", action="store", dest="name", default="WarBerry",help="Hostname to use." + bcolors.WARNING + " Default: Auto" + bcolors.ENDC)
    parser.add_option("-i", "--intensity", action="store", dest="intensity", default="-T1", help="Port scan intensity." + bcolors.WARNING + " Default: T1" + bcolors.ENDC,choices=['-T1', '-T2', '-T3', '-T4'])
    parser.add_option("-P", "--poison", action="store_false",dest="poison",default=True, help="Turn Poisoning off."+ bcolors.WARNING + " Default: On" + bcolors.ENDC)
    parser.add_option("-t", "--time", action="store", dest="time", default=900, type=int, help="Responder Timeout Seconds")
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



    if options.clear == True:
        clear_output()
    elif options.manpage == True:
        subprocess.call('clear', shell=True)
        banner_full_help()
    elif options.attacktype == "-A" or options.attacktype == '--attack':
        subprocess.call('clear', shell=True)
        banner()
        if not os.geteuid() == 0:
            print bcolors.FAIL + '*** You are not running as root and some modules will fail ***\nRun again with sudo.' + bcolors.ENDC
            sys.exit(-1)
        dhcp_check()
        if (os.path.isfile('/sys/class/net/' + options.iface + '/carrier') == True):
            iface = options.iface
        else:
            for ifaces in os.listdir("/sys/class/net/"):
                if ifaces[0] == "e":
                    file_iface = open("/sys/class/net/" + ifaces + "/carrier")
                    if file_iface.readline()[0] == "1":
                        iface = ifaces
        host_name = options.name
        int_ip = iprecon(iface)
        if (int_ip == None):
            exit
        else:
            if options.malicious == True:
                netmask = netmask_recon(iface)
                with open('../Results/running_status', 'a') as status:
                    status.write("Entering poisoning mode\n")
                    poison_time = options.time
                    poison(iface, poison_time)
            else:
                netmask = netmask_recon(iface)
                CIDR = subnet(int_ip, netmask)
                scope_definition(iface, CIDR)
                with open('../Results/running_status', 'a') as status:
                    status.write("Completed IP Recon\n")
                packets = options.packets
                expire = options.expire
                sniffer(iface, packets, expire)
                with open('../Results/running_status', 'a') as status:
                    status.write("Completed sniffing network packets\n")
                mail_creds(iface, expire)
                with open('../Results/running_status', 'a') as status:
                    status.write("Completed sniffing mail info from packets\n")
                pcap_parser()
                hostnames(CIDR)
                with open('../Results/running_status', 'a') as status:
                    status.write("Completed hostnames search\n")
                nbtscan(CIDR)
                with open('../Results/running_status', 'a') as status:
                    status.write("Completed NBTScan\n")
                if host_name != "WarBerry":
                    manual_namechange(host_name)
                if options.hostname == True and host_name == "WarBerry":
                    namechange()
                if options.reconmode == False:
                    intensity = options.intensity
                    if options.fast == False:
                        single_port_scanner(CIDR, intensity, iface)
                    else:
                        thread_port_scanner(CIDR, intensity, iface)
                    with open('../Results/running_status', 'a') as status:
                        status.write("Completed Port Scanning\n")
                    if options.enum == False:
                        shares_enum(iface)
                        with open('../Results/running_status', 'a') as status:
                            status.write("Completed Enumerating Shares\n")
                        smb_users(iface)
                        with open('../Results/running_status', 'a') as status:
                            status.write("Completed Enumerating Users\n")
                        webs_prep()
                        http_title_enum(iface)
                        with open('../Results/running_status', 'a') as status:
                            status.write("Completed Enumerating HTTP Titles\n")
                        nfs_enum(iface)
                        with open('../Results/running_status', 'a') as status:
                            status.write("Completed NFS Enumeration\n")
                        waf_enum(iface)
                        with open('../Results/running_status', 'a') as status:
                            status.write("Completed Robots.txt Enumeration\n")
                        robots_txt()
                        with open('../Results/running_status', 'a') as status:
                            status.write("Completed WAF Enumeration\n")
                        mysql_enum(iface)
                        with open('../Results/running_status', 'a') as status:
                                status.write("Completed MYSQL Enumeration\n")
                        mssql_enum(iface)
                        with open('../Results/running_status', 'a') as status:
                            status.write("Completed MSSQL Enumeration\n")
                        ftp_enum(iface)
                        with open('../Results/running_status', 'a') as status:
                            status.write("Completed FTP Enumeration\n")
                        snmp_enum(iface)
                        with open('../Results/running_status', 'a') as status:
                            status.write("Completed SNMP Enumeration\n")
                        clamav_enum(iface)
                        with open('../Results/running_status', 'a') as status:
                            status.write("Completed ClamAV Enumeration\n")
                        informix_enum(iface)
                        with open('../Results/running_status', 'a') as status:
                            status.write("Completed Informix DB Enumeration\n")
                        informix_tables(iface)
                        with open('../Results/running_status', 'a') as status:
                            status.write("Completed Informix Tables Enumeration\n")
                        sip_methods_enum(iface)
                        with open('../Results/running_status', 'a') as status:
                            status.write("Completed SIP Methods Enumeration\n")
                        sip_users_enum(iface)
                        with open('../Results/running_status', 'a') as status:
                            status.write("Completed SIP Users Enumeration\n")
                        aggressive_vpn()
                        with open('../Results/running_status', 'a') as status:
                            status.write("Completed Aggressive VPN Enumeration\n")
                        os_enum(CIDR,iface)
                        with open('../Results/running_status', 'a') as status:
                            status.write("Completed OS Enumeration\n")
                        #enum4linux()
                        #with open('../Results/running_status', 'a') as status:
                        #    status.write("Completed enum4linux Enumeration\n")
                        zone_transfers(CIDR,iface)
                        with open('../Results/running_status', 'a') as status:
                            status.write("Completed zones Enumeration\n")
                    if options.btooth == True:
                        bluetooth_enum()
                        with open('../Results/running_status', 'a') as status:
                            status.write("Completed bluetooth scan\n")
                    if options.wifi == True:
                        wifi_enum()
                        with open('../Results/running_status', 'a') as status:
                            status.write("Completed wifi networks scan\n")
                    print ""
                print bcolors.TITLE + "All scripts completed. Check the /Results directory" + bcolors.ENDC
                print " "
                if options.poison == True:
                    with open('../Results/running_status', 'a') as status:
                        status.write("Entering poisoning mode\n")
                        poison_time = options.time
                        poison(iface, poison_time)

    elif options.attacktype == '-T' or options.attacktype == '--toptcp':
        subprocess.call('clear', shell=True)
        banner()
        iface = options.iface
        int_ip = iprecon(iface)
        if (int_ip == None):
            exit
        netmask = netmask_recon(iface)
        external_IP_recon()
        CIDR = subnet(int_ip, netmask)
        #scope_definition(iface, CIDR)
        top_ports_scanner(CIDR, options.intensity, iface)
        print bcolors.TITLE + "All scripts completed. Check the /Results directory" + bcolors.ENDC

    elif options.attacktype == '-B' or options.attacktype == '--tcpudp':
        subprocess.call('clear', shell=True)
        banner()
        iface = options.iface
        int_ip = iprecon(iface)
        if (int_ip == None):
            exit
        netmask = netmask_recon(iface)
        external_IP_recon()
        CIDR = subnet(int_ip, netmask)
        #scope_definition(iface, CIDR)
        if options.fast == True:
            tcpudp_thread_scanner(CIDR,options.intensity, iface)
        else:
            tcpudp_scanner(CIDR, options.intensity,iface)
        print bcolors.TITLE + "All scripts completed. Check the /Results directory" + bcolors.ENDC
    elif options.attacktype == '-F' or options.attacktype == '--fulltcp':
        subprocess.call('clear', shell=True)
        banner()
        iface = options.iface
        int_ip = iprecon(iface)
        netmask = netmask_recon(iface)
        external_IP_recon()
        CIDR = subnet(int_ip, netmask)
        #scope_definition(iface, CIDR)
        if options.fast == True:
            full_thread_scanner(CIDR,options.intensity, iface)
        else:
            full_scanner(CIDR, options.intensity, iface)
        print bcolors.TITLE + "All scripts completed. Check the /Results directory" + bcolors.ENDC
    elif options.attacktype == '-S' or options.attacktype == '--sniffer':
        iface = options.iface
        packets = options.packets
        subprocess.call('clear', shell=True)
        sniffer(iface, packets)


if __name__ == '__main__':

    try:
        main()
    except KeyboardInterrupt:
        try:
            if os.path.exists("../Results") == False:
                subprocess.call("sudo mkdir ../Results", shell = True)
                subprocess.call("sudo mkdir  ../Results/Responder_logs", shell=True)
                subprocess.call("sudo mv  ../Tools/Responder/logs/* ../Results/Responder_logs/", shell=True)
        finally:
            subprocess.call("clear", shell=True)
            banner_full()


