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
import cryptomath
import random
import os
from src.utils.info_banners import *

SYMBOLS = """ !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~""" # note the space at the front

def main():
    myMessage = """"A computer would deserve to be called intelligent if \n it could deceive a human into believing that it was human." -Alan Turing"""

    key = getRandomKey()
    keyA, keyB = getKeyParts(key)
    translated = encryptMessage(key, myMessage)
    print "ENCRYPTED"
    print translated
    translated = decryptMessage(key, translated)
    print "DECRYPTED"
    print translated
    print "THE KEY WAS:"
    print key



#This method encrypts a specific file named filename
def encrypt_file(filename):
    with open(filename, 'r') as file:
        data = file.read()
    key = getRandomKey()
    encrypted_data= encryptMessage(key, data)
    with open(filename, 'w') as new_file:
        new_file.write(encrypted_data)
        new_file.write("\n")
        new_file.write(str(key))
    new_file.close


"""This method checks and encrypts all the apporpriate
files. The key for decryption is a random number and its
saved at the end of the file in order to be used in a later
stage for decryption"""
def encrypt_files():
    files_encrypted=0
    if os.path.exists("../Results/hostnames")and os.stat("../Results/hostnames").st_size !=0 :
        encrypt_file("../Results/hostnames")
        files_encrypted+=1
    if os.path.exists("../Results/http_titles")and os.stat("../Results/http_titles").st_size !=0 :
        encrypt_file("../Results/http_titles")
        files_encrypted+=1
    if os.path.exists("../Results/live_ips")and os.stat("../Results/live_ips").st_size !=0 :
        encrypt_file("../Results/live_ips")
        files_encrypted+=1
    if os.path.exists("../Results/liveip_hosts")and os.stat("../Results/liveip_hosts").st_size !=0 :
        encrypt_file("../Results/liveip_hosts")
        files_encrypted+=1
    if os.path.exists("../Results/mvp_names")and os.stat("../Results/mvp_names").st_size !=0 :
        encrypt_file("../Results/mvp_names")
        files_encrypted+=1
    if os.path.exists("../Results/mvps")and os.stat("../Results/mvps").st_size !=0 :
        encrypt_file("../Results/mvps")
        files_encrypted+=1
    if os.path.exists("../Results/nameservers")and os.stat("../Results/nameservers").st_size !=0 :
        encrypt_file("../Results/nameservers")
        files_encrypted+=1
    if os.path.exists("../Results/os_enum")and os.stat("../Results/os_enum").st_size != 0:
        encrypt_file("../Results/os_enum")
        files_encrypted+=1
    if os.path.exists("../Results/pcap_results")and os.stat("../Results/pcap_results").st_size !=0 :
        encrypt_file("../Results/pcap_results")
        files_encrypted+=1
    if os.path.exists("../Results/robots")and os.stat("../Results/robots").st_size != 0:
        encrypt_file("../Results/robots")
        files_encrypted+=1
    if os.path.exists("../Results/running_status")and os.stat("../Results/running_status").st_size !=0 :
        encrypt_file("../Results/running_status")
        files_encrypted+=1
    if os.path.exists("../Results/targets")and os.stat("../Results/targets").st_size !=0 :
        encrypt_file("../Results/targets")
        files_encrypted+=1
    if os.path.exists("../Results/titles_webhosts")and os.stat("../Results/titles_webhosts").st_size !=0 :
        encrypt_file("../Results/titles_webhosts")
        files_encrypted+=1
    if os.path.exists("../Results/unique_hosts")and os.stat("../Results/unique_hosts").st_size !=0 :
        encrypt_file("../Results/unique_hosts")
        files_encrypted+=1
    if os.path.exists("../Results/urls")and os.stat("../Results/urls").st_size !=0 :
        encrypt_file("../Results/urls")
        files_encrypted+=1
    if os.path.exists("../Results/wafed")and os.stat("../Results/wafed").st_size !=0 :
        encrypt_file("../Results/wafed")
        files_encrypted+=1
    if os.path.exists("../Results/webhosts")and os.stat("../Results/webhosts").st_size !=0 :
        encrypt_file("../Results/webhosts")
        files_encrypted+=1
    if os.path.exists("../Results/webs")and os.stat("../Results/webs").st_size != 0:
        encrypt_file("../Results/webs")
        files_encrypted+=1
    if os.path.exists("../Results/webservers80") and os.stat("../Results/webservers80").st_size !=0 :
        encrypt_file("../Results/webservers80")
        files_encrypted+=1
    if os.path.exists("../Results/webservers8080") and os.stat("../Results/webservers8080").st_size !=0 :
        encrypt_file("../Results/webservers8080")
        files_encrypted+=1
    if os.path.exists("../Results/avail_ips") and os.stat("../Results/avail_ips").st_size !=0 :
        encrypt_file("../Results/avail_ips")
        files_encrypted+=1
    if os.path.exists("../Results/dns") and os.stat("../Results/dns").st_size !=0 :
        encrypt_file("../Results/dns")
        files_encrypted+=1
    if os.path.exists("../Results/mysql") and os.stat("../Results/mysql").st_size !=0 :
        encrypt_file("../Results/mysql")
        files_encrypted+=1
    if os.path.exists("../Results/nfs") and os.stat("../Results/nfs").st_size !=0 :
        encrypt_file("../Results/nfs")
        files_encrypted+=1
    if os.path.exists("../Results/statics") and os.stat("../Results/statics").st_size !=0 :
        encrypt_file("../Results/statics")
        files_encrypted+=1
    if os.path.exists("../Results/tightvnc") and os.stat("../Results/tightvnc").st_size !=0 :
        encrypt_file("../Results/tightvnc")
        files_encrypted+=1
    if os.path.exists("../Results/unique_CIDR") and os.stat("../Results/unique_CIDR").st_size != 0:
        encrypt_file("../Results/unique_CIDR")
        files_encrypted += 1
    if os.path.exists("../Results/used_ips") and os.stat("../Results/used_ips").st_size != 0:
        encrypt_file("../Results/used_ips")
        files_encrypted += 1
    if os.path.exists("../Results/vnc") and os.stat("../Results/vnc").st_size != 0:
        encrypt_file("../Results/vnc")
        files_encrypted += 1
    if os.path.exists("../Results/webservers443") and os.stat("../Results/webservers443").st_size != 0:
        encrypt_file("../Results/webservers443")
        files_encrypted += 1
    if os.path.exists("../Results/wifis") and os.stat("../Results/wifis").st_size != 0:
        encrypt_file("../Results/wifis")
        files_encrypted += 1
    if os.path.exists("../Results/windows") and os.stat("../Results/windows").st_size != 0:
        encrypt_file("../Results/windows")
        files_encrypted += 1
    if os.path.exists("../Results/titles_webhosts") and os.stat("../Results/titles_webhosts").st_size != 0:
        encrypt_file("../Results/titles_webhosts")
        files_encrypted += 1
    if os.path.exists("../Results/blues") and os.stat("../Results/blues").st_size != 0:
        encrypt_file("../Results/blues")
        files_encrypted += 1
    if os.path.exists("../Results/snmp") and os.stat("../Results/snmp").st_size != 0:
        encrypt_file("../Results/snmp")
        files_encrypted += 1
    if os.path.exists("../Results/snmp_hosts") and os.stat("../Results/snmp_hosts").st_size != 0:
        encrypt_file("../Results/snmp_hosts")
        files_encrypted += 1
    if os.path.exists("../Results/radius") and os.stat("../Results/radius").st_size != 0:
        encrypt_file("../Results/radius")
        files_encrypted += 1
    if os.path.exists("../Results/snmp_enum") and os.stat("../Results/snmp_enum").st_size != 0:
        encrypt_file("../Results/snmp_enum")
        files_encrypted += 1
    if os.path.exists("../Results/sql_resolution") and os.stat("../Results/sql_resolution").st_size != 0:
        encrypt_file("../Results/sql_resolution")
        files_encrypted += 1
    if os.path.exists("../Results/upnp") and os.stat("../Results/upnp").st_size != 0:
        encrypt_file("../Results/upnp")
        files_encrypted += 1
    if os.path.exists("../Results/win_hosts") and os.stat("../Results/win_hosts").st_size != 0:
        encrypt_file("../Results/win_hosts")
        files_encrypted += 1
    if os.path.exists("../Results/smb_users") and os.stat("../Results/smb_users").st_size != 0:
        encrypt_file("../Results/smb_users")
        files_encrypted += 1
    if os.path.exists("../Results/shares") and os.stat("../Results/shares").st_size != 0:
        encrypt_file("../Results/shares")
        files_encrypted += 1
    if os.path.exists("../Results/arp") and os.stat("../Results/arp").st_size != 0:
        encrypt_file("../Results/arp")
        files_encrypted += 1
    if os.path.exists("../Results/traceroute") and os.stat("../Results/traceroute").st_size != 0:
        encrypt_file("../Results/traceroute")
        files_encrypted += 1
    if os.path.exists("../Results/sap_router") and os.stat("../Results/sap_router").st_size != 0:
        encrypt_file("../Results/sap_router")
        files_encrypted += 1
    if os.path.exists("../Results/sip_methods") and os.stat("../Results/sip_methods").st_size != 0:
        encrypt_file("../Results/sip_methods")
        files_encrypted += 1
    if os.path.exists("../Results/model") and os.stat("../Results/model").st_size != 0:
        encrypt_file("../Results/model")
        files_encrypted += 1
    if files_encrypted==48:
        print bcolors.TITLE + "All files encrypted successfully. Check the /Results directory" + bcolors.ENDC
    else:
        print bcolors.TITLE + str(files_encrypted)+" files encrypted successfully. Check the /Results directory" + bcolors.ENDC


