# -*- coding:utf-8 -*-
# Compiler for emacs
# @author Tang Ling
# @email tangling.life@gmail.com

from configuration import *
from os.path import join,exists
import os
import sys
import argparse

all_modules={}

def scan_files_and_generate_target(directory):
    """
    
    Arguments:
    - `directory`:
    """
    base_build = join(directory,'build')
    if not exists(base_build):
        os.makedirs(base_build)
    for root,dirs,files in os.walk(directory):
        if "build" in dirs:
            dirs.remove("build")
        for file_name in files:
            if file_name.endswith("el"):
                scan_file_content(base_build,join(root,file_name),file_name)

def scan_file_content(build_target_path,file_path,file_name):
    """
    
    Arguments:
    - `file_path`:
    """
    print 'Start scanning file [%s]' % (file_path)
    target_file_object = open(file_path)
    output = open(join(build_target_path,file_name),'w')
    provide_alias = None
    try:
        while True:
            lines = target_file_object.readlines(1024)
            if not lines:
                break
            for line in lines:
                if line.startswith(';'):
                    pass
                elif line.strip().startswith('(require '):
                    handle_require_el_package(line.strip())
                elif line.strip().startswith('(provide '):
                    provide_alias = handle_provide_statement(line.strip(),file_name)
                else:
                    if line.strip():
                        output.write(line.rstrip()+'\n')
    finally:
        target_file_object.close()
        output.close()

    if not provide_alias:
       all_modules[file_name] = Configuration(file_name,65535)

def handle_require_el_package(require_package):
    """
    
    Arguments:
    - `require_package`:
    """
    start = require_package.find('\'')
    end = require_package.rfind(')')
    require_package_alias = require_package[start+1:end]
    if all_modules.has_key(require_package_alias):
        if all_modules[require_package_alias].file_path:
            all_modules[require_package_alias].referenced_count-=1
    else:
        all_modules[require_package_alias] = Configuration(None,0)


def handle_provide_statement(el_package_alias,file_name):
    """
    
    Arguments:
    - `el_package_alias`:
    - `file_name`:
    """
    start = el_package_alias.find('\'')
    end = el_package_alias.rfind(')')
    provide_alias = el_package_alias[start+1:end]
    if all_modules.has_key(provide_alias):
        all_modules[provide_alias].file_path = file_name
        all_modules[provide_alias].referenced_count -= 1
    else:
        all_modules[provide_alias] = Configuration(file_name,0)
    return provide_alias

def merge_all_modules(base_path):
    base = join(base_path,'build')
    generate_file_name = 'target.el'
    if exists(join(base,generate_file_name)):
        os.remove(join(base,generate_file_name))
    sorted_modules = sorted(all_modules.items(),key=lambda el:el[1],reverse=False)
    output = open(join(base,generate_file_name),'w+')
    try:
        for module in sorted_modules:
            key = module[0]
            config = module[1]
            print 'key is %s ==> configuration properties: %s ' % (key,config)
            if not config.file_path:
                output.write('(require \''+key+')\n')
            else:
                output.write('\n;;begin configutation with ======'+config.file_path+'============\n')
                module_file_object = open(join(base,config.file_path))
                try:
                    while True:
                        lines = module_file_object.readlines(1024)
                        if not lines:
                            break
                        for line in lines:
                            output.write(line)
                    
                    os.remove(join(base,config.file_path))
                finally:
                    module_file_object.close()

    finally:
        output.close() 

def compile(lisp_package_path):
    """
    
    Arguments:
    - `lisp_package_path`:
    """
    scan_files_and_generate_target(lisp_package_path)
    merge_all_modules(lisp_package_path)
                        

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Emacs extension package compiler')
    parser.add_argument('-path',help='The absolute path of your lisp packages')
    args = parser.parse_args()
    if args.path and len(args.path) > 0:
        compile(args.path)
    else:
        parser.print_help()
