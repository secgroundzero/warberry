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

import subprocess
import os
import nmap
from src.utils.console_colors import bcolors
import urllib2



def shares_enum(iface):
        if os.path.isfile('../Results/windows'):
                print " "
                print bcolors.OKGREEN + "      [ SMB SHARES ENUMERATION MODULE ]\n" + bcolors.ENDC
        else:
                return "SMB SHARES DOES NOT EXIST!\n"
        if os.path.isfile('../Results/shares'):
                print bcolors.WARNING + "[!] Shares Results File Exists. Previous results will be overwritten\n" + bcolors.ENDC
        subprocess.call("sudo sort ../Results/windows | uniq > ../Results/win_hosts", shell=True)
        with open('../Results/win_hosts', 'r') as hosts:
                for host in hosts:
                        print bcolors.TITLE +"[*] " + bcolors.ENDC + "Enumerating shares on %s" %host.strip()
                        nm = nmap.PortScanner()
                        nm.scan(hosts=host, arguments='-Pn -T4 --script smb-enum-shares -p445 -e ' + iface + ' --open -o ../Results/shares')

        print bcolors.TITLE + "[+] Done! Results saved in /Results/shares" + bcolors.ENDC
        return "Completed Enumerating Shares\n"


def smb_users(iface):

        if os.path.isfile('../Results/windows'):
                print " "
                print bcolors.OKGREEN + "      [ SMB USERS ENUMERATION MODULE ]\n" + bcolors.ENDC
        else:
                return "SMB USERS ENUMERATION DOES NOT EXIST!\n"
        if os.path.isfile('../Results/smb_users'):
                print bcolors.WARNING + "[!] SMB Users Results File Exists. Previous Results will be Overwritten\n" +bcolors.ENDC
        subprocess.call("sudo sort ../Results/windows | uniq > ../Results/win_hosts", shell=True)
        with open('../Results/win_hosts') as hosts:
                for host in hosts:
                        print bcolors.TITLE + "[*] " + bcolors.ENDC + "Enumerating users on %s" %host.strip()
                        nm = nmap.PortScanner()
                        nm.scan(hosts=host, arguments='-Pn -T4 -sU -sS --script smb-enum-users -p U:137,T:139 -e ' + iface + ' --open -o ../Results/smb_users')

        print bcolors.TITLE + "[+] Done! Results saved in /Results/smb_users" + bcolors.ENDC
        return "Completed Enumerating Users\n"


def domains_enum(iface):

        if os.path.isfile('../Results/windows'):
                print " "
                print bcolors.OKGREEN + "      [ SMB DOMAINS ENUMERATION MODULE ]\n" + bcolors.ENDC
        else:
                return "SMB DOMAINS ENUMERATION MODULE NOT FOUND!\n"
        if os.path.isfile('../Results/domains_enum'):
                print bcolors.WARNING + "[!] SMB DOMAINS Results File Exists. Previous Results will be Overwritten\n" +bcolors.ENDC

        subprocess.call("sudo sort ../Results/windows | uniq > ../Results/win_hosts", shell=True)

        with open('../Results/win_hosts') as hosts:
                for host in hosts:
                        print bcolors.TITLE + "[*] " + bcolors.ENDC + "Enumerating domains on %s" %host.strip()
                        nm = nmap.PortScanner()
                        nm.scan(hosts=host, arguments='-Pn -T4 -sU -sS --script smb-enum-domains -p U:137,T:139 -e ' + iface + ' --open -o ../Results/domains_enum')

        print bcolors.TITLE + "[+] Done! Results saved in /Results/domains_enum" + bcolors.ENDC



def webs_prep():
        if (os.path.isfile('../Results/webservers80') or os.path.isfile('../Results/webservers8080')
            or os.path.isfile('../Results/webservers8181') or os.path.isfile('../Results/webservers443')
            or os.path.isfile('../Results/webservers4443')or os.path.isfile('../Results/webservers9090')
            or os.path.isfile('../Results/webhosts')):
                subprocess.call("sudo cat ../Results/webserver* > ../Results/webs", shell=True)


