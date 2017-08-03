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

from src.utils.info_banners import *
import sys
import os

"""This function is used to create .xml files for database creation purposes.
Files not processed by this function:
'robots': allready in xml format.
capture.pcap: not needed for database representation."""
def create_xmls():
    xmls_created=0
    if os.path.exists("../Results/targets") and os.stat("../Results/targets").st_size != 0:
        create_xml("../Results/targets","targets")
        xmls_created+=1
    if os.path.exists("../Results/live_ips") and os.stat("../Results/live_ips").st_size != 0:
        create_xml("../Results/live_ips","live_ips")
        xmls_created += 1
    if os.path.exists("../Results/liveip_hosts")and os.stat("../Results/liveip_hosts").st_size != 0:
        create_xml("../Results/liveip_hosts","liveip_hosts")
        xmls_created += 1
    if os.path.exists("../Results/urls")and os.stat("../Results/urls").st_size != 0:
        create_xml("../Results/urls", "urls")
        xmls_created += 1
    if os.path.exists("../Results/webhosts")and os.stat("../Results/webhosts").st_size != 0:
        create_xml("../Results/webhosts", "webhosts")
        xmls_created += 1
    if os.path.exists("../Results/running_status")and os.stat("../Results/running_status").st_size != 0:
        create_xml("../Results/running_status", "running_status")
        xmls_created += 1
    if os.path.exists("../Results/avail_ips") and os.stat("../Results/avail_ips").st_size !=0 :
        create_xml("../Results/avail_ips", "avail_ips")
        xmls_created += 1
    if os.path.exists("../Results/dns") and os.stat("../Results/dns").st_size !=0 :
        create_xml("../Results/dns", "dns")
        xmls_created += 1
    if os.path.exists("../Results/mysql") and os.stat("../Results/mysql").st_size != 0:
        create_xml("../Results/mysql", "mysql")
        xmls_created += 1
    if os.path.exists("../Results/nfs") and os.stat("../Results/nfs").st_size != 0:
        create_xml("../Results/nfs", "nfs")
        xmls_created += 1
    if os.path.exists("../Results/statics") and os.stat("../Results/statics").st_size != 0:
        create_xml("../Results/statics", "statics")
        xmls_created += 1
    if os.path.exists("../Results/tightvnc") and os.stat("../Results/tightvnc").st_size !=0 :
        create_xml("../Results/tightvnc", "tightvnc")
        xmls_created += 1
    if os.path.exists("../Results/unique_CIDR") and os.stat("../Results/unique_CIDR").st_size !=0 :
        create_xml("../Results/unique_CIDR", "unique_CIDR")
        xmls_created += 1
    if os.path.exists("../Results/used_ips") and os.stat("../Results/used_ips").st_size !=0 :
        create_xml("../Results/used_ips", "used_ips")
        xmls_created += 1
    if os.path.exists("../Results/vnc") and os.stat("../Results/vnc").st_size !=0 :
        create_xml("../Results/vnc", "vnc")
        xmls_created += 1
    if os.path.exists("../Results/webservers443") and os.stat("../Results/webservers443").st_size !=0 :
        create_xml("../Results/webservers443", "webservers443")
        xmls_created += 1
    if os.path.exists("../Results/windows") and os.stat("../Results/windows").st_size !=0 :
        create_xml("../Results/windows", "windows")
        xmls_created += 1
    if os.path.exists("../Results/http_titles") and os.stat("../Results/http_titles").st_size !=0 :
        create_xml_2("../Results/http_titles","ip_add","name")
        xmls_created += 1
    if os.path.exists("../Results/titles_webhosts") and os.stat("../Results/titles_webhosts").st_size !=0 :
        create_xml("../Results/titles_webhosts","titles_webhosts")
        xmls_created += 1
    if os.path.exists("../Results/webs") and os.stat("../Results/webs").st_size !=0 :
        create_xml("../Results/webs","webs")
        xmls_created += 1
    if os.path.exists("../Results/blues") and os.stat("../Results/blues").st_size !=0 :
        create_xml("../Results/blues","blues")
        xmls_created += 1
    if os.path.exists("../Results/wafed") and os.stat("../Results/wafed").st_size !=0 :
        #create_xml_3("../Results/wafed")
        xmls_created += 1
    if os.path.exists("../Results/nameservers") and os.stat("../Results/nameservers").st_size !=0 :
        create_xml_4("../Results/nameservers")
        xmls_created += 1
    if os.path.exists("../Results/wifis") and os.stat("../Results/wifis").st_size != 0:
        create_xml("../Results/wifis", "wifis")
        xmls_created += 1
    if os.path.exists("../Results/windows") and os.stat("../Results/windows").st_size != 0:
        create_xml("../Results/windows", "windows")
        xmls_created += 1
    if os.path.exists("../Results/snmp_hosts") and os.stat("../Results/snmp_hosts").st_size != 0:
        create_xml("../Results/snmp_hosts", "snmp_hosts") #na thkialexw xml function
        xmls_created += 1
    if os.path.exists("../Results/snmp") and os.stat("../Results/snmp").st_size != 0:
        create_xml("../Results/snmp", "snmp")
        xmls_created += 1
    if os.path.exists("../Results/radius") and os.stat("../Results/radius").st_size != 0:
        create_xml("../Results/radius", "radius")
        xmls_created += 1
    if os.path.exists("../Results/sql_resolution") and os.stat("../Results/sql_resolution").st_size != 0:
        create_xml("../Results/sql_resolution", "sql_resolution")
        xmls_created += 1
    if os.path.exists("../Results/webservers80") and os.stat("../Results/webservers80").st_size !=0 :
        create_xml("../Results/webservers80","webservers80")
        xmls_created += 1
    if os.path.exists("../Results/webservers8080") and os.stat("../Results/webservers8080").st_size !=0 :
        create_xml("../Results/webservers8080","webservers8080")
        xmls_created += 1
    if os.path.exists("../Results/mvp_names") and os.stat("../Results/mvp_names").st_size !=0 :
        create_xml_5("../Results/mvp_names")
        xmls_created += 1
    if os.path.exists("../Results/hostnames")and os.stat("../Results/hostnames").st_size != 0:
        create_xml("../Results/hostnames", "hostnames")
        xmls_created += 1
    if os.path.exists("../Results/unique_hosts")and os.stat("../Results/unique_hosts").st_size != 0:
        create_xml("../Results/unique_hosts", "unique_hosts")
        xmls_created += 1
    if os.path.exists("../Results/mvps") and os.stat("../Results/mvps").st_size != 0:
        create_xml("../Results/mvps", "mvps")
        xmls_created += 1
    if os.path.exists("../Results/smb_users") and os.stat("../Results/smb_users").st_size != 0:
        #create_xml("../Results/smb_users", "smb_users") FIX IT
        xmls_created += 1
    if xmls_created==37:
        print bcolors.TITLE + "All .xml files created successfully. Check the /Results directory" + bcolors.ENDC
    else:
        print bcolors.TITLE + str(xmls_created)+" .xml files created successfully. Check the /Results directory" + bcolors.ENDC


