# WarBerryPi 
@sec_groundzero


![alt tag](https://github.com/secgroundzero/warberry/blob/master/Warberry_Logo_Transparent.png)


The **WarBerry** was built with one goal in mind; to be used in red teaming engagement where we want to obtain as much information 
as possible in a short period of time with being as stealth as possible. 
Just find a network port and plug it in. The scripts have been designed in a way that the approach is targeted to avoid noise 
in the network that could lead to detection and to be as efficient as possible. 
The WarBerry script is a collection of scanning tools put together to provide that functionality.


####Usage

To get a list of all options and switches use:

"sudo python warberry.py -h"

```
Parameters:
-h,  --help         [*] Print this help banner
-m,  --man          [*] Prints WarBerry's Man Page
-A,  --attack       [*] Run All Enumeration Scripts
-S,  --sniffer      [*] Run Sniffing Modules Only
-C,  --clear        [*] Clear Output Directories
-F,  --fulltcp      [*] Full TCP Port Scan
-T,  --toptcp       [*] Top Port Scan
-U,  --topudp       [*] Top UDP Port Scan

example usage: sudo python warberry.py -A
               sudo python warberry.py --attack
               sudo python warberry.py -C
```


#### Installation

Change the hostname of the RaspberryPi to **WarBerry**
- sudo nano /etc/hosts
- sudo nano /etc/hostname

Create a directory under /home/pi
-sudo mkdir WarBerry

Create the Results subdirectory in /WarBerry
- sudo mkdir Results
 
Download WarBerry by cloning the Git repository:
    sudo git clone https://github.com/secgroundzero/warberry.git


#### Dependencies

- sudo apt-get install nbtscan 
- sudo apt-get install python-scapy 
- sudo apt-get install tcpdump 
- sudo apt-get install nmap 
- sudo pip install python-nmap 
- sudo pip install ipaddress 
- sudo apt-get install ppp 
- sudo apt-get install sg3-utils 
- sudo apt-get install netdiscover 
- sudo apt-get install macchanger 

#### Extra Tools for Post Exploitation. Best to install in /home/pi/WarBerry/Tools/ directory

- sudo apt-get install onesixtyone
- sudo pip install ipaddress
- sudo apt-get install ppp
- sudo apt-get install sg3-utils
- sudo apt-get install macchanger
- sudo apt-get install nikto
- sudo apt-get install hydra
- sudo apt-get install john
- sudo apt-get install w3af-console
- sudo git clone https://github.com/stasinopoulos/commix.git 
- sudo git clone https://github.com/sqlmapproject/sqlmap.git 
- sudo git clone https://github.com/CoreSecurity/impacket.git

#### Aircrack Installation
- sudo apt-get -y install libssl-dev 
- sudo wget http://download.aircrack-ng.org/aircrack-ng-1.2-beta1.tar.gz 
- sudo tar -zxvf aircrack-ng-1.2-beta1.tar.gz 
- cd aircrack-ng-1.2-beta1 
- sudo make 
- sudo make install 
- sudo airodump-ng-oui-update 
- sudo apt-get -y install iw 
- sudo wget https://download.sysinternals.com/files/SysinternalsSuite.zip 
- sudo git clone https://github.com/samratashok/nishang.git 
- sudo git clone https://github.com/SpiderLabs/Responder.git 
- sudo git clone https://github.com/sophron/wifiphisher.git 
- sudo git clone https://github.com/DanMcInerney/net-creds.git 
- sudo git clone https://github.com/Dionach/CMSmap 
- sudo git clone https://github.com/PowerShellMafia/PowerSploit.git
