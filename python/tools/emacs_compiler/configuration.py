# -*- coding:utf-8 -*-
# This is the configuration entry for each *.el
# @author Tang Ling
# @email tangling.life@gmail.com

class Configuration(object):
    """
    """
    
    def __init__(self, file_path, referenced_count):
        """
        
        Arguments:
        - `path`:
        - `rely`:
        """
        self.file_path = file_path
        self.referenced_count = referenced_count
    
    def __str__(self):
        """
        
        Arguments:
        - `self`:
        """
        return "path: %s, ref_count: %d" % (self.file_path, self.referenced_count)

    def __cmp__(self,compared):
        """Compare two configutations class according the referenced_count
        
        Arguments:
        - `self`:
        - `compared`:
        """
        result = cmp(self.referenced_count,compared.referenced_count)
        if self.referenced_count==0 and compared.referenced_count==0:
            result = cmp(self.file_path,compared.file_path) * -1
        return result





        
        

