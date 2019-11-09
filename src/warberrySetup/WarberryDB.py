import sqlite3
from src.warberrySetup.WarberryInformationGathered import *
import time
import subprocess

class WarberryDB:

    conn=""
    cursor=""
    elements=""
    session=""

    def __init__(self, informationG={}):
        self.conn = sqlite3.connect('warberry.db')
        self.cursor = self.conn.cursor()
        self.elements = informationG
    
    def connection(self):
        self.conn = sqlite3.connect('warberry.db')
        self.cursor = self.conn.cursor()
    
    def updateElements(self, informationG):
        self.elements=informationG
    
    def connectDB(self):
        self.conn = sqlite3.connect('warberry.db')
        self.cursor = self.conn.cursor()

    def getSession(self):
        return self.session
    
    def insertSession(self):
        start = int(time.time())
        subprocess.call("sudo cat /proc/cpuinfo | grep Revision | awk {'print $3'} > Results/model", shell=True)
	modelPI="Custom"
        with open('Results/model', 'r') as pi_model:
            for model in pi_model:
                modelPI=model.strip()
        subprocess.call("rm Results/model", shell=True)
        self.connectDB()
        db=(modelPI,)
        self.cursor.execute("SELECT * FROM warberry WHERE WarBerryModel=?;", db)
        result=self.cursor.fetchone()
        warberryID=result[0]
        self.conn.close()
        db_in=(warberryID, start)
        self.connectDB()
        self.cursor.execute('INSERT INTO warberry_session (WarberryID, WarberryStart) VALUES (?,?)', db_in)
        self.conn.commit()
        self.conn.close()
        self.connectDB()
        self.cursor.execute('SELECT * FROM warberry_session WHERE WarberryID=? AND WarberryStart=?', db_in)
        result = self.cursor.fetchone()
        self.session=result[0]

    def insertcommonWarInfo(self):

        internal_ip=self.elements.getInternalIP()
        CIDR=self.elements.getCIDR()
        netmask=self.elements.getNetmask()
        external_ip=self.elements.getExternalIP()
        session=self.session
        commonInfo = (session, CIDR, netmask, internal_ip, external_ip)
        self.connectDB()
        self.cursor.execute('INSERT INTO common_war_info (WarberrySession, CIDR, netmask,internal_IP, external_ip) VALUES (?,?,?,?,?)', commonInfo)
        self.conn.commit()
        self.conn.close()
    
    def insertLiveIPS(self):
        ips=self.elements.getLiveIPS()
        session=self.session
        for ip in ips:
            db_in=(session, ip)
            self.connectDB()
            self.cursor.execute('INSERT INTO war_ips (WarberrySession, ip) VALUES (?,?)', db_in)
            self.conn.commit()
            self.conn.close()

    def insertWifis(self):

        wifis=self.elements.getWifis()
        session=self.session
        for wifi in wifis:
            db_in=(session, wifi)
            self.connectDB()
            self.cursor.execute('INSERT INTO war_wifis (WarberrySession, wifiName) VALUES (?,?)', db_in)
            self.conn.commit()
            self.conn.close()

    def insertBlues(self):
        blues=self.elements.getBlues()
        session=self.session
        for blue in blues:
            blueName=blue["name"]
            blueDevice=blue["device"]
            db_in=(session, blueName, blueDevice)
            self.connectDB()
            self.cursor.execute('INSERT INTO war_blues (WarberrySession, blueName, blueDevice) VALUES (?,?,?)', db_in)
            self.conn.commit()
            self.conn.close()

    def insertHostnamesF(self):
        session=self.session
        hostnamesF=self.elements.getHostnamesF()
        if (len(hostnamesF)>0):
            #HostnamesGathered
            ips=hostnamesF["ips"]
            os=hostnamesF["os"]
            domains=hostnamesF["domains"]
            hostnames=hostnamesF["hostnamesGathered"]
            length = len(ips)
            # Write the results on stdout and DB
            for i in range(0, length):
                hostname=hostnames[i]
                hostname_IP=ips[i]
                hostname_os=os[i]
                hostname_domain=domains[i]
                db_in = (session, hostname, hostname_IP, hostname_os, hostname_domain)
                self.connectDB()
                self.cursor.execute('INSERT INTO war_hostnames(WarberrySession, hostname, hostname_IP, hostname_os, hostname_domain) VALUES (?,?,?,?,?)', db_in)
                self.conn.commit()
                self.conn.close()

    def insertScanner(self, service, host):
        session=self.session
        #scanners=self.elements.getScanners()
        #for key in scanners.keys():
        #if len(scanners[key])>0:
        #        for host in scanners[key]:
        db_in=(session, service, host)
        self.connectDB()
        self.cursor.execute('INSERT INTO war_scanners (WarberrySession, scannerName, host) VALUES (?,?,?)', db_in)
        self.conn.commit()
        self.conn.close()

    def insertScannerQ(self,session, service, host):
        db_in=(session, service, host)
        self.connectDB()
        self.cursor.execute('INSERT INTO war_scanners (WarberrySession, scannerName, host) VALUES (?,?,?)', db_in)
        self.conn.commit()
        self.conn.close()

    def updateStatus(self,status):
        session=self.session
        db_in=(status,session)
        self.connectDB()
        self.cursor.execute('UPDATE warberry_session SET WarberryStatus = ? WHERE WarberrySessionID = ?',db_in)
        self.conn.commit()
        self.conn.close()

    def updateEndTime(self):
        session=self.session
        status="Completed."
        db_in=(status, session)
        self.connectDB()
        self.cursor.execute('UPDATE warberry_session SET WarberryStatus = ? WHERE WarberrySessionID = ?',db_in)
        self.conn.commit()
        self.conn.close()
        self.connectDB()
        end = int(time.time())
        warberryID='1'
        db_in=(end, session)
        self.connectDB()
        self.cursor.execute('UPDATE warberry_session SET WarberryEnd = ? WHERE WarberrySessionID = ?',db_in)
        self.conn.commit()
        self.conn.close()

    def saveHashes(self,hashes):
        session=self.session
        length=len(hashes)
        for i in range(0,length):
            client=hashes[i]["Client"]
            username=hashes[i]["Username"]
            hash=hashes[i]["Hash"]
            db_in=(session,client, hash, username)
            self.connectDB()
            self.cursor.execute('INSERT INTO war_hashes (WarberrySession, client, hash, username) VALUES (?,?,?,?)', db_in)
            self.conn.commit()
            self.conn.close()





#def insertEnumeration(self):


