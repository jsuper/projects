# -*- coding:utf-8 -*-
# Emacs compiler
# @author Tang Ling
# @email tangling.life@gmail.com

import os
import sys
from os.path import join
from file_op import print_first_last_line

contains_provide=dict()

def init_priority_dicts(file_path):
    contains_provide.clear()
    for root,dirs,files in os.walk(file_path):
        for name in files:
            if name.endswith('el'):
                print join(root,name)
                print_first_last_line(join(root,name))
            
def get_alias_file_name(file_path):
    """
    Arguments:
    - `file_path`:
    """
    return ""


def parse_depend_el(file_path):
    """
    Arguments:
    - `file_path`:
    """
    file = open(file_path)
    while True:
        lines = file.readlines(1024)
        if not lines:
            break
        for line in lines:
            line = line.strip()
            if line.startswith('(require '):
                start = line.find('\'')+1
                end = line.find(')')
                print line[start:end]
            else:
                pass
    file.close()


def walk_directory(dir_path):
    """
    Arguments:
    - `dir_path`:
    """
    for root,dirs,files in os.walk(dir_path):
        for file_name in files:
            if file_name.endswith('el'):
                parse_depend_el(join(root,file_name))

def optimistic(file_path):
    """
    
    Arguments:
    - `file_path`:
    """
    file = open(file_path)
    while True:
        lines = file.readlines(1024)
        if not lines:
            break
        for line in lines:
            if line.startwith(';'):
                pass
            else:
                print line




def compile():
    """
    """
    dist_path = sys.argv[1]
    init_priority_dicts(dist_path)
    walk_directory(dist_path)

if __name__=="__main__":
    compile()

