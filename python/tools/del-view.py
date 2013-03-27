# -*- coding:utf-8 -*-
# Using this script to delete the snapshot view of clearcase which was not used
# @author Tang Ling
# @email tangling.life@gmail.com

import os
import argparse
import re
from subprocess import Popen, PIPE, STDOUT

def del_snapshot_view(args):
    """This function is used to delete the snaptshot view in current computer
    
    Arguments:
    - `args`: The view name which should be ignored
    """
    views_data_dict = dict()
    username = os.environ['USERNAME']
    pattern = re.compile(r'^' + username + '.*snap.*')
    views = os.popen('cleartool lsview').readlines()
    for line in views:
        strip_line = line.strip()
        if pattern.match(strip_line) :
            spilt_lines = strip_line.split(' ')
            del_view(spilt_lines[0])

def del_view(view_name):
    """delete the view
    
    Arguments:
    - `view_name`:
    """
    print view_name + ' will be deleted '
    proc = Popen(['cleartool','rmview','-tag',view_name], stdout=PIPE, stdin=PIPE,stderr=STDOUT)
    stdoutdata,stderrdata = proc.communicate('yes\n')
    print stdoutdata
    while p.wait():
        if p.returncode == 1:
            break   
    if p.returncode == 1:
        print 'delete view [' + view_name+ '] failed'
    else:
        print 'delete view successfully'

def clean_file(view_name):
    """Clean all related files according to the filename
    
    Arguments:
    - `view_name`:
    """
    src = 'c:/viewdata/'+view_name
    if os.path.exist(src) and os.path.isdir(src):
        
        
        

    

if __name__ == '__main__':
    
    parser = argparse.ArgumentParser(description='Clearcase snapshot view deltet tools')
    parser.add_argument('-iv', nargs='+', help='The view name you want to ignore, support regex')
    parser.add_argument('-name', nargs='+', help='The view name you want to detele, must be fully view name')
    args = parser.parse_args()
#    del_snapshot_view(args.iv)
    if args.name and len(args.name) > 0:
        for name in args.name:
            del_view(name)
    elif args.iv and len(args.iv) > 0:
        del_snapshot_view(args.iv)
    else:
        parser.print_help()

    
    







