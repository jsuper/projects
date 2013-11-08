
# craft login helper

import os
from os import path
import argparse

root_path=""

def get_all_installed_craft(base_path):
    all_crafts = {}
    if path.exists(base_path):
        count = 1
        root_path = base_path
        for dir_name in os.listdir(base_path):
            if path.isdir(path.join(base_path,dir_name)):
                all_crafts[count]=dir_name
                count += 1
    return all_crafts



if '__main__' == __name__:
    parser = argparse.ArgumentParser(description='MINI LINK Craft login helper')
    parser.add_argument('-i',metavar="CRAFT_VERSION",help='install craft')
    parser.add_argument('-u',metavar="CRAFT_VERSION",help='uninstall craft')
    parser.add_argument('-path',help='the root path of all installed crafts')
    parser.add_argument('-ip',help='The ip of node, default is 172.16.121.133')
    parser.add_argument('-username',help='The username used to login, default is control_user')
    parser.add_argument('-password',help='The password used to login, default is ericsson')
    
    args = parser.parse_args()
    if args.path and len(args.path)>0:
        _path = args.path
    else:
        _path = 'C:/Program Files/MINI-LINK-Craft'
        
    if args.ip and len(args.ip)>0:
        _ip = args.ip
    else:
        _ip = '172.16.121.133'

    if args.username and len(args.username)>0:
        _username = args.username
    else:
        _username = 'control_user'
    

    if args.password and len(args.password)>0:
        _password = args.password
    else:
        _password = 'ericsson'
        
    all_crafts = get_all_installed_craft(_path)
    from print_helper import *
    print_header('Craft login helper')
    print_to_table(all_crafts)
    print ''
    try:
       login_to = int(raw_input('\nEnter the number of Craft which you want to login:'))
    except:
        print '\nPlease enter corrected number'
        login_to = int(raw_input('Enter the number of Craft which you want to login:'))

    target_ = all_crafts[login_to]
    for file_name in os.listdir(path.join(_path,target_,'bin')):
        if file_name.endswith('.exe'):
            executable = path.join(_path,target_,'bin',file_name)
            cmd = '"{0}" -ip {1} -user {2} -password {3}'.format(str(executable),_ip,_username,_password)
            from subprocess import call
            call(cmd,shell=True)                                                                   
            break
        

    
    
