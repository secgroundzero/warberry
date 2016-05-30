#!/usr/bin/env bash

##
## WarBerry bootstrap script
## Ver. 0.0.1
##

APT_GET_CMD=$(which apt-get)
OLD_HOSTNAME="$( hostname )"
NEW_HOSTNAME="WarBerry"
WARBERRYDIR=/home/pi/WarBerry
VENVDIR=/opt/warberry
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

echo "CHANGING HOSTNAME FROM $OLD_HOSTNAME TO $NEW_HOSTNAME..."
hostname "$NEW_HOSTNAME"
if [ -n "$( grep "$OLD_HOSTNAME" /etc/hosts )" ]; then
 sed -i "s/$OLD_HOSTNAME/$NEW_HOSTNAME/g" /etc/hosts
else
 echo -e "$( hostname -I | awk '{ print $1 }' )\t$NEW_HOSTNAME" >> /etc/hosts
fi

echo "CREATING DIRECTORIES..."
mkdir -p $WARBERRYDIR/{Results,Tools}

if [[ ! -z $APT_GET_CMD ]]; then
    echo """
        PERFORMING BASIC DEPENDENCIES INSTALLATION...
    """
    apt-get -y update && apt-get -y upgrade;
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
                    ettercap-text-only;

    echo """
        BOOTSTRAPPING PYTHON UTILS...
    """
    pip install --upgrade pip;
    pip install virtualenv;
    /usr/local/bin/virtualenv $VENVDIR;
    echo "source $VENVDIR/bin/activate" >> /home/pi/.bashrc

    echo """
        INSTALLING PYTHON PACKAGES...
    """
    /opt/warberry/bin/pip install scapy python-nmap;

    echo """
        CLONING GIT PACKAGES TO WarBerry/Tools directory...
    """
    # This is script that allows to clone multiple gh-repos in one command
    cd  $WARBERRYDIR/Tools;
    for f in "${GITREPOS[@]}"; do `git clone $f`; done

    echo """
        DONE!
    """
    echo """

        WarBerry IS READY TO ROCK!
        Run warberry.py via /opt/warberry/python warberry.py

        NOTE: WarBerry should activate virtualenv on next reboot so next time python warberry.py will work like a charm.

    """
else
    echo "ERROR: can't find apt."
exit 1;
fi
