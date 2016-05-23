import subprocess
import os, os.path
import sys, getopt
import socket
import fcntl
import struct
import re
import nmap
from socket import inet_aton
import socket


class bcolors:

    HEADER   =  '\033[95m'
    OKBLUE   =  '\033[34m'
    OKGREEN  =  '\033[32m'
    WARNING  =  '\033[93m'
    FAIL     =  '\033[31m'
    ENDC     =  '\033[0m'
    BOLD     =  '\033[1m'
    TITLE    =  '\033[96m'


def shares_enum():

        if os.path.isfile('/home/pi/WarBerry/Results/windows'):
                print " "
                print bcolors.OKGREEN + "      [ SMB SHARES ENUMERATION MODULE ]\n" + bcolors.ENDC
        else:
                return

        if os.path.isfile('/home/pi/WarBerry/Results/shares'):
                print bcolors.WARNING + "[!] Shares Results File Exists. Previous results will be overwritten\n" + bcolors.ENDC

        subprocess.call("sudo sort /home/pi/WarBerry/Results/windows | uniq > /home/pi/WarBerry/Results/win_hosts", shell=True)

        with open('/home/pi/WarBerry/Results/win_hosts', 'r') as hosts:

                for host in hosts:

                        print "[*] Enumerating shares on %s" %host.strip()
                        nm = nmap.PortScanner()
                        nm.scan(hosts=host, arguments='-Pn -T4 --script smb-enum-shares -p445 --open -o /home/pi/WarBerry/Results/shares')

        print bcolors.TITLE + "[+] Done! Results saved in /Results/shares/" + bcolors.ENDC

def smb_users():

        if os.path.isfile('/home/pi/WarBerry/Results/windows'):
                print " "
                print bcolors.OKGREEN + "      [ SMB USERS ENUMERATION MODULE ]\n" + bcolors.ENDC
        else:
                return
        if os.path.isfile('/home/pi/WarBerry/Results/smb_users'):
                print bcolors.WARNING + "[!] SMB Users Results File Exists. Previous Results will be Overwritten\n" +bcolors.ENDC

        subprocess.call("sudo sort /home/pi/WarBerry/Results/windows | uniq > /home/pi/WarBerry/Results/win_hosts", shell=True)

        with open('/home/pi/WarBerry/Results/win_hosts') as hosts:
                for host in hosts:
                        print "[*] Enumerating users on %s" %host.strip()
                        nm = nmap.PortScanner()
                        nm.scan(hosts=host, arguments='-Pn -T4 -sU -sS --script smb-enum-users -p U:137,T:139 --open -o /home/pi/WarBerry/Results/smb_users')

        print bcolors.TITLE + "[+] Done! Results saved in /Results/smb_users/" + bcolors.ENDC

def http_title_enum():

        print " "
        print bcolors.OKGREEN + "      [ HTTP TITLE ENUMERATION MODULE ]\n" + bcolors.ENDC

        subprocess.call("sudo cat /home/pi/WarBerry/Results/webserver* > /home/pi/WarBerry/Results/webs", shell = True)

        if os.path.isfile('/home/pi/WarBerry/Results/http_titles'):
                print bcolors.WARNING + "[!] HTTP Titles Results File Exists. Previous Results will be Overwritten\n " + bcolors.ENDC

        subprocess.call("sudo sort /home/pi/WarBerry/Results/webs | uniq > /home/pi/WarBerry/Results/web_hosts", shell=True)

        with open('/home/pi/WarBerry/Results/web_hosts') as webs:
                for host in webs:
                        print "[*] Enumerating HTTP Title on %s" %host.strip()
                        nm = nmap.PortScanner()
                        nm.scan(hosts=host, arguments='-Pn -T4 -sC -p80,8080,443,4443,8081,8181,9090 --open -o /home/pi/WarBerry/Results/http_titles')

        print bcolors.TITLE + "[+] Done! Results saved in /Results/http_titles/" + bcolors.ENDC