def getKeyParts(key):
    keyA = key // len(SYMBOLS)
    keyB = key % len(SYMBOLS)
    return (keyA, keyB)


def checkKeys(keyA, keyB, mode):
    if keyA == 1 and mode == 'encrypt':
        return -1
    if keyB == 0 and mode == 'encrypt':
        return -1
    if keyA < 0 or keyB < 0 or keyB > len(SYMBOLS) - 1:
        return -1
    if cryptomath.gcd(keyA, len(SYMBOLS)) != 1:
        return -1

"""This function is used to encrypt a message with a given key.
If the key does not meet the requirements a new random key is 
automatically created and placed at the end of the same file 
after the valuable data."""
def encryptMessage(key, message):
    keyA, keyB = getKeyParts(key)
    checkKeys(keyA, keyB, 'encrypt')
    ciphertext = ''
    for symbol in message:
        if symbol in SYMBOLS:
            # encrypt this symbol
            symIndex = SYMBOLS.find(symbol)
            ciphertext += SYMBOLS[(symIndex * keyA + keyB) % len(SYMBOLS)]
        else:
            ciphertext += symbol  # just append this symbol unencrypted
    return ciphertext

"""This function is used to decrypt a message with a given key.
The new encrypted1 text will be overwritten in the same file."""
def decryptMessage(key, message):
    keyA, keyB = getKeyParts(key)
    checkKeys(keyA, keyB, 'decrypt')
    plaintext = ''
    modInverseOfKeyA = cryptomath.findModInverse(keyA, len(SYMBOLS))

    for symbol in message:
        if symbol in SYMBOLS:
            # decrypt this symbol
            symIndex = SYMBOLS.find(symbol)
            plaintext += SYMBOLS[(symIndex - keyB) * modInverseOfKeyA % len(SYMBOLS)]
        else:
            plaintext += symbol  # just append this symbol undecrypted
    return plaintext


def getRandomKey():
    while True:
        keyA = random.randint(2, len(SYMBOLS))
        keyB = random.randint(2, len(SYMBOLS))
        if cryptomath.gcd(keyA, len(SYMBOLS)) == 1:
            return keyA * len(SYMBOLS) + keyB

