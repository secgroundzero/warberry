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
import os, os.path
import subprocess
import socket
from src.utils.console_colors import *
import struct
import linecache
import urllib2
from src.core.bypass.mac import *
from src.core.bypass.nac import *
from random import randint
import fcntl
from netaddr import *
from scapy.all import *

def dhcp_check():

    print bcolors.OKGREEN + "      [ DHCP SERVICE CHECK MODULE ]\n" + bcolors.ENDC

    dhcp_out = subprocess.check_output(['ps', '-A'])
    if "dhcp" in dhcp_out:
        status = bcolors.FAIL + "Running - Not Stealth" + bcolors.ENDC
        print "DHCP Service Status... %s\n" % status
    else:
        status = bcolors.OKGREEN + "Not Running - Stealth" + bcolors.ENDC
        print "DHCP Service Status... %s\n" %status


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


def set_static(CIDR, ifname):
	length = CIDR.split('/')[1]

	bits = 0
	for i in xrange(32 - int(length), 32):
		bits |= (1 << i)
	netmask = "%d.%d.%d.%d" % ((bits & 0xff000000) >> 24, (bits & 0xff0000) >> 16, (bits & 0xff00) >> 8, (bits & 0xff))

	print "\nARP Scanning based on targetted CIDR\n"
	subprocess.call("sudo sort ../Results/CIDR | uniq > ../Results/unique_CIDR", shell=True)
	subprocess.call("sudo rm ../Results/CIDR", shell=True)
	subprocess.call("sudo netdiscover -i %s -P -l ./src/discover | grep -P -o \'([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+).*? ' | grep -P -o \'[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+' > ../Results/used_ips" %ifname, shell=True)

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
			return(macbypass(CIDR, ifname))


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


def ip_validate(ip):
	ip_addr = IPAddress(ip)
	return not ip_addr.is_private() and not ip_addr.is_loopback() and not ip_addr.is_reserved() and not ip_addr.is_hostmask()


def net_length(netmask):

		binary_str = ''
		for octet in netmask:
			binary_str += bin(int(octet))[2:].zfill(8)
		return str(len(binary_str.rstrip('0')))


def netmask_recon(ifname):

		s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		int_ip =  socket.inet_ntoa(fcntl.ioctl(s.fileno(),0x8915, struct.pack('256s', ifname[:15]))[20:24])
		netmask = socket.inet_ntoa(fcntl.ioctl(socket.socket(socket.AF_INET, socket.SOCK_DGRAM), 35099, struct.pack('256s', ifname))[20:24])
		return netmask



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
                print '[+] External IP obtained: ' + bcolors.OKGREEN + '%s\n' %address + bcolors.ENDC
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
