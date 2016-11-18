import os, os.path
import subprocess
from src.utils.console_colors import *


def nbtscan(CIDR):

       print bcolors.OKGREEN + "      [ NAMESERVER ENUMERATION MODULE ]\n" + bcolors.ENDC

       subprocess.call('sudo nbtscan  %s 2>/dev/null > ../Results/nameservers' %CIDR , shell = True )
       subprocess.call("sudo cat ../Results/nameservers | awk {'print $2'} > ../Results/mvp_names", shell=True)

       print " "
       with open('../Results/nameservers', 'r') as nameservers:
            names = nameservers.read()
            print names