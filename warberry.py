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
sys.path.append('./resources/')
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
from bluetooth import *
#External modules
from info_banners import *
from network_scanners import *
from services_enum import *
from rest_bypass import *
from console_colors import bcolors
from network_thread_scanner import *


def main():

    version = bcolors.TITLE + ( '''
 _    _  ___  ____________ ___________________   __
| |  | |/ _ \ | ___ \ ___ \  ___| ___ \ ___ \ \ / /
| |  | / /_\ \| |_/ / |_/ / |__ | |_/ / |_/ /\ V /
| |/\| |  _  ||    /| ___ \  __||    /|    /  \ /
\  /\  / | | || |\ \| |_/ / |___| |\ \| |\ \  | |
 \/  \/\_| |_/\_| \_\____/\____/\_| \_\_| \_| \_/

            TACTICAL EXPLOITATION

v2.0                              @sec_groundzero
''') + bcolors.ENDC


    parser = OptionParser(usage= "usage: sudo %prog [options]",version=version)
    parser.add_option("-a", "--attack", action="store", dest="attacktype", default="-A", help="Attack Mode."+ bcolors.WARNING + " Default: --attack" + bcolors.ENDC)
    parser.add_option("-p", "--packets", action="store", dest="packets", default=20, type=int, help="Number of Network Packets to capture")
    parser.add_option("-i", "--interface", action="store", dest="iface", default="eth0",help="Network Interface to use." + bcolors.WARNING + " Default: eth0" + bcolors.ENDC, choices=['eth0', 'eth1', 'wlan0', 'wlan1', 'wlan2', 'at0'])
    parser.add_option("-P", "--poison", action="store_false",dest="poison",default=True, help="Turn Poisoning on/off."+ bcolors.WARNING + " Default: On" + bcolors.ENDC)
    parser.add_option("-H", "--hostname", action="store_false", dest="hostname", default= True, help="Change WarBerry hostname" + bcolors.WARNING + " Default: On" + bcolors.ENDC)
    parser.add_option("-e", "--enumeration", action="store_true",dest="enum", default=False, help="Turn enumeration mode on/off." + bcolors.WARNING + " Default: On" + bcolors.ENDC)
    parser.add_option("-r", "--recon", action="store_true", dest="reconmode", default=False,help="Recon only mode. No port scans")
    parser.add_option("-S", "--sniffer", action="store_true", dest="sniffer", default=False,help="Sniffer only mode.")
    parser.add_option("-C", "--clear", action="store_true", dest="clear", default=False, help="Clear previous output folders in ../Results")
    parser.add_option("-m", "--man", action="store_true", dest="manpage", default=False, help="Print WarBerry man pages")


    (options, args) = parser.parse_args()



    if options.clear == True:
        clear_output()
    elif options.manpage == True:
        subprocess.call('clear', shell=True)
        banner_full_help()
    elif options.attacktype == '-A' or options.attacktype == '--attack':
        subprocess.call('clear', shell=True)
        banner()
        if not os.geteuid() == 0:
            print bcolors.FAIL + '*** You are not running as root and some modules will fail ***\nRun again with sudo.' + bcolors.ENDC
            sys.exit(-1)
        dhcp_check()
        iface = options.iface
        int_ip = iprecon(iface)
        if (int_ip == None):
            exit
        else:
            netmask = netmask_recon(iface)
            external_IP_recon()
            with open('../Results/running_status', 'a') as status:
                status.write("Completed IP Recon\n")
            packets = options.packets
            sniffer(iface, packets)
            with open('../Results/running_status', 'a') as status:
                status.write("Completed sniffing network packets\n")
            pcap_parser()
            CIDR = subnet(int_ip, netmask)
            hostnames(CIDR)
            with open('../Results/running_status', 'a') as status:
                status.write("Completed hostnames search\n")
            nbtscan(CIDR)
            with open('../Results/running_status', 'a') as status:
                status.write("Completed NBTScan\n")
            if options.hostname == True:
                namechange()
            if options.reconmode == False:
                scanner_thread(CIDR)
                with open('../Results/running_status', 'a') as status:
                    status.write("Completed targeted scanning\n")
                if options.enum == False:
                    shares_enum()
                    with open('../Results/running_status', 'a') as status:
                        status.write("Completed enumerating shares\n")
                    smb_users()
                    with open('../Results/running_status', 'a') as status:
                        status.write("Completed enumerating users\n")
                    webs_prep()
                    http_title_enum()
                    with open('../Results/running_status', 'a') as status:
                        status.write("Completed enumerating HTTP Titles\n")
                    nfs_enum()
                    with open('../Results/running_status', 'a') as status:
                        status.write("Completed NFS Enumeration\n")
                    waf_enum()
                    with open('../Results/running_status', 'a') as status:
                        status.write("Completed WAF Enumeration\n")
                    mysql_enum()
                    with open('../Results/running_status', 'a') as status:
                        status.write("Completed MYSQL Enumeration\n")
                    mssql_enum()
                    with open('../Results/running_status', 'a') as status:
                        status.write("Completed MSSQL Enumeration\n")
                    ftp_enum()
                    with open('../Results/running_status', 'a') as status:
                        status.write("Completed FTP Enumeration\n")
                    snmp_enum()
                    with open('../Results/running_status', 'a') as status:
                        status.write("Completed SNMP Enumeration\n")
            bluetooth_scan()
            with open('../Results/running_status', 'a') as status:
                status.write("Completed bluetooth scan\n")
            wifi_scan()
            with open('../Results/running_status', 'a') as status:
                status.write("Completed wifi networks scan\n")
                print ""
            print bcolors.TITLE + "All scripts completed. Check the /Results directory" + bcolors.ENDC
            print " "
            if options.poison == True:
                with open('../Results/running_status', 'a') as status:
                    status.write("Entering poisoning mode\n")
                    poison(iface)

    elif options.attacktype == '-T' or options.attacktype == '--toptcp':
        subprocess.call('clear', shell=True)
        banner()
        iface = options.iface
        int_ip = iprecon(iface)
        if (int_ip == None):
            exit
        netmask = netmask_recon(iface)
        print external_IP_recon()
        CIDR = subnet(int_ip, netmask)
        scanner_top(CIDR)
        print bcolors.TITLE + "All scripts completed. Check the /Results directory" + bcolors.ENDC

    elif options.attacktype == '-B' or options.attacktype == '--tcpudp':
        subprocess.call('clear', shell=True)
        banner()
        iface = options.iface
        int_ip = iprecon(iface)
        if (int_ip == None):
            exit
        netmask = netmask_recon(iface)
        print external_IP_recon()
        CIDR = subnet(int_ip, netmask)
        scanner_full(CIDR)
        print bcolors.TITLE + "All scripts completed. Check the /Results directory" + bcolors.ENDC
    elif options.attacktype == '-F' or options.attacktype == '--fulltcp':
        subprocess.call('clear', shell=True)
        banner()
        iface = options.iface
        int_ip = iprecon(iface)
        netmask = netmask_recon(iface)
        print external_IP_recon()
        CIDR = subnet(int_ip, netmask)
        scanner_tcp_full(CIDR)
        print bcolors.TITLE + "All scripts completed. Check the /Results directory" + bcolors.ENDC
    elif options.attacktype == '-S' or options.attacktype == '--sniffer':
        iface = options.iface
        packets = options.packets
        subprocess.call('clear', shell=True)
        sniffer(iface, packets)


