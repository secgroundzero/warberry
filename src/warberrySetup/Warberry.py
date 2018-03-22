from src.warberrySetup.WarberryArgs import *
from src.warberrySetup.WarberryInformationGathered import *
from src.warberrySetup.WarberryStatus import *
from src.warberrySetup.WarberryDB import *
from src.utils.utils import *
from src.core.exploits.Responder import *
import time

import os,sys
import signal

class Warberry:

    def __init__(self,parser):
        self.status = WarberryStatus()
        start=int(time.time())
        #If not sudo
        if not os.geteuid() == 0:
            self.status.warberryFAIL("*** You are not running as root and some modules will fail ***\nRun again with sudo.")
            sys.exit(-1)

        dhcp_check(self.status)

        #Initialize arguments and information Gathering
        self.warberryArgs = WarberryArgs(parser)
        self.warberryInformationGathering = WarberryInformationGathered()
        
        #Execute Responder
        #if (self.warberryArgs.getMalicious == True):
        pid = subprocess.Popen(["sudo","python","run_responder.py",str(self.warberryArgs.getTime()),str(self.warberryArgs.getInterface())]) # call subprocess
        
        #Initialize the Database
        warberryDB = WarberryDB(self.warberryInformationGathering)
        warberryDB.insertSession()
    
        #Define Common Variables used within the Warberry Execution
        self.warberryInformationGathering.setNetmask(self.warberryArgs.getInterface())
        self.warberryInformationGathering.setInternalIP(self.warberryArgs.getInterface())
        self.warberryInformationGathering.setCIDR()
        self.warberryInformationGathering.setExternalIP()
        warberryDB.updateStatus("Completed Common Info gathering")
        
        if self.warberryInformationGathering.getInternalIP() is None:
            print("exit")
            exit
        else:
            warberryDB.updateElements(self.warberryInformationGathering)
            warberryDB.insertcommonWarInfo()
            self.warberryInformationGathering.pcap(self.status, self.warberryArgs.getInterface(),
                                                   self.warberryArgs.getPackets(), self.warberryArgs.getExpire())
            self.warberryInformationGathering.hostnames()
            warberryDB.updateElements(self.warberryInformationGathering)
            warberryDB.insertLiveIPS()
            warberryDB.updateStatus("Completed Scope Definition Module")
            warberryDB.insertHostnamesF()
            self.warberryInformationGathering.namechange(self.warberryArgs.getHostname(), self.warberryArgs.getName())

            if self.warberryArgs.getRecon() == False:
                self.warberryInformationGathering.scanning(self.status, self.warberryArgs.getIntensity(),
                                                       self.warberryArgs.getInterface(), self.warberryArgs.getQuick(), warberryDB)
                warberryDB.updateStatus("Completed Scanning Module")
                self.warberryInformationGathering.enumerate(self.status, self.warberryArgs.getEnumeration(), self.warberryArgs.getInterface(),warberryDB)
                self.warberryInformationGathering.bluetooth(self.status, self.warberryArgs.getBluetooth(),warberryDB)
                warberryDB.updateElements(self.warberryInformationGathering)
                warberryDB.insertBlues()
                self.warberryInformationGathering.wifi(self.status, self.warberryArgs.getWifi(),warberryDB)
                warberryDB.updateElements(self.warberryInformationGathering)
                warberryDB.insertWifis()
        

        FinishTime=start+int(self.warberryArgs.getTime())
        print ("Waiting for Responder ...")
        current=int (time.time())
        while (current<FinishTime):
            current=int(time.time())
    
        responderResults=Responder()
        hashes=responderResults.retrieveHashes()
        if (len(hashes)>0):
            warberryDB.saveHashes(hashes)

        warberryDB.updateEndTime()
        
        #p = subprocess.Popen(['ps', '-A'], stdout=subprocess.PIPE)
        #out, err = p.communicate()
        #for line in out.splitlines():
        #    if 'python' in line:
        #        pid = int(line.split(None, 1)[0])
#        os.kill(pid, signal.SIGKILL)



