def nfs_enum(iface):

        if os.path.isfile('../Results/nfs'):
                print " "
                print bcolors.OKGREEN + "      [ NFS ENUMERATION MODULE ]\n" + bcolors.ENDC
        else:
                return "../Results/nfs file does not exist!\n"
        if os.path.isfile('../Results/nfs_enum'):
                print bcolors.WARNING + "[!] NFS Enum Results File Exists. Previous results will be Overwritten\n " + bcolors.ENDC

        subprocess.call("sudo sort ../Results/nfs | uniq > ../Results/nfs_hosts", shell=True)
        with open('../Results/nfs_hosts') as shares:
                for share in shares:
                        print bcolors.TITLE + "[*] " + bcolors.ENDC + "Enumerating NFS Shares on %s" %share.strip()
                        nm = nmap.PortScanner()
                        nm.scan(hosts=share, arguments='-Pn -sV -T4 --script afp-showmount -p111 -e ' + iface + ' --open -o ../Results/nfs_enum')

        print bcolors.TITLE + "[+] Done! Results saved in /Results/nfs_enum" + bcolors.ENDC
        return "Completed NFS Enumeration\n"

def mysql_enum(iface):

        if os.path.isfile('../Results/mysql'):
                print " "
                print bcolors.OKGREEN + "      [ MYSQL ENUMERATION MODULE ]\n" + bcolors.ENDC
        else:
                return "../Results/mysql file does not exist!\n"
        if os.path.isfile('../Results/mysql_enum'):
                print bcolors.WARNING + "[!] MYSQL Enum Results File Exists. Rrevious Results will be Overwritten\n " + bcolors.ENDC

        subprocess.call("sudo sort ../Results/mysql | uniq > ../Results/mysql_hosts", shell=True)
        with open('../Results/mysql_hosts') as dbs:
                for db in dbs:
                        print "[*] Enumerating MYSQL DB on %s" %db.strip()
                        nm = nmap.PortScanner()
                        nm.scan(hosts=db, arguments='-Pn -T4 -sV --script mysql-enum -p3306 -e ' + iface + ' --open -o ../Results/mysql_enum')

        print bcolors.TITLE + "[+] Done! Results saved in /Results/mysql_enum" + bcolors.ENDC
        return "Completed MYSQL Enumeration\n"

def mssql_enum(iface):

        if os.path.isfile('../Results/mssql'):
                print " "
                print bcolors.OKGREEN + "      [ MSSQL ENUMERATION MODULE ]\n" + bcolors.ENDC
        else:
                return "../Results/mssql file does not exist!\n"
        if os.path.isfile('../Results/mssql_enum'):
                print bcolors.WARNING + "[!] MSSQL Enum Results File Exists. Previous Results will be Overwritten\n " + bcolors.ENDC

        subprocess.call("sudo sort ../Results/mssql | uniq > ../Results/mssql_hosts", shell=True)
        with open('../Results/mssql_hosts') as dbs:
                for db in dbs:
                        print "[*] Enumerating MSSQL DB on %s" %db.strip()
                        nm = nmap.PortScanner()
                        nm.scan(hosts=db, arguments='-Pn -T4 -sV --script ms-sql-info -p1433 -e ' + iface + ' --open -o ../Results/mssql_enum')

        print bcolors.TITLE + "[+] Done! Results saved in /Results/mssql_enum" + bcolors.ENDC
        return "Completed MSSQL Enumeration\n"

def ftp_enum(iface):

        if os.path.isfile('../Results/ftp'):
                print " "
                print bcolors.OKGREEN + "      [ ANON FTP ENUMERATION MODULE ]\n" + bcolors.ENDC
        else:
                return "../Results/ftp file does not exist!\n"
        if os.path.isfile('../Results/ftp_enum'):
                print bcolors.WARNING + "[!] FTP Enum Results File Exists. Previous Results will be Overwritten\n " + bcolors.ENDC

        subprocess.call("sudo sort ../Results/ftp | uniq > ../Results/ftp_hosts", shell=True)
        with open('../Results/ftp_hosts') as ftps:
                for ftp in ftps:
                        print bcolors.TITLE + "[*] " + bcolors.ENDC + "Enumerating FTP on %s" %ftp.strip()
                        nm = nmap.PortScanner()
                        nm.scan(hosts=ftp, arguments='-Pn -T4 -sV --script ftp-anon -p22 -e ' + iface + ' --open -o ../Results/ftp_enum')

        print bcolors.TITLE + "[+] Done! Results saved in /Results/ftp_enum" + bcolors.ENDC
        return "Completed FTP Enumeration\n"

