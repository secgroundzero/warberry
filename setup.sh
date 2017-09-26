apt-get update
apt-get -y upgrade
mkdir /home/pi/WarBerry/Results
apt-get install -y python-pip
apt-get install -y nbtscan
apt-get install -y python-scapy
apt-get install -y tcpdump
apt-get install -y nmap
apt-get install -y python-urllib3
pip install python-nmap
apt-get install -y python-bluez
pip install optparse-pretty
pip install netaddr
pip install prettytable
pip install ipaddress
apt-get install -y ppp
apt-get install -y xprobe2
apt-get install -y sg3-utils
apt-get install -y netdiscover
apt-get install -y macchanger
apt-get install -y unzip
wget http://seclists.org/nmap-dev/2016/q2/att-201/clamav-exec.nse -O /usr/share/nmap/scripts/clamav-exec.nse
mkdir /home/pi/WarBerry/Tools
cd /home/pi/WarBerry/Tools
git clone https://github.com/DanMcInerney/net-creds.git
apt-get install -y onesixtyone
apt-get install -y nikto
apt-get install -y hydra
apt-get install -y john
apt-get install -y bridge-utils
apt-get install -y w3af-console
apt-get install -y ettercap-text-only
apt-get install -y cryptcat
apt-get install -y ike-scan
git clone https://github.com/sqlmapproject/sqlmap.git
git clone https://github.com/CoreSecurity/impacket.git
git clone https://github.com/samratashok/nishang.git
git clone https://github.com/SpiderLabs/Responder.git
git clone https://github.com/PowerShellMafia/PowerSploit.git
git clone https://github.com/offensive-security/exploit-database.git
wget https://download.sysinternals.com/files/SysinternalsSuite.zip
wget https://labs.portcullis.co.uk/download/enum4linux-0.8.9.tar.gz -O /home/pi/WarBerry/Tools/enum4linux-0.8.9.tar.gz
tar -zxvf enum4linux-0.8.9.tar.gz
mv enum4linux-0.8.9 enum4linux
cd /home/pi/WarBerry

