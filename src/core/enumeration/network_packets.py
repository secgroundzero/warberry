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
from src.utils.console_colors import *
from scapy.all import *

def sniffer(iface, packets, expire):
        print " "
        pcap_location = "../Results/capture.pcap"
        print bcolors.OKGREEN + "      [ NETWORK PACKET SNIFFING MODULE ]\n" + bcolors.ENDC
        print "Sniffer will begin capturing %d packets for %d seconds" %(packets,expire)
        packets = sniff(iface=iface, count= packets, timeout=expire)
        wrpcap(pcap_location, packets)
        print bcolors.OKGREEN + "[+] " + bcolors.ENDC + "Capture Completed." + bcolors.ENDC + " PCAP File Saved at " + bcolors.OKGREEN + "%s!\n" %pcap_location + bcolors.ENDC


def pcap_parser():

        if os.path.isfile('../Results/capture.pcap'):
                print " "
                print bcolors.OKGREEN + "      [ PCAP CAPTURE PARSER MODULE ]\n" + bcolors.ENDC
        else:
                return

        if os.path.isfile('../Results/pcap_results'):
                print bcolors.WARNING + "[!] PCAP Results File Exists. Previous Results will be overwritten\n " + bcolors.ENDC

        print bcolors.TITLE + "[*] Looking for interesting data in /Results/capture.pcap" + bcolors.ENDC
        subprocess.call("sudo python ../Tools/net-creds/net-creds.py -p ../Results/capture.pcap > ../Results/pcap_results", shell = True)


        if os.stat('../Results/pcap_results').st_size == 0:
                print bcolors.WARNING + "[-] No interesting data found in the PCAP file\n" + bcolors.ENDC
        else:
                print bcolors.OKGREEN + "[+] Done! Results saved in /Results/pcap_results\n" + bcolors.ENDC




