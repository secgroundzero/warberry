# coding=utf-8
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

import linecache
import os.path
import socket
import subprocess
from random import randint

from console_colors import bcolors

import requests.packages.urllib3
# !/usr/bin/python
import logging

logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
logging.captureWarnings(True)
# Suppress Scapy IPv6 Warnings


requests.packages.urllib3.disable_warnings()


def hostnames(cidr):
    print(bcolors.OKGREEN + "      [ HOSTNAMES ENUMERATION MODULE ]\n" + bcolors.ENDC)
    hostname = socket.gethostname()
    print("Current Hostname:" + bcolors.TITLE + " %s" % hostname + bcolors.ENDC)
    # print bcolors.WARNING + "[!] If you want to continue undetected stop the script and change /etc/hosts and /etc/hostname" + bcolors.ENDC
    print(" ")

    print("Searching for hostnames in %s\n" % cidr)
    try:
        subprocess.call('sudo nbtscan -q %s | egrep "^[^A-Z]*[A-Z]{5,15}[^A-Z]*$" | awk {\'print $2\'} > ../Results/hostnames' % cidr, shell=True)
        subprocess.call("sudo sort ../Results/hostnames | uniq > ../Results/unique_hosts", shell=True)
        with open('../Results/unique_hosts', 'r') as unique_hostnames:
            hosts = unique_hostnames.readlines()
            for host in hosts:
                print(bcolors.OKGREEN + "[+] Found Hostname: %s" % host.strip() + bcolors.ENDC)

    except:
        print(bcolors.FAIL + "No Hostnames Found" + bcolors.ENDC)
    print(" ")


def namechange():
    mvp_hosts = ['DEMO', 'DEV', 'PRINTER', 'BACKUP', 'DC', 'DC1', 'DC2']

    mvp_found = False
    with open('../Results/mvps', 'a') as mvps:
        with open('../Results/mvp_names', 'r') as mvp_names:
            hosts = mvp_names.readlines()
            for host in hosts:
                for mvp in mvp_hosts:
                    if host.strip() == mvp.strip():
                        print(bcolors.OKGREEN + "[+] Found interesting hostname %s" % mvp.strip() + bcolors.ENDC)
                        mvps.write(host.strip() + '\n')
                        mvp_found = True

    if mvp_found is not True:
        print(bcolors.WARNING + "[-] No interesting names found. Continuing with the same Hostname" + bcolors.ENDC)

    elif mvp_found is True:
        with open('../Results/mvps', 'r') as mvps:
            mvp = mvps.readline()
            with open('/etc/hosts', 'w') as hosts:
                print("[*] Changing Hostname from " + bcolors.WARNING + socket.gethostname() + bcolors.ENDC + " to " + bcolors.OKGREEN + "%s" % mvp + bcolors.ENDC)
                hosts.write('127.0.0.1\tlocalhost\n::1\tlocalhost ip6-localhost ip6-loopback\nff02::1\tip6-allnodes\nff02::2\tip6-allrouters\n\n127.0.1.1\t%s' % mvp.strip())
            with open('/etc/hostname', 'w') as hostname:
                hostname.write(mvp.strip())
        subprocess.call('sudo /etc/init.d/hostname.sh', shell=True)
        subprocess.call('sudo systemctl daemon-reload', shell=True)
        print("[+] New hostname: " + bcolors.TITLE + socket.gethostname() + bcolors.ENDC)


def static_bypass():
    print(bcolors.OKGREEN + "      [ STATIC IP SETUP MODULE ]\n" + bcolors.ENDC)

    print("ARP Scanning Network for IPs\n")
    subprocess.call("sudo netdiscover -i eth0 -P -l ./resources/discover | grep -P -o \'([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+).*? ' | grep -P -o \'[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+' > ../Results/ips_discovered", shell=True)

    if os.stat('../Results/ips_discovered').st_size != 0:
        discover = open("../Results/ips_discovered", "r")
        ips = discover.readlines()
        discover.close()

        discover = open("../Results/ips_discovered", "r")
        print("Testing validity of %s IP(s)captured" % (sum(1 for _ in discover)))
        discover.close()
        discover = open("../Results/ips_discovered", "w")

        for ip in ips:
            if ("192.168." or "172." or "10.") in ip:
                print(bcolors.OKGREEN + "[+] %s is valid" % ip.strip() + bcolors.ENDC)
                discover.write(ip)
            else:
                print(bcolors.FAIL + "[-] %s is invalid" % ip.strip() + bcolors.ENDC)

        discover.close()
        return create_subnet()
    else:
        print(bcolors.FAIL + "[-] No IPs captured! Exiting" + bcolors.ENDC)
        return


