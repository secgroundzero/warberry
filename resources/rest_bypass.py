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
logging.captureWarnings(True)
#Suppress Scapy IPv6 Warnings
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()


import subprocess
import os, os.path
import sys, getopt
sys.path.append('./resources/')
import socket
import fcntl
import struct
import ipaddress
import urllib,urllib2
import re
from scapy.all import *
from socket import inet_aton
import socket
from info_banners import *
import nmap
import random
from random import randint
import linecache
from warberry import *
from console_colors import bcolors


def hostnames(CIDR):
	print bcolors.OKGREEN + "      [ HOSTNAMES ENUMERATION MODULE ]\n" + bcolors.ENDC
	hostname = socket.gethostname()
	print "Current Hostname:" + bcolors.TITLE + " %s" %hostname + bcolors.ENDC
	print " "

	print "Searching for hostnames in %s\n" %CIDR
	try:
		subprocess.call('sudo nbtscan -q %s | egrep "^[^A-Z]*[A-Z]{5,15}[^A-Z]*$" | awk {\'print $2\'} > ../Results/hostnames' %CIDR, shell = True)
		subprocess.call("sudo sort ../Results/hostnames | uniq > ../Results/unique_hosts", shell = True)
		with open('../Results/unique_hosts', 'r') as hostnames:
			hosts = hostnames.readlines()
			for host in hosts:
				print bcolors.OKGREEN + "[+] Found Hostname: %s" %host.strip() + bcolors.ENDC

	except:
		print bcolors.FAIL + "No Hostnames Found" + bcolors.ENDC
	print " "


def manual_namechange(host_name):

	print "[*] Changing Hostname from " + bcolors.WARNING + socket.gethostname() + bcolors.ENDC + " to " + bcolors.OKGREEN + "%s" %host_name + bcolors.ENDC
	with open('/etc/hostname', 'w') as hostname:
		hostname.write(host_name)
	with open('/etc/hosts', 'w') as hosts:
		hosts.write('127.0.0.1\tlocalhost\n::1\tlocalhost ip6-localhost ip6-loopback\nff02::1\tip6-allnodes\nff02::2\tip6-allrouters\n\n127.0.1.1\t%s' %host_name)
	subprocess.call('sudo systemctl daemon-reload 2>/dev/null', shell=True)
	subprocess.call('sudo /etc/init.d/hostname.sh 2>/dev/null', shell=True)
	print "[+] New hostname: " + bcolors.TITLE + socket.gethostname() + bcolors.ENDC

def namechange():

	mvp_hosts = ['DEMO', 'DEV', 'PRINTER', 'BACKUP', 'DC', 'DC1', 'DC2']
	hostname = socket.gethostname()
	mvp_found=False
	with open('../Results/mvps', 'a') as mvps:
		with open('../Results/mvp_names', 'r') as hostnames:
			hosts = hostnames.readlines()
			for host in hosts:
				for mvp in mvp_hosts:
					if host.strip()==mvp.strip():
						print bcolors.OKGREEN + "[+] Found interesting hostname %s\n" %mvp.strip() + bcolors.ENDC
						mvps.write(host.strip()+'\n')
						mvp_found = True

	if mvp_found != True:
		print bcolors.WARNING + "[-] No interesting names found. Continuing with the same hostname" + bcolors.ENDC

	elif mvp_found == True:
		with open('../Results/mvps', 'r') as mvps:
			mvp = mvps.readline()
			if mvp.strip() == hostname:
				print bcolors.TITLE + "[*] Hostname is stealthy as is. Keeping the same" + bcolors.ENDC
			else:
				with open('../Results/mvps', 'r') as hostnames:
					mvp = hostnames.readline()
					with open('/etc/hostname', 'w') as hostname:
						hostname.write(mvp.strip())
					with open('/etc/hosts', 'w') as hosts:
						print "[*] Changing Hostname from " + bcolors.WARNING + socket.gethostname() + bcolors.ENDC + " to " + bcolors.OKGREEN + "%s" %mvp + bcolors.ENDC
						hosts.write('127.0.0.1\tlocalhost\n::1\tlocalhost ip6-localhost ip6-loopback\nff02::1\tip6-allnodes\nff02::2\tip6-allrouters\n\n127.0.1.1\t%s' %mvp.strip())
				subprocess.call('sudo systemctl daemon-reload 2>/dev/null', shell=True)
				subprocess.call('sudo /etc/init.d/hostname.sh 2>/dev/null', shell=True)
				print "[+] New hostname: " + bcolors.TITLE + socket.gethostname() + bcolors.ENDC