def create_xml_5(filename):
    with open(filename, 'r') as prexml:
        lines = prexml.read().splitlines()
    prexml.close()
    with open(filename, 'w') as xml:
        xml.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>")
        xml.write("\n")
        xml.write("<root>\n")
        xml.write("\t<NBT_addresses>\n")
        count=4
        for i in range(4,len(lines)):
            xml.write("\t\t<name>")
            xml.write(str(lines[count].split()))
            xml.write("</name>\n")
        xml.write("\t</NBT_addresses>\n")
        xml.write("</root>")
    xml.close()


def create_xml(filename,data_name):
    with open(filename, 'r') as prexml:
        lines = prexml.read().splitlines()
    prexml.close()
    with open(filename, 'w') as xml:
        xml.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>")
        xml.write("\n")
        xml.write("<root>\n")
        for i in lines:
            xml.write("\t<"+data_name+">")
            xml.write(str(i))
            xml.write("</"+data_name+">"+"\n")
        xml.write("</root>")
    xml.close()



def create_xml_2(filename,data_n1,data_n2):
    with open(filename, 'r') as prexml:
        lines = prexml.read().splitlines()
    prexml.close()
    flag=0
    with open(filename, 'w') as xml:
        xml.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>")
        xml.write("\n")
        xml.write("<root>\n")
        for i in lines:
            if flag==0:
                xml.write("\t<"+data_n1+">")
                xml.write(str(i))
                xml.write("</"+data_n1+">"+"\n")
                flag=1
            elif flag==1:
                xml.write("\t<" + data_n2 + ">")
                xml.write(str(i))
                xml.write("</" + data_n2 + ">" + "\n")
                flag=1
        xml.write("</root>")
    xml.close()

