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


class bcolors:

    HEADER   =  '\033[95m'
    OKBLUE   =  '\033[34m'
    OKGREEN  =  '\033[32m'
    WARNING  =  '\033[93m'
    FAIL     =  '\033[31m'
    ENDC     =  '\033[0m'
    BOLD     =  '\033[1m'
    TITLE    =  '\033[96m'


def banner():

        print bcolors.TITLE + ( '''
 _    _  ___  ____________ ___________________   __
| |  | |/ _ \ | ___ \ ___ \  ___| ___ \ ___ \ \ / /
| |  | / /_\ \| |_/ / |_/ / |__ | |_/ / |_/ /\ V /
| |/\| |  _  ||    /| ___ \  __||    /|    /  \ /
\  /\  / | | || |\ \| |_/ / |___| |\ \| |\ \  | |
 \/  \/\_| |_/\_| \_\____/\____/\_| \_\_| \_| \_/

            TACTICAL EXPLOITATION

v4.c1f                             @sec_groundzero
                           secgroundzero@gmail.com
''') + bcolors.ENDC


def banner_full():

        print bcolors.TITLE + ( '''
 _    _  ___  ____________ ___________________   __
| |  | |/ _ \ | ___ \ ___ \  ___| ___ \ ___ \ \ / /
| |  | / /_\ \| |_/ / |_/ / |__ | |_/ / |_/ /\ V /
| |/\| |  _  ||    /| ___ \  __||    /|    /  \ /
\  /\  / | | || |\ \| |_/ / |___| |\ \| |\ \  | |
 \/  \/\_| |_/\_| \_\____/\____/\_| \_\_| \_| \_/

[-] Warberry Usage [-]

Options:

  --version                             show program's version number and exit
  -h, --help                            show this help message and exit
  -a ATTACKTYPE, --attack=ATTACKTYPE    Attack Mode. Default: --attack
  -p PACKETS, --packets=PACKETS         Number of Network Packets to capture
  -I IFACE, --interface=IFACE           Network Interface to use. Default: eth0
  -N NAME, --name=NAME                  Hostname to use. Default: Auto
  -i INTENSITY, --intensity=INTENSITY   Port scan intensity. Default: T1
  -Q, --quick                           Scan using threads. Default: Off
  -P, --poison                          Turn Poisoning on/off. Default: On
  -t, --time                            Responder timeout time. Default: 900 seconds
  -H, --hostname                        Do not Change WarBerry hostname Default: Off
  -e, --enumeration                     Disable Enumeration mode. Default: Off
  -M, --malicious                       Enable Malicious only mode Default: Off
  -B, --bluetooth                       Enable Bluetooth Scanning. Default: Off
  -W, --wifi                            Enable WiFi Scanning. Default: Off
  -r, --recon                           Enable Recon only mode. Default: Off
  -S, --sniffer                         Enable Sniffer only mode. Default: Off
  -C, --clear                           Clear previous output folders in ../Results
  -m, --man                             Print WarBerry man pages


example usage: sudo python warberry.py -a -T                Attack all TCP Ports
               sudo python warberry.py --attack --topudp    Scan only the top udp ports
               sudo python warberry.py -r                   Use only the recon modules
               sudo python warberry.py -H -I wlan0          Use the wlan0 interface and dont change hostname
               sudo python warberry.py -I eth0 -i -T3       Use the eth0 interface and T3 scanning intensity
               sudo python warberry.py -I eth0 -N HackerPC  Use the eth0 interface and change hostname to HackerPC


''') + bcolors.ENDC