def static_bypass(ifname):

	print bcolors.OKGREEN + "      [ STATIC IP SETUP MODULE ]\n" + bcolors.ENDC

	print "ARP Scanning Network for IPs\n"
	subprocess.call("sudo netdiscover -i %s -P -l ./resources/discover | grep -P -o \'([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+).*? ' | grep -P -o \'[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+' > ../Results/ips_discovered" %ifname, shell = True)

	if os.stat('../Results/ips_discovered').st_size !=0:
		discover = open("../Results/ips_discovered","r")
		ips = discover.readlines()
		discover.close()

		discover = open("../Results/ips_discovered", "r")
		print "Testing validity of %s IP(s)captured" % (sum(1 for _ in discover))
		discover.close()
		discover = open("../Results/ips_discovered","w")

		for ip in ips:
			if not ip_validate(ip):
				print bcolors.OKGREEN + "[+] %s is valid" %ip.strip() + bcolors.ENDC
				discover.write(ip)
			else:
				print bcolors.FAIL + "[-] %s is invalid" %ip.strip() + bcolors.ENDC

		discover.close()
		return(create_subnet(ifname))
	else:
		print bcolors.FAIL + "[-] No IPs captured! Exiting" + bcolors.ENDC
		return


def ip_validate(ip):
	ip_addr = IPAddress(ip)
	return not ip_addr.is_private() and not ip_addr.is_loopback() and not ip_addr.is_reserved() and not ip_addr.is_hostmask()



def create_subnet(ifname):

	with open('../Results/ips_discovered', 'r') as disc:
		int_ip = disc.readlines()

	print "\nCreating CIDRs based on IPs captured\n"

	for ip in int_ip:
		a = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		ipaddr = ip.split('.')
		net = "255.255.255.0"
		netmask = net.split('.')
		net_start =  [str(int(ipaddr[x]) & int(netmask[x]))
             for x in range(0,4)]
		CIDR = '.'.join(net_start) + '/' + net_length(netmask)
		with open('../Results/CIDR', 'w') as netlength:
			netlength.write(CIDR)
		netlength.close()

	with open('../Results/subnets', 'w') as subnets:
		with open('../Results/ips_discovered', 'r') as ips:
			subs = ips.readlines()
			for sub in subs:
				subnets.write('.'.join(sub.split('.')[0:-1] ) + '.' + '\n')

	subprocess.call("sudo sort ../Results/subnets | uniq > ../Results/unique_subnets", shell = True)
	subprocess.call("sudo rm ../Results/subnets", shell=True)

	with open('../Results/unique_subnets', 'r') as subnets:
		subs = subnets.readlines()
		for sub in subs:
			print bcolors.OKGREEN + "[+] Found subnet: %s" %sub.strip() + bcolors.ENDC

	return(set_static(CIDR, ifname))

def net_length(netmask):

		binary_str = ''
		for octet in netmask:
			binary_str += bin(int(octet))[2:].zfill(8)
		return str(len(binary_str.rstrip('0')))


