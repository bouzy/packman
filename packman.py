#!/usr/bin/python3.5

from os import system as sys
from sys import argv
from time import strftime

title = 'PACKMAN'
version = '1.0'
updating = '------------\n- UPDATING -\n------------'
removing = '------------\n- REMOVING -\n------------'
adding = '--------------\n- INSTALLING - \n--------------'
cleaning_up = '---------------\n- CLEANING UP -\n---------------'
to_be_removed = '-----------------\n- TO BE REMOVED -\n-----------------'
to_be_added = '-------------------\n- TO BE INSTALLED -\n-------------------'
log_file = 'log_file.log'
full_time = '%X'
month = '%m'
day = '%d'
full_day = '%A'
full_year = '%Y'
log_date = strftime(month + '/' + day + '/' + full_year + '-' + full_time)
app_remove_list = (['libreoffice-core',
    'libreoffice-common',
    'account-plugin',
    'totem',
    'totem-common',
    'unity-scopes-runner',
    'unity-scope-video-remote',
    'unity-lens-files',
    'unity-lens-photos',
    'unity-lens-music',
    'unity-lens-video'])
app_add_list = (['gcc',
    'g++',
    'make',
    'vim',
    'git',
    'python-pip',
    'htop',
    'p7zip-full',
    'wget', 'curl',
    'traceroute',
    'nmap',
    'vlc'])
app_remove_list_amount = 0
app_add_list_amount = 0

for list_count_zero in app_remove_list:
    app_remove_list_amount += 1

for list_count_one in app_add_list:
    app_add_list_amount += 1

def file_space_validator():
    log_file_content_validator = open(log_file, 'r')
    log_file_content_validator_reader = log_file_content_validator.read()
    if log_file_content_validator_reader == '':
        log_file_content_validator.close()
    else:
        log_file_content_validator.close()
        log_file_space_adder = open(log_file, 'a')
        log_file_space_adder.write('\n')
        log_file_space_adder.close()

def app_remove():
    remove_counter = 0
    print(removing)
    file_space_validator()
    sys('echo ' + log_date + ' >> ' + log_file)
    for remove in app_remove_list:
        remove_counter += 1
        remove_counter_string = '[' + str(remove_counter) + '/' + str(app_remove_list_amount) + ']'
        print(str(remove_counter_string + ' ' + remove))
        sys('sudo apt-get -y remove ' + remove + ' >> ' + log_file)
    print(cleaning_up)
    print('Removing packages which are no longer needed')
    sys('sudo apt-get -y autoremove >> ' + log_file)

def app_add():
    add_counter = 0
    print(updating)
    sys('sudo apt-get update')
    file_space_validator()
    sys('echo ' + log_date + ' >> ' + log_file)
    print(adding)
    for add in app_add_list:
        add_counter += 1
        add_counter_string = '[' + str(add_counter) + '/' + str(app_add_list_amount) + ']'
        print(str(add_counter_string + ' ' + add))
        sys('sudo apt-get -y install ' + add + ' >> ' + log_file)
    print(updating)
    sys('sudo apt-get update')

def app_remove_list_terminal():
    remove_list_counter = 0
    print(to_be_removed)
    for remove_list in app_remove_list:
        remove_list_counter += 1
        remove_list_counter_string = '[' + str(remove_list_counter) + '/' + str(app_remove_list_amount) + ']'
        print(str(remove_list_counter_string + ' ' + remove_list))

def app_add_list_terminal():
    add_list_counter = 0
    print(to_be_added)
    for add_list in app_add_list:
        add_list_counter += 1
        add_list_counter_string = '[' + str(add_list_counter) + '/' + str(app_add_list_amount) + ']'
        print(str(add_list_counter_string + ' ' + add_list))

def help():
    options_dictionary = (['rm - removes the selected packages',
        'in - installs the selected packages',
        'lrm - lists the selected packages to be removed',
        'lin - lists the selected packages to be installed',
        'h - help menu'])
    print(title + ' ' + version + '\n')
    print('USAGE: sudo python packman.py [option]\n\nOPTIONS:')
    for print_options_dictionary in options_dictionary:
        print('  ' + print_options_dictionary)

def main():
    if 'rm' in argv:
        app_remove()
    elif 'in' in argv:
        app_add()
    elif 'lrm' in argv:
        app_remove_list_terminal()
    elif 'lin' in argv:
        app_add_list_terminal()
    elif 'h' in argv:
        help()
    else:
        help()

if __name__ == '__main__':
    main()
