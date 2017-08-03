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

from src.utils.info_banners import *
from src.core.bypass.static import *
from src.utils.utils import *
from scapy.all import *

def iprecon(ifname):

        print bcolors.OKGREEN + "      [ IP ENUMERATION MODULE ]\n" + bcolors.ENDC

        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            int_ip = socket.inet_ntoa(fcntl.ioctl(s.fileno(),0x8915, struct.pack('256s', ifname[:15]))[20:24])

        except:
            subprocess.call('clear', shell=True)
            banner_full()
            print bcolors.FAIL + "Interface %s seems to be down. Try Running with -I to specify an interface" %ifname + bcolors.ENDC
            exit()
        netmask = socket.inet_ntoa(fcntl.ioctl(socket.socket(socket.AF_INET, socket.SOCK_DGRAM), 35099, struct.pack('256s', ifname))[20:24])

        if not ip_validate(int_ip) and int_ip!="169.254.253.251":
            print '[+] Internal IP obtained on '+ bcolors.TITLE + '%s:' % ifname + bcolors.ENDC + bcolors.OKGREEN + " %s" % int_ip + bcolors.ENDC + ' netmask ' + bcolors.OKGREEN + '%s' % netmask + bcolors.ENDC
            netmask = netmask_recon(ifname)
            external_IP_recon()
            CIDR = subnet(int_ip, netmask)
            return int_ip
        else:

            print bcolors.FAIL + "[!] Invalid IP obtained." + bcolors.ENDC + " Checking if we can bypass with static IP.\n"
            return (static_bypass(ifname))


def scope_definition(ifname, CIDR):
    print bcolors.OKGREEN + "      [  SCOPE DEFINITION MODULE ]\n" + bcolors.ENDC
    print "Finding live IPs in order to include only those in the scans to minimize footprint\n"
    conf.verb = 0
    subprocess.call("sudo arp -vn | awk {'if (NR!=1) if ($2==\"ether\") print $1'} >../Results/arp_temp ", shell=True)
    with open('../Results/arp_temp', 'r') as arpips:
        lines=arpips.readlines()
    arpips.close
    lines = lines[:-1] #exclude last line because its label
    ips1=[]
    lines_seen = set()  # holds lines already seen
    for line in lines:
        if line not in lines_seen:  # not a duplicate
            ips1.append(line)
            lines_seen.add(line)

    if not ips1:
        print bcolors.WARNING+"NO LIVE IPS FOUND! THERE IS NO NEED TO CONTINUE! WARBERRY WILL NOW EXIT!"+bcolors.ENDC
        sys.exit(1)
    with open('../Results/live_ips', 'w') as ip_addresses:
        for ip in ips1:
            ip_n=ip
            ip_addresses.write(ip_n)
    print bcolors.TITLE + "IP Addresses Found " + bcolors.ENDC
    print bcolors.TITLE + "--------------------" + bcolors.ENDC
    with open('../Results/live_ips', 'r') as liveips:
        lines=liveips.read()
    liveips.close
    print lines
    with open('../Results/live_ips', 'w') as ip_addresses:
        for ip in ips1:
            ip_n=ip
            ip_addresses.write(ip_n)
    subprocess.call("sudo rm ../Results/arp_temp", shell=True) #delete temporary file.
    return "Completed IP Recon\n"
