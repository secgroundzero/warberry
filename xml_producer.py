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
from xml.etree import ElementTree, cElementTree
from xml.dom import minidom

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
        create_xml_2("../Results/http_titles","http_title","ip_add","name")
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
        create_xml_nameservers("../Results/nameservers")
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
        create_xml_mvps("../Results/mvp_names")
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


def create_xml_mvps(filename):
    with open(filename, 'r') as prexml:
        lines = prexml.read().splitlines()
    prexml.close()

    XMLFile = filename + str(".xml")
    root = ElementTree.Element('root')
    NBTAddress=ElementTree.SubElement(root, 'NBTAddresses')
    count=4
    for i in range(4,len(lines)):
        name=ElementTree.SubElement(NBTAddress,'Name')
        name.text=str(lines[count].split())

    tree = cElementTree.ElementTree(root)  # wrap it in an ElementTree instance, and save as XML

    t = minidom.parseString(ElementTree.tostring(
        root)).toprettyxml()  # Since ElementTree write() has no pretty printing support, used minidom to beautify the xml.
    tree1 = ElementTree.ElementTree(ElementTree.fromstring(t))

    tree1.write(XMLFile, encoding='utf-8', xml_declaration=True)



def create_xml(filename,targetName):
    with open(filename, 'r') as prexml:
        lines = prexml.read().splitlines()
    prexml.close()

    XMLFile=filename+str(".xml")
    root = ElementTree.Element('root')
    for i in lines:
        child1 = ElementTree.SubElement(root, targetName)
        child1.text = str(i)

    tree = cElementTree.ElementTree(root)  # wrap it in an ElementTree instance, and save as XML

    t = minidom.parseString(ElementTree.tostring(
        root)).toprettyxml()  # Since ElementTree write() has no pretty printing support, used minidom to beautify the xml.
    tree1 = ElementTree.ElementTree(ElementTree.fromstring(t))

    tree1.write(XMLFile, encoding='utf-8', xml_declaration=True)


def create_xml_2(filename,element, data_n1,data_n2):
    with open(filename, 'r') as prexml:
        lines = prexml.read().splitlines()
    prexml.close()

    flag=0
    XMLFile = filename + str(".xml")
    root = ElementTree.Element('root')
    elementRoot=ElementTree.SubElement(root, element)
    for i in lines:
        if flag==0:
            child1=ElementTree.SubElement(elementRoot, data_n1)
            child1_text=str(i)
            flag=1
        elif flag==1:
            child2=ElementTree.SubElement(elementRoot, data_n2)
            child2.text=str(i)
            flag=0
            elementRoot=ElementTree.SubElement(root, element)

    tree = cElementTree.ElementTree(root)  # wrap it in an ElementTree instance, and save as XML

    t = minidom.parseString(ElementTree.tostring(
                root)).toprettyxml()  # Since ElementTree write() has no pretty printing support, used minidom to beautify the xml.
    tree1 = ElementTree.ElementTree(ElementTree.fromstring(t))
    tree1.write(XMLFile, encoding='utf-8', xml_declaration=True)


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


def create_xml_nameservers(filename):
    with open(filename, 'r') as prexml:
        lines = prexml.read().splitlines()
    prexml.close()

    XMLFile = filename + str(".xml")
    root = ElementTree.Element('root')
    subnet=ElementTree.SubElement(root, 'subnet')
    temp = lines[0].split()
    subnet.text=str(temp[7])
    ipAddresses=ElementTree.SubElement(root, 'IP_Addresses')
    sum=len(lines)-4
    count=4
    for i in range(0,sum):
        line = lines[count].split()
        line_len = len(line)
        ip=ElementTree.SubElement(ipAddresses, 'IP')
        address=ElementTree.SubElement(ip,'Address')
        address.text=str(line[0]).translate(None, '\'<>')
        netBIOS=ElementTree.SubElement(ip, 'NetBIOS_name')
        netBIOS.text=str(line[1]).translate(None, '\'<>')
        if line_len==5:
            server=ElementTree.SubElement(ip, 'Server')
            server.text=str(line[2]).translate(None, '\'<>')
            user=ElementTree.SubElement(ip, 'User')
            user.text=str(line[3]).translate(None, '\'<>')
            macAddress=ElementTree.SubElement(ip, 'MAC_Address')
            macAddress.text=str(line[4]).translate(None, '\'<>')
        elif line_len==4:
            server = ElementTree.SubElement(ip, 'Server')
            server.text = "None"
            user = ElementTree.SubElement(ip, 'User')
            user.text = str(line[2]).translate(None, '\'<>')
            macAddress = ElementTree.SubElement(ip, 'MAC_Address')
            macAddress.text = str(line[3]).translate(None, '\'<>')
        else:
            print bcolors.TITLE + "NAMESERVERS FILE HAS INAPPROPRIATE FORMAT!!!\n" + bcolors.ENDC
            sys.exit(1)
        count += 1

    tree = cElementTree.ElementTree(root)  # wrap it in an ElementTree instance, and save as XML

    t = minidom.parseString(ElementTree.tostring(
        root)).toprettyxml()  # Since ElementTree write() has no pretty printing support, used minidom to beautify the xml.
    tree1 = ElementTree.ElementTree(ElementTree.fromstring(t))
    tree1.write(XMLFile, encoding='utf-8', xml_declaration=True)
