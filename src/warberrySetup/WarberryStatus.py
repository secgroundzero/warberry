from src.utils.console_colors import *


class WarberryStatus:

    def __init__(self):
        self.status = ""

    def updateStatus(self, str):
        self.status+=str

    def warberryHEADER(self, str):
        print (bcolors.HEADER + str + bcolors.ENDC)
        self.updateStatus(str)

    def warberryOKBLUE(self, str):
        print (bcolors.OKBLUE + str + bcolors.ENDC)
        self.updateStatus(str)

    def warberryOKGREEN(self, str):
        print (bcolors.OKGREEN + str + bcolors.ENDC)
        self.updateStatus(str)

    def warberryWARNING(self, str):
        print (bcolors.WARNING + str + bcolors.ENDC)
        self.updateStatus( str)

    def warberryFAIL(self, str):
        print (bcolors.FAIL + str + bcolors.ENDC)
        self.updateStatus(str)

    def warberryBOLD(self, str):
        print (bcolors.BOLD + str + bcolors.ENDC)
        self.updateStatus(str)

    def warberryTITLE(self, str):
        print (bcolors.TITLE + str + bcolors.ENDC)
        self.updateStatus(str)
