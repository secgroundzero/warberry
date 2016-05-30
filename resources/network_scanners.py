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


import nmap
from socket import inet_aton
from banners import *
from services_enum import *


class bcolors:

    HEADER   =  '\033[95m'
    OKBLUE   =  '\033[34m'
    OKGREEN  =  '\033[32m'
    WARNING  =  '\033[93m'
    FAIL     =  '\033[31m'
    ENDC     =  '\033[0m'
    BOLD     =  '\033[1m'
    TITLE    =  '\033[96m'

def scanner_targetted(CIDR):

        print(" ")
        print(bcolors.OKGREEN + "      [ TARGETTED SERVICES NETWORK SCANNER MODULE ]\n" + bcolors.ENDC)

        if os.path.isfile('/home/pi/WarBerry/Results/windows'):
                print(bcolors.WARNING + "[!]" + bcolors.ENDC + " Windows Results File Exists. New results will be appended ")
        if os.path.isfile('/home/pi/WarBerry/Results/ftp'):
                print(bcolors.WARNING + "[!]" + bcolors.ENDC + " FTP Results File Exists. New results will be appended ")
        if os.path.isfile('/home/pi/WarBerry/Results/mssql'):
                print(bcolors.WARNING + "[!]" + bcolors.ENDC + " MSSQL Results File Exists. New results will be appended ")
        if os.path.isfile('/home/pi/WarBerry/Results/mysql'):
                print(bcolors.WARNING + "[!]" + bcolors.ENDC + " MYSQL Results File Exists. New results will be appended ")
        if os.path.isfile('/home/pi/WarBerry/Results/oracle'):
                print(bcolors.WARNING + "[!]" + bcolors.ENDC + " ORACLE Results File Exists. New results will be appended ")
        if os.path.isfile('/home/pi/WarBerry/Results/nfs'):
                print(bcolors.WARNING + "[!]" + bcolors.ENDC + " NFS Results File Exists. New results will be appended ")
        if os.path.isfile('/home/pi/WarBerry/Results/webservers'):
                print(bcolors.WARNING + "[!]" + bcolors.ENDC + " Web Servers Results File Exists. New results will be appended ")
        if os.path.isfile('/home/pi/WarBerry/Results/printers'):
                print(bcolors.WARNING + "[!]" + bcolors.ENDC + " Printers Results File Exists. New results will be appended ")
        if os.path.isfile('/home/pi/WarBerry/Results/mongo'):
                print(bcolors.WARNING + "[!]" + bcolors.ENDC + " MongoDB Results File Exists. New results will be appended ")
        if os.path.isfile('/home/pi/WarBerry/Results/telnet'):
                print(bcolors.WARNING + "[!]" + bcolors.ENDC + " Telnet Results File Exists. New results will be appended ")
        if os.path.isfile('/home/pi/WarBerry/Results/vnc'):
                print(bcolors.WARNING + "[!]" + bcolors.ENDC + " VNC Results File Exists. New results will be appended ")
        if os.path.isfile('/home/pi/WarBerry/Results/dns'):
                print(bcolors.WARNING + "[!]" + bcolors.ENDC + " DNS Results File Exists. New results will be appended ")
        if os.path.isfile('/home/pi/WarBerry/Results/phpmyadmin'):
                print(bcolors.WARNING + "[!]" + bcolors.ENDC + " PHPMyAdmin Results File Exists. New results will be appended ")
        if os.path.isfile('/home/pi/WarBerry/Results/tightvnc'):
                print(bcolors.WARNING + "[!]" + bcolors.ENDC + " TightVNC Results File Exists. New results will be appended ")
        if os.path.isfile('/home/pi/WarBerry/Results/websphere'):
                print(bcolors.WARNING + "[!]" + bcolors.ENDC + " IBM WebSphere Results File Exists. New results will be appended ")
        if os.path.isfile('/home/pi/WarBerry/Results/firebird'):
                print(bcolors.WARNING + "[!]" + bcolors.ENDC + " Firebird DB Results File Exists. New results will be appended ")
        if os.path.isfile('/home/pi/WarBerry/Results/xserver'):
                print(bcolors.WARNING + "[!]" + bcolors.ENDC + " XServer Results File Exists. New results will be appended ")
        if os.path.isfile('/home/pi/WarBerry/Results/svn'):
                print(bcolors.WARNING + "[!]" + bcolors.ENDC + " SVN Results File Exists. New results will be appended ")
        if os.path.isfile('/home/pi/WarBerry/Results/snmp'):
                print(bcolors.WARNING + "[!]" + bcolors.ENDC + " SNMP Results File Exists. New results will be appended ")

        print("\n[*] Beginning Scanning Subnet %s" % CIDR)
        print(" ")
        nm = nmap.PortScanner()

        print("[+] Scanning for Windows Hosts...")
        nm.scan(hosts=CIDR, arguments='-Pn -p445 -T4 --open')
        for host in nm.all_hosts():
                with open('/home/pi/WarBerry/Results/windows', 'a') as windows:
                        print('----------------------------------------------------')
                        print(bcolors.OKGREEN + ('   *** Windows Host Found : %s via port 445 ***' % (host)) + bcolors.ENDC)
                        print(bcolors.TITLE + "[*] You may want to check for open shares here\n" + bcolors.ENDC)
                        windows.write('%s\n' %host)

        print("[+] Scanning for FTP...")
        nm.scan(hosts=CIDR, arguments='-Pn -p21 -T4 --open')
        for host in nm.all_hosts():
                with open('/home/pi/WarBerry/Results/ftp', 'a') as ftp:
                        print('----------------------------------------------------')
                        print(bcolors.OKGREEN + ('   *** FTP Found : %s via port 21 ***' % (host)) + bcolors.ENDC)
                        print(bcolors.TITLE + "[*] You may want to try log in as user ANONYMOUS\n" + bcolors.ENDC)
                        ftp.write('%s\n' %host)

        print("[+] Scanning for MSSQL Databases...")
        nm.scan(hosts=CIDR, arguments='-Pn -T4 -p1433 --open')
        for host in nm.all_hosts():
                with open('/home/pi/WarBerry/Results/mssql', 'a') as mssql:
                        print('----------------------------------------------------')
                        print(bcolors.OKGREEN + ('   *** MSSQL DB Found : %s via port 1433 ***' % (host)) + bcolors.ENDC)
                        print(bcolors.TITLE + "[*] Default user for MSSQL installations is SA\n" + bcolors.ENDC)
                        mssql.write('%s\n'  %host)

        print("[+] Scanning for MySQL Databases...")
        nm.scan(hosts=CIDR, arguments='-Pn -T4 -p3306 --open')
        for host in nm.all_hosts():
                with open('/home/pi/WarBerry/Results/mysql', 'a') as mysql:
                        print('----------------------------------------------------')
                        print(bcolors.OKGREEN + ('   *** MYSQL DB Found : %s via port 3306 ***' % (host)) + bcolors.ENDC)
                        print(bcolors.TITLE + "[*] Default creds for MYSQL are U:root P:blank\n" + bcolors.ENDC)
                        mysql.write('%s\n'  %host)

        print("[+] Scanning for Oracle Databases...")
        nm.scan(hosts=CIDR, arguments='-Pn -T4 -p1521 --open')
        for host in nm.all_hosts():
                with open('/home/pi/WarBerry/Results/oracle', 'a') as oracle:
                        print('----------------------------------------------------')
                        print(bcolors.OKGREEN + ('   *** Oracle DB Found : %s via port 1521 ***' % (host)) + bcolors.ENDC)
                        print(bcolors.OKGREEN + ('   *** Oracle DB Found : %s via port 1521 ***' % (host)) + bcolors.ENDC)
                        print(bcolors.TITLE + "[*] Default user on Oracle DBs are SYS, SYSTEM, SCOTT\n" + bcolors.ENDC)
                        oracle.write('%s\n'  %host)

        print("[+] Scanning for NFS...")
        nm.scan(hosts=CIDR, arguments='-Pn -T4 -p111 --open')
        for host in nm.all_hosts():
                with open('/home/pi/WarBerry/Results/nfs', 'a') as nfs:
                        print('----------------------------------------------------')
                        print(bcolors.OKGREEN + ('   *** NFS Found : %s via port 111 ***' % (host)) + bcolors.ENDC)
                        print(bcolors.TITLE + "[*] You can view NFS contents by showmount -e <IP>\n" + bcolors.ENDC)
                        nfs.write('%s\n'  %host)

        print("[+] Scanning for Web Servers...")
        nm.scan(hosts=CIDR, arguments='-Pn -T4 -p80 --open')
        for host in nm.all_hosts():
                with open('/home/pi/WarBerry/Results/webservers80', 'a') as webservers80:
                        print('----------------------------------------------------')
                        print(bcolors.OKGREEN + ('   *** Web Server Found : %s via port 80 ***' % (host)) + bcolors.ENDC)
                        webservers80.write('%s\n'  %host)

        nm.scan(hosts=CIDR, arguments='-Pn -T4 -p443 --open')
        for host in nm.all_hosts():
                with open('/home/pi/WarBerry/Results/webservers443', 'a') as webservers443:
                        print('----------------------------------------------------')
                        print(bcolors.OKGREEN + ('   *** Web Server Found : %s via port 443 ***' % (host)) + bcolors.ENDC)
                        webservers443.write('%s\n'  %host)

        nm.scan(hosts=CIDR, arguments='-Pn -T4 -p8080 --open')
        for host in nm.all_hosts():
                with open('/home/pi/WarBerry/Results/webservers8080', 'a') as webservers8080:
                        print('----------------------------------------------------')
                        print(bcolors.OKGREEN + ('   *** Web Server Found : %s via port 8080 ***' % (host)) + bcolors.ENDC)
                        webservers8080.write('%s\n'  %host)

        nm.scan(hosts=CIDR, arguments='-Pn -T4 -p4443 --open')
        for host in nm.all_hosts():
                with open('/home/pi/WarBerry/Results/webservers4443', 'a') as webservers4443:
                        print('----------------------------------------------------')
                        print(bcolors.OKGREEN + ('   *** Web Server Found : %s via port 4443 ***' % (host)) + bcolors.ENDC)
                        webservers4443.write('%s\n'  %host)

        nm.scan(hosts=CIDR, arguments='-Pn -T4 -p8081 --open')
        for host in nm.all_hosts():
                with open('/home/pi/WarBerry/Results/webservers8081', 'a') as webservers8081:
                        print('----------------------------------------------------')
                        print(bcolors.OKGREEN + ('   *** Web Server Found : %s via port 8081 ***' % (host)) + bcolors.ENDC)
                        webservers8081.write('%s\n'  %host)

        nm.scan(hosts=CIDR, arguments='-Pn -T4 -p8181 --open')
        for host in nm.all_hosts():
                with open('/home/pi/WarBerry/Results/webservers8181', 'a') as webservers8181:
                        print('----------------------------------------------------')
                        print(bcolors.OKGREEN + ('   *** Web Server Found : %s via port 8181 ***' % (host)) + bcolors.ENDC)
                        webservers8181.write('%s\n'  %host)

        nm.scan(hosts=CIDR, arguments='-Pn -T4 -p9090 --open')
        for host in nm.all_hosts():
                with open('/home/pi/WarBerry/Results/webservers9090', 'a') as webservers9090:
                        print('----------------------------------------------------')
                        print(bcolors.OKGREEN + ('   *** Web Server Found : %s via port 9090 ***' % (host)) + bcolors.ENDC)
                        webservers9090.write('%s\n'  %host)

        print("[+] Scanning for Printers...")
        nm.scan(hosts=CIDR, arguments='-Pn -T4 -p8611,8612,5222,5223 --open')
        for host in nm.all_hosts():
                with open('/home/pi/WarBerry/Results/printers', 'a') as printers:
                        print('----------------------------------------------------')
                        print(bcolors.OKGREEN + ('   *** Printer Found : %s via port 8611/8612/5222/5223 ***' % (host)) + bcolors.ENDC)
                        printers.write('%s\n'  %host)

        print("[+] Scanning for Telnet...")
        nm.scan(hosts=CIDR, arguments='-Pn -T4 -p23 --open')
        for host in nm.all_hosts():
                with open('/home/pi/WarBerry/Results/telnet', 'a') as telnet:
                        print('----------------------------------------------------')
                        print(bcolors.OKGREEN + ('   *** Telnet Found : %s via port 23 ***' % (host)) + bcolors.ENDC)
                        telnet.write('%s\n' %host)

        print("[+] Scanning for Mongo Dababases...")
        nm.scan(hosts=CIDR, arguments='-Pn -T4 -p27017,27018,27019,28017 --open')
        for host in nm.all_hosts():
                with open('/home/pi/WarBerry/Results/mongo', 'a') as mongo:
                        print('----------------------------------------------------')
                        print(bcolors.OKGREEN + ('   *** Mongo Database Found : %s via port 27017/27018/27019/28017 ***' % (host)) + bcolors.ENDC)
                        mongo.write('%s\n' %host)

        print("[+] Scanning for VNC...")
        nm.scan(hosts=CIDR, arguments='-Pn -T4 -p5900 --open')
        for host in nm.all_hosts():
                with open('/home/pi/WarBerry/Results/vnc', 'a') as vnc:
                        print('----------------------------------------------------')
                        print(bcolors.OKGREEN + ('   *** VNC Service Found : %s via port 5900 ***' % (host)) + bcolors.ENDC)
                        vnc.write('%s\n' %host)

        print("[+] Scanning for DNS...")
        nm.scan(hosts=CIDR, arguments='-T4 -Pn -p53 --open')
        for host in nm.all_hosts():
                with open('/home/pi/WarBerry/Results/dns', 'a') as dns:
                        print('----------------------------------------------------')
                        print(bcolors.OKGREEN + ('   *** DNS Server Found : %s via port 53 ***' % (host)) + bcolors.ENDC)
                        dns.write('%s\n' %host)

        print("[+] Scanning for PHPMyAdmin...")
        nm.scan(hosts=CIDR, arguments='-T4 -Pn -p8089 --open')
        for host in nm.all_hosts():
                with open('/home/pi/WarBerry/Results/phpmyadmin', 'a') as phpmyadmin:
                        print('----------------------------------------------------')
                        print(bcolors.OKGREEN + ('   *** PHP My Admin Interface Found : %s via port 8089 ***' % (host)) + bcolors.ENDC)
                        phpmyadmin.write('%s\n' %host)

        print("[+] Scanning for TightVNC...")
        nm.scan(hosts=CIDR, arguments='-T4 -Pn -p5800 --open')
        for host in nm.all_hosts():
                with open('/home/pi/WarBerry/Results/tightvnc', 'a') as tightvnc:
                        print('----------------------------------------------------')
                        print(bcolors.OKGREEN + ('   *** TightVNC Viewer Found : %s via port 5800 ***' % (host)) + bcolors.ENDC)
                        tightvnc.write('%s\n' %host)

        print("[+] Scanning for IBM WebSphere...")
        nm.scan(hosts=CIDR, arguments='-T4 -Pn -p9443 --open')
        for host in nm.all_hosts():
                with open('/home/pi/WarBerry/Results/websphere', 'a') as websphere:
                        print('----------------------------------------------------')
                        print(bcolors.OKGREEN + ('   *** IBM WebSphere Found : %s via port 9443 ***' % (host)) + bcolors.ENDC)
                        print(bcolors.ENDC + "[*] Default logins for Websphere are U:system P:manager" + bcolors.ENDC)
                        websphere.write('%s\n' %host)

        print("[+] Scanning for Firebird Databases...")
        nm.scan(hosts=CIDR, arguments='-T4 -Pn -p3050 --open')
        for host in nm.all_hosts():
                with open('/home/pi/WarBerry/Results/firebird', 'a') as firebird:
                        print('----------------------------------------------------')
                        print(bcolors.OKGREEN + ('   *** Firebird DB Found : %s via port 3050 ***' % (host)) + bcolors.ENDC)
                        print(bcolors.TITLE + "[*] Default logins on Firebird DB are U:SYSDBA P:masterkey" + bcolors.ENDC)
                        firebird.write('%s\n' %host)

        print("[+] Scanning for XServer...")
        nm.scan(hosts=CIDR, arguments='-T4 -Pn -p6000 --open')
        for host in nm.all_hosts():
                with open('/home/pi/WarBerry/Results/xserver', 'a') as xserver:
                        print('----------------------------------------------------')
                        print(bcolors.OKGREEN + ('   *** XServer Found : %s via port 6000 ***' % (host)) + bcolors.ENDC)
                        xserver.write('%s\n' %host)

        print("[+] Scanning for SNV Repositories...")
        nm.scan(hosts=CIDR, arguments='-T4 -Pn -p3690 --open')
        for host in nm.all_hosts():
                with open('/home/pi/WarBerry/Results/svn', 'a') as svn:
                        print('----------------------------------------------------')
                        print(bcolors.OKGREEN + ('   *** SNV Repositoriy Found : %s via port 3690 ***' % (host)) + bcolors.ENDC)
                        svn.write('%s\n' % host)

        print("[+] Scanning for SNMP...")
        nm.scan(hosts=CIDR, arguments='-T4 -Pn -p161 --open')
        for host in nm.all_hosts():
                with open('/home/pi/WarBerry/Results/snmp', 'a') as snmp:
                        print('----------------------------------------------------')
                        print(bcolors.OKGREEN + ('   *** SNMP Found : %s via port 161 ***' % (host)) + bcolors.ENDC)
                        snmp.write('%s\n' % host)


