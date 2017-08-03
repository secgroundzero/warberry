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

import os, os.path
from src.utils.info_banners import *
import subprocess

"""This function deletes all the following files, for propper execution
of the warberry tool. It's used at the start of the warberry.py"""
def move_files(timestamp):
    move_files=0
    if os.path.exists("../ResultLogs")==False:
        subprocess.call("sudo mkdir ../ResultLogs", shell=True)

    endDest="../ResultLogs/"+str(timestamp)
    if os.path.exists(endDest)==False:
        subprocess.call("sudo mkdir  ../ResultLogs/%s" % timestamp, shell=True)
        subprocess.call("sudo mv ../Results/* ../ResultLogs/%s" % timestamp, shell=True)
    """if os.path.exists("../Results/capture.pcap"):
        endFile="../ResultLogs/"+str(timestamp)+"/capture.pcap"
        os.rename("../Results/capture.pcap", endFile)
        move_files+=1
    if os.path.exists("../Results/hostnames"):
        endFile="../ResultLogs/"+str(timestamp)+"/hostnames"
        os.rename("../Results/hostnames", endFile)
        move_files+=1
    if os.path.exists("../Results/http_titles"):
        endFile="../ResultLogs/"+str(timestamp)+"/http_titles"
        os.rename("../Results/http_titles", endFile)
        move_files += 1
    if os.path.exists("../Results/live_ips"):
        endFile = "../ResultLogs/" + str(timestamp) + "/live_ips"
        os.rename("../Results/live_ips", endFile)
        move_files += 1
    if os.path.exists("../Results/liveip_hosts"):
        endFile = "../ResultLogs/" + str(timestamp) + "/liveip_hosts"
        os.rename("../Results/liveip_hosts", endFile)
        move_files += 1
    if os.path.exists("../Results/mvp_names"):
        endFile = "../ResultLogs/" + str(timestamp) + "/mvp_names"
        os.rename("../Results/mvp_names", endFile)
        move_files += 1
    if os.path.exists("../Results/mvps"):
        endFile = "../ResultLogs/" + str(timestamp) + "/mvps"
        os.rename("../Results/mvps", endFile)
        move_files += 1
    if os.path.exists("../Results/nameservers"):
        endFile = "../ResultLogs/" + str(timestamp) + "/nameservers"
        os.rename("../Results/nameservers", endFile)
        move_files += 1
    if os.path.exists("../Results/os_enum"):
        endFile = "../ResultLogs/" + str(timestamp) + "/os_enum"
        os.remove("../Results/os_enum", endFile)
        move_files += 1
    if os.path.exists("../Results/pcap_results"):
        endFile = "../ResultLogs/" + str(timestamp) + "/pcap_results"
        os.rename("../Results/pcap_results", endFile)
        move_files += 1
    if os.path.exists("../Results/robots"):
        endFile = "../ResultLogs/" + str(timestamp) + "/robots"
        os.rename("../Results/robots", endFile)
        move_files += 1
    if os.path.exists("../Results/running_status"):
        endFile = "../ResultLogs/" + str(timestamp) + "/running_status"
        os.rename("../Results/running_status", endFile)
        move_files += 1
    if os.path.exists("../Results/targets"):
        endFile = "../ResultLogs/" + str(timestamp) + "/targets"
        os.rename("../Results/targets", endFile)
        move_files += 1
    if os.path.exists("../Results/titles_webhosts"):
        endFile = "../ResultLogs/" + str(timestamp) + "/titles_webhosts"
        os.rename("../Results/titles_webhosts", endFile)
        move_files += 1
    if os.path.exists("../Results/unique_hosts"):
        endFile = "../ResultLogs/" + str(timestamp) + "/unique_hosts"
        os.rename("../Results/unique_hosts", endFile)
        move_files += 1
    if os.path.exists("../Results/urls"):
        endFile = "../ResultLogs/" + str(timestamp) + "/urls"
        os.rename("../Results/urls", endFile)
        move_files += 1
    if os.path.exists("../Results/wafed"):
        endFile = "../ResultLogs/" + str(timestamp) + "/wafed"
        os.rename("../Results/wafed", endFile)
        move_files += 1
    if os.path.exists("../Results/webhosts"):
        os.remove("../Results/webhosts")
        del_files += 1
    if os.path.exists("../Results/webs"):
        os.remove("../Results/webs")
        del_files += 1
    if os.path.exists("../Results/webservers80"):
        os.remove("../Results/webservers80")
        del_files += 1
    if os.path.exists("../Results/webservers443"):
        os.remove("../Results/webservers443")
        del_files += 1
    if os.path.exists("../Results/avail_ips"):
        os.remove("../Results/avail_ips")
        del_files += 1
    if os.path.exists("../Results/dns"):
        os.remove("../Results/dns")
        del_files += 1
    if os.path.exists("../Results/mysql"):
        os.remove("../Results/mysql")
        del_files += 1
    if os.path.exists("../Results/nfs"):
        os.remove("../Results/nfs")
        del_files += 1
    if os.path.exists("../Results/statics"):
        os.remove("../Results/statics")
        del_files += 1
    if os.path.exists("../Results/tightvnc"):
        os.remove("../Results/tightvnc")
        del_files += 1
    if os.path.exists("../Results/unique_CIDR"):
        os.remove("../Results/unique_CIDR")
        del_files += 1
    if os.path.exists("../Results/used_ips"):
        os.remove("../Results/used_ips")
        del_files += 1
    if os.path.exists("../Results/vnc"):
        os.remove("../Results/vnc")
        del_files += 1
    if os.path.exists("../Results/wifis"):
        os.remove("../Results/wifis")
        del_files += 1
    if os.path.exists("../Results/windows"):
        os.remove("../Results/windows")
        del_files += 1
    if os.path.exists("../Results/blues"):
        os.remove("../Results/blues")
        del_files += 1
    if os.path.exists("../Results/snmp"):
        os.remove("../Results/snmp")
        del_files += 1
    if os.path.exists("../Results/snmp_hosts"):
        os.remove("../Results/snmp_hosts")
        del_files += 1
    if os.path.exists("../Results/radius"):
        os.remove("../Results/radius")
        del_files += 1
    if os.path.exists("../Results/snmp_enum"):
        os.remove("../Results/snmp_enum")
        del_files += 1
    if os.path.exists("../Results/sql_resolution"):
        os.remove("../Results/sql_resolution")
        del_files += 1
    if os.path.exists("../Results/upnp"):
        os.remove("../Results/upnp")
        del_files += 1
    if os.path.exists("../Results/shares"):
        os.remove("../Results/shares")
        del_files += 1
    if os.path.exists("../Results/smb_users"):
        os.remove("../Results/smb_users")
        del_files += 1
    if os.path.exists("../Results/win_hosts"):
        os.remove("../Results/win_hosts")
        del_files += 1
    if os.path.exists("../Results/traceroute"):
        os.remove("../Results/traceroute")
        del_files += 1
    if os.path.exists("../Results/arp"):
        os.remove("../Results/arp")
        del_files += 1
    if os.path.exists("../Results/h323"):
        os.remove("../Results/h323")
        del_files += 1
    if os.path.exists("../Results/clamav"):
        os.remove("../Results/clamav")
        del_files += 1
    if os.path.exists("../Results/distcc"):
        os.remove("../Results/distcc")
        del_files += 1
    if os.path.exists("../Results/finger"):
        os.remove("../Results/finger")
        del_files += 1
    if os.path.exists("../Results/firebird"):
        os.remove("../Results/firebird")
        del_files += 1
    if os.path.exists("../Results/ftp"):
        os.remove("../Results/ftp")
        del_files += 1
    if os.path.exists("../Results/ftp_enum"):
        os.remove("../Results/ftp_enum")
        del_files += 1
    if os.path.exists("../Results/ftp_hosts"):
        os.remove("../Results/ftp_hosts")
        del_files += 1
    if os.path.exists("../Results/lotus_notes"):
        os.remove("../Results/lotus_notes")
        del_files += 1
    if os.path.exists("../Results/ldap"):
        os.remove("../Results/ldap")
        del_files += 1
    if os.path.exists("../Results/java_rmi"):
        os.remove("../Results/java_rmi")
        del_files += 1
    if os.path.exists("../Results/informix_serv"):
        os.remove("../Results/informix_serv")
        del_files += 1
    if os.path.exists("../Results/ipsec"):
        os.remove("../Results/ipsec")
        del_files += 1
    if os.path.exists("../Results/isql"):
        os.remove("../Results/isql")
        del_files += 1
    if os.path.exists("../Results/mssql"):
        os.remove("../Results/mssql")
        del_files += 1
    if os.path.exists("../Results/mssql_enum"):
        os.remove("../Results/mssql_enum")
        del_files += 1
    if os.path.exists("../Results/mssql_hosts"):
        os.remove("../Results/mssql_hosts")
        del_files += 1
    if os.path.exists("../Results/mysql_enum"):
        os.remove("../Results/mysql_enum")
        del_files += 1
    if os.path.exists("../Results/mysql_hosts"):
        os.remove("../Results/mysql_hosts")
        del_files += 1
    if os.path.exists("../Results/nfs_enum"):
        os.remove("../Results/nfs_enum")
        del_files += 1
    if os.path.exists("../Results/nfs_hosts"):
        os.remove("../Results/nfs_hosts")
        del_files += 1
    if os.path.exists("../Results/openvpn"):
        os.remove("../Results/openvpn")
        del_files += 1
    if os.path.exists("../Results/oracle"):
        os.remove("../Results/oracle")
        del_files += 1
    if os.path.exists("../Results/phpmyadmin"):
        os.remove("../Results/phpmyadmin")
        del_files += 1
    if os.path.exists("../Results/pop3"):
        os.remove("../Results/pop3")
        del_files += 1
    if os.path.exists("../Results/rlogin"):
        os.remove("../Results/rlogin")
        del_files += 1
    if os.path.exists("../Results/sap_gui"):
        os.remove("../Results/sap_gui")
        del_files += 1
    if os.path.exists("../Results/sap_icf"):
        os.remove("../Results/sap_icf")
        del_files += 1
    if os.path.exists("../Results/webservers4443"):
        os.remove("../Results/webservers4443")
        del_files += 1
    if os.path.exists("../Results/webservers8080"):
        os.remove("../Results/webservers8080")
        del_files += 1
    if os.path.exists("../Results/webservers8081"):
        os.remove("../Results/webservers8081")
        del_files += 1
    if os.path.exists("../Results/websphere"):
        os.remove("../Results/websphere")
        del_files += 1
    if os.path.exists("../Results/webservers9090"):
        os.remove("../Results/webservers9090")
        del_files += 1
    if os.path.exists("../Results/xserver"):
        os.remove("../Results/xserver")
        del_files += 1
    if os.path.exists("../Results/pjl'"):
        os.remove("../Results/pjl'")
        del_files += 1
    if os.path.exists("../Results/voip_hosts"):
        os.remove("../Results/voip_hosts")
        del_files += 1
    if os.path.exists("../Results/smtp"):
        os.remove("../Results/smtp")
        del_files += 1
    if os.path.exists("../Results/svn"):
        os.remove("../Results/svn")
        del_files += 1
    if os.path.exists("../Results/telnet"):
        os.remove("../Results/telnet")
        del_files += 1
    if os.path.exists("../Results/voip"):
        os.remove("../Results/voip")
        del_files += 1
    if os.path.exists("../Results/webservers8181"):
        os.remove("../Results/webservers8181")
        del_files += 1
    if os.path.exists("../Results/webmin"):
        os.remove("../Results/webmin")
        del_files += 1
    if os.path.exists("../Results/sip_users"):
        os.remove("../Results/sip_users")
        move_files += 1
    if os.path.exists("../Results/sip_methods"):
        os.remove("../Results/sip_methods")
        del_files += 1
    if os.path.exists("../Results/sap_router"):
        os.remove("../Results/sap_router")
        move_files += 1

    if del_files==44:
        print bcolors.TITLE + "All files deleted successfully. Check the /Results directory" + bcolors.ENDC
    else:
        print bcolors.TITLE + str(del_files)+" files deleted successfully. Check the /Results directory" + bcolors.ENDC"""