def create_subnet():
    with open('../Results/ips_discovered', 'r') as disc:
        int_ip = disc.readlines()

    print("\nCreating CIDRs based on IPs captured\n")

    cidr = ""

    for ip in int_ip:
        a = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        ipaddr = ip.split('.')
        net = "255.255.255.0"
        netmask = net.split('.')
        net_start = [str(int(ipaddr[x]) & int(netmask[x]))
                     for x in range(0, 4)]
        cidr = '.'.join(net_start) + '/' + net_length(netmask)
        with open('../Results/CIDR', 'w') as netlength:
            netlength.write(cidr)
        netlength.close()

    with open('../Results/subnets', 'w') as subnets:
        with open('../Results/ips_discovered', 'r') as ips:
            subs = ips.readlines()
            for sub in subs:
                subnets.write('.'.join(sub.split('.')[0:-1]) + '.' + '\n')

    subprocess.call("sudo sort ../Results/subnets | uniq > ../Results/unique_subnets", shell=True)
    subprocess.call("sudo rm ../Results/subnets", shell=True)

    with open('../Results/unique_subnets', 'r') as subnets:
        subs = subnets.readlines()
        for sub in subs:
            print(bcolors.OKGREEN + "[+] Found subnet: %s" % sub.strip() + bcolors.ENDC)

    return set_static(cidr)


def net_length(netmask):
    binary_str = ''
    for octet in netmask:
        binary_str += bin(int(octet))[2:].zfill(8)
    return str(len(binary_str.rstrip('0')))


def set_static(cidr):
    length = cidr.split('/')[1]

    bits = 0
    for i in range(32 - int(length), 32):
        bits |= (1 << i)
    netmask = "%d.%d.%d.%d" % ((bits & 0xff000000) >> 24, (bits & 0xff0000) >> 16, (bits & 0xff00) >> 8, (bits & 0xff))

    print("\nARP Scanning based on targetted CIDR\n")
    subprocess.call("sudo sort ../Results/CIDR | uniq > ../Results/unique_CIDR", shell=True)
    subprocess.call("sudo rm ../Results/CIDR", shell=True)
    subprocess.call("sudo netdiscover -i eth0 -P -l ./resources/discover | grep -P -o \'([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+).*? ' | grep -P -o \'[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+' > ../Results/used_ips", shell=True)

    with open('../Results/avail_ips', 'w') as avail:
        with open('../Results/unique_subnets', 'r') as subs:
            for sub in subs:
                for i in range(1, 255):
                    avail.write(sub.strip() + str(i) + "\n")

    with open('../Results/used_ips', 'r') as used:
        used_ips = used.readlines()
        with open('../Results/statics', 'w') as statics:
            with open('../Results/avail_ips', 'r') as avail_ips:
                for available in avail_ips:
                    isUsed = False
                    for used_ip in used_ips:
                        if (available.strip() == used_ip.strip()) and (isUsed is False):
                            print(bcolors.FAIL + "[-] IP %s is in use, excluding from static list" % used_ip.strip() + bcolors.ENDC)
                            isUsed = True
                    if not isUsed:
                        statics.write(available)

    with open('../Results/statics') as static:
        total_frees = sum(1 for _ in static)
        if total_frees > 0:
            print(bcolors.TITLE + '\n%s Available IPs to choose from.' % total_frees + bcolors.ENDC)
        else:
            print(bcolors.FAIL + "No free IPs Found\n" + bcolors.ENDC)

    with open('../Results/statics', 'r') as statics:
        line_count = (sum(1 for _ in statics))
        for i in range(0, line_count):
            newline = randint(0, line_count)

            static = linecache.getline('../Results/statics', newline)
            print(bcolors.WARNING + "[*] Attempting to set random static ip %s" % static.strip() + bcolors.ENDC)
            subprocess.call(["ifconfig", "eth0", static.strip(), "netmask", netmask.strip()])

            for used in reversed(open('../Results/used_ips').readlines()):
                print("[*] Pinging %s to ensure that we are live..." % used.strip())
                ping_response = subprocess.call(['ping', '-c', '5', '-W', '3', used.strip()], stdout=open(os.devnull, 'w'), stderr=open(os.devnull, 'w'))
                if ping_response == 0:
                    print(bcolors.OKGREEN + "[+] Success. IP %s is valid and %s is reachable" % (static.strip(), used.strip()) + bcolors.ENDC)
                    return static.strip()
                else:
                    print(bcolors.WARNING + "[-] Failed. IP %s is not valid" % static.strip() + bcolors.ENDC)
            print("Attempting to bypass MAC Filtering\n")
            macbypass(unique_CIDR)