def create_xml_3(filename):
    with open(filename, 'r') as prexml:
        lines = prexml.read().splitlines()
    prexml.close()
    with open(filename, 'w') as xml:
        xml.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>")
        xml.write("\n")
        xml.write("<root>\n")
        count=0
        for i in lines:
            if "Nmap scan report" in str(i):
                xml.write("\t<wafed>\n")
                temp = i.split()
                ip_add=temp[4]
                xml.write("\t\t<ip_address>")
                xml.write(ip_add)
                xml.write("</ip_address>\n")
                xml.write("\t\t<port>")
                port=lines[count+4].split()
                port=port[0]
                xml.write(port)
                xml.write("</port>\n")
                waf_line=lines[count+5]
                if "http-waf-detect:" in waf_line:
                    xml.write("\t\t<wafed_detection>")
                    waf_line=waf_line.split()
                    xml.write(waf_line[2]+" "+waf_line[3])
                    xml.write("</wafed_detection>\n")
                    xml.write("\t\t<mac_address>")
                    mac = lines[count + 7].split()
                    mac = mac[2]
                    xml.write(mac)
                    xml.write("</mac_address>\n")
                else:
                    xml.write("\t\t<mac_address>")
                    mac = lines[count + 5].split()
                    mac = mac[2]
                    xml.write(mac)
                    xml.write("</mac_address>\n")
                xml.write("\t</wafed>\n")
            count+=1
        xml.write("</root>")
    xml.close()


def create_xml_4(filename):
    with open(filename, 'r') as prexml:
        lines = prexml.read().splitlines()
    prexml.close()
    with open(filename, 'w') as xml:
        xml.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>")
        xml.write("\n")
        xml.write("<root>\n")
        count=4
        xml.write("\t<subnet>")
        temp = lines[0].split()
        xml.write(str(temp[7]))
        xml.write("</subnet>\n")
        xml.write("\t\t<IP_Addresses>\n")
        sum= len(lines)-4
        for i in range(0,sum):
            line =lines[count].split()
            line_len=len(line)
            xml.write("\t\t\t<IP>\n")
            xml.write("\t\t\t\t<Address>")
            xml.write(str(line[0]).translate(None, '\'<>'))
            xml.write("</Address>\n")
            xml.write("\t\t\t\t<NetBIOS_name>")
            xml.write(str(line[1]).translate(None, '\'<>'))
            xml.write("</NetBIOS_name>\n")
            if line_len ==5:
                xml.write("\t\t\t\t<Server>")
                xml.write(str(line[2]).translate(None, '\'<>'))
                xml.write("</Server>\n")
                xml.write("\t\t\t\t<User>")
                xml.write(str(line[3]).translate(None, '\'<>'))
                xml.write("</User>\n")
                xml.write("\t\t\t\t<MAC_address>")
                xml.write(str(line[4]).translate(None, '\'<>'))
                xml.write("</MAC_address>\n")
            elif line_len==4:
                xml.write("\t\t\t\t<Server>")
                xml.write("'None'")
                xml.write("</Server>\n")
                xml.write("\t\t\t\t<User>")
                xml.write(str(line[2]).translate(None, '\'<>'))
                xml.write("</User>\n")
                xml.write("\t\t\t\t<MAC_address>")
                xml.write(str(line[3]).translate(None, '\'<>'))
                xml.write("</MAC_address>\n")
            else:
                print bcolors.TITLE+"NAMESERVERS FILE HAS INAPPROPRIATE FORMAT!!!\n"+bcolors.ENDC
                sys.exit(1)
            xml.write("\t\t\t</IP>\n")
            count+=1
        xml.write("\t\t</IP_Addresses>\n")
        xml.write("</root>")
    xml.close()