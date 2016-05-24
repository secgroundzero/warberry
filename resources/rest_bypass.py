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
sys.path.append('/home/pi/WarBerry/resources/')
import socket
import fcntl
import struct
import ipaddress
import urllib,urllib2
import re
from scapy.all import *
from socket import inet_aton
import socket
from banners import *
import nmap
import random
from random import randint
import linecache


class bcolors:

    HEADER   =  '\033[95m'
    OKBLUE   =  '\033[34m'
    OKGREEN  =  '\033[32m'
    WARNING  =  '\033[93m'
    FAIL     =  '\033[31m'
    ENDC     =  '\033[0m'
    BOLD     =  '\033[1m'
    TITLE    =  '\033[96m'


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
sys.path.append('/home/pi/WarBerry/resources/')
sys.path.append('/home/pi/WarBerry/')
import socket
import fcntl
import struct
import ipaddress
import urllib,urllib2
import re
from scapy.all import *
from socket import inet_aton
import socket
from banners import *
import nmap
from warberry import *


class bcolors:
    HEADER   =  '\033[95m'
    OKBLUE   =  '\033[34m'
    OKGREEN  =  '\033[32m'
    WARNING  =  '\033[93m'
    FAIL     =  '\033[31m'
    ENDC     =  '\033[0m'
    BOLD     =  '\033[1m'
    TITLE    =  '\033[96m'


def hostnames(CIDR):




	print bcolors.OKGREEN + "      [ HOSTNAMES ENUMERATION MODULE ]\n" + bcolors.ENDC
	hostname = socket.gethostname()
	print "Current Hostname:" + bcolors.TITLE + " %s" %hostname + bcolors.ENDC
	#print bcolors.WARNING + "[!] If you want to continue undetected stop the script and change /etc/hosts and /etc/hostname" + bcolors.ENDC
	print " "

	print "Searching for hostnames in %s\n" %CIDR
	try:
		subprocess.call('sudo nbtscan -q %s | egrep "^[^A-Z]*[A-Z]{5,15}[^A-Z]*$" | awk {\'print $2\'} > /home/pi/WarBerry/Results/hostnames' %CIDR, shell = True)
		subprocess.call("sudo sort /home/pi/WarBerry/Results/hostnames | uniq > /home/pi/WarBerry/Results/unique_hosts", shell = True)
		with open('/home/pi/WarBerry/Results/unique_hosts', 'r') as hostnames:
			hosts = hostnames.readlines()
			for host in hosts:
				print bcolors.OKGREEN + "[+] Found Hostname: %s" %host.strip() + bcolors.ENDC

	except:
		print bcolors.FAIL + "No Hostnames Found" + bcolors.ENDC
	print " "


def namechange():

	mvp_hosts = ['DEMO', 'DEV', 'PRINTER', 'BACKUP', 'DC', 'DC1', 'DC2']


	with open('/home/pi/WarBerry/Results/mvps', 'a') as mvps:
		with open('/home/pi/WarBerry/Results/mvp_names', 'r') as hostnames:
			hosts = hostnames.readlines()
			for host in hosts:
				for mvp in mvp_hosts:
					if host.strip()==mvp.strip():
						print bcolors.OKGREEN + "[+] Found interesting hostname %s" %mvp.strip() + bcolors.ENDC
						mvps.write(host.strip()+'\n')
						mvp_found = True

	if mvp_found != True:
		print bcolors.WARNING + "[-] No interesting names found. Continuing with the same Hostname" + bcolors.ENDC

	elif mvp_found == True:
		with open('/home/pi/WarBerry/Results/mvps', 'r') as hostnames:
			mvp = hostnames.readline()
			with open('/etc/hosts', 'w') as hosts:
				print bcolors.WARNING + "[*] Changing Hostame from " + socket.gethostname() + bcolors.ENDC + " to " + bcolors.OKGREEN + "%s" %mvp + bcolors.ENDC
				hosts.write('127.0.0.1  localhost\n::1          locahost ip6-localhost ip6-loopback\nff02::1            ip6-allnodes\nff02::2           ip6-allrouters\n\n127.0.0.1     %s' %mvp.strip())
			with open('/etc/hostname', 'w') as hostname:
				hostname.write(mvp.strip())
		subprocess.call('sudo /etc/init.d/hostname.sh', shell=True)
		print "[+] New hostname: " + bcolors.TITLE + socket.gethostname() + bcolors.ENDC