def waf_enum():

        if os.path.isfile('/home/pi/WarBerry/Results/webs'):
                print " "
                print bcolors.OKGREEN + "      [ WAF DETECTION MODULE ]\n" + bcolors.ENDC
        else:
                return
        if os.path.isfile('/home/pi/WarBerry/Results/wafed'):
                print bcolors.WARNING + "[!] WAF Results File Exists. Previous Results will be Overwritten\n " + bcolors.ENDC

        subprocess.call("sudo cat /home/pi/WarBerry/Results/webserver* > /home/pi/WarBerry/Results/webs", shell=True)
        subprocess.call("sudo sort /home/pi/WarBerry/Results/webs | uniq > /home/pi/WarBerry/Results/web_hosts", shell=True)
        with open('/home/pi/WarBerry/Results/web_hosts') as hosts:
                for host in hosts:
                        print "[*] Enumerating WAF on %s" %host.strip()
                        nm = nmap.PortScanner()
                        nm.scan(hosts=host, arguments='-Pn -T4 --script http-waf-detect -p80,8080,443,4443,8081,8181,9090 --open -o /home/pi/WarBerry/Results/wafed')

        print bcolors.TITLE + "[+] Done! Results saved in /Results/wafed/" + bcolors.ENDC

def nfs_enum():

        if os.path.isfile('/home/pi/WarBerry/Results/nfs'):
                print " "
                print bcolors.OKGREEN + "      [ NFS ENUMERATION MODULE ]\n" + bcolors.ENDC
        else:
                return
        if os.path.isfile('/home/pi/WarBerry/Results/nfs_enum'):
                print bcolors.WARNING + "[!] NFS Enum Results File Exists. Previous Pesults will be Overwritten\n " + bcolors.ENDC

        subprocess.call("sudo sort /home/pi/WarBerry/Results/nfs | uniq > /home/pi/WarBerry/Results/nfs_hosts", shell=True)
        with open('/home/pi/WarBerry/Results/nfs_hosts') as shares:
                for share in shares:
                        print "[*] Enumerating NFS Shares on %s" %share.strip()
                        nm = nmap.PortScanner()
                        nm.scan(hosts=share, arguments='-Pn -sV -T4 --script afp-showmount -p111 --open -o /home/pi/WarBerry/Results/nfs_enum')

        print bcolors.TITLE + "[+] Done! Results saved in /Results/nfs_enum/" + bcolors.ENDC

def mysql_enum():

        if os.path.isfile('/home/pi/WarBerry/Results/mysql'):
                print " "
                print bcolors.OKGREEN + "      [ MYSQL ENUMERATION MODULE ]\n" + bcolors.ENDC
        else:
                return
        if os.path.isfile('/home/pi/WarBerry/Results/mysql_enum'):
                print bcolors.WARNING + "[!] MYSQL Enum Results File Exists. Rrevious Results will be Overwritten\n " + bcolors.ENDC

        subprocess.call("sudo sort /home/pi/WarBerry/Results/mysql | uniq > /home/pi/WarBerry/Results/mysql_hosts", shell=True)
        with open('/home/pi/WarBerry/Results/mysql_hosts') as dbs:
                for db in dbs:
                        print "[*] Enumerating MYSQL DB on %s" %db.strip()
                        nm = nmap.PortScanner()
                        nm.scan(hosts=db, arguments='-Pn -T4 -sV --script mysql-enum -p3306 --open -o /home/pi/WarBerry/Results/mysql_enum')

        print bcolors.TITLE + "[+] Done! Results saved in /Results/mysql_enum/" + bcolors.ENDC

def mssql_enum():

        if os.path.isfile('/home/pi/WarBerry/Results/mssql'):
                print " "
                print bcolors.OKGREEN + "      [ MSSQL ENUMERATION MODULE ]\n" + bcolors.ENDC
        else:
                return
        if os.path.isfile('/home/pi/WarBerry/Results/mssql_enum'):
                print bcolors.WARNING + "[!] MSSQL Enum Results File Exists. Previous Results will be Overwritten\n " + bcolors.ENDC

        subprocess.call("sudo sort /home/pi/WarBerry/Results/mssql | uniq > /home/pi/WarBerry/Results/mssql_hosts", shell=True)
        with open('/home/pi/WarBerry/Results/mssql_hosts') as dbs:
                for db in dbs:
                        print "[*] Enumerating MSSQL DB on %s" %db.strip()
                        nm = nmap.PortScanner()
                        nm.scan(hosts=db, arguments='-Pn -T4 -sV --script ms-sql-info -p1433 --open -o /home/pi/WarBerry/Results/mssql_enum')

        print bcolors.TITLE + "[+] Done! Results saved in /Results/mssql_enum/" + bcolors.ENDC

