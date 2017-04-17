#!/bin/bash
#By itcarsales
#Installer for WarBerry

if [ "$(id -u)" != "0" ]; then
	echo "ERROR: INVALID PERMISSIONS (Sorry, plese run this script as root or with sudo)"
	exit 1
fi

echo """
		Welcome to the WarBerry Installer 
	"""
echo && read -p "Would you like to install WarBerry? (y/n)" -n 1 -r -s installWar && echo
if [ "$installWar" != 'y' ]; then
	echo "WarBerry install cancelled."  
	exit 1
else
    echo """
            Install will continue after update......
        """    
    apt-get update -y
    
    echo """
            Selecting Custom Settings......
        """ 
    apt-get -y install macchanger   
    echo && read -p "Would you like to install the report server with Apache and PHP? (y/n)" -n 1 -r -s installReports && echo
    echo && read -p "Is this running on a Raspberry Pi 3? (y/n)" -n 1 -r -s installRPi3 && echo
    if [[ $installRPi3 == "Y" || $installRPi3 == "y" ]]; then
		echo && read -p "Do you wish to Install Aircrack for embedded wifi? (y/n)" -n 1 -r -s installAircrack && echo
	fi
 
    echo && read -p "Will you be following the 3G Covert Channel Setup? (y/n)" -n 1 -r -s install3G && echo
    if [[ $install3G == "Y" || $install3G == "y" ]]; then
		echo && read -p "Will you be using REMOT3.IT? (y/n)" -n 1 -r -s installRemot3 && echo
	fi
    
    echo """
            Installing GIT and PIP
        """
    apt-get -y install git
    apt-get -y install python-pip

    echo """
            Starting WarBerry Installation
        """
    echo """
            Creating necessary directories...
        """
    cd /home/pi/
    mkdir WarBerry
    mv warberry/ WarBerry/
    cd WarBerry/
    mkdir Results
    mkdir Tools
    
    echo """
            Installing necessary tools...
        """
    apt-get -y install nbtscan 
    apt-get -y install python-scapy
    apt-get -y install tcpdump
    apt-get -y install nmap
    apt-get -y install python-nmap
    apt-get -y install python-bluez
    apt-get -y install smbclient
    apt-get -y install samba
    apt-get -y install samba_common_bin
    apt-get -y install unzip
    apt-get -y install python-dev
    apt-get -y install python3-dev
    apt-get -y install libpcap-dev
    apt-get -y install ppp
    apt-get -y install xprobe2
    apt-get -y install sg3-utils
    apt-get -y install netdiscover
    apt-get -y instal  python-beautifulsoup
    yes | pip install optparse-pretty 
    yes | pip install netaddr 
    yes | pip install ipaddress 
    yes | pip install subprocess32
    yes | pip install pypcap
    wget http://seclists.org/nmap-dev/2016/q2/att-201/clamav-exec.nse -O /usr/share/nmap/scripts/clamav-exec.nse
    cd /home/pi/WarBerry/Tools/
    wget https://labs.portcullis.co.uk/download/enum4linux-0.8.9.tar.gz
    tar -zxvf enum4linux-0.8.9.tar.gz
    mv enum4linux-0.8.9 enum4linux

    echo """
            Adding some extra Tools...
        """
    apt-get -y install onesixtyone
    apt-get -y install nikto
    apt-get -y install hydra
    apt-get -y install john
    apt-get -y install bridge-utils
    apt-get -y install w3af-console
    apt-get -y install ettercap-text-only
    apt-get -y install cryptcat
    apt-get -y install ike-scan

    echo """
            Cloning some awesome repos...
        """
    cd /home/pi/WarBerry/Tools
    git clone https://github.com/DanMcInerney/net-creds.git
    git clone https://github.com/sqlmapproject/sqlmap.git
    git clone https://github.com/CoreSecurity/impacket.git
    git clone https://github.com/samratashok/nishang.git
    git clone https://github.com/SpiderLabs/Responder.git
    git clone https://github.com/PowerShellMafia/PowerSploit.git
    git clone https://github.com/offensive-security/exploit-database.git
    wget https://download.sysinternals.com/files/SysinternalsSuite.zip
    unzip SysinternalsSuite.zip -d sysinternals/
    
#Cleaning Up 
    rm /home/pi/WarBerry/Tools/enum4linux-0.8.9.tar.*
    rm /home/pi/WarBerry/Tools/SysinternalsSuite.*
    rm /home/pi/WarBerry/warberry/warInstall.sh
    mv /home/pi/WarBerry/warberry/startWar.sh /home/pi/WarBerry/
    
#Apache and PHP for Reporting install section
    if [[ $installReports == "Y" || $installReports == "y" ]]; then
        echo """
                Installing Apache and PHP for Reporting
            """
        apt-get install apache2 -y
        update-rc.d apache2 disable
        service apache2 stop
        apt-get install php5 libapache2-mod-php5 -y
        cp -a /home/pi/WarBerry/warberry/REPORTING/. /var/www/html/
        mkdir /var/www/html/Results/
        cd /var/www/html/
        mv index.html index.html.old
        mv reporting.html index.html
        mv /home/pi/WarBerry/warberry/warReport.sh /home/pi/WarBerry/
        cd /home/pi/
    else
        rm /home/pi/WarBerry/warberry/report.sh
        rm /home/pi/WarBerry/warberry/warReport.sh
    fi

#Aircrack install section with Raspberry Pi v3 check
    if [[ $installRPi3 == "Y" || $installRPi3 == "y" ]]; then
        if [[ $installAircrack == "Y" || $installAircrack == "y" ]]; then
            echo """
                    Installing Aircrack
                """
            apt-get -y install libssl-dev
            cd /home/pi/WarBerry/Tools/
            wget http://download.aircrack-ng.org/aircrack-ng-1.2-beta1.tar.gz
            tar -zxvf aircrack-ng-1.2-beta1.tar.gz
            cd aircrack-ng-1.2-beta1
            make
            make install
            airodump-ng-oui-update
            apt-get -y install iw
            rm /home/pi/WarBerry/Tools/aircrack-ng-1.2-beta1.tar.*
        fi
    fi
    
#3G Covert Channel Installer - per wiki
    if [[ $install3G == "Y" || $install3G == "y" ]]; then
        echo """
                Installing 3G per Guide
            """
        cd /home/pi/WarBerry/Tools/
        wget "http://downloads.sourceforge.net/project/vim-n4n0/sakis3g.tar.gz?r=http%3A%2F%2Fsourceforge.net%2Fprojects%2Fvim-n4n0%2Ffiles%2F&ts=1363537696&use_mirror=tene~t" -O sakis3g.tar.gz
        tar -xzvf sakis3g.tar.gz
        apt-get install sg3-utils
        chmod +x sakis3g
        ./sakis3g --interactive
        rm /home/pi/WarBerry/Tools/sakis3g.tar.*

	#remot3.it installer for 3G connection
        if [[ $installRemot3 == "Y" || $installRemot3 == "y" ]]; then
            apt-get -y install weavedconnectd
            weavedinstaller
        fi
    fi

    echo """
            Installation Complete - Please use Responsibly
        """
fi
