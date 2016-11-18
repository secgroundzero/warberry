## UPCOMING ADDITIONS

* Wireless Attacks
* Vlans enumeration
* Support for IPv6


## Version 4c1f

- Fixed a bug with nameservers enumeration

## Version 4c1e

- Mailowner works with all interfaces now
- Fixed a typo in the examples section
- Created a hall of fame page in the wiki for the contributors
- Create a page in the wiki for the conferences that the WarBerryPi was presented

## Version 4c1d

- Updated bootstrap for the subprocess32 installation
- Added for subnets in discover
- Added the mailowner python script

## Version 4c1c

- Added the mailowner module developed by thecarterb

## Version 4c1b

- Updated reporting package
- Timeout for robots.txt enumeration
- Updated bootstrap to include subprocess32 and pyrcap
- Added mailowner script

## Version 4c1a

- Fixed a bug in WAF enumeration
- Fixed a bug in SNMP enumeration
- Fied a bug in zone transfers
- Changed the services enumeration intensity


## Version 4c1

- Added a timeout for responder using the -t switch
- Fixed a bug in the zones enumeration
- Added robots.txt enumeration


## Version 4c

* Removed duplicate code
* Added VPN Aggressive mode scanning
* Added SMBclient & enum4linux installation
* Added Zone Transfer Enumeration
* Updated wiki & bootstrap 


## Version 4b

* Fixed an error in the output when interface is not available"
* Changed the way that interfaces are handled

## Version 4a

* nmap scans are now performed based on the interface chose at start
* various bug fixes
* bootstrap file update
* WiFi and Bluetooth scans are now optional


## Version 4

* Support for turning threads on and off
* Scan default profile changed for T4 to T1 for stealthiness
* New and improved folder layout
* Only active IPs are included in the scans reducing the network footprint
* Added Blackhat Arsenal 2016 Badge
* Bug fixes
* Enchancements of wiki pages 

## Version 3

* Bug fixes and experimentation with scapy
* Wiki Pages
* Reduced clutter in the README file

## VERSION 2.0b8 

* Catching exception when interface is down
* Added option to scan with or without threads 


## VERSION 2.0b7 

* Removed support for spoofing source IP
* Updated reporting module

## VERSION 2.0b6 beta

* Added support for spoofing source IP


## VERSION 2.0b6 

* Added thread support for all scans
* Added support for UDP Scanning
	- SQL Resolution Service
	- UPNP
	- RADIUS Authentication and Accounting messages


## VERSION 2.0b5 

* Revised reporting module

## VERSION 2.0b4 

* Added support for PJL Language Scanning
* Added support for vSphere Client Scanning
* Added support for Informix Server Scanning
* Added support for Informix Client Scanning
* Added support for H323 Scanning
* Added support for Lotus Notes Client Scanning
* Added more examples to the help menu
* Fixed nameserver enumeration errors output
* Fixed os enumeration errors output
* Added SIP Methods Enumeration
* Added SIP Users Enumeration
* Added Informix DB Enumeration
* Added Informix Tables Enumeration
* Added functionality to manually set hostname via -N

## VERSION 2.0b3 

* Added support for OS Fingerprint
* Changed bootstrap to include xprobe2
* Added SMB Domains enumeration scanning
* Added support for finger protocol scanning
* Added support for distcc daemon scanning
* Added support for webmin scanning


## VERSION 2.0b2 

* Support for ClamAV Scanning and Enumeration


## VERSION 2.0b1 

* Fixed Example usages


## VERSION 2.0b

* Added SAP scanning support 
* Added Oracle iSQL scanning support
* Added Java RMI Endpoint scan support


## VERSION 2.0a 

* Added Reporting Module
* Added rlogin, openvpn, ipsec, ldap, pop3, smtp support


## VERSION 2.0

* Added support for VOIP, rlogin, openvpn and IPSec scanning
* Added nearby Bluetooth devices scan
* Added optparse installation in README
* Changed menu to use optparse 
* Added support for granular attack
	- -r --recon        : This attack mode will only run the recon modules without performing any port scans
	- -i --interface    : Manually specify the interface to use. Default is eth0
	- -H --hostname     : Set this flag to disable changing the WarBerry's hostname during bypass modes
	- -p --packets      : Manually set the number of packets to capture. Default is 20 packets
	- -e --enumeration  : Set this flag to disable the enumeration scripts

* Added bootstrap script for automatic installation of dependencies
* Updated man pages
* No need to pass the attack type now. Default is -A --attack
* Enumeration flag is under bug testing



## VERSION 1.9 

* Added support for threaded network scans when using -A --attack