def ftp_enum():

        if os.path.isfile('/home/pi/WarBerry/Results/ftp'):
                print " "
                print bcolors.OKGREEN + "      [ ANON FTP ENUMERATION MODULE ]\n" + bcolors.ENDC
        else:
                return
        if os.path.isfile('/home/pi/WarBerry/Results/ftp_enum'):
                print bcolors.WARNING + "[!] FTP Enum Results File Exists. Previous Results will be Overwritten\n " + bcolors.ENDC

        subprocess.call("sudo sort /home/pi/WarBerry/Results/ftp | uniq > /home/pi/WarBerry/Results/ftp_hosts", shell=True)
        with open('/home/pi/WarBerry/Results/ftp_hosts') as ftps:
                for ftp in ftps:
                        print "[*] Enumerating FTP on %s" %ftp.strip()
                        nm = nmap.PortScanner()
                        nm.scan(hosts=ftp, arguments='-Pn -T4 -sV --script ftp-anon -p22 --open -o /home/pi/WarBerry/Results/ftp_enum')

        print bcolors.TITLE + "[+] Done! Results saved in /Results/ftp_enum/" + bcolors.ENDC


def snmp_enum():

        if os.path.isfile('/home/pi/WarBerry/Results/snmp'):
                print " "
                print bcolors.OKGREEN + "      [ SNMP ENUMERATION MODULE ]\n" + bcolors.ENDC
        else:
                return
        if os.path.isfile('/home/pi/WarBerry/Results/snmp_enum'):
                print bcolors.WARNING + "[!] SNMP Enum Results File Exists. Previous Results will be Overwritten\n " + bcolors.ENDC

        subprocess.call("sudo sort /home/pi/WarBerry/Results/snmp | uniq > /home/pi/WarBerry/Results/snmp_hosts", shell=True)
        with open('/home/pi/WarBerry/Results/snmp_hosts') as snmps:
                for snmp in snmps:
                        print "[*] Enumerating SNMP on %s" %snmp.strip()
                        nm = nmap.PortScanner()
                        nm.scan(hosts=snmp, arguments='-Pn -T4 -sV -p161 --open -o /home/pi/WarBerry/Results/snmp_enum')

        print bcolors.TITLE + "[+] Done! Results saved in /Results/snmp_enum/" + bcolors.ENDC



def pcap_parser():

        if os.path.isfile('/home/pi/WarBerry/Results/capture.pcap'):
                print " "
                print bcolors.OKGREEN + "      [ PCAP CAPTURE PARSER MODULE ]\n" + bcolors.ENDC
        else:
                return

        if os.path.isfile('/home/pi/WarBerry/Results/pcap_results'):
                print bcolors.WARNING + "[!] PCAP Results File Exists. Previous Results will be Overwritten\n " + bcolors.ENDC

        print bcolors.TITLE + "[*] Looking for interesting data in /Results/capture.pcap\n" + bcolors.ENDC

        subprocess.call("sudo python /home/pi/WarBerry/Tools/net-creds/net-creds.py -p /home/pi/WarBerry/Results/capture.pcap > /home/pi/WarBerry/Results/pcap_results", shell = True)

        print bcolors.TITLE + "[+] Done! Results saved in /Results/pcap_results/\n" + bcolors.ENDC


def webs_prep():

        if os.path.isfile('/home/pi/WarBerry/Results/webservers80'):
                subprocess.call("sudo sort /home/pi/WarBerry/Results/webservers80 | uniq > /home/pi/WarBerry/Results/webservers80_hosts", shell=True)


        if os.path.isfile('/home/pi/WarBerry/Results/webservers443'):
                subprocess.call("sudo sort /home/pi/WarBerry/Results/webservers443 | uniq > /home/pi/WarBerry/Results/webservers443_hosts", shell=True)

        if os.path.isfile('/home/pi/WarBerry/Results/webservers8080'):
                subprocess.call("sudo sort /home/pi/WarBerry/Results/webservers8080 | uniq > /home/pi/WarBerry/Results/webservers8080_hosts", shell=True)


        if os.path.isfile('/home/pi/WarBerry/Results/webservers4443'):
                subprocess.call("sudo sort /home/pi/WarBerry/Results/webservers4443 | uniq > /home/pi/WarBerry/Results/webservers4443_hosts", shell=True)


        if os.path.isfile('/home/pi/WarBerry/Results/webservers8081'):
                subprocess.call("sudo sort /home/pi/WarBerry/Results/webservers8081 | uniq > /home/pi/WarBerry/Results/webservers8081_hosts", shell=True)


        if os.path.isfile('/home/pi/WarBerry/Results/webservers8181'):
                subprocess.call("sudo sort /home/pi/WarBerry/Results/webservers8181_hosts | uniq > /home/pi/WarBerry/Results/webservers8181_hosts", shell=True)


        if os.path.isfile('/home/pi/WarBerry/Results/webservers9090'):
                subprocess.call("sudo sort /home/pi/WarBerry/Results/webservers9090 | uniq > /home/pi/WarBerry/Results/webservers9090_hosts", shell=True)