def macbypass(unique_cidr):
    print(bcolors.OKGREEN + "      [ MAC FILTERING BYPASS MODULE ]\n" + bcolors.ENDC)

    print("ARP Scanning Network for MAC Addresses\n")
    subprocess.call("sudo netdiscover -i eth0 -P -r  %s | grep -o -E /'([[:xdigit:]]{1,2}:){5}[[:xdigit:]]{1,2}/' > ../Results/macs_discovered" % unique_cidr, shell=True)

    subprocess.call("sudo sort ../Results/macs_discovered | uniq > ../Results/unique_macs", shell=True)
    subprocess.call("sudo rm ../Results/macs_discovered", shell=True)
    with open('../Results/unique_macs', 'r') as macs:
        if os.stat('../Results/unique_macs').st_size != 0:
            print(bcolors.OKGREEN + "%s unique MACs Captured!" % (sum(1 for _ in macs)))
        else:
            print(bcolors.FAIL + "No MAC Addresses Captured. Exiting")

    with open('../Results/unique_macs', 'r') as macs:
        for mac in macs:
            print(bcolors.TITLE + "Attempting to change MAC Address to %s" % mac)
            subprocess.call("sudo ifdown eth0", shell=True)
            subprocess.call("sudo maccchanger -m %s eth0" % mac, shell=True)
            subprocess.call('sudo ifup eth0', shell=True)
            line_count = (sum(1 for _ in macs))

            for i in range(0, line_count):

                newline = randint(0, line_count)

                static = linecache.getline('../Results/statics', newline)
                print(bcolors.WARNING + "[*] Attempting to set random static ip %s" % static.strip() + bcolors.ENDC)
                subprocess.call(["ifconfig", "eth0", static.strip(), "netmask", netmask.strip()])

                for used in reversed(open('../Results/used_ips').readlines()):
                    print("[*] Pinging %s to ensure that we are live..." % used.strip())
                    ping_response = subprocess.call(['ping', '-c', '5', '-W', '3', used.strip()], stdout=open(os.devnull, 'w'), stderr=open(os.devnull, 'w'))
                    if ping_response == 0:
                        print(bcolors.OKGREEN + "[+] Success. IP %s is valid and %s is reachable" % (static.strip(), used.strip()) + bcolors.ENDC)
                        return static.strip()
                    else:
                        print(bcolors.FAIL + "Unable to bypass Filtering." + bcolors.ENDC)
                        nacbypass(unique_cidr)


