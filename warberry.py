#!/usr/bin/python
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
logging.info("finished")
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
import urllib,urllib2
import re
import httplib
from scapy.all import *
import nmap
from socket import inet_aton
import socket
import json
from urllib import urlopen
import ftplib
#External modules
from banners import *
from network_scanners import *
from services_enum import *
from rest_bypass import *

class bcolors:

    HEADER   =  '\033[95m'
    OKBLUE   =  '\033[34m'
    OKGREEN  =  '\033[32m'
    WARNING  =  '\033[93m'
    FAIL     =  '\033[31m'
    ENDC     =  '\033[0m'
    BOLD     =  '\033[1m'
    TITLE    =  '\033[96m'


def main(argv):
        if argv == '-h' or argv == '--help':
            subprocess.call('clear', shell = True)
            banner_full()
        elif argv == '-m' or argv == '--man':
            subprocess.call('clear', shell = True)
            banner_full_help()
        elif argv== '-A' or argv == '--attack':
            subprocess.call('clear', shell = True)
            banner()
            if not os.geteuid() == 0:
                print bcolors.FAIL + '*** You are not running as root and some modules may fail ***. Run again with sudo. \n' + bcolors.ENDC
            dhcp_check()
            int_ip = iprecon('eth0')
            if (int_ip==None):
                exit
            else:
                netmask = netmask_recon('eth0')
                external_IP_recon()
                sniffer()
                pcap_parser()
                CIDR = subnet(int_ip, netmask)
                hostnames(CIDR)
                nbtscan(CIDR)
                scanner_targetted(CIDR)
                shares_enum()
                smb_users()
                http_title_enum()
                nfs_enum()
                waf_enum()
                mysql_enum()
                mssql_enum()
                ftp_enum()
                snmp_enum()
                wifi_scan()
                print ""
                print bcolors.TITLE + "All scripts completed. Check the /Results directory" + bcolors.ENDC
                print " "
                poison()
		
        elif argv == '-T' or argv == '--toptcp':
            subprocess.call('clear', shell = True)
            banner()
            int_ip = internal_IP_recon('eth0')
            netmask = netmask_recon('eth0')
            print external_IP_recon()
            CIDR = subnet(int_ip, netmask)
            scanner_top(CIDR)
            print bcolors.TITLE + "All scripts completed. Check the /Results directory" + bcolors.ENDC
        elif argv == '-B' or argv == '--tcpudp':
            subprocess.call('clear', shell = True)
            banner()
            int_ip = internal_IP_recon('eth0')
            netmask = netmask_recon('eth0')
            print external_IP_recon()
            CIDR = subnet(int_ip, netmask)
            scanner_full(CIDR)
            print bcolors.TITLE + "All scripts completed. Check the /Results directory" + bcolors.ENDC
        elif argv == '-F' or argv == '--fulltcp':
            subprocess.call('clear', shell = True)
            banner()
            int_ip = internal_IP_recon('eth0')
            netmask = netmask_recon('eth0')
            print external_IP_recon()
            CIDR = subnet(int_ip, netmask)
            scanner_tcp_full(CIDR)
            print bcolors.TITLE + "All scripts completed. Check the /Results directory" + bcolors.ENDC
        elif argv == '-S' or argv == '--sniffer':
            subprocess.call('clear', shell = True)
            sniffer()
        elif argv == '-C' or argv == '--clear':
            clear_output()
        elif argv == ' ':
            subprocess.call('clear', shell = True)
            banner()
        else:
            print bcolors.WARNING + "[!] Invalid Module Selected. Use -h or --help for the help function\n" + bcolors.ENDC



def dhcp_check():

	print bcolors.OKGREEN + "      [ DHCP SERVICE CHECK MODULE ]\n" + bcolors.ENDC

	dhcp_out = subprocess.check_output(['ps', '-A'])
	if "dhcp" in dhcp_out:
		status = bcolors.FAIL + "Running - Not Stealth" + bcolors.ENDC
	else:
		status = bcolors.OKGREEN + "Not Running - Stealth" + bcolors.ENDC

        print "DHCP Service Status... %s\n" %status

def iprecon(ifname):

        print bcolors.OKGREEN + "      [ IP ENUMERATION MODULE ]\n" + bcolors.ENDC

        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        int_ip =  socket.inet_ntoa(fcntl.ioctl(s.fileno(),0x8915, struct.pack('256s', ifname[:15]))[20:24])
        netmask = socket.inet_ntoa(fcntl.ioctl(socket.socket(socket.AF_INET, socket.SOCK_DGRAM), 35099, struct.pack('256s', ifname))[20:24])

        if ("192." or "172." or "10.") in int_ip:
                print '[+] Internal IP obtained on %s:' %ifname + bcolors.OKGREEN + " %s" %int_ip + bcolors.ENDC + ' netmask ' + bcolors.OKGREEN + '%s' %netmask + bcolors.ENDC
                return int_ip
        else:
                print bcolors.FAIL + "[!] Invalid IP obtained." + bcolors.ENDC + " Checking if we can bypass with static IP.\n"
                return (static_bypass())



