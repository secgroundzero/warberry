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

from src.utils.console_colors import *
import subprocess
import os, os.path
from src.utils.utils import *

def static_bypass(ifname):

	print bcolors.OKGREEN + "      [ STATIC IP SETUP MODULE ]\n" + bcolors.ENDC

	print "ARP Scanning Network for IPs\n"
	subprocess.call("sudo netdiscover -i %s -P -l ./src/discover | grep -P -o \'([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+).*? ' | grep -P -o \'[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+' > ../Results/ips_discovered" %ifname, shell = True)

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