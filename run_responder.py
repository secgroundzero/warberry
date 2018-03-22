"""
This file is part of the WarBerry tool.
Copyright (c) 2018 Yiannis Ioannides (@sec_groundzero).
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
import os, sys

def main():
    # delete responder_output file!!!
    if os.path.exists("Results/responder_output"):
        os.remove("Results/responder_output")
    # delete responder_outputERR file!!!
    if os.path.exists("Results/responder_outputERR"):
        os.remove("Results/responder_outputERR")
    stdout = open("Results/responder_output", "wb")
    stderr = open("Results/responder_outputERR", "wb")
    subprocess.call("sudo timeout "+ sys.argv[1]+ " python Tools/Responder/Responder.py -I "+sys.argv[2],shell=True,stdout=stdout,stderr=stderr)

if __name__ == "__main__":
    # execute main function
    main()
