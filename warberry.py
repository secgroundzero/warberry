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
import sys, os
from src.utils.info_banners import *


def war(string):
    string = "sudo python wrapper.py " + string+" -P"
    print string
    subprocess.call(string, shell=True)

def main():

    war_arg_list=[]
    responder_time = 1000
    for i in range(1,len(sys.argv)):
        if sys.argv[i]=="-t" or sys.argv[i]=="-time":
            responder_time= sys.argv[i+1]
            break
        else:
            war_arg_list.append(sys.argv[i])
        if sys.argv[i]=="-I":
            iface = sys.argv[i+1]

    war_string = ' '.join(war_arg_list)
    pro= []
    # Spawn process for responder
    pid = subprocess.Popen(["sudo","python","run_responder.py",str(responder_time),str(iface)]) # call subprocess
    #start warberry
    war(war_string)
    #wait until responder finishes
    print bcolors.WARNING +"Waiting for Responder to finish!!!"+bcolors.ENDC
    pid.wait()
    print bcolors.TITLE+"Responder has Finished. Results in ../Results/responder_output"+bcolors.ENDC
    #atexit.register(cleanup(pid))


def cleanup(pid):
    if pid.poll():
        pid.terminate()

if __name__ == "__main__":
    # execute main function
    main()
