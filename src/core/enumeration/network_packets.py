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

import os, os.path,sys
import subprocess
from src.utils.console_colors import *
from scapy.all import *

def sniffer(status, iface, packets, expire):
        print (" ")
        pcap_location = "Results/capture.pcap"
	pcap_location1= "Results/capture1.pcap"
	pcap_location2= "Results/capture2.pcap"
	pcap_location3= "Results/capture3.pcap"

        print (bcolors.OKGREEN + "      [ NETWORK PACKET SNIFFING MODULE ]\n" + bcolors.ENDC)
        print ("Sniffer will begin capturing %d packets for %d seconds" %(packets,expire))
        try:
                pack = sniff(iface=iface, timeout=expire)
		wrpcap(pcap_location1, pack)
		pack2=[]
		if (len(pack)<packets):
			packetsTo=packets-len(pack)
			print (bcolors.OKGREEN + "[*] "+ bcolors.ENDC +"Sniffer will continue capturing another %s packets" %packetsTo)
			pack2=sniff (iface=iface, count=int(packetsTo))
			wrpcap(pcap_location2, pack2)
		else:
			print ("Sniffer captured more than %s packets" %packets)
			for i in range(0, length):
				pack2.append(pack[i])
			wrpcap(pcap_location3, pack2)
		if (os.path.exists(pcap_location2)):
			subprocess.call("mergecap -w %s %s %s" %pcap_location%pcap_location1%pcap_location2, shell=True)
			subprocess.call("rm %s %s" %pcap_location1%pcap_location2, shell=True)
		else:
			if (os.path.exists(pcap_location3)):
				subprocess.call("mv %s %s" %pcap_location3%pcap_location, shell=True)
			else:
				subprocess.call("mv %s %s" %pcap_location1%pcap_location,shell=True)
        except IOError as (errno, strerror):
                print ("I/O error({0}): {1}".format(errno, strerror))
                print ("THE SYSTEM WILL NOW EXIT!!!")
                sys.exit(1)
        except ValueError:
                print ("Could not convert data to an integer.")
                print ("THE SYSTEM WILL NOW EXIT!!!")
                sys.exit(1)
        except:
                print (" ")
        print(bcolors.OKGREEN + "[+] " + bcolors.ENDC + "Capture Completed." + bcolors.ENDC + " PCAP File Saved at " + bcolors.OKGREEN + "%s!\n" %pcap_location + bcolors.ENDC)
        if os.path.exists("Results/arp_flush_temp"):
                subprocess.call("sudo rm Results/arp_flush_temp", shell=True)  # delete temporary file.

        status.warberryOKGREEN("Completed sniffing network packets\n")
