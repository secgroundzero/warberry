from src.core.enumeration.ip_enum import *
from src.core.enumeration.network_packets import *
from src.core.enumeration.hostnames import *
from src.core.scanners.targetted_scanner import *
from src.core.scanners.thread_targetted_scanner import *
from src.core.enumeration.services_enum import *
from src.core.enumeration.bluetooth_enum import *
from src.core.enumeration.wifi_enum import *
from src.utils.utils import *
from src.utils.console_colors import *

class WarberryInformationGathered:

    IPsFound=""

    def __init__(self):
        self.int_ip=""
        self.netmask=""
        self.CIDR=""
        self.external_ip=""
        self.liveIPs=[]
        self.hostnamesF = {}
        self.scanners={}
        self.enumeration={}
        self.bluetooths=[]
        self.wifis=[]

    def getLiveIPS(self):
        return self.liveIPs
    
    def setInternalIP(self, iface):
        self.int_ip = iprecon(iface, self.netmask)

    def getInternalIP(self):
        return self.int_ip
    
    def setExternalIP(self):
        self.external_ip=external_IP_recon()
        if (self.external_ip==None):
            print(bcolors.WARNING + "[!] Could not reach the outside world. Possibly behind a firewall or some kind filtering\n" + bcolors.ENDC)
        else:
            print('[+] External IP obtained: ' + bcolors.OKGREEN + '%s\n' %self.external_ip + bcolors.ENDC)

    def getExternalIP(self):
        return self.external_ip

    def setNetmask(self,iface):
        self.netmask = netmask_recon(iface)

    def getNetmask(self):
        return self.netmask

    def setCIDR(self):
        self.CIDR=subnet(self.int_ip,self.netmask)

    def getCIDR(self):
        return self.CIDR

    def getWifis(self):
        return self.wifis

    def getBlues(self):
        return self.bluetooths

    def getHostnamesF(self):
        return self.hostnamesF

    def getScanners(self):
        return self.scanners

    def pcap(self,status, iface, packets, expire):
        sniffer(status, iface, packets, expire)

    def hostnames(self):
        warHostnames = Hostname()
        warHostnames.findHostnames(self.int_ip, self.CIDR)
        self.hostnamesF["ips"]=warHostnames.getIPsGathered()
        self.hostnamesF["os"]=warHostnames.getOSGathered()
        self.hostnamesF["domains"]=warHostnames.getDomainsGathered()
        self.hostnamesF["hostnamesGathered"]=warHostnames.getHostnamesGathered()
        self.liveIPs=warHostnames.getLiveIPS()

    def scanning(self,status, intensity, iface, quick, war_db):
        if quick == False:
            scanner = targettedScanner()
            scanner.single_port_scanner(self.CIDR, intensity, iface, self.liveIPs,war_db)
        else:
            scanner = ThreadPortScanner()
            session=war_db.getSession()
            self.scanners = scanner.thread_port_scanner(self.CIDR, intensity, iface, self.liveIPs,session)
        self.scanners = scanner.scanners
	print(bcolors.TITLE + "\n[+] Done! Results saved in warberry.db"  "\n" + bcolors.ENDC)
        war_db.updateStatus("Completed Port Scanning")
        status.warberryOKGREEN("Completed Port Scanning")
        

    def enumerate(self,status, enumeration,iface, war_db):
        session=war_db.getSession()
        if enumeration == False:
            if "Windows Hosts" in self.scanners:
                if len(self.scanners["Windows Hosts"]) > 0:
                    windows_set = set(self.scanners["Windows Hosts"])
                    self.scanners["Windows Hosts"] = list(windows_set)
                    self.enumeration["shares_enum"] = shares_enum(iface, self.scanners["Windows Hosts"])
                    status.warberryOKGREEN("Completed Enumerating Shares")
                    self.enumeration["smb_users_enum"]=smb_users(iface, self.scanners["Windows Hosts"])
                    war_db.updateStatus("Completed Enumerating Users")
                    status.warberryOKGREEN("Completed Enumerating Users")
            if "NFS" in self.scanners:
                if len(self.scanners["NFS"]) > 0:
                    nfs_set = set(self.scanners["NFS"])
                    self.scanners["NFS"] = list(nfs_set)
                    self.enumeration["nfs_enum"] = nfs_enum(iface, self.scanners["NFS"])
                    war_db.updateStatus("Completed NFS Enumeration")
                    status.warberryOKGREEN("Completed NFS Enumeration")
            if "MySQL Databases" in self.scanners:
                if len(self.scanners["MySQL Databases"]) > 0:
                    mysql_set = set(self.scanners["MySQL Databases"])
                    self.scanners["MySQL Databases"] = list(mysql_set)
                    self.enumeration["mysql_enum"] = mysql_enum(iface, self.scanners["MySQL Databases"])
                    war_db.updateStatus("Completed MySQL Enumeration")
            if "MSSQL Databases" in self.scanners:
                if len(self.scanners["MSSQL Databases"]) > 0:
                    mssql_set = set(self.scanners["MSSQL Databases"])
                    self.scanners["MSSQL Databases"] = list(mssql_set)
                    self.enumeration["mssql_enum"] = mssql_enum(iface, self.scanners["MSSQL Databases"])
                    war_db.updateStatus("Completed MSSQL Enumeration")
            if "SNMP" in self.scanners:
                if len(self.scanners["SNMP"]) > 0:
                    snmp_set = set(self.scanners["SNMP"])
                    self.scanners["SNMP_Unique"] = list(snmp_set)
                    self.enumeration["snmp_enum"] = snmp_enum(iface, self.scanners["SNMP_Unique"])
                    war_db.updateStatus("Completed SNMP Enumeration")
                    status.warberryOKGREEN("Completed SNMP Enumeration")
            if "FTP" in self.scanners:
                if len(self.scanners["FTP"]) > 0:
                    ftp_set = set(self.scanners["FTP"])
                    self.scanners["FTP"] = list(ftp_set)
                    self.enumeration["ftp_enum"] = ftp_enum(iface, self.scanners["FTP"])
                    war_db.updateStatus("Completed FTP Enumeration")
                    status.warberryOKGREEN("Completed FTP Enumeration")
            if "VOIP" in self.scanners:
                if len(self.scanners["VOIP"]) > 0:
                    voip_set = set(self.scanners["VOIP"])
                    self.scanners["VOIP"] = list(voip_set)
                    self.enumeration["sip_methods_enum"] = sip_methods_enum(iface, self.scanners["VOIP"])
                    status.warberryOKGREEN("Completed SIP Methods Enumeration")
                    self.enumeration["sip_users_enum"] = sip_users_enum(iface, self.scanners["VOIP"])
                    war_db.updateStatus("Completed VOIP Enumeration")
                    status.warberryOKGREEN("Completed VOIP Enumeration")
            webs=[]
            if ("Web Servers Running on Port 80" in self.scanners) and (len(self.scanners["Web Servers Running on Port 80"])>0):
                for h in self.scanners["Web Servers Running on Port 80"]:
                    webs.append(h.strip())
            if "Web Servers Running on Port 8080" in self.scanners and (len(self.scanners["Web Servers Running on Port 8080"])>0):
                for h in self.scanners["Web Servers Running on Port 8080"]:
                    webs.append(h.strip())
            if "Web Servers Running on Port 443" in self.scanners and (len(self.scanners["Web Servers Running on Port 443"])>0):
                for h in self.scanners["Web Servers Running on Port 443"]:
                    webs.append(h.strip())
            if "Web Servers Running on Port 4443" in self.scanners and (len(self.scanners["Web Servers Running on Port 4443"])>0):
                for h in self.scanners["Web Servers Running on Port 4443"]:
                    webs.append(h.strip())
            if "Web Servers Running on Port 8081" in self.scanners and (len(self.scanners["Web Servers Running on Port 8081"])>0):
                for h in self.scanners["Web Servers Running on Port 8081"]:
                    webs.append(h.strip())
            if "Web Servers Running on Port 8181" in self.scanners and (len(self.scanners["Web Servers Running on Port 8181"])>0):
                for h in self.scanners["Web Servers Running on Port 8181"]:
                    webs.append(h.strip())
            if "Web Servers Running on Port 9090" in self.scanners and (len(self.scanners["Web Servers Running on Port 9090"])>0):
                for h in self.scanners["Web Servers Running on Port 9090"]:
                    webs.append(h.strip())
            self.scanners["Webservers"]=webs
            if len(self.scanners["Webservers"])>0:
                webs_set = set(self.scanners["Webservers"])
                self.enumeration["Webservers_enum"] = list(webs_set)
#            print(self.enumeration)

    def bluetooth(self,status, blue,war_db):
        if blue == True:
            self.bluetooths = bluetooth_enum()
            war_db.updateStatus("Completed Bluetooth Scan")
            status.warberryOKGREEN("Completed Bluetooth Scan")

    def wifi(self,status, wif, war_db):
        if wif == True:
            self.wifis = wifi_enum()
            war_db.updateStatus("Completed WIFI networks scan")
            status.warberryOKGREEN("Completed WIFI networks scan")

    def namechange(self, hostnameOption, host_name):
        if (hostnameOption == True) and (host_name == 'WarBerry'):
            mvp_hosts = ['DEMO', 'DEV', 'PRINTER', 'BACKUP', 'DC', 'DC1', 'DC2']
            hostname = socket.gethostname()
            mvp_found = False
            mvps=[]
            hosts=self.hostnamesF["hostnamesGathered"]
            for host in hosts:
                for mvp in mvp_hosts:
                    if host.strip() == mvp.strip():
                        print (bcolors.OKGREEN + "\n[+] Found interesting hostname %s\n" % mvp.strip() + bcolors.ENDC)
                        mvps.append(host.strip())
                        mvp_found = True

            if mvp_found != True:
                print(bcolors.WARNING + "\n[-] No interesting names found. Continuing with the same hostname" + bcolors.ENDC)

            elif mvp_found == True:
		mvp_changed = False
                for mvp in mvps:
                    if mvp.strip() == hostname:
                        print(bcolors.TITLE + "[*] Hostname is stealthy as is. Keeping the same!" + bcolors.ENDC)
                    else:
			if mvp_changed == False:
				mvp_changed = True
                        	with open('/etc/hostname', 'w') as hostname:
                           		 hostname.write(mvp.strip())
                        	with open('/etc/hosts', 'w') as hosts:
                                    	print ("[*] Changing Hostname from " + bcolors.WARNING + socket.gethostname() + bcolors.ENDC + " to " + bcolors.OKGREEN + mvp + bcolors.ENDC)
                                    	hosts.write('127.0.0.1\tlocalhost\n::1\tlocalhost ip6-localhost ip6-loopback\nff02::1\tip6-allnodes\nff02::2\tip6-allrouters\n\n127.0.1.1\t%s' % mvp.strip())
					#hosts.write('127.0.0.1\tlocalhost.localdomain\tlocalhost ip6-localhost\n127.0.1.1\t%s' % mvp.strip())
					subprocess.call('hostname %s' %mvp.strip(),shell=True)
                                    	subprocess.call('sudo systemctl daemon-reload 2>/dev/null', shell=True)
                                    	subprocess.call('sudo /etc/init.d/hostname.sh 2>/dev/null', shell=True)
                                    	print ("[+] New hostname: " + bcolors.TITLE + socket.gethostname() + bcolors.ENDC)
				hosts.close()
				hostname.close()


