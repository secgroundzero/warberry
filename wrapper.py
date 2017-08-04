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
requests.packages.urllib3.disable_warnings()
import os, os.path
#External modules
from src.core.scanners.targetted_scanner import *
from src.core.scanners.targetted_thread_scanner import *
from src.core.enumeration.nameservers import *
from src.core.enumeration.bluetooth_enum import *
from src.core.enumeration.ip_enum import *
from src.core.enumeration.network_packets import *
from src.core.enumeration.os_enum import *
from src.core.enumeration.services_enum import *
from src.core.enumeration.wifi_enum import *
from src.core.enumeration.zones import *
from src.utils.console_colors import *
from optparse import OptionParser
from src.utils.encryption import *
from src.utils.move_files import *
from src.utils.delete_files import *
from xml_producer import *
from multiprocessing import Process
from scapy.all import *
from src.core.exploits.responder_poison import poison

def warberry():

    start_time = time.time()
    #move previous files in /Results
    move_files(int(start_time))
    delete_files()
    version = bcolors.TITLE + ( '''
 _    _  ___  ____________ ___________________   __
| |  | |/ _ \ | ___ \ ___ \  ___| ___ \ ___ \ \ / /
| |  | / /_\ \| |_/ / |_/ / |__ | |_/ / |_/ /\ V /
| |/\| |  _  ||    /| ___ \  __||    /|    /  \ /
\  /\  / | | || |\ \| |_/ / |___| |\ \| |\ \  | |
 \/  \/\_| |_/\_| \_\____/\____/\_| \_\_| \_| \_/

            TACTICAL EXPLOITATION

v5                                @sec_groundzero
                          secgroundzero@gmail.com
''') + bcolors.ENDC


    parser = OptionParser(usage= "usage: sudo %prog [options]",version=version)
    parser.add_option("-a", "--attack", action="store", dest="attacktype", default="-A", help="Attack Mode."+ bcolors.WARNING + " Default: --attack" + bcolors.ENDC)
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
                with open('../Results/running_status', 'w') as status:
                    status.write("<root>")
                    status.write("Entering poisoning mode\n")
                    poison_time = options.time
                    poison(iface, poison_time)
                    status.write("</root>")
            else:
                netmask = netmask_recon(iface)
                CIDR = subnet(int_ip, netmask)
                status_str = str(scope_definition(iface, CIDR))
                packets = options.packets
                expire = options.expire
                status_str+=str(sniffer(iface, packets, expire))
                status_str +=str(hostnames(CIDR))
                status_str +=str(nbtscan(CIDR))
                with open('../Results/running_status', 'w') as status:
                    status.write(status_str)
                if host_name != "WarBerry":
                    manual_namechange(host_name)
                if options.hostname == True and host_name == "WarBerry":
                    namechange()
                if options.reconmode == False:
                    intensity = options.intensity
                    status_str=""
                    if options.fast == False:
                        status_str +=str(single_port_scanner(CIDR, intensity, iface))
                    else:
                        status_str +=str(thread_port_scanner(CIDR, intensity, iface))
                    if options.enum == False:
                        status_str +=str(shares_enum(iface))
                        status_str +=str(smb_users(iface))
                        status_str += str(webs_prep())
                        status_str +=str(http_title_enum(iface))
                        status_str +=str(nfs_enum(iface))
                        status_str +=str(waf_enum(iface))
                        status_str +=str(robots_txt())
                        status_str +=str(mysql_enum(iface))
                        status_str +=str(mssql_enum(iface))
                        status_str +=str(ftp_enum(iface))
                        #status_str +=str(snmp_enum(iface))
                        status_str +=str(sip_methods_enum(iface))
                        status_str +=str(sip_users_enum(iface))
                        status_str +=str(os_enum(CIDR,iface))

                        #enum4linux()
                        #with open('../Results/running_status', 'a') as status:
                        #status.write("Completed enum4linux Enumeration\n")
                        status_str +=str(zone_transfers(CIDR,iface))

                        with open('../Results/running_status', 'a') as status:
                            status.write(status_str)
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
    elif options.attacktype == '-S' or options.attacktype == '--sniffer':
        status_str=""
        iface = options.iface
        packets = options.packets
        subprocess.call('clear', shell=True)
        status_str+=str(sniffer(iface, packets))

    create_xmls()
    encrypt_files()

    #Sytem exit due to finish.
    print bcolors.TITLE + "Warberry is now finished. The system will now exit.\n" + bcolors.ENDC
    print bcolors.TITLE + "Time of execution: " + "--- %s seconds ---\n" % (time.time() - start_time) + bcolors.ENDC
    sys.exit(0)
    

def main():
    #Spawn thread for responder
    q = Process(target=warberry())
    q.start()
    q.join()



if __name__ == '__main__':

    try:
        warberry()
    except KeyboardInterrupt:
        try:
            if os.path.exists("../Results") == False:
                subprocess.call("sudo mkdir ../Results", shell = True)
                subprocess.call("sudo mkdir  ../Results/Responder_logs", shell=True)
                subprocess.call("sudo mv  ../Tools/Responder/logs/* ../Results/Responder_logs/", shell=True)
        finally:
            subprocess.call("clear", shell=True)
            banner_full()