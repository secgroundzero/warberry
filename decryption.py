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

from src.utils.encryption import *
import os,sys
from src.utils.delete_files import *

"""This method decrypts a specific file named filename and 
the encrypted new text is on the same file. The file is now
overwritten."""

def decrypt_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines() #read file and create lines
        key = (lines[len(lines)-1]) #last line is key
        #check if key is empty and error
        if  not key:
            print "The key is empty!!!!"
            sys.exit(-1)
        #read key
        temp_key=""
        for i in key:
            if not(i.isdigit()):
                break
            else:
                temp_key=temp_key.strip()+i
        #convert  key string to int
        temp_key=int(temp_key)
        key= temp_key
        lines = lines[:-1] #read all lines expect last one cause its the key
        #combine decrypted1 text lines.
        temp_translated=""
        for i in lines:
            temp_translated+=str(i)
        #decrypt text string.
        translated = decryptMessage(key, temp_translated)
        #finally overwrite file with encrypted text.
        with open(filename, 'w') as new_file:
            new_file.write(translated)

"""This function is used to decrypt the decryption part password.
Returns the access password."""
def decrypt_password_file(filename):
    temp_translated = ""
    with open(filename, 'r') as file:
        lines = file.readlines() #read file and create lines
        key = (lines[len(lines)-1]) #last line is key
        #check if key is empty and error
        if  not key:
            print "The key is empty!!!!"
            sys.exit(-1)
        #read key
        temp_key=""
        for i in key:
            if not(i.isdigit()):
                break
            else:
                temp_key=temp_key.strip()+i
        #convert  key string to int
        temp_key=int(temp_key)
        key= temp_key
        lines = lines[:-1] #read all lines expect last one cause its the key
        #combine translated text lines.
        for i in lines:
            temp_translated+=str(i)
    password = decryptMessage(key, temp_translated)
    return password