def dhcp_check():

    print bcolors.OKGREEN + "      [ DHCP SERVICE CHECK MODULE ]\n" + bcolors.ENDC

    dhcp_out = subprocess.check_output(['ps', '-A'])
    if "dhcp" in dhcp_out:
        status = bcolors.FAIL + "Running - Not Stealth" + bcolors.ENDC
        print "DHCP Service Status... %s\n" % status
    else:
        status = bcolors.OKGREEN + "Not Running - Stealth" + bcolors.ENDC
        print "DHCP Service Status... %s\n" %status


def iprecon(ifname):

        print bcolors.OKGREEN + "      [ IP ENUMERATION MODULE ]\n" + bcolors.ENDC

        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        int_ip =  socket.inet_ntoa(fcntl.ioctl(s.fileno(),0x8915, struct.pack('256s', ifname[:15]))[20:24])
        netmask = socket.inet_ntoa(fcntl.ioctl(socket.socket(socket.AF_INET, socket.SOCK_DGRAM), 35099, struct.pack('256s', ifname))[20:24])

        if not ip_validate(int_ip):
            print '[+] Internal IP obtained on '+ bcolors.TITLE + '%s:' % ifname + bcolors.ENDC + bcolors.OKGREEN + " %s" % int_ip + bcolors.ENDC + ' netmask ' + bcolors.OKGREEN + '%s' % netmask + bcolors.ENDC
            return int_ip

        else:

            print bcolors.FAIL + "[!] Invalid IP obtained." + bcolors.ENDC + " Checking if we can bypass with static IP.\n"
            return (static_bypass(ifname))


