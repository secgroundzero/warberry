import os, os.path 
import subprocess 
import nmap 
import threading 
import time

path_file=['../Results/windows','../Results/ftp', '../Results/mssql', '../Results/mysql', '../Results/oracle', '../Results/nfs', '../Results/webservers80','../Results/webservers443', '../Results/webservers8080','../Results/webservers4443','../Results/webservers8081', '../Results/webservers8181', '../Results/webservers9090','../Results/printers', '../Results/telnet', '../Results/mongo', '../Results/vnc', '../Results/dns', '../Results/phpmyadmin','../Results/tightvnc','../Results/websphere','../Results/firebird', '../Results/xserver', '../Results/svn', '../Results/snmp','../Results/voip','../Results/rlogin','../Results/openvpn','../Results/ipsec','../Results/ldap','../Results/pop3','../Results/smtp','../Results/sap_mgmt','../Results/sap_router','../Results/sap_gui','../Results/sap_icf','../Results/java_rmi','../Results/isql']

result_file = ['windows', 'ftp', 'mssql','mysql', 'oracle', 'nfs','webservers80', 'webservers443','webservers8080', 'webservers4443', 'webservers8081', 'webservers8181','webservers9090', 'printers','telnet', 'mongo', 'vnc', 'dns', 'phpmyadmin','tightvnc', 'websphere','firebird', 'xserver', 'svn', 'snmp','voip','rlogin','openvpn','ipsec','ldap','pop3','smtp','sap_mgmt','sap_router','sap_gui','sap_icf','java_rmi','isql']

message=["[*] You may want to check for open shares here\n", "[*] You may want to try log in as user ANONYMOUS\n", "[*] Default user for MSSQL installations is SA\n", "[*] Default creds for MYSQL are U:root P:blank\n", "[*] Default user on Oracle DBs are SYS, SYSTEM, SCOTT\n", "[*] You can view NFS contents by showmount -e <IP>\n", "","","","","","","","","","","","","","", "[*] Default logins for Websphere are U:system P:manager\n","[*] Default logins on Firebird DB are U:SYSDBA P:masterkey\n","","","","","","","","","","","","","","","",""]

name = ['Windows Hosts', 'FTP', 'MSSQL Databases','MySQL Databases', 'Oracle Databases', 'NFS','Web Servers 80', 'Web Servers 443','Web Servers 8080', 'Web Servers 4443','Web Servers 8081', 'Web Servers 8181','Web Servers 9090', 'Printers','Telnet', 'Mongo Databases', 'VNC','DNS', 'PHPMyAdmin','Tight VNC', 'IBM WebSphere','Firebird Databases', 'XServer', 'SVN Repositories','SNMP','VOIP','rLogin','OpenVPN','IPSec','LDAP','POP3','SMTP','SAP MGMT Console','SAP Router','SAP Web GUI','SAP ICF','Java RMI Endpoint','Oracle iSQL Login Page']

port=['445', '21', '1433', '3306', '1521', '111', '80', '443', '8080', '4443', '8081', '8181', '9090', '8611,8612,5222,5223', '23', '27017,27018,27019,28017', '5900', '53', '8089', '5800', '9443', '3050', '6000', '3690', '161','5060','513','1194','500','389','110','25','50013','3299','8000','8042','1099','5560']

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[34m'
    OKGREEN = '\033[32m'
    WARNING = '\033[93m'
    FAIL = '\033[31m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    TITLE = '\033[96m' 

class ScanThread(threading.Thread):
    def __init__(self,name, path_file,port, message, file,CIDR, intensity):
        threading.Thread.__init__(self)
        self.name = name
        self.path_file = path_file
        self.port=port
        self.message=message
        self.result_file=file
        self.CIDR=CIDR
        self.intensity=intensity
        self.output=""
    def run(self):
        file=self.path_file
        if os.path.isfile(file):
            self.output=self.output + bcolors.WARNING + "[!] " + bcolors.ENDC + self.name + " Results File Exists. New results will be appended\n"
        
        scan_targetted(self)
        return self.output

def scan_targetted(self):
    self.output=self.output+ "[+] Scanning for "+ self.name + " ..."
    scanning(self)
    if (os.path.isfile(self.path_file)):
        self.output = self.output + bcolors.TITLE + "\n[+] Done! Results saved in /Results/"+self.result_file+"\n" + bcolors.ENDC

def scanning(self):
    nm=nmap.PortScanner()
    arg= "-Pn -p"+self.port + " " + self.intensity + " --open"
    nm.scan(hosts=self.CIDR, arguments=arg)
    for host in nm.all_hosts():
        writeFile=self.path_file
        with open(writeFile, 'a') as hosts:
            self.output=self.output+ "\n----------------------------------------------------\n"
            hosts.write('%s\n' % host)
            self.output = self.output + bcolors.OKGREEN + "*** " + self.name + " Found : %s via port " %host + self.port + " ***" + bcolors.ENDC
            self.output = self.output +"\n"+bcolors.TITLE + self.message +  bcolors.ENDC

def scanner_thread(CIDR, intensity):
    
    print " "
    print bcolors.OKGREEN + " [ TARGETTED SERVICES NETWORK SCANNER MODULE ]\n" + bcolors.ENDC
    print "\n[*] Beginning Scanning Subnet %s with %s intensity" %(CIDR, intensity)
    print " "
    threads=[]
    for i in range(len(path_file)):
        t = ScanThread(name[i],path_file[i],port[i],message[i], result_file[i],CIDR,intensity)
        t.start()
        threads.append(t)
    for t in threads:
        t.join()
        print t.output