"""This method is used to decrypt all the appropriate files.
The decryption key is at the last line at the end of the file."""
def decrypt_files():
    files_decrypted=0

    if os.path.exists("../Results/hostnames")and os.stat("../Results/hostnames").st_size != 0:
        decrypt_file("../Results/hostnames")
        files_decrypted+=1
    if os.path.exists("../Results/http_titles")and os.stat("../Results/http_titles").st_size != 0:
        decrypt_file("../Results/http_titles")
        files_decrypted+=1
    if os.path.exists("../Results/live_ips")and os.stat("../Results/live_ips").st_size != 0:
        decrypt_file("../Results/live_ips")
        files_decrypted+=1
    if os.path.exists("../Results/liveip_hosts")and os.stat("../Results/liveip_hosts").st_size != 0:
        decrypt_file("../Results/liveip_hosts")
        files_decrypted+=1
    if os.path.exists("../Results/mvp_names")and os.stat("../Results/mvp_names").st_size != 0:
        decrypt_file("../Results/mvp_names")
        files_decrypted+=1
    if os.path.exists("../Results/mvps")and os.stat("../Results/mvps").st_size != 0:
        decrypt_file("../Results/mvps")
        files_decrypted+=1
    if os.path.exists("../Results/nameservers")and os.stat("../Results/nameservers").st_size != 0:
        decrypt_file("../Results/nameservers")
        files_decrypted+=1
    if os.path.exists("../Results/os_enum")and os.stat("../Results/os_enum").st_size != 0:
        decrypt_file("../Results/os_enum")
        files_decrypted+=1
    if os.path.exists("../Results/pcap_results")and os.stat("../Results/pcap_results").st_size != 0:
        decrypt_file("../Results/pcap_results")
        files_decrypted+=1
    if os.path.exists("../Results/robots")and os.stat("../Results/robots").st_size != 0:
        decrypt_file("../Results/robots")
        files_decrypted+=1
    if os.path.exists("../Results/running_status")and os.stat("../Results/running_status").st_size != 0:
        decrypt_file("../Results/running_status")
        files_decrypted+=1
    if os.path.exists("../Results/targets")and os.stat("../Results/targets").st_size != 0:
        decrypt_file("../Results/targets")
        files_decrypted+=1
    if os.path.exists("../Results/titles_webhosts")and os.stat("../Results/titles_webhosts").st_size != 0:
        decrypt_file("../Results/titles_webhosts")
        files_decrypted+=1
    if os.path.exists("../Results/unique_hosts")and os.stat("../Results/unique_hosts").st_size != 0:
        decrypt_file("../Results/unique_hosts")
        files_decrypted+=1
    if os.path.exists("../Results/urls")and os.stat("../Results/urls").st_size != 0:
        decrypt_file("../Results/urls")
        files_decrypted+=1
    if os.path.exists("../Results/wafed")and os.stat("../Results/wafed").st_size != 0:
        decrypt_file("../Results/wafed")
        files_decrypted+=1
    if os.path.exists("../Results/webhosts")and os.stat("../Results/webhosts").st_size != 0:
        decrypt_file("../Results/webhosts")
        files_decrypted+=1
    if os.path.exists("../Results/webs")and os.stat("../Results/webs").st_size != 0:
        decrypt_file("../Results/webs")
        files_decrypted+=1
    if os.path.exists("../Results/webservers80") and os.stat("../Results/webservers80").st_size != 0:
        decrypt_file("../Results/webservers80")
        files_decrypted+=1
    if os.path.exists("../Results/webservers8080") and os.stat("../Results/webservers8080").st_size != 0:
        decrypt_file("../Results/webservers8080")
        files_decrypted+=1
    if os.path.exists("../Results/avail_ips") and os.stat("../Results/avail_ips").st_size !=0 :
        decrypt_file("../Results/avail_ips")
        files_decrypted+=1
    if os.path.exists("../Results/dns") and os.stat("../Results/dns").st_size !=0 :
        decrypt_file("../Results/dns")
        files_decrypted+=1
    if os.path.exists("../Results/mysql") and os.stat("../Results/mysql").st_size !=0 :
        decrypt_file("../Results/mysql")
        files_decrypted+=1
    if os.path.exists("../Results/nfs") and os.stat("../Results/nfs").st_size !=0 :
        decrypt_file("../Results/nfs")
        files_decrypted+=1
    if os.path.exists("../Results/statics") and os.stat("../Results/statics").st_size !=0 :
        decrypt_file("../Results/statics")
        files_decrypted+=1
    if os.path.exists("../Results/tightvnc") and os.stat("../Results/tightvnc").st_size !=0 :
        decrypt_file("../Results/tightvnc")
        files_decrypted+=1
    if os.path.exists("../Results/unique_CIDR") and os.stat("../Results/unique_CIDR").st_size != 0:
        decrypt_file("../Results/unique_CIDR")
        files_decrypted += 1
    if os.path.exists("../Results/used_ips") and os.stat("../Results/used_ips").st_size != 0:
        decrypt_file("../Results/used_ips")
        files_decrypted += 1
    if os.path.exists("../Results/vnc") and os.stat("../Results/vnc").st_size != 0:
        decrypt_file("../Results/vnc")
        files_decrypted += 1
    if os.path.exists("../Results/webservers443")and os.stat("../Results/webservers443").st_size != 0:
        decrypt_file("../Results/webservers443")
        files_decrypted+=1
    if os.path.exists("../Results/wifis")and os.stat("../Results/wifis").st_size != 0:
        decrypt_file("../Results/wifis")
        files_decrypted+=1
    if os.path.exists("../Results/windows")and os.stat("../Results/windows").st_size != 0:
        decrypt_file("../Results/windows")
        files_decrypted+=1
    if os.path.exists("../Results/titles_webhosts")and os.stat("../Results/titles_webhosts").st_size != 0:
        decrypt_file("../Results/titles_webhosts")
        files_decrypted+=1
    if os.path.exists("../Results/blues")and os.stat("../Results/blues").st_size != 0:
        decrypt_file("../Results/blues")
        files_decrypted+=1
    if os.path.exists("../Results/snmp")and os.stat("../Results/snmp").st_size != 0:
        decrypt_file("../Results/snmp")
        files_decrypted+=1
    if os.path.exists("../Results/snmp_hosts")and os.stat("../Results/snmp_hosts").st_size != 0:
        decrypt_file("../Results/snmp_hosts")
        files_decrypted+=1
    if os.path.exists("../Results/radius") and os.stat("../Results/radius").st_size != 0:
        decrypt_file("../Results/radius")
        files_decrypted += 1
    if os.path.exists("../Results/snmp_enum") and os.stat("../Results/snmp_enum").st_size != 0:
        decrypt_file("../Results/snmp_enum")
        files_decrypted += 1
    if os.path.exists("../Results/sql_resolution") and os.stat("../Results/sql_resolution").st_size != 0:
        decrypt_file("../Results/sql_resolution")
        files_decrypted += 1
    if os.path.exists("../Results/upnp") and os.stat("../Results/upnp").st_size != 0:
        decrypt_file("../Results/upnp")
        files_decrypted += 1
    if os.path.exists("../Results/win_hosts") and os.stat("../Results/win_hosts").st_size != 0:
        decrypt_file("../Results/win_hosts")
        files_decrypted += 1
    if os.path.exists("../Results/smb_users") and os.stat("../Results/smb_users").st_size != 0:
        decrypt_file("../Results/smb_users")
        files_decrypted += 1
    if os.path.exists("../Results/shares") and os.stat("../Results/shares").st_size != 0:
        decrypt_file("../Results/shares")
        files_decrypted += 1
    if os.path.exists("../Results/traceroute") and os.stat("../Results/traceroute").st_size != 0:
        decrypt_file("../Results/traceroute")
        files_decrypted += 1
    if os.path.exists("../Results/arp") and os.stat("../Results/arp").st_size != 0:
        decrypt_file("../Results/arp")
        files_decrypted += 1
    if os.path.exists("../Results/sap_router") and os.stat("../Results/sap_router").st_size != 0:
        decrypt_file("../Results/sap_router")
        files_decrypted += 1
    if os.path.exists("../Results/sip_methods") and os.stat("../Results/sip_methods").st_size != 0:
        decrypt_file("../Results/sip_methods")
        files_decrypted += 1
    if os.path.exists("../Results/model") and os.stat("../Results/model").st_size != 0:
        decrypt_file("../Results/model")
        files_decrypted += 1
    if files_decrypted==48:
        print bcolors.TITLE + "All files decrypted successfully. Check the /Results directory" + bcolors.ENDC
    else:
        print bcolors.TITLE + str(files_decrypted)+" files decrypted successfully. Check the /Results directory" + bcolors.ENDC