def static_bypass():

	print bcolors.OKGREEN + "      [ STATIC IP SETUP MODULE ]\n" + bcolors.ENDC

	print "ARP Scanning Network for IPs\n"
	subprocess.call("sudo netdiscover -i eth0 -P -l /home/pi/WarBerry/resources/discover | grep -P -o \'([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+).*? ' | grep -P -o \'[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+' > /home/pi/WarBerry/Results/ips_discovered", shell = True)

	if os.stat('/home/pi/WarBerry/Results/ips_discovered').st_size !=0:
		discover = open("/home/pi/WarBerry/Results/ips_discovered","r")
		ips = discover.readlines()
		discover.close()

		discover = open("/home/pi/WarBerry/Results/ips_discovered", "r")
		print "Testing validity of %s IP(s)captured" % (sum(1 for _ in discover))
		discover.close()
		discover = open("/home/pi/WarBerry/Results/ips_discovered","w")

		for ip in ips:
			if ("192.168." or "172." or "10.") in ip:
				print bcolors.OKGREEN + "[+] %s is valid" %ip.strip() + bcolors.ENDC
				discover.write(ip)
			else:
				print bcolors.FAIL + "[-] %s is invalid" %ip.strip() + bcolors.ENDC

		discover.close()
		return(create_subnet())
	else:
		print bcolors.FAIL + "[-] No IPs captured! Exiting" + bcolors.ENDC
		return

def create_subnet():

	with open('/home/pi/WarBerry/Results/ips_discovered', 'r') as disc:
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
		with open('/home/pi/WarBerry/Results/CIDR', 'w') as netlength:
			netlength.write(CIDR)
		netlength.close()

	with open('/home/pi/WarBerry/Results/subnets', 'w') as subnets:
		with open('/home/pi/WarBerry/Results/ips_discovered', 'r') as ips:
			subs = ips.readlines()
			for sub in subs:
				subnets.write('.'.join(sub.split('.')[0:-1] ) + '.' + '\n')

	subprocess.call("sudo sort /home/pi/WarBerry/Results/subnets | uniq > /home/pi/WarBerry/Results/unique_subnets", shell = True)
	subprocess.call("sudo rm /home/pi/WarBerry/Results/subnets", shell=True)

	with open('/home/pi/WarBerry/Results/unique_subnets', 'r') as subnets:
		subs = subnets.readlines()
		for sub in subs:
			print bcolors.OKGREEN + "[+] Found subnet: %s" %sub.strip() + bcolors.ENDC

	return(set_static(CIDR))

def net_length(netmask):

        binary_str = ''
        for octet in netmask:
                binary_str += bin(int(octet))[2:].zfill(8)
        return str(len(binary_str.rstrip('0')))