def ip_validate(ip_addr):
    ip_addr = IPAddress(ip_addr)
    return not ip_addr.is_private() and not ip_addr.is_loopback() and not ip_addr.is_reserved() and not ip_addr.is_hostmask()


def netmask_recon(ifname):

        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        int_ip =  socket.inet_ntoa(fcntl.ioctl(s.fileno(),0x8915, struct.pack('256s', ifname[:15]))[20:24])
        netmask = socket.inet_ntoa(fcntl.ioctl(socket.socket(socket.AF_INET, socket.SOCK_DGRAM), 35099, struct.pack('256s', ifname))[20:24])

        return netmask


def net_length(netmask):

        binary_str = ''
        for octet in netmask:
                binary_str += bin(int(octet))[2:].zfill(8)
        return str(len(binary_str.rstrip('0')))


def subnet(int_ip, netmask):

        ipaddr = int_ip.split('.')
        netmask = netmask.split('.')


        net_start = [str(int(ipaddr[x]) & int(netmask[x]))
             for x in range(0,4)]

        CIDR =  '.'.join(net_start) + '/' + net_length(netmask)
        return CIDR


def external_IP_recon():

        try:
                site = urllib2.urlopen("http://checkip.dyndns.org/", timeout = 5)
                url = site.read()
                grab = re.findall('([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+)', url)
                address = grab[0]
                print 'External IP obtained: ' + bcolors.OKGREEN + '%s\n' %address + bcolors.ENDC
        except:
                print bcolors.WARNING + "[!] Could not reach the outside world. Possibly behind a firewall or some kind filtering\n" + bcolors.ENDC
        return


def clear_output():

        yes = set(['yes','y', ''])
        no = set(['no','n'])

        choice = raw_input(bcolors.WARNING + "[!] " + bcolors.ENDC + "You are about to delete all previous results. Do you want to continue? y/n: ")

        work_path = '../Results/'
        responder_path = '../Tools/Responder/logs/'


        if choice in yes:

            if os.listdir(work_path)!=[]:
                subprocess.call('sudo rm -rf ../Results/* ', shell = True)
                print bcolors.WARNING + '[*] All previous results in ../Results removed\n'+ bcolors.ENDC
            elif os.listdir(responder_path)!=[]:
                if os.path.isdir("../old_responder_logs") == True:
                    subprocess.call("sudo mv ../Tools/Responder/logs/* ../old_Responder_logs", shell = True)
                    print bcolors.WARNING + "[*] Previous Responder logs moved to ../WarBerry/old_Responder_logs" + bcolors.ENDC
                else:
                    subprocess.call("sudo mkdir ../old_Responder_logs/", shell=True)
                    subprocess.call("sudo mv ../Tools/Responder/logs/* ../old_Responder_logs/",shell=True)
                    print bcolors.WARNING + "[*] Previous Responder logs moved to ../old_Responder_logs/" + bcolors.ENDC
            elif os.listdir(work_path) == [] and os.listdir(responder_path) == []:
                print  bcolors.WARNING + '[*] No previous results found' + bcolors.ENDC

        elif choice in no:
            print bcolors.OKGREEN + "[-] Results files left intact" + bcolors.ENDC

        else:

            sys.stdout.write("Please respond with 'y/yes' or 'n/no'\n")