def nacbypass(unique_cidr):
    print(bcolors.OKGREEN + "      [ NAC FILTERING BYPASS MODULE ]\n" + bcolors.ENDC)

    print("ARP Scanning Network for MAC Addresses\n")

    goodwords = ['PRINTER', 'DEMO', 'DEV', 'DC', 'DC1', 'DC2']

    subprocess.call("sudo tcpdump -i eth0 -vvv port 137 -c 10 > ../Results/network_traffic")
    search = ".netbios"
    subprocess.call("grep %s ../Results/network_traffic > ../Results/ips_found" % search, shell=True)
    ip_net = []
    with open('../Results/ips_found', 'r') as a:
        ips = a.readlines()
        for line in ips:
            ip_net.append(line.split('n')[0].strip()[:-1])

    search = "Name="
    subprocess.call("grep %s ../Results/network_traffic > ../Results/names_found " % search, shell=True)
    n = []
    with open('../Results/names_found', 'r') as a:
        names = a.readlines()
        for line in names:
            n.append(line.split(' ')[0].split('=')[1])

    names = []
    for i in range(len(n)):
        if i % 2 == 0:
            names.append(n[i])

    subprocess.call("sudo netdiscover -P -r %s | awk {'print $1,$2'} > ../Results/ips_macs" % unique_cidr, shell=True)

    with open('../Results/ips_macs', 'r') as ip_m:
        ip_mac = ip_m.readlines()
        macs = [None] * len(ip_net)
        for line in ip_mac:
            found = False
            for i in range(len(ip_net)):
                if line.split(' ')[0] == ip_net[i]:
                    found = True
                    macs[i] = line.split(' ')[1]
                else:
                    found = False
                    macs[i] = '-'
    Fname = []
    Fmac = []

    for i in range(len(macs)):
        if macs[i] != "-":
            Fname.append(names[i])
            Fmac.append(macs[i])

    for word in goodwords:
        for name in Fname:
            if word == name:
                ic = Fname.index(name)
                print("Changing hostname to %s and MAC address to %s" % (name, Fmac[ic]))
                with open('/etc/hosts', 'w') as hosts:
                    hosts.write('127.0.0.1\tlocalhost\n::1\tlocahost ip6-localhost ip6-loopback\nff02::1\tip6-allnodes\nff02::2\tip6-allrouters\n\n127.0.1\t%s' % name)
                with open('/etc/hostname', 'w') as hostname:
                    hostname.write(name)
                    subprocess.call('sudo /etc/init.d/hostname.sh', shell=True)
                    subprocess.call('sudo systemctl daemon-reload', shell=True)
                subprocess.call('sudo ifdown eth0', shell=True)
                subprocess.call('sudo macchanger -m %s eth0' % Fmac[ic], shell=True)
                subprocess.call('sudo ifup eth0', shell=True)

    with open('../Results/used_ips', 'r') as used:
        used_ips = used.readlines()
        with open('../Results/statics', 'w') as statics:
            with open('../Results/avail_ips', 'r') as avail_ips:
                for available in avail_ips:
                    isUsed = False
                    for used_ip in used_ips:
                        if (available.strip() == used_ip.strip()) and (isUsed is False):
                            print(bcolors.FAIL + "[-] IP %s is in use, excluding from static list" % used_ip.strip() + bcolors.ENDC)
                            isUsed = True
                        if isUsed is False:
                            statics.write(available)

                with open('../Results/statics') as static:
                    total_frees = sum(1 for _ in static)
                    if total_frees > 0:
                        print(bcolors.TITLE + '\n%s Available IPs to choose from.' % total_frees + bcolors.ENDC)
                    else:
                        print(bcolors.FAIL + "No free IPs Found\n" + bcolors.ENDC)

    with open('../Results/statics', 'r') as statics:
        line_count = (sum(1 for _ in statics))
        for i in range(0, line_count):
            newline = randint(0, line_count)

            static = linecache.getline('../Results/statics', newline)
            print(bcolors.WARNING + "[*] Attempting to set random static ip %s" % static.strip() + bcolors.ENDC)
            subprocess.call(["ifconfig", "eth0", static.strip(), "netmask", netmask.strip()])

    for used in reversed(open('../Results/used_ips').readlines()):
        print("[*] Pinging %s to ensure that we are live..." % used.strip())
        ping_response = subprocess.call(['ping', '-c', '5', '-W', '3', used.strip()], stdout=open(os.devnull, 'w'), stderr=open(os.devnull, 'w'))

        if ping_response == 0:
            print(bcolors.OKGREEN + "[+] Success. IP %s is valid and %s is reachable" % (static.strip(), used.strip()) + bcolors.ENDC)

        else:
            print(bcolors.WARNING + "[-] Failed. IP %s is not valid" % static.strip() + bcolors.ENDC)