def set_static(CIDR):
	length = CIDR.split('/')[1]

	bits = 0
	for i in xrange(32 - int(length), 32):
		bits |= (1 << i)
	netmask = "%d.%d.%d.%d" % ((bits & 0xff000000) >> 24, (bits & 0xff0000) >> 16, (bits & 0xff00) >> 8, (bits & 0xff))

	print "\nARP Scanning based on targetted CIDR\n"
	subprocess.call("sudo sort /home/pi/WarBerry/Results/CIDR | uniq > /home/pi/WarBerry/Results/unique_CIDR", shell=True)
	subprocess.call("sudo rm /home/pi/WarBerry/Results/CIDR", shell=True)
	subprocess.call("sudo netdiscover -i eth0 -P -l /home/pi/WarBerry/resources/discover | grep -P -o \'([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+).*? ' | grep -P -o \'[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+' > /home/pi/WarBerry/Results/used_ips", shell=True)

	with open('/home/pi/WarBerry/Results/avail_ips', 'w') as avail:
		with open('/home/pi/WarBerry/Results/unique_subnets', 'r') as subs:
			for sub in subs:
				for i in range(1, 255):
					avail.write(sub.strip() + str(i) + "\n")

	with open('/home/pi/WarBerry/Results/used_ips', 'r') as used:
		used_ips = used.readlines()
		with open('/home/pi/WarBerry/Results/statics', 'w') as statics:
			with open('/home/pi/WarBerry/Results/avail_ips', 'r') as avail_ips:
				for available in avail_ips:
					isUsed = False
					for used in used_ips:
						if ((available.strip() == used.strip()) and (isUsed == False)):
							print bcolors.FAIL + "[-] IP %s is in use, excluding from static list" % used.strip() + bcolors.ENDC
							isUsed = True
					if (isUsed == False):
						statics.write(available)

	with open('/home/pi/WarBerry/Results/statics') as static:
		total_frees = sum(1 for _ in static)
		if total_frees > 0:
			print bcolors.TITLE + '\n%s Available IPs to choose from.' % total_frees + bcolors.ENDC
		else:
			print bcolors.FAIL + "No free IPs Found\n" + bcolors.ENDC


	with open('/home/pi/WarBerry/Results/statics', 'r') as statics:
		line_count = (sum(1 for _ in statics))
		for i in range(0,line_count):
			newline = randint(0,line_count)

			static = linecache.getline('/home/pi/WarBerry/Results/statics', newline)
			print bcolors.WARNING + "[*] Attempting to set random static ip %s" % static.strip() + bcolors.ENDC
			subprocess.call(["ifconfig", "eth0", static.strip(), "netmask", netmask.strip()])

			for used in reversed(open('/home/pi/WarBerry/Results/used_ips').readlines()):
				print "[*] Pinging %s to ensure that we are live..." % used.strip()
				ping_response = subprocess.call(['ping', '-c', '5', '-W', '3', used.strip()],stdout=open(os.devnull, 'w'), stderr=open(os.devnull, 'w'))
				if ping_response == 0:
					print bcolors.OKGREEN + "[+] Success. IP %s is valid and %s is reachable" % (static.strip(), used.strip()) + bcolors.ENDC
					return static.strip()
				else:
					print bcolors.WARNING + "[-] Failed. IP %s is not valid" % static.strip() + bcolors.ENDC
			print "Attempting to bypass MAC Filtering\n"
			macbypass(unique_CIDR)



def macbypass(unique_CIDR):

	print bcolors.OKGREEN + "      [ MAC FILTERING BYPASS MODULE ]\n" + bcolors.ENDC

	print "ARP Scanning Network for MAC Addresses\n"
	subprocess.call("  grep -o -E /'([[:xdigit:]]{1,2}:){5}[[:xdigit:]]{1,2}/' > /home/pi/WarBerry/Results/macs_discovered" %unique_CIDR, shell = True)

	subprocess.call("sudo sort /home/pi/WarBerry/Results/macs_discovered | uniq > /home/pi/WarBerry/Results/unique_macs", shell=True)
	subprocess.call("sudo rm /home/pi/WarBerry/Results/macs_discovered", shell=True)
	with open('/home/pi/WarBerry/Results/unique_macs', 'r') as macs:
		if os.stat('/home/pi/WarBerry/Results/unique_macs').st_size != 0:
			print bcolors.OKGREEN + "%s uniue MACs Captured!" % ((sum(1 for _ in macs)))
		else:
			print bcolors.FAIL + "No MAC Addresses Captured. Exiting"


	with open('/home/pi/WarBerry/Results/unique_macs', 'r') as macs:
		for mac in macs:
			print bcolors.TITLE + "Attempting to change MAC Address to %s" %mac
			subprocess.call("sudo maccchanger --m %s") %mac
			for i in range(0, line_count):
				newline = randint(0, line_count)

				static = linecache.getline('/home/pi/WarBerry/Results/statics', newline)
				print bcolors.WARNING + "[*] Attempting to set random static ip %s" % static.strip() + bcolors.ENDC
				subprocess.call(["ifconfig", "eth0", static.strip(), "netmask", netmask.strip()])

				for used in reversed(open('/home/pi/WarBerry/Results/used_ips').readlines()):
					print "[*] Pinging %s to ensure that we are live..." % used.strip()
					ping_response = subprocess.call(['ping', '-c', '5', '-W', '3', used.strip()], stdout=open(os.devnull, 'w'), stderr=open(os.devnull, 'w'))
					if ping_response == 0:
						print bcolors.OKGREEN + "[+] Success. IP %s is valid and %s is reachable" % (static.strip(), used.strip()) + bcolors.ENDC
						return static.strip()
					else:
							print bcolors.FAIL + "Unable to bypass MAC Filtering. Exiting" + bcolors.ENDC