def scanner_full(CIDR):

        print(bcolors.OKGREEN + "      [ TCP/UDP NETWORK SCANNER MODULE ]\n" + bcolors.ENDC)

        if os.path.isfile('/home/pi/WarBerry/Results/tcp_udp_scan'):
                print(bcolors.WARNING + "[!] TCP/UDP Results File Exists. Previous Results will be Overwritten " + bcolors.ENDC)

        print("Beginning Scanning Subnet %s" % CIDR)

        print(" ")
        nm = nmap.PortScanner()

        print("[+] Scanning TCP/UDP Ports in all hosts...")
        nm.scan(hosts=CIDR, arguments='-Pn -T4 -sT -sU --open -o /home/pi/WarBerry/Results/tcp_udp_scan')
        for host in nm.all_hosts():
                print('----------------------------------------------------')




def scanner_tcp_full(CIDR):

        print(bcolors.OKGREEN + "      [ FULL TCP NETWORK SCANNER MODULE ]\n" + bcolors.ENDC)

        if os.path.isfile('/home/pi/WarBerry/Results/tcp_full'):
                print(bcolors.WARNING + "[!] Full TCP Results File Exists. Previous Results will be Overwritten" + bcolors.ENDC)

        print("Beginning Scanning Subnet %s" % CIDR)

        print(" ")
        nm = nmap.PortScanner()

        print("[+] Scanning All TCP Ports in all hosts...")
        nm.scan(hosts=CIDR, arguments='-Pn -T4 -p1-65535 --open -o /home/pi/WarBerry/Results/tcp_full')
        for host in nm.all_hosts():
                print('----------------------------------------------------')
                print(host + nm[host].hostname() + " open TCP ports: ")
                for proto in nm[host].all_protocols():
                        lport = nm[host][proto].keys()
                        lport.sort()
                for port in lport:
                        print(bcolors.OKGREEN + ' [+] ' + bcolors.ENDC + '%s' % port)


def scanner_top(CIDR):

        print(bcolors.OKGREEN + "      [ TOP TCP PORTS NETWORK SCANNER MODULE ]\n" + bcolors.ENDC)

        if os.path.isfile('/home/pi/WarBerry/Results/top_tcp'):
                print(bcolors.WARNING + "[!] Top TCP Ports Results File Exists. Previous Results will be Overwritten" + bcolors.ENDC)

        print("Beginning Scanning Subnet %s" % CIDR)
        print(" ")
        nm = nmap.PortScanner()

        print("[+] Scanning TOP 1000 TCP Ports in all hosts...")
        nm.scan(hosts=CIDR, arguments='-Pn -T4 --top-ports 1000 --open -o /home/pi/WarBerry/Results/tcp_top')
        for host in nm.all_hosts():
                print('----------------------------------------------------')
                print(host + nm[host].hostname() + " open TCP ports: ")
                for proto in nm[host].all_protocols():
                        lport = nm[host][proto].keys()
                        lport.sort()
                for port in lport:
                        print(bcolors.OKGREEN + ' [+] ' + bcolors.ENDC + '%s' % port)

