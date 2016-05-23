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

v1.2                              @sec_groundzero

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

Parameters:
-h,  --help         [*] Print this help banner
-m,  --man          [*] Prints WarBerry's Man Page
-A,  --attack       [*] Run All Enumeration Scripts
-S,  --sniffer      [*] Run Sniffing Modules Only
-C,  --clear        [*] Clear Output Directories
-F,  --fulltcp      [*] Full TCP Port Scan
-T,  --toptcp       [*] Top Port Scan
-B,  --tcpudp       [*] Top TCP & UDP Port Scan

example usage: sudo python warberry.py -A
               sudo python warberry.py --attack
               sudo python warberry.py -C

[*] Parameter selection is mandatory

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

-A,  --attack       [*] Run All Enumeration Scripts   

This module will run all enumeration scripts which consist of:

1) DHCP Service Enumeration. This is only an informational script which checks if the DHCP
service is running. If the service is running before we perfom basic tasks such as changing 
our hostname we might alert the Blue Teams of our presense.

1) Sniffing module which sniffs network traffic and saves the results to /Results capture.pcap. 
This file can be used later on to extract usefull information that was captured from the wire.

2) NBT Scan - Netbios Scanner which scans the network for advertised NETBIOS names. This is used
to change the hostname of the WarBerry in order to not look suspicious inside the network as 
the name will resemble other machines in the netowork.

3) IP Enumeration module. This script will check to see if after we have changed our hostname and 
started the DHCP service we have a valid IP. If we dont it will attempt to obtain a valid IP by
observing the range of the network and setting the WarBerry's IP to a free one statically. If this
does not success the script will proceed by observing the MAC addresses inside the network and begin
mimicin one by one until the WarBerry obtains a valid IP. 


4) Nmap scans - This module will perform scans to enumerate for the following:

- Windows Machines                     - MongoDB Databases
- FTP                                  - VNC
- MSSQL Databases                      - DNS
- MYSQL Databases                      - PHPMyAdmin
- Oracle Databases                     - TightVNC
- NFS                                  - IBM Websphere
- WebServers                           - Firebird Databases
- Printers                             - XServer
- SVN                                  - SNMP

5) Enumeration Modules - This set of modules will attempt to enumerate the following based on the previous results:

- Windows open shares contents enumeration
- Windows users through SMB
- HTTP WebServers titles enumeration

[*] IP Configuration & Setup

The first phase of the enumeration begins by checking if the DHCP Service is running as described in [1]. After the
initial network reconnaisance is performed the WarBerry attempts to enable the DHCP service and obtain an IP through
this method. If the IP is found not to be a valid internal IP then the WarBerry enumerates IPs by observing network
packets and builds the CIDR based on those IP. The script then performs a scan to find which host is down in order to
set a static IP of one host that is down and once again checks if the IP is valid. The script will go through the entire
list of unused IPs found and check if any of those will work. If none of the IPs work then the script proceeds by
enumerating all MAC addresses in the network and attempts to change its own MAC to one of those in order to bypass
any MAC filtering in place. The script goes through the entire list of MAC addresses found and checks if any of those
MAC addresses allow the WarBerry to obtain a valid internal IP.

-S,  --sniffer      [*] Run Sniffing Modules Only     [+] Network packet sniffer for a predefined number of packets and exits
[*] Change the number of packets in warberry.py accordingly - Default=20

-C, --clear         [*] Clear Output Directories      [+] Clears all previous results output directories

-F, --fulltcp       [*] Full TCP Network Scan         [+] Performs a Full TCP Network Scan

-T, --toptcp        [*] Top Ports Network Scan        [+] Performs a scan on the top 1000 TCP Ports

-B, --tcpudp        [*] TCP & UDP Port Scan           [+] UDP Scan Network Scan

All results from the scans are saved at /home/pi/WarBerry/Results



''') + bcolors.ENDC


