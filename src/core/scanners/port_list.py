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

path_file=['../Results/windows','../Results/ftp', '../Results/mssql', '../Results/mysql', '../Results/oracle', '../Results/nfs', '../Results/webservers80','../Results/webservers443', '../Results/webservers8080','../Results/webservers4443','../Results/webservers8081', '../Results/webservers8181', '../Results/webservers9090','../Results/printers', '../Results/telnet', '../Results/mongo', '../Results/vnc', '../Results/dns', '../Results/phpmyadmin','../Results/tightvnc','../Results/websphere','../Results/firebird', '../Results/xserver', '../Results/svn', '../Results/snmp','../Results/voip','../Results/rlogin','../Results/openvpn','../Results/ipsec','../Results/ldap','../Results/pop3','../Results/smtp','../Results/sap_mgmt','../Results/sap_router','../Results/sap_gui','../Results/sap_icf','../Results/java_rmi','../Results/isql','../Results/clamav','../Results/finger','../Results/distcc','../Results/webmin','../Results/pjl','../Results/informix_serv','../Results/h323','../Results/vsphere','../Results/informix_db','../Results/imap','../Results/lotus_notes','../Results/sql_resolution','../Results/upnp','../Results/radius']

result_file = ['windows', 'ftp', 'mssql','mysql', 'oracle', 'nfs','webservers80', 'webservers443','webservers8080', 'webservers4443', 'webservers8081', 'webservers8181','webservers9090', 'printers','telnet', 'mongo', 'vnc', 'dns', 'phpmyadmin','tightvnc', 'websphere','firebird', 'xserver', 'svn', 'snmp','voip','rlogin','openvpn','ipsec','ldap','pop3','smtp','sap_mgmt','sap_router','sap_gui','sap_icf','java_rmi','isql','clamav','finger','distcc','webmin','pjl','informix_serv','h323','vsphere','informix_db','imap','lotus_notes','sql_resolution','upnp','radius']

message=["[*] You may want to check for open shares here\n", "[*] You may want to try log in as user ANONYMOUS\n", "[*] Default user for MSSQL installations is SA\n", "[*] Default creds for MYSQL are U:root P:blank\n", "[*] Default user on Oracle DBs are SYS, SYSTEM, SCOTT\n", "[*] You can view NFS contents by showmount -e <IP>\n", "","","","","","","","","","","","","","", "[*] Default logins for Websphere are U:system P:manager\n","[*] Default logins on Firebird DB are U:SYSDBA P:masterkey\n","","","","","","","","","","","","","","","","","","Get information using finger -l @<ip> or finger 0@<ip>","","","","","","","","","","Multiple SQL Instances on this server","",""]

name = ['Windows Hosts', 'FTP', 'MSSQL Databases','MySQL Databases', 'Oracle Databases', 'NFS','Web Servers at Port 80', 'Web Servers at Port 443','Web Servers at Port 8080', 'Web Servers at Port 4443','Web Servers at Port 8081', 'Web Servers at Port 8181','Web Servers at Port 9090', 'Printers','Telnet', 'Mongo Databases', 'VNC','DNS', 'PHPMyAdmin','Tight VNC', 'IBM WebSphere','Firebird Databases', 'XServer', 'SVN Repositories','SNMP','VOIP','rLogin','OpenVPN','IPSec','LDAP','POP3','SMTP','SAP MGMT Console','SAP Router','SAP Web GUI','SAP ICF','Java RMI Endpoint','Oracle iSQL Login Page','Clam AV','Finger Protocol','DistCC Daemon','Webmin','PJL Language Support','Informix Server','H323','Vsphere Client','Informix DB','IMAP','Lotus Notes Client','SQL Resolution Service','UPNP','RADIUS']

port=['445', '21', '1433', '3306', '1521', '111', '80', '443', '8080', '4443', '8081', '8181', '9090', '8611,8612,5222,5223', '23', '27017,27018,27019,28017', '5900', '53', '8089', '5800', '9443', '3050', '6000', '3690', '161','5060','513','1194','500','389','110','25','50013','3299','8000','8042','1099','5560','3310','79','3632','10000','9100','1526','1720','902,903','9088','143,999','1352','1434','1900','1812,1813,1645,1646']

scan_type=['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'y','n','n','n','n','n','n','n','n','n','n','n','n','n','n','n','n','n','n','n','n','n','n','n','n','y','y','y']