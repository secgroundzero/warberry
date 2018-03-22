import sys,os
import subprocess
from src.utils.info_banners import *
class WarberryArgs:

    packets = False
    expire = False
    interface = False
    name = False
    intensity = False
    poison = False
    time = False
    quick = False
    hostname = False
    enumeration = False
    malicious = False
    bluetooth = False
    wifi = False
    recon = False
    clear = False
    man = False


    def getPackets(self):
        return self.packets

    def setPackets(self, p):
        self.packets = p

    def getExpire(self):
        return self.expire

    def setExpire(self,e):
        self.expire=e

    def getInterface(self):
        return self.interface

    def setInterface(self, i):
        if (os.path.isfile('/sys/class/net/'+i+'/carrier') == True):
            self.interface = i
        else:
            for ifaces in os.listdir("/sys/class/net/"):
                if ifaces[0] == "e":
                    file_iface=open("/sys/class/net/"+ifaces+"/carrier")
                    if file_iface.readline()[0] == "1":
                        self.interface = ifaces

        subprocess.call('clear', shell=True)
        banner()

    def getName(self):
        return self.name

    def setName(self, n):
        self.name = n

    def getIntensity(self):
        return self.intensity

    def setIntensity(self, i):
        self.intensity = i

    def getPoison(self):
        return self.poison

    def setPoison(self, p):
        self.poison=p

    def getTime(self):
        return self.time

    def setTime(self, t):
        self.time = t

    def getQuick(self):
        return self.quick

    def setQuick(self, q):
        self.quick=q

    def getHostname(self):
        return self.hostname

    def setHostname(self, h):
        self.hostname=h

    def getEnumeration(self):
        return self.enumeration

    def setEnumeration(self,e):
        self.enumeration = e

    def getMalicious(self):
        return self.malicous

    def setMalicious(self, m):
        self.malicious=m

    def getBluetooth(self):
        return self.bluetooth

    def setBluetooth(self, b):
        self.bluetooth = b

    def setRecon(self, r):
        self.recon=r

    def getRecon (self):
        return self.recon

    def setWifi(self, w):
        self.wifi=w

    def getWifi (self):
        return self.wifi

    def clearFunction(self):
        if (self.clear == True):
            subprocess.call('./empty.sh',shell=True);
            subprocess.call('./restore.sh',shell=True);
            sys.exit(0)

    def setClear(self, c):
        self.clear = c
        self.clearFunction()

    def getClear(self):
        return self.clear

    def setMan(self, s):
        self.man=s
        self.manualPage()

    def getMan(self):
        return self.man

    def manualPage(self):
        if (self.man == True):
            subprocess.call('clear', shell=True)
            banner_full()
            sys.exit(0)

    def __init__(self, parser):
        self.setPackets(parser.packets)
        self.setExpire(parser.expire)
        self.setInterface(parser.iface)
        self.setName(parser.name)
        self.setIntensity(parser.intensity)
        self.setPoison(parser.poison)
        self.setQuick(parser.fast)
        self.setHostname(parser.hostname)
        self.setEnumeration(parser.enum)
        self.setTime(parser.time)
        self.setMalicious(parser.malicious)
        self.setBluetooth(parser.btooth)
        self.setWifi(parser.wifi)
        self.setRecon(parser.reconmode)
        self.setClear(parser.clear)
        self.setMan(parser.manpage)




