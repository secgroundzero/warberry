mkdir /home/pi/WarBerry/Results
apt-get update
apt-get upgrade
apt-get install python-pip
apt-get install nbtscan
apt-get install python-scapy
apt-get install tcpdump
apt-get install nmap
pip install python-nmap
apt-get install python-bluez
pip install optparse-pretty
pip install netaddr
pip install ipaddress
apt-get install ppp
apt-get install xprobe2
apt-get install sg3-utils
apt-get install netdiscover
apt-get install macchanger
apt-get install unzip
wget http://seclists.org/nmap-dev/2016/q2/att-201/clamav-exec.nse -O /usr/share/nmap/scripts/clamav-exec.nse
mkdir /home/pi/WarBerry/Tools
cd /home/pi/WarBerry/Tools
git clone https://github.com/DanMcInerney/net-creds.git
apt-get install onesixtyone
apt-get install nikto
apt-get install hydra
apt-get install john
apt-get install bridge-utils
apt-get install w3af-console
apt-get install ettercap-text-only
apt-get install cryptcat
apt-get install ike-scan
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
