#!/usr/bin/env bash

##
## WarBerry bootstrap script
## Ver. 1.0.0
##

APT_GET_CMD=$(which apt-get)
WARBERRYDIR=/home/pi/WarBerry
GITREPOS=("https://github.com/DanMcInerney/net-creds.git"
          "https://github.com/stasinopoulos/commix.git"
          "https://github.com/sqlmapproject/sqlmap.git"
          "https://github.com/CoreSecurity/impacket.git"
          "https://github.com/samratashok/nishang.git"
          "https://github.com/SpiderLabs/Responder.git"
          "https://github.com/sophron/wifiphisher.git"
          "https://github.com/Dionach/CMSmap.git"
          "https://github.com/PowerShellMafia/PowerSploit.git"
          "https://github.com/offensive-security/exploit-database.git")

echo """

        STARTING WarBerry INSTALLATION SCRIPT...
"""

if [ "$(id -u)" != "0" ]; then
	echo "ERROR: Sorry, you are not root. Run this script as root or with sudo."
	exit 1
fi

echo "CREATING DIRECTORIES..."
mkdir -p $WARBERRYDIR/{Results,Tools}

if [[ ! -z $APT_GET_CMD ]]; then
    echo """
        PERFORMING BASIC DEPENDENCIES INSTALLATION...
    """
    apt-get -y update;
    apt-get -y install nbtscan   \
                    curl         \
                    tcpdump      \
                    nmap         \
                    ppp          \
                    sg3-utils    \
                    netdiscover  \
                    macchanger   \
                    onesixtyone  \
                    nikto        \
                    hydra        \
                    john         \
                    w3af-console \
                    python-dev   \
                    python-pip   \
                    cryptcat     \
                    ike-scan     \
                    libssl-dev   \
                    make         \
                    g++          \
                    iw           \
		    xprobe2      \
		    bridge-utils \
                    ettercap-text-only;

    echo """
        BOOTSTRAPPING PYTHON UTILS...
    """
    pip install --upgrade pip;

    echo """
        INSTALLING PYTHON PACKAGES...
    """
    pip2 install scapy python-nmap ipaddress netaddr optparse-pretty pybluez;

    echo """
        CLONING GIT PACKAGES TO WarBerry/Tools directory...
    """
    # This is script that allows to clone multiple gh-repos in one command
    cd  $WARBERRYDIR/Tools;
    for f in "${GITREPOS[@]}"; do `git clone $f`; done

   echo """
        DONE!

        WarBerry IS READY TO ROCK!
    
    """
else
    echo "ERROR: can't find apt."
exit 1;
fi