def nikto_scan():

        print bcolors.OKGREEN + "      [ WEBSERVERS VULNERABILITY SCANNING MODULE ]\n" + bcolors.ENDC#

        if os.path.isfile('/home/pi/WarBerry/Results/webservers80_hosts'):
                with open('/home/pi/WarBerry/Results/webservers80_hosts') as sites:
                        hosts = sites.readlines()
                        for host in hosts:
                                subprocess.call('sudo nikto -h %s -port 80 -C all -o /home/pi/WarBerry/Results/%s_nikto_results.txt' %(host, host),shell = True)

        if os.path.isfile('/home/pi/WarBerry/Results/webservers443_hosts'):
                with open('/home/pi/WarBerry/Results/webservers443_hosts') as sites:
                        hosts = sites.readlines()
                        for host in hosts:
                                subprocess.call('sudo nikto -h %s -port 443 -C all -o /home/pi/WarBerry/Results/%s_nikto_results.txt' %(host, host),shell = True)

        if os.path.isfile('/home/pi/WarBerry/Results/webservers8080_hosts'):
                with open('/home/pi/WarBerry/Results/webservers8080_hosts') as sites:
                        hosts = sites.readlines()
                        for host in hosts:
                                subprocess.call('sudo nikto -h %s -port 8080 -C all -o /home/pi/WarBerry/Results/%s_nikto_results.txt' %(host, host),shell = True)

        if os.path.isfile('/home/pi/WarBerry/Results/webservers4443_hosts'):
                with open('/home/pi/WarBerry/Results/webservers4443_hosts') as sites:
                        hosts = sites.readlines()
                        for host in hosts:
                                subprocess.call('sudo nikto -h %s -port 4443 -C all -o /home/pi/WarBerry/Results/%s_nikto_results.txt' %(host, host),shell = True)

        if os.path.isfile('/home/pi/WarBerry/Results/webservers8081_hosts'):
                with open('/home/pi/WarBerry/Results/webservers8081_hosts') as sites:
                        hosts = sites.readlines()
                        for host in hosts:
                                subprocess.call('sudo nikto -h %s -port 8081 -C all -o /home/pi/WarBerry/Results/%s_nikto_results.txt' %(host, host),shell = True)

        if os.path.isfile('/home/pi/WarBerry/Results/webservers8181_hosts'):
                with open('/home/pi/WarBerry/Results/webservers8181_hosts') as sites:
                        hosts = sites.readlines()
                        for host in hosts:
                                subprocess.call('sudo nikto -h %s -port 8181 -C all -o /home/pi/WarBerry/Results/%s_nikto_results.txt' %(host, host),shell = True)

        if os.path.isfile('/home/pi/WarBerry/Results/webservers9090_hosts'):
                with open('/home/pi/WarBerry/Results/webservers9090_hosts') as sites:
                        hosts = sites.readlines()
                        for host in hosts:
                                subprocess.call('sudo nikto -h %s -port 9090 -C all -o /home/pi/WarBerry/Results/%s_nikto_results.txt' %(host, host),shell = True)

        else:
                print bcolors.WARNING + "No Webservers found\n" + bcolors.ENDC


def poison():

       print " "
       print bcolors.OKGREEN + "      [ POISON MODE ]\n" + bcolors.ENDC

       subprocess.call('sudo python /home/pi/WarBerry/Tools/Responder/Responder.py -I eth0', shell = True)




