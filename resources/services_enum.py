# coding=utf-8
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

import os
import os.path
import subprocess

import nmap


class bcolors(object):
    HEADER = '\033[95m'
    OKBLUE = '\033[34m'
    OKGREEN = '\033[32m'
    WARNING = '\033[93m'
    FAIL = '\033[31m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    TITLE = '\033[96m'


def shares_enum():
    if os.path.isfile('../Results/windows'):
        print(" ")
        print(bcolors.OKGREEN + "      [ SMB SHARES ENUMERATION MODULE ]\n" + bcolors.ENDC)
    else:
        return

    if os.path.isfile('../Results/shares'):
        print(bcolors.WARNING + "[!] Shares Results File Exists. Previous results will be overwritten\n" + bcolors.ENDC)

    subprocess.call("sudo sort ../Results/windows | uniq > ../Results/win_hosts", shell=True)

    with open('../Results/win_hosts', 'r') as hosts:

        for host in hosts:
            print("[*] Enumerating shares on %s" % host.strip())
            nm = nmap.PortScanner()
            nm.scan(hosts=host, arguments='-Pn -T4 --script smb-enum-shares -p445 --open -o ../Results/shares')

    print(bcolors.TITLE + "[+] Done! Results saved in /Results/shares" + bcolors.ENDC)


def smb_users():
    if os.path.isfile('../Results/windows'):
        print(" ")
        print(bcolors.OKGREEN + "      [ SMB USERS ENUMERATION MODULE ]\n" + bcolors.ENDC)
    else:
        return
    if os.path.isfile('../Results/smb_users'):
        print(bcolors.WARNING + "[!] SMB Users Results File Exists. Previous Results will be Overwritten\n" + bcolors.ENDC)

    subprocess.call("sudo sort ../Results/windows | uniq > ../Results/win_hosts", shell=True)

    with open('../Results/win_hosts') as hosts:
        for host in hosts:
            print("[*] Enumerating users on %s" % host.strip())
            nm = nmap.PortScanner()
            nm.scan(hosts=host, arguments='-Pn -T4 -sU -sS --script smb-enum-users -p U:137,T:139 --open -o ../Results/smb_users')

    print(bcolors.TITLE + "[+] Done! Results saved in /Results/smb_users" + bcolors.ENDC)


def http_title_enum():
    print(" ")
    print(bcolors.OKGREEN + "      [ HTTP TITLE ENUMERATION MODULE ]\n" + bcolors.ENDC)

    subprocess.call("sudo cat ../Results/webserver* > ../Results/webs", shell=True)

    if os.path.isfile('../Results/http_titles'):
        print(bcolors.WARNING + "[!] HTTP Titles Results File Exists. Previous Results will be Overwritten\n " + bcolors.ENDC)

    subprocess.call("sudo sort ../Results/webs | uniq > ../Results/web_hosts", shell=True)

    with open('../Results/web_hosts') as webs:
        for host in webs:
            print("[*] Enumerating HTTP Title on %s" % host.strip())
            nm = nmap.PortScanner()
            nm.scan(hosts=host, arguments='-Pn -T4 -sC -p80,8080,443,4443,8081,8181,9090 --open -o ../Results/http_titles')

    print(bcolors.TITLE + "[+] Done! Results saved in /Results/http_titles" + bcolors.ENDC)


def waf_enum():
    if os.path.isfile('../Results/webs'):
        print(" ")
        print(bcolors.OKGREEN + "      [ WAF DETECTION MODULE ]\n" + bcolors.ENDC)
    else:
        return
    if os.path.isfile('../Results/wafed'):
        print(bcolors.WARNING + "[!] WAF Results File Exists. Previous Results will be Overwritten\n " + bcolors.ENDC)

    subprocess.call("sudo cat ../Results/webserver* > ../Results/webs", shell=True)
    subprocess.call("sudo sort ../Results/webs | uniq > ../Results/web_hosts", shell=True)
    with open('../Results/web_hosts') as hosts:
        for host in hosts:
            print("[*] Enumerating WAF on %s" % host.strip())
            nm = nmap.PortScanner()
            nm.scan(hosts=host, arguments='-Pn -T4 --script http-waf-detect -p80,8080,443,4443,8081,8181,9090 --open -o ../Results/wafed')

    print(bcolors.TITLE + "[+] Done! Results saved in /Results/wafed" + bcolors.ENDC)


def nfs_enum():
    if os.path.isfile('../Results/nfs'):
        print(" ")
        print(bcolors.OKGREEN + "      [ NFS ENUMERATION MODULE ]\n" + bcolors.ENDC)
    else:
        return
    if os.path.isfile('../Results/nfs_enum'):
        print(bcolors.WARNING + "[!] NFS Enum Results File Exists. Previous results will be Overwritten\n " + bcolors.ENDC)

    subprocess.call("sudo sort ../Results/nfs | uniq > ../Results/nfs_hosts", shell=True)
    with open('../Results/nfs_hosts') as shares:
        for share in shares:
            print("[*] Enumerating NFS Shares on %s" % share.strip())
            nm = nmap.PortScanner()
            nm.scan(hosts=share, arguments='-Pn -sV -T4 --script afp-showmount -p111 --open -o ../Results/nfs_enum')

    print(bcolors.TITLE + "[+] Done! Results saved in /Results/nfs_enum" + bcolors.ENDC)


def mysql_enum():
    if os.path.isfile('../Results/mysql'):
        print(" ")
        print(bcolors.OKGREEN + "      [ MYSQL ENUMERATION MODULE ]\n" + bcolors.ENDC)
    else:
        return
    if os.path.isfile('../Results/mysql_enum'):
        print(bcolors.WARNING + "[!] MYSQL Enum Results File Exists. Rrevious Results will be Overwritten\n " + bcolors.ENDC)

    subprocess.call("sudo sort ../Results/mysql | uniq > ../Results/mysql_hosts", shell=True)
    with open('../Results/mysql_hosts') as dbs:
        for db in dbs:
            print("[*] Enumerating MYSQL DB on %s" % db.strip())
            nm = nmap.PortScanner()
            nm.scan(hosts=db, arguments='-Pn -T4 -sV --script mysql-enum -p3306 --open -o ../Results/mysql_enum')

    print(bcolors.TITLE + "[+] Done! Results saved in /Results/mysql_enum" + bcolors.ENDC)


def mssql_enum():
    if os.path.isfile('../Results/mssql'):
        print(" ")
        print(bcolors.OKGREEN + "      [ MSSQL ENUMERATION MODULE ]\n" + bcolors.ENDC)
    else:
        return
    if os.path.isfile('../Results/mssql_enum'):
        print(bcolors.WARNING + "[!] MSSQL Enum Results File Exists. Previous Results will be Overwritten\n " + bcolors.ENDC)

    subprocess.call("sudo sort ../Results/mssql | uniq > ../Results/mssql_hosts", shell=True)
    with open('../Results/mssql_hosts') as dbs:
        for db in dbs:
            print("[*] Enumerating MSSQL DB on %s" % db.strip())
            nm = nmap.PortScanner()
            nm.scan(hosts=db, arguments='-Pn -T4 -sV --script ms-sql-info -p1433 --open -o ../Results/mssql_enum')

    print(bcolors.TITLE + "[+] Done! Results saved in /Results/mssql_enum" + bcolors.ENDC)


def ftp_enum():
    if os.path.isfile('../Results/ftp'):
        print(" ")
        print(bcolors.OKGREEN + "      [ ANON FTP ENUMERATION MODULE ]\n" + bcolors.ENDC)
    else:
        return
    if os.path.isfile('../Results/ftp_enum'):
        print(bcolors.WARNING + "[!] FTP Enum Results File Exists. Previous Results will be Overwritten\n " + bcolors.ENDC)

    subprocess.call("sudo sort ../Results/ftp | uniq > ../Results/ftp_hosts", shell=True)
    with open('../Results/ftp_hosts') as ftps:
        for ftp in ftps:
            print("[*] Enumerating FTP on %s" % ftp.strip())
            nm = nmap.PortScanner()
            nm.scan(hosts=ftp, arguments='-Pn -T4 -sV --script ftp-anon -p22 --open -o ../Results/ftp_enum')

    print(bcolors.TITLE + "[+] Done! Results saved in /Results/ftp_enum" + bcolors.ENDC)


def snmp_enum():
    if os.path.isfile('../Results/snmp'):
        print(" ")
        print(bcolors.OKGREEN + "      [ SNMP ENUMERATION MODULE ]\n" + bcolors.ENDC)
    else:
        return
    if os.path.isfile('../Results/snmp_enum'):
        print(bcolors.WARNING + "[!] SNMP Enum Results File Exists. Previous Results will be Overwritten\n " + bcolors.ENDC)

    subprocess.call("sudo sort ../Results/snmp | uniq > ../Results/snmp_hosts", shell=True)
    with open('../Results/snmp_hosts') as snmps:
        for snmp in snmps:
            print("[*] Enumerating SNMP on %s" % snmp.strip())
            nm = nmap.PortScanner()
            nm.scan(hosts=snmp, arguments='-Pn -T4 -sV -p161 --open -o ../Results/snmp_enum')

    print(bcolors.TITLE + "[+] Done! Results saved in /Results/snmp_enum" + bcolors.ENDC)


def pcap_parser():
    if os.path.isfile('../Results/capture.pcap'):
        print(" ")
        print(bcolors.OKGREEN + "      [ PCAP CAPTURE PARSER MODULE ]\n" + bcolors.ENDC)
    else:
        return

    if os.path.isfile('../Results/pcap_results'):
        print(bcolors.WARNING + "[!] PCAP Results File Exists. Previous Results will be Overwritten\n " + bcolors.ENDC)

    print(bcolors.TITLE + "[*] Looking for interesting data in /Results/capture.pcap\n" + bcolors.ENDC)

    subprocess.call("sudo python ../Tools/net-creds/net-creds.py -p ../Results/capture.pcap > ../Results/pcap_results", shell=True)

    print(bcolors.OKGREEN + "[+] Done! Results saved in /Results/pcap_results\n" + bcolors.ENDC)


def poison():
    print(" ")
    print(bcolors.OKGREEN + "      [ POISON MODE ]\n" + bcolors.ENDC)

    subprocess.call('sudo python Responder.py -I eth0', cwd=r'../Tools/Responder/', shell=True)