def sniffer(iface, packets):
        print " "
        packet_count = 20
        pcap_location = "../Results/capture.pcap"
        print bcolors.OKGREEN + "      [ NETWORK SNIFFING MODULE ]\n" + bcolors.ENDC
        print "Sniffer will begin capturing %d packets" %packet_count #Change the count number accordingly
        packets = sniff(iface=iface, count= packet_count)
        wrpcap(pcap_location, packets)
        print bcolors.OKGREEN + "[+] " + bcolors.ENDC + "Capture Completed." + bcolors.ENDC + " PCAP File Saved at " + bcolors.OKGREEN + "%s!\n" %pcap_location + bcolors.ENDC


def wifi_scan():

    subprocess.call("sudo cat /proc/cpuinfo | grep Revision | awk {'print $3'} > ../Results/model", shell=True)

    with open('../Results/model', 'r') as pi_model:
        for model in pi_model:
            if model.strip() == "a02082":
                print " "
                print bcolors.OKGREEN + "      [ Wi-Fi ENUMERATION MODULE ]\n" + bcolors.ENDC

                subprocess.call("sudo iwlist wlan0 scan | grep ESSID | awk {'print $1'} > ../Results/wifis", shell = True)
                if os.path.isfile('../Results/wifis'):
                    with open('../Results/wifis', 'r') as wifis:
                        if os.stat('../Results/wifis').st_size != 0:
                            for wifi in wifis:
                                print bcolors.OKGREEN + "[+] " + bcolors.ENDC + "Found Wireless Network: %s" %wifi.strip() + bcolors.ENDC
                        else:
                            print bcolors.WARNING + "[-] No Wireless Networks Captured" + bcolors.ENDC
                else:
                    return
            else:
                return


def bluetooth_scan():

    subprocess.call("sudo cat /proc/cpuinfo | grep Revision | awk {'print $3'} > ../Results/model", shell=True)

    with open('../Results/model', 'r') as pi_model:
        for model in pi_model:
            if model.strip() == "a02082":
                print " "
                print bcolors.OKGREEN + "      [ BLUETOOTH ENUMERATION MODULE ]\n" + bcolors.ENDC

                def discover():
                    blues = discover_devices()
                    for device in blues:
                        name = str(lookup_name(device))
                        with open('../Results/blues','a') as bluesfile:
                            bluesfile.write(str(name) + " " + str(device)+ "\n")

                        print bcolors.OKGREEN + "[+]" + bcolors.ENDC + " Found Bluetooth Device: " + str(name)
                        print bcolors.OKGREEN + "[+]" + bcolors.ENDC + " MAC address: " + str(device)

                for i in range(10):
                    discover()
            else:
                return
    if os.path.isfile('../Results/blues'):
        if os.stat('../Results/blues').st_size != 0:
            print bcolors.TITLE + "[+] Done! Results saved in /Results/blues" + bcolors.ENDC
    else:
        print bcolors.WARNING + "[-] No Bluetooth Devices Captured" + bcolors.ENDC
    

def nbtscan(CIDR):

       print " "
       print bcolors.OKGREEN + "      [ NAMESERVER ENUMERATION MODULE ]\n" + bcolors.ENDC

       subprocess.call('sudo nbtscan -r %s > ../Results/nameservers' %CIDR , shell = True )
       subprocess.call("sudo cat ../Results/nameservers | awk {'print $2'} > ../Results/mvp_names", shell=True)

       print " "
       with open('../Results/nameservers', 'r') as nameservers:
            names = nameservers.read()
            print names


if __name__ == '__main__':

    try:
        main()
    except KeyboardInterrupt:
        subprocess.call("sudo mkdir ../Results/Responder_logs", shell=True)
        subprocess.call("sudo mv ../Tools/Responder/logs/* ../Results/Responder_logs/",shell=True)
        subprocess.call('clear', shell=True)
        banner_full()