def banner_full_help():

        print bcolors.TITLE + ( '''
 _    _  ___  ____________ ___________________   __
| |  | |/ _ \ | ___ \ ___ \  ___| ___ \ ___ \ \ / /
| |  | / /_\ \| |_/ / |_/ / |__ | |_/ / |_/ /\ V /
| |/\| |  _  ||    /| ___ \  __||    /|    /  \ /
\  /\  / | | || |\ \| |_/ / |___| |\ \| |\ \  | |
 \/  \/\_| |_/\_| \_\____/\____/\_| \_\_| \_| \_/

[-] Warberry Man Page [-]

example usage: sudo python warberry.py -a -T                Attack all TCP Ports
               sudo python warberry.py --attack --toptcp    Scan only the top tcp ports
               sudo python warberry.py -r                   Use only the recon modules
               sudo python warberry.py -H -I wlan0          Use the wlan0 interface and dont change hostname
               sudo python warberry.py -I eth0 -i -T3       Use the eth0 interface and T3 scanning intensity
               sudo python warberry.py -I eth0 -N DC5       Use the eth0 interface and change hostname to DC5


FLAG SPECIFICATION
-------------------
-p --poison : This flag in ON by default. This means that after all the enumeration scripts are completed, Responder will
kick in and attempt to poison users to obtain credentials.

-r --recon : This flag is OFF by default. When this flag is set only the reconnaissance modules will run. This modules are:
. Internal IP recon
. Network sniffer. Default is a 20 packet capture but it can be changed with the -p parameter
. CIDR creation
. Network Names Scan
. Hostnames emumeration based on CIDR
. Change of hostname. The name will be changed accordingly by default based on the names capture. This can be turned off
    using this -H flag
. Nearby wifi enumeration

-i --intensity : Set the intensity of the scanning module. Accepted values are -T1,-T2,-T3,-T4
-H --hostname: This flag is OFF by default. When enabled, the hostname change will not be performed and the WarBerry will
    keep its initial hostname. The change is recommended for remaining hidden in the network.

-S --sniffer: When this flag is enabled only the network packet sniffer will run. Default is a 20 packet capture but
    it can be changed with the -p parameter

-I --interface : Set the interface for the scripts to run on. Default is eth0.

-a --attack : Set the attack mode. Default is -A. The modes are explained below.


-F, --fulltcp       [*] Full TCP Network Scan         [+] Performs a Full TCP Network Scan
-T, --toptcp        [*] Top Ports Network Scan        [+] Performs a scan on the top 1000 TCP Ports
-B, --tcpudp        [*] TCP & UDP Port Scan           [+] UDP Scan Network Scan


-A, --attack

This mode will run all enumeration scripts which consist of:

.DHCP Service Enumeration. This is only an informational script which checks if the DHCP
    service is running. If the service is running before we perfom basic tasks such as changing
    our hostname we might alert the Blue Teams of our presence.
. Internal IP recon. Verify if a valid internal IP is obtained. If not check the BYPASS section below.
    If yes then the CIDR for that IP is created.
. External IP recon. Check if a valid external IP is obtained.
. Sniffing module which sniffs network traffic and saves the results to /Results capture.pcap.
    This file can be used later on to extract useful information that was captured from the wire.
    The default number of network packets captured is 20. This can be change with the -s flag.
. PCAP Parser. This module parses the pcap file obtained before for any useful information.
. Hostnames enumeration. Scan for hostnames in the network
. Hostname change. This module parses the list of network names obtained and checks if they match any of the "interesting"
    names in our list. If so the hostname of the WarBerry is changed based on the first match found". This module runs
    by default but it can be switched off with the -H flag.
. Scanner module for the following services:

- Windows Machines                     - MongoDB Databases              - VOIP
- FTP                                  - VNC                            - rlogin
- MSSQL Databases                      - DNS                            - OpenVPN
- MYSQL Databases                      - PHPMyAdmin                     - IPSec
- Oracle Databases                     - TightVNC
- NFS                                  - IBM Websphere
- WebServers                           - Firebird Databases
- Printers                             - XServer
- SVN                                  - SNMP

. Enumeration Modules - This set of modules will attempt to enumerate the following based on the previous results:

- Windows open shares contents enumeration
- Windows users through SMB
- HTTP WebServers titles enumeration
- Web application firewalls
- NFS
- MYSQL
- MSSQL
- FTP
- SNMP

    The enumeration module will run by default. It can be turned off using the -e flag

. Nearby wifi networks enumeration.
    This is useful for phishing campaigns
. Nearby wifi networks enumeration
    This is useful for phishing campaigns
. Poisoning modules for credentials harvesting

All results from the scans are saved at ../Results


RESTRICTIONS BYPASS MODES
-------------------------

Static IP Bypass

MAC Address Filtering Bypass

NAC Filtering Bypass

''') + bcolors.ENDC


