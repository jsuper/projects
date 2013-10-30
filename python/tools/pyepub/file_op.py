#file operatoin
from os.path import exists as fexists
from shutil import rmtree, copytree, ignore_patterns

class Dir():
    def remove(path):
        '''
        remove the directory
        '''
        if fexists(path):
            rmtree(path)
    
    def create(path):
        '''
        create directory
        '''
        if not fexists(path):
            from os import makedirs
            makedirs(path)
        

    def remove_then_create(path):
        '''
        remove the directory firstly, then create new one
        '''
        Dir.remove(path)
        Dir.create(path)

    def copy(source, dist, ignore=None):
        '''
        copy the directory to distination
        '''
        if ignore:
            ignore_pattern = ignore_patterns(ignore)
        copytree(source, dist, ignore=ignore_pattern)
        
        

