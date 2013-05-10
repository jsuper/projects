# -*- coding:utf-8 -*-
# Compiler for emacs
# @author Tang Ling
# @email tangling.life@gmail.com

from configuration import *
from os.path import join
import os
import sys

all_modules={}

def scan_files_and_generate_target(directory):
    """
    
    Arguments:
    - `directory`:
    """
    for root,dirs,files in os.walk(directory):
        for fileName in files:
            if fileName.endswith("el"):
                scan_file_content(join(root,fileName),fileName)

def scan_file_content(filePath,fileName):
    """
    
    Arguments:
    - `filePath`:
    """
    print 'start scanning file [%s]' % (fileName)
    targetFile = open(filePath)
    output = open('test/'+fileName,'w')
    provideAlias = None
    try:
        while True:
            lines = targetFile.readlines(1024)
            if not lines:
                break
            for line in lines:
                if line.startswith(';'):
                    pass
                elif line.strip().startswith('(require '):
                    handle_require_el_package(line.strip())
                elif line.strip().startswith('(provide '):
                    provideAlias = handle_provide_statement(line.strip(),fileName)
                else:
                    if line.strip():
                        output.write(line.rstrip()+'\n')
    finally:
        targetFile.close()
        output.close()

    if not provideAlias:
        all_modules[fileName] = Configuration(fileName,65535)

def handle_require_el_package(requireStatement):
    """
    
    Arguments:
    - `requireStatement`:
    """
    start = requireStatement.find('\'')
    end = requireStatement.rfind(')')
    moduleKey = requireStatement[start+1:end]
    if all_modules.has_key(moduleKey):
        all_modules[moduleKey].referencedCount+=1
    else:
        moduleConfiguraion = Configuration(None,-1)
        all_modules[moduleKey] = moduleConfiguraion


def handle_provide_statement(provideStatement,fileName):
    """
    
    Arguments:
    - `provideStatement`:
    - `fileName`:
    """
    start = provideStatement.find('\'')
    end = provideStatement.rfind(')')
    provideAlias = provideStatement[start+1:end]
    if all_modules.has_key(provideAlias):
        all_modules[provideAlias].filePath = fileName
    else:
        all_modules[provideAlias] = Configuration(fileName,-1)
    
    return provideAlias

def merge_all_modules():
    """
    """
    base = 'test'
    resultModules = sorted(all_modules.items(),key=lambda el:el[1],reverse=False)
    
    mergeTo = 'target.el'
    output = open(join(base,mergeTo),'w+')
    try:
        for module in resultModules:
            key = module[0]
            config = module[1]
            if not config.filePath:
                output.write('(require \''+key+')\n')
            else:
                output.write('\n;;begin configutation with ======'+config.filePath+'============\n')
                moduleFile = open(join(base,config.filePath))
                try:
                    while True:
                        lines = moduleFile.readlines(1024)
                        if not lines:
                            break
                        for line in lines:
                            output.write(line)
                finally:
                    moduleFile.close()
                os.remove(join(base,config.filePath))
    finally:
        output.close()                         

if __name__ == "__main__":
    
    target = sys.argv[1]
    scan_files_and_generate_target(target)
    merge_all_modules()
