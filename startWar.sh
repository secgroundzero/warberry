#!/bin/bash
#By itcarsales
#Modify to create two quick-start custom modes

cd /home/pi/WarBerry/warberry/
echo && read -p "Would you like to run in Demo Mode? (y/n)" -n 1 -r -s demoMode && echo
if [[ $demoMode == "Y" || $demoMode == "y" ]]; then
	echo "Starting Demo Mode"
	sudo python warberry.py -I eth0 -p 250 -x 60 -i -T3 -Q
else
	echo "Starting Standard Mode"
	sudo python warberry.py -I eth0 -p 250 -x 60
fi
