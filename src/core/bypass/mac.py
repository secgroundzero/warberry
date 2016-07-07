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
import linecache
from random import randint
from src.core.bypass.nac import *
from src.core.bypass.static import *
from src.utils.console_colors import *
from src.utils.utils import *


def macbypass(unique_CIDR, ifname):

	print bcolors.OKGREEN + "      [ MAC FILTERING BYPASS MODULE ]\n" + bcolors.ENDC

	print "ARP Scanning Network for MAC Addresses\n"
	subprocess.call("sudo netdiscover -i %s -P -r  %s | grep -o -E /'([[:xdigit:]]{1,2}:){5}[[:xdigit:]]{1,2}/' > ../Results/macs_discovered" %(unique_CIDR,ifname), shell = True)

	subprocess.call("sudo sort ../Results/macs_discovered | uniq > ../Results/unique_macs", shell=True)
	subprocess.call("sudo rm ../Results/macs_discovered", shell=True)
	with open('../Results/unique_macs', 'r') as macs:
		if os.stat('../Results/unique_macs').st_size != 0:
			print bcolors.OKGREEN + "%s unique MACs Captured!" % ((sum(1 for _ in macs)))
			with open('../Results/unique_macs', 'r') as macs:
				for mac in macs:
					print bcolors.TITLE + "Attempting to change MAC Address to %s" % mac
					subprocess.call("sudo ifdown %s" % ifname, shell=True)
					subprocess.call("sudo macchanger -m %s %s" % (mac, ifname), shell=True)
					subprocess.call('sudo ifup %s' % ifname, shell=True)
					line_count = sum(1 for _ in macs)
					for i in range(0, line_count):
						newline = randint(0, line_count)
						static = linecache.getline('../Results/statics', newline)
						print bcolors.WARNING + "[*] Attempting to set random static ip %s" % static.strip() + bcolors.ENDC
						subprocess.call(["ifconfig", ifname, static.strip(), "netmask", netmask.strip()])


						for used in reversed(open('../Results/used_ips').readlines()):
							print "[*] Pinging %s to ensure that we are live..." % used.strip()
							ping_response = subprocess.call(['ping', '-c', '5', '-W', '3', used.strip()],
														stdout=open(os.devnull, 'w'), stderr=open(os.devnull, 'w'))
							if ping_response == 0:
								print bcolors.OKGREEN + "[+] Success. IP %s is valid and %s is reachable" % (static.strip(), used.strip()) + bcolors.ENDC
								return static.strip()

					print bcolors.FAIL + "Unable to bypass Filtering." + bcolors.ENDC
					return(nacbypass(unique_CIDR, ifname))
		else:
			print bcolors.FAIL + "No MAC Addresses Captured. Entering NAC Bypass. \n"
			return(nacbypass(unique_CIDR, ifname))



