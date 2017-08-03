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

import os, os.path,sys
import subprocess
from src.utils.console_colors import *
from scapy.all import *

def sniffer(iface, packets, expire):
        print " "
        pcap_location = "../Results/capture.pcap"
        print bcolors.OKGREEN + "      [ NETWORK PACKET SNIFFING MODULE ]\n" + bcolors.ENDC
        print "Sniffer will begin capturing %d packets for %d seconds" %(packets,expire)
        try:
                packets = sniff(iface=iface, count= packets, timeout=expire)
                wrpcap(pcap_location, packets)
        except IOError as (errno, strerror):
                print "I/O error({0}): {1}".format(errno, strerror)
                print "THE SYSTEM WILL NOW EXIT!!!"
                sys.exit(1)
        except ValueError:
                print "Could not convert data to an integer."
                print "THE SYSTEM WILL NOW EXIT!!!"
                sys.exit(1)
        except:
                print "Unexpected error:", sys.exc_info()[0]
        print bcolors.OKGREEN + "[+] " + bcolors.ENDC + "Capture Completed." + bcolors.ENDC + " PCAP File Saved at " + bcolors.OKGREEN + "%s!\n" %pcap_location + bcolors.ENDC
        if os.path.exists("../Results/arp_flush_temp"):
                subprocess.call("sudo rm ../Results/arp_flush_temp", shell=True)  # delete temporary file.
        return "Completed sniffing network packets\n"

