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

import subprocess
import socket
import fcntl
import struct
import urllib2
import re
from netaddr import *
import xml.etree.ElementTree as ET
from src.utils.info_banners import *
from src.utils.console_colors import *


def dhcp_check(status):
        status.warberryOKGREEN("      [ DHCP SERVICE CHECK MODULE ]\n")
        dhcp_out = subprocess.check_output(['ps', '-A'])
        if "dhcp" in dhcp_out:
            print ("DHCP Service Status...\n")
            status.warberryFAIL("Running - Not Stealth")
        else:
            print ("DHCP Service Status...\n")
            status.warberryOKGREEN("Not Running - Stealth")

def netmask_recon(iface):

        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:

            return socket.inet_ntoa(fcntl.ioctl(s.fileno(), 35099, struct.pack('256s', iface))[20:24])

        except:
            subprocess.call('clear', shell=True)
            banner_full()
            print(
                bcolors.FAIL + "Interface %s seems to be down. Try Running with -I to specify an interface" % iface + bcolors.ENDC)
            exit()

def ip_validate(ip):
        ip_addr = IPAddress(ip)
        return not ip_addr.is_private() and not ip_addr.is_loopback() and not ip_addr.is_reserved() and not ip_addr.is_hostmask()

def external_IP_recon():
            try:
                    site = urllib2.urlopen("http://checkip.dyndns.org/", timeout=5)
                    url = site.read()
                    grab = re.findall('([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+)', url)
                    address = grab[0]
                    return address
            except:
                    return None

def net_length(netmask):
        binary_str = ''
        for octet in netmask:
            binary_str += bin(int(octet))[2:].zfill(8)
        return str(len(binary_str.rstrip('0')))

def subnet(int_ip, netmask):
        ipaddr = int_ip.split('.')
        netmask = netmask.split('.')

        net_start = [str(int(ipaddr[x]) & int(netmask[x]))
                     for x in range(0, 4)]

        CIDR = '.'.join(net_start) + '/' + net_length(netmask)
        return CIDR

def XMLParser(file):

    with open(file, 'rb') as xml_file:
        tree = ET.parse(xml_file)
        root = tree.getroot()
        hosts = []
        for hostChild in root:
            host = {}
            addresses = []
            for hostAttr in hostChild:
                if hostAttr.tag.startswith("status"):
                    host["state"] = hostAttr.get('state')
                elif hostAttr.tag.startswith("address"):
                    addr = {}
                    addr["addr"] = hostAttr.get('addr')
                    addr["addrtype"] = hostAttr.get('addrtype')
                    addr["vendor"] = hostAttr.get("vendor")
                    addresses.append(addr)
                elif hostAttr.tag.startswith("hostnames"):
                    hostnames=[]
                    for h in hostAttr:
                        hostsn={}
                        hostsn["name"]=h.get('name')
                        hostsn["type"]=h.get('type')
                        hostnames.append(hostsn)
                    host["hostnames"]=hostnames
                elif hostAttr.tag.startswith("ports"):
                    ports = []
                    for port in hostAttr:
                        p = {}
                        p["protocol"] = port.get('protocol')
                        p["portid"] = port.get('portid')
                        services = []
                        for service in port:
                            serv = {}
                            serv["state"] = service.get('state')
                            serv["name"] = service.get('name')
                            serv["product"] = service.get('product')
                            serv["version"] = service.get('version')
                            serv["ostype"] = service.get('ostype')
                            serv["extrainfo"] = service.get('extrainfo')
                            services.append(serv)
                        services.pop(0)
                        p["services"] = services
                        ports.append(p)
                    host["ports"] = ports
            host["addresses"] = addresses
            hosts.append(host)
        return hosts


def manual_namechange(host_name):
    print
    ("[*] Changing Hostname from " + bcolors.WARNING + socket.gethostname() + bcolors.ENDC + " to " + bcolors.OKGREEN + "%s" % host_name + bcolors.ENDC)
    with open('/etc/hostname', 'w') as hostname:
        hostname.write(host_name)
    with open('/etc/hosts', 'w') as hosts:
        hosts.write(
            '127.0.0.1\tlocalhost\n::1\tlocalhost ip6-localhost ip6-loopback\nff02::1\tip6-allnodes\nff02::2\tip6-allrouters\n\n127.0.1.1\t%s' % host_name)
    subprocess.call('sudo systemctl daemon-reload 2>/dev/null', shell=True)
    subprocess.call('sudo /etc/init.d/hostname.sh 2>/dev/null', shell=True)
    print
    ("[+] New hostname: " + bcolors.TITLE + socket.gethostname() + bcolors.ENDC)
