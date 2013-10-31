#file operatoin
import os, stat
from os.path import exists as fexists
from shutil import rmtree, copytree, ignore_patterns

class File():
    @staticmethod
    def write(content, path, mode='w'):
        '''
        write the content to the path
        '''
        with open(path, mode) as f:
            f.write(content)

class Dir():
    @staticmethod
    def remove(path):
        '''
        remove the directory
        '''
        if fexists(path):
            rmtree(path)
    
    @staticmethod
    def create(path):
        '''
        create directory
        '''
        if not fexists(path):
            os.makedirs(path)
            os.chmod(path, stat.S_IWRITE | stat.S_IREAD)
        
    @staticmethod
    def remove_then_create(path):
        '''
        remove the directory firstly, then create new one
        '''
        Dir.remove(path)
        Dir.create(path)
    
    @staticmethod
    def copy(source, dist, *ignore):
        '''
        copy the directory to distination
        '''
        if ignore:
            ignore_pattern = ignore_patterns(*ignore)
        copytree(source, dist, ignore=ignore_pattern)
