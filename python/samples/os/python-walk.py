# -*- coding:utf-8 -*-
# This is the sample about the walk function in OS module
# @author Tang Ling
# @email tangling.life@gmail.com

import sys
import os,stat
import argparse

def rmdir(path):
    """Recrusivly delete all files in the given directory
    
    Arguments:
    - `path`:
    """
    if os.path.exists(path):
        for root,dirs,file_names in os.walk(path,topdown=False):
            for file_name in file_names:
                del_path(os.path.join(root,file_name))
            for dir_name in dirs:
                del_path(os.path.join(root,dir_name))
        
        os.rmdir(path)

def del_path(path):
    """Delete the given file or folder
    
    Arguments:
    - `path`:
    """
    if check_path(path):
        if os.path.isdir(path):
            os.rmdir(path)
        else:
            os.remove(path)


def check_path(path):
    """Check the given path is read-only, if that then change it to rw
    
    Arguments:
    - `path`:
    """
    exist = os.path.exists(path)
    if exist:
        os.chmod(full_path,stat.S_IWRITE)

    return exist


if __name__=='__main__':
     parser = argparse.ArgumentParser(description='Remove directory')
     parser.add_argument('-rm', help='The directory path you want to remove',required=True)
     args = parser.parse_args()
     if args.rm and len(args.rm) > 0:
         print args.rm
         from time import clock
         start = clock()
         rmdir(args.rm)
         end = clock()
         
         print 'Spend times(sec) ', (end-start)/1000000
         