def set_static(CIDR, ifname):
	length = CIDR.split('/')[1]

	bits = 0
	for i in xrange(32 - int(length), 32):
		bits |= (1 << i)
	netmask = "%d.%d.%d.%d" % ((bits & 0xff000000) >> 24, (bits & 0xff0000) >> 16, (bits & 0xff00) >> 8, (bits & 0xff))

	print "\nARP Scanning based on targetted CIDR\n"
	subprocess.call("sudo sort ../Results/CIDR | uniq > ../Results/unique_CIDR", shell=True)
	subprocess.call("sudo rm ../Results/CIDR", shell=True)
	subprocess.call("sudo netdiscover -i %s -P -l ./resources/discover | grep -P -o \'([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+).*? ' | grep -P -o \'[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+' > ../Results/used_ips" %ifname, shell=True)

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
					for used in used_ips:
						if ((available.strip() == used.strip()) and (isUsed == False)):
							print bcolors.FAIL + "[-] IP %s is in use, excluding from static list" % used.strip() + bcolors.ENDC
							isUsed = True
					if (isUsed == False):
						statics.write(available)

	with open('../Results/statics') as static:
		total_frees = sum(1 for _ in static)
		if total_frees > 0:
			print bcolors.TITLE + '\n%s Available IPs to choose from.' % total_frees + bcolors.ENDC
		else:
			print bcolors.FAIL + "No free IPs Found\n" + bcolors.ENDC


	with open('../Results/statics', 'r') as statics:
		line_count = (sum(1 for _ in statics))
		for i in range(0,line_count):
			newline = randint(0,line_count)

			static = linecache.getline('../Results/statics', newline)
			print bcolors.WARNING + "[*] Attempting to set random static ip %s" % static.strip() + bcolors.ENDC
			subprocess.call(["ifconfig", ifname, static.strip(), "netmask", netmask.strip()])

			for used in reversed(open('../Results/used_ips').readlines()):
				print "[*] Pinging %s to ensure that we are live..." % used.strip()
				ping_response = subprocess.call(['ping', '-c', '5', '-W', '3', used.strip()],stdout=open(os.devnull, 'w'), stderr=open(os.devnull, 'w'))
				if ping_response == 0:
					print bcolors.OKGREEN + "[+] Success. IP %s is valid and %s is reachable" % (static.strip(), used.strip()) + bcolors.ENDC
					return static.strip()
				else:
					print bcolors.WARNING + "[-] Failed. IP %s is not valid" % static.strip() + bcolors.ENDC
			print "Attempting to bypass MAC Filtering\n"
			macbypass(unique_CIDR, ifname)



def macbypass(unique_CIDR, ifname):

	print bcolors.OKGREEN + "      [ MAC FILTERING BYPASS MODULE ]\n" + bcolors.ENDC

	print "ARP Scanning Network for MAC Addresses\n"
	subprocess.call("sudo netdiscover -i %s -P -r  %s | grep -o -E /'([[:xdigit:]]{1,2}:){5}[[:xdigit:]]{1,2}/' > ../Results/macs_discovered" %(unique_CIDR,ifname), shell = True)

	subprocess.call("sudo sort ../Results/macs_discovered | uniq > ../Results/unique_macs", shell=True)
	subprocess.call("sudo rm ../Results/macs_discovered", shell=True)
	with open('../Results/unique_macs', 'r') as macs:
		if os.stat('../Results/unique_macs').st_size != 0:
			print bcolors.OKGREEN + "%s unique MACs Captured!" % ((sum(1 for _ in macs)))
		else:
			print bcolors.FAIL + "No MAC Addresses Captured. Exiting"


	with open('../Results/unique_macs', 'r') as macs:
		for mac in macs:
			print bcolors.TITLE + "Attempting to change MAC Address to %s" %mac
			subprocess.call("sudo ifdown %s" %ifname, shell = True)
			subprocess.call("sudo maccchanger -m %s %s" %(mac, ifname), shell = True)
			subprocess.call('sudo ifup %s'%ifname, shell = True)
			for i in range(0, line_count):
				newline = randint(0, line_count)

				static = linecache.getline('../Results/statics', newline)
				print bcolors.WARNING + "[*] Attempting to set random static ip %s" % static.strip() + bcolors.ENDC
				subprocess.call(["ifconfig", ifname, static.strip(), "netmask", netmask.strip()])

				for used in reversed(open('../Results/used_ips').readlines()):
					print "[*] Pinging %s to ensure that we are live..." % used.strip()
					ping_response = subprocess.call(['ping', '-c', '5', '-W', '3', used.strip()], stdout=open(os.devnull, 'w'), stderr=open(os.devnull, 'w'))
					if ping_response == 0:
						print bcolors.OKGREEN + "[+] Success. IP %s is valid and %s is reachable" % (static.strip(), used.strip()) + bcolors.ENDC
						return static.strip()
					else:
							print bcolors.FAIL + "Unable to bypass Filtering." + bcolors.ENDC
							nacbypass(unique_CIDR, ifname)



