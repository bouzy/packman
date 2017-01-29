#!/usr/bin/python

from os import system as sys
from sys import argv
from time import strftime

def app_remove():
    print removing
    remove_counter = 0
    file_space_validate()
    sys("echo " + log_date + " >> " + log_file)
    for remove in app_remove_list:
        remove_counter += 1
	remove_counter_string = "[" + str(remove_counter) + "/" + str(app_remove_list_amount) + "]"
	print str(remove + remove_counter_string)
	sys("sudo apt-get -y remove " + remove + " >> " + log_file)
    print cleaning_up
    print "Removing unused dependencies"
    sys("sudo apt-get -y autoremove >> " + log_file)
    sys("sudo apt-get clean")

def app_add():
    print updating
    sys("sudo apt-get update")
    add_counter = 0
    file_space_validate()
    sys("echo " + log_date + " >> " + log_file)
    print adding
    for add in app_add_list:
        add_counter += 1
        add_counter_string = "[" + str(add_counter) + "/" + str(app_add_list_amount) + "]"
	print str(add + add_counter_string)
	sys("sudo apt-get -y install " + add + " >> " + log_file)
    print updating
    sys("sudo apt-get update")

def app_remove_list_terminal():
    remove_list_counter = 0
    print to_be_removed
    for remove_list in app_remove_list:
        remove_list_counter += 1
	remove_list_counter_string = "[" + str(remove_list_counter) + "/" + str(app_remove_list_amount) + "]"
	print str(remove_list + remove_list_counter_string)

def app_add_list_terminal():
    add_list_counter = 0
    print to_be_added
    for add_list in app_add_list:
        add_list_counter += 1
	add_list_counter_string = "[" + str(add_list_counter) + "/" + str(app_add_list_amount) + "]"
	print str(add_list + add_list_counter_string)

def notes():
    print readme + 'The virtualbox application "virtualbox" and virtualbox extension pack "virtualbox-ext-pack" must be installed manually'

def help():
    print "\n\nCOMMAND     DESCRIPTON"
    print "     -h     Displays the list of commands"
    print "     -r     Removes the listed applictions."
    print "     -a     Adds the listed applications."
    print "    -rl     Lists the applications to be removed."
    print "    -al     Lists the applications to be added."

def command_selector():
    if "-r" in argv:
        app_remove()
    elif "-a" in argv:
        app_add()
    elif "-rl" in argv:
        app_remove_list_terminal()
    elif "-al" in argv:
        app_add_list_terminal()
    elif "-h" in argv:
        help()
    else:
        help()

if __name__ == "__main__":
    title = "UCAM" #Ubuntu Custom Application Manager
    version = "0.1"
    updating = "\n\n------------\n- UPDATING -\n------------"
    removing = "\n\n------------\n- REMOVING -\n------------"
    adding = "\n\n----------\n- ADDING - \n----------"
    cleaning_up = "\n\n---------------\n- CLEANING UP -\n---------------"
    to_be_removed = "\n\n-----------------\n- TO BE REMOVED -\n-----------------"
    to_be_added = "\n\n---------------\n- TO BE ADDED -\n---------------"
    readme = "\n\n---------\n- NOTES -\n---------\n"
    log_file = "log_file.log"
    #log_file = "test_log_file.log"
    full_time = "%X"
    month = "%m"
    day = "%d"
    full_day = "%A"
    full_year = "%Y"
    log_date = strftime(month + "/" + day + "/" + full_year + "-" + full_time)
    app_remove_list = ["libreoffice-core", "libreoffice-common", "account-plugin", "totem", 
    "totem-common", "unity-scopes-runner", "unity-scope-video-remote", "unity-lens-files", 
    "unity-lens-photos", "unity-lens-music", "unity-lens-video"]
    app_add_list = ["gcc", "g++", "make", "vim", "terminator", "octave", "git", "python-pip",
    "dconf-tools", "htop", "p7zip-full", "psensor", "wget", "curl", "nmap", "zenmap", "filezilla","vlc"]
    app_remove_list_amount = 0
    for list_count_zero in app_remove_list:
        app_remove_list_amount += 1
    app_add_list_amount = 0
    for list_count_one in app_add_list:
        app_add_list_amount += 1
    def file_space_validate():
        log_file_content_validator = open(log_file, "r")
	log_file_content_validator_reader = log_file_content_validator.read()
	if log_file_content_validator_reader == "":
            log_file_content_validator.close()
	else:
            log_file_content_validator.close()
	    log_file_space_adder = open(log_file, "a")
	    log_file_space_adder.write("\n")
	    log_file_space_adder.close()
    print title, version
    command_selector()
    notes()