def snmp_enum(iface):

        if os.path.isfile('../Results/snmp'):
                print " "
                print bcolors.OKGREEN + "      [ SNMP ENUMERATION MODULE ]\n" + bcolors.ENDC
        else:
                return "../Results/snmp file does not exist!\n"
        if os.path.isfile('../Results/snmp_enum'):
                print bcolors.WARNING + "[!] SNMP Enum Results File Exists. Previous Results will be Overwritten\n " + bcolors.ENDC

        subprocess.call("sudo sort ../Results/snmp | uniq > ../Results/snmp_hosts", shell=True)
        with open('../Results/snmp_hosts') as snmps:
                for snmp in snmps:
                        print bcolors.TITLE + "[*] " + bcolors.ENDC + "Enumerating SNMP on %s" %snmp.strip()
                        nm = nmap.PortScanner()
                        nm.scan(hosts=snmp, arguments='-Pn -T4 -sV -sU -p161 -e ' + iface + ' --open -o ../Results/snmp_enum')

        print bcolors.TITLE + "[+] Done! Results saved in /Results/snmp_enum" + bcolors.ENDC
        return "Completed SNMP Enumeration\n"



def sip_methods_enum(iface):

        if os.path.isfile('../Results/voip'):
                print " "
                print bcolors.OKGREEN + "      [ SIP METHODS ENUMERATION MODULE ]\n" + bcolors.ENDC
        else:
                return "../Results/voip file does not exist!\n"
        if os.path.isfile('../Results/sip_methods'):
                print bcolors.WARNING + "[!] SIP Methods Results File Exists. Previous Results will be Overwritten\n " + bcolors.ENDC

        subprocess.call("sudo sort ../Results/voip | uniq > ../Results/voip_hosts", shell=True)
        with open('../Results/voip_hosts') as sips:
                for sip in sips:
                        print bcolors.TITLE + "[*] " + bcolors.ENDC + "Enumerating SIP Methods on %s" %sip.strip()
                        nm = nmap.PortScanner()
                        nm.scan(hosts=sip, arguments='-Pn -T4 --script sip-methods -sU -e ' + iface + ' -p 5060  -o ../Results/sip_methods')

        print bcolors.TITLE + "[+] Done! Results saved in /Results/sip_methods" + bcolors.ENDC
        return "Completed SIP Methods Enumeration\n"

def sip_users_enum(iface):

        if os.path.isfile('../Results/voip'):
                print " "
                print bcolors.OKGREEN + "      [ SIP USERS ENUMERATION MODULE ]\n" + bcolors.ENDC
        else:
                return "../Results/voip file does not exist!\n"
        if os.path.isfile('../Results/sip_users'):
                print bcolors.WARNING + "[!] SIP Users Results File Exists. Previous Results will be Overwritten\n " + bcolors.ENDC

        subprocess.call("sudo sort ../Results/voip | uniq > ../Results/voip_hosts", shell=True)
        with open('../Results/voip_hosts') as sips:
                for sip in sips:
                        print bcolors.TITLE + "[*] " + bcolors.ENDC + "Enumerating SIP Users on %s" %sip.strip()
                        nm = nmap.PortScanner()
                        nm.scan(hosts=sip, arguments='-Pn -T4 --script sip-enum-users -sU -e ' + iface + ' -p 5060  -o ../Results/sip_users')

        print bcolors.TITLE + "[+] Done! Results saved in /Results/sip_users" + bcolors.ENDC
        return "Completed SIP Users Enumeration\n"