def nacbypass(unique_CIDR, ifname):

	print bcolors.OKGREEN + "      [ NAC FILTERING BYPASS MODULE ]\n" + bcolors.ENDC

	print "ARP Scanning Network for MAC Addresses\n"

	goodwords = ['PRINTER', 'DEMO', 'DEV', 'DC', 'DC1', 'DC2']

	subprocess.call("sudo tcpdump -i %s -vvv port 137 -c 10 > ../Results/network_traffic"%ifname);
	search = ".netbios"
	subprocess.call("grep %s ../Results/network_traffic > ../Results/ips_found" %search, shell=True)
	ip_net = []
	with open('../Results/ips_found', 'r') as a:
		ips = a.readlines()
		for line in ips:
			ip_net.append(line.split('n')[0].strip()[:-1])

	search = "Name="
	subprocess.call("grep %s ../Results/network_traffic > ../Results/names_found " %search, shell=True)
	n = []
	with open('../Results/names_found', 'r') as a:
		names = a.readlines()
		for line in names:
			n.append(line.split(' ')[0].split('=')[1])

	names = []
	for i in range(len(n)):
		if (i % 2 == 0):
			names.append(n[i])

	subprocess.call("sudo netdiscover -P -r %s | awk {'print $1,$2'} > ../Results/ips_macs" % unique_CIDR,shell=True)

	with open('../Results/ips_macs', 'r') as ip_m:
		ip_mac = ip_m.readlines()
		macs = [None] * len(ip_net)
		for line in ip_mac:
			found = False
			for i in range(len(ip_net)):
				if (line.split(' ')[0] == ip_net[i]):
					found = True
					macs[i] = line.split(' ')[1]
				else:
					found = False
					macs[i] = '-'
	Fname = []
	Fmac = []

	for i in range(len(macs)):
		if (macs[i] != "-"):
			Fname.append(names[i])
			Fmac.append(macs[i])

	for word in goodwords:
		for name in Fname:
			if word == name:
				ic = Fname.index(name)
				print "Changing hostname to %s and MAC address to %s" % (name, Fmac[ic])
				with open('/etc/hosts', 'w') as hosts:
					hosts.write('127.0.0.1\tlocalhost\n::1\tlocahost ip6-localhost ip6-loopback\nff02::1\tip6-allnodes\nff02::2\tip6-allrouters\n\n127.0.1\t%s' % name)
				with open('/etc/hostname', 'w') as hostname:
					hostname.write(name)
					subprocess.call('sudo /etc/init.d/hostname.sh', shell=True)
					subprocess.call('sudo systemctl daemon-reload', shell=True)
				subprocess.call('sudo ifdown %s'%ifname, shell=True)
				subprocess.call('sudo macchanger -m %s %s' %(Fmac[ic], ifname), shell=True)
				subprocess.call('sudo ifup %s'%ifname, shell=True)

	with open('../Results/used_ips', 'r') as used:
		used_ips = used.readlines()
		with open('../Results/statics', 'w') as statics:
			with open('../Results/avail_ips', 'r') as avail_ips:
				for available in avail_ips:
					isUsed = False
					for used in used_ips:
						if ((available.strip() == used.strip()) and (isUsed == False)):
							print bcolors.FAIL + "[-] IP %s is in use, excluding from static list" % used.strip() + bcolors.ENDC
							isUsed = True
						if isUsed==False:
							statics.write(available)

				with open('../Results/statics') as static:
					total_frees = sum(1 for _ in static)
					if total_frees > 0:
						print bcolors.TITLE + '\n%s Available IPs to choose from.' % total_frees + bcolors.ENDC
					else:
						print bcolors.FAIL + "No free IPs Found\n" + bcolors.ENDC

	with open('../Results/statics', 'r') as statics:
		line_count = (sum(1 for _ in statics))
		for i in range(0, line_count):
			newline = randint(0, line_count)

			static = linecache.getline('../Results/statics', newline)
			print bcolors.WARNING + "[*] Attempting to set random static ip %s" % static.strip() + bcolors.ENDC
			subprocess.call(["ifconfig", ifname, static.strip(), "netmask", netmask.strip()])

	for used in reversed(open('../Results/used_ips').readlines()):
		print "[*] Pinging %s to ensure that we are live..." % used.strip()
		ping_response = subprocess.call(['ping', '-c', '5', '-W', '3', used.strip()], stdout=open(os.devnull, 'w'),stderr=open(os.devnull, 'w'))

		if ping_response == 0:
			print bcolors.OKGREEN + "[+] Success. IP %s is valid and %s is reachable" % (static.strip(), used.strip()) + bcolors.ENDC

		else:
			print bcolors.WARNING + "[-] Failed. IP %s is not valid" % static.strip() + bcolors.ENDC
