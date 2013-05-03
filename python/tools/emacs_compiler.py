# -*- coding:utf-8 -*-
# Emacs compiler
# @author Tang Ling
# @email tangling.life@gmail.com

import os
import sys
from os.path import join

contains_provide=dict()

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
            if line.lstrip.startswith('(require '):
                print line
            else:
                pass


def walk_directory(dir_path):
    """
    
    Arguments:
    - `dir_path`:
    """
    for root,dirs,files in os.walk(dir_path):
        for file_name in files:
            if file_name.endswith('el'):
                

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
    walk_directory(dist_path)

if __name__=="__main__":
    compile()