def netmask_recon(ifname):

        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        int_ip =  socket.inet_ntoa(fcntl.ioctl(s.fileno(),0x8915, struct.pack('256s', ifname[:15]))[20:24])
        netmask = socket.inet_ntoa(fcntl.ioctl(socket.socket(socket.AF_INET, socket.SOCK_DGRAM), 35099, struct.pack('256s', ifname))[20:24])

        return netmask



def net_length(netmask):

        binary_str = ''
        for octet in netmask:
                binary_str += bin(int(octet))[2:].zfill(8)
        return str(len(binary_str.rstrip('0')))


def subnet(int_ip, netmask):

        ipaddr = int_ip.split('.')
        netmask = netmask.split('.')


        net_start = [str(int(ipaddr[x]) & int(netmask[x]))
             for x in range(0,4)]

        CIDR =  '.'.join(net_start) + '/' + net_length(netmask)
        return CIDR


def external_IP_recon():

        try:
                site = urllib2.urlopen("http://checkip.dyndns.org/", timeout = 1)
                url = site.read()
                grab = re.findall('([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+)', url)
                address = grab[0]
                print 'External IP obtained: ' + bcolors.OKGREEN + '%s\n' %address + bcolors.ENDC
        except:
                print bcolors.WARNING + "[!] Could not reach the outside world. Possibly behind a firewall or some kind filtering\n" + bcolors.ENDC
		return


def clear_output():

        yes = set(['yes','y', ''])
        no = set(['no','n'])

        choice = raw_input(bcolors.WARNING + "[!] " + bcolors.ENDC + "You are about to delete all previous results. Do you want to continue? y/n: ")
        #choice = raw_input().lower()
        if choice in yes:
		work_path = '/home/pi/WarBerry/Results/'
		if os.listdir(work_path)!=[]:
    			subprocess.call('sudo rm -rf /home/pi/WarBerry/Results/* ', shell = True)
                	print bcolors.WARNING + '[*] All previous results in /home/pi/WarBerry/Results removed' + bcolors.ENDC
		else:
			print  bcolors.WARNING + '[*] No previous results found' + bcolors.ENDC

        elif choice in no:
                print bcolors.OKGREEN + "[-] Results files left intact" + bcolors.ENDC
        else:
                sys.stdout.write("Please respond with 'y/yes' or 'n/no'\n")



def sniffer():

        print " "
        packet_count = 20
        pcap_location = "/home/pi/WarBerry/Results/capture.pcap"
        print bcolors.OKGREEN + "      [ NETWORK SNIFFING MODULE ]\n" + bcolors.ENDC
        print "Sniffer will begin capturing %d packets" %packet_count #Change the count number accordingly
        packets = sniff(iface="eth0", count= packet_count)
        wrpcap(pcap_location, packets)
        print bcolors.OKGREEN + "[+] Capture Completed." + bcolors.ENDC + " PCAP File Saved at " + bcolors.OKGREEN + "%s!\n" %pcap_location + bcolors.ENDC


def wifi_scan():

    subprocess.call("sudo rm /home/pi/WarBerry/Results/model", shell=True)
    subprocess.call("sudo cat /proc/cpuinfo | grep Revision | awk {'print $3'} > /home/pi/WarBerry/Results/model", shell=True)

    with open('/home/pi/WarBerry/Results/model', 'r') as pi_model:
        for model in pi_model:
            if model.strip() == "a02082":
                print " "
                print bcolors.OKGREEN + "      [ Wi-Fi ENUMERATION MODULE ]\n" + bcolors.ENDC

                subprocess.call("sudo iwlist wlan0 scan | grep ESSID | awk {'print $1'} > /home/pi/WarBerry/Results/wifis", shell = True)
                with open('/home/pi/WarBerry/Results/wifis', 'r') as wifis:
                    if os.stat('/home/pi/WarBerry/Results/wifis').st_size != 0:
                        for wifi in wifis:
                            print bcolors.OKGREEN + "[+] Found Wireless Network: %s" %wifi.strip() + bcolors.ENDC
                    else:
                        print bcolors.WARNING + "[-] No Wireless Networks Captured" + bcolors.ENDC

            else:
                return


def nbtscan(CIDR):

       print " "
       print bcolors.OKGREEN + "      [ NAMESERVER ENUMERATION MODULE ]\n" + bcolors.ENDC

       subprocess.call('sudo nbtscan -r %s > /home/pi/WarBerry/Results/nameservers' %CIDR , shell = True )
       print " "
       with open('/home/pi/WarBerry/Results/nameservers', 'r') as nameservers:
            names = nameservers.read()
            print names

if __name__ == '__main__':

        #try:
         main(sys.argv[1])
        #except:
                #subprocess.call('clear', shell = True)
                #banner_full()
                #print "errror"
