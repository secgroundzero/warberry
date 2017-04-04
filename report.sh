#!/bin/bash
#By itcarsales
#Check for Contents in Server Results Folder
#If reports are found, prompt to replace, then auto copy or skip
#If empty, auto copy
echo """
        WarBerry Demo Reporting Interface
    """
if [ "$(ls -A /var/www/html/Results/)" ]; then
	echo && read -p "Would you like to replace the existing report data? (y/n)" -n 1 -r -s reportReplace && echo
	if [[ $reportReplace == "Y" || $reportReplace == "y" ]]; then
		rm -rf /var/www/html/Results/*.*
		cp -v /home/pi/WarBerry/Results/* /var/www/html/Results/
	fi
else
	cp -v /home/pi/WarBerry/Results/* /var/www/html/Results/
fi
#Start Web Server
service apache2 start

echo """
	Reports are ready at:
	"http://$1"
	Open the URL in your Browser
    """

echo && read -p "Press any key to stop the server and exit." -n 1 -r -s reportStop
#Stop Web Server
service apache2 stop
echo && echo "Apache Service stopped: Exiting now......"