"""This function is used to display a menu on the console and read-validate the
action that the user wants to perform. Returns the users choice."""
def show_menu():
    print "Select one of the following options by giving the number of your choice:"
    print "1. Decrypt files in /Result directory. (Give '1' for this option.)"
    print "2. Change the current password for decryption access.  (Give '2' for this option)"
    print "3. Exit. (Give '3' for this option)"
    choice = raw_input()
    while choice!="1" and choice!="2" and choice!="3":
        print "WRONG INPUT! PLEASE GIVE 1,2 OR 3 FOR THE DESIRED ACTION!"
        print "1. Decrypt files in /Result directory. (Give '1' for this option.)"
        print "2. Change the current password for decryption access.  (Give '2' for this option)"
        print "3. Exit. (Give '3' for this option)"
        choice=raw_input()
    #correct option given by the user till this point.
    return choice


"""This dunction is used to perform one of the applicable actions that the
user has on the decryption part of the warrberry."""
def perform_action(choice,password):
    if str(choice) == "1":
        decrypt_files()
        print bcolors.TITLE+"The System will now exit."+bcolors.ENDC
    elif str(choice) == "2":
        print bcolors.TITLE+"PLEASE GIVE THE NEW PASSWORD:"+bcolors.ENDC
        new_password=str(input())
        with open("password", 'w') as pass_file:
            key = randint(0, 100000000)
            keyA, keyB = getKeyParts(key)
            while checkKeys(keyA, keyB, 'encrypt') == -1 or gcd(keyA, len(SYMBOLS)) != 1:
                key = randint(0, 100000000)
                keyA, keyB = getKeyParts(key)
            encrypted_pass = encryptMessage(key, new_password)
            pass_file.write(encrypted_pass+"\n"+str(key))
        print bcolors.TITLE+"PASSWORD SUCCESSFULLY REPLACED!!! THE SYSTEM WILL NOW EXIT!!!"+bcolors.ENDC
        sys.exit(0)
    elif str(choice)=="3":
        print bcolors.TITLE + "THE SYSTEM WILL NOW EXIT!!!" + bcolors.ENDC
        sys.exit(0)
    else:
        print bcolors.TITLE+"WRONG CHOICE GIVEN!!!!"+bcolors.ENDC
        sys.exit(1)

def main():
    #read decryption password from file.
    password=decrypt_password_file("password")
    #default password is 123.
    #counter for wrong times input.
    wrong_t=0
    #ask for user password.
    user_pass=raw_input("Please provide your password:\n")
    #maximum tries equals 3.
    while wrong_t<2:
        if user_pass==str(password).translate(None,' \n'):
            # successful login.
            # show main menu and get user's choice.
            choice = show_menu()
            # perform appropriate action according to the user's choice.
            perform_action(choice, password)
            sys.exit(0)
        #wrong password given by the user if this point is reached.
        print "WRONG PASSWORD ENTERED! PLEASE GIVE YOUR PASSWORD AGAIN:\n"
        user_pass = raw_input() #read new user input.
        wrong_t = wrong_t + 1  #increase number of tries.
    #password given wrong 3 times if this point is reached so exit for safety.
    print "WRONG PASSWORD ENTERED TOO MANY TIMES, THE SYSTEM WILL EXIT FOR SAFETY!\n"
    print "ALL FILES WILL BE DELETED!!!\n"
    delete_files()
    sys.exit(-1)



if __name__ == "__main__":
    # execute main function
    main()
