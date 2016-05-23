# WarBerryPi @sec_groundzero
WarBerryPi - Tactical Exploitation


The WarBerry was built with one goal in mind; to be used in red teaming engagement where we want to obtain as much information 
as possible in a short period of time with being as stealth as possible. 
Just find a network port and plug it in. The scripts have been designed in a way that the approach is targeted to avoid noise 
in the network that could lead to detection and to be as efficient as possible. 
The WarBerry script is a collection of scanning tools put together to provide that functionality.


USAGE:

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

