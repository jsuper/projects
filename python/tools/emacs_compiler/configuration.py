# -*- coding:utf-8 -*-
# This is the configuration entry for each *.el
# @author Tang Ling
# @email tangling.life@gmail.com

class Configuration(object):
    """
    """
    
    def __init__(self, filePath, referencedCount):
        """
        
        Arguments:
        - `path`:
        - `rely`:
        """
        self.filePath = filePath
        self.referencedCount = referencedCount
    
    def __str__(self):
        """
        
        Arguments:
        - `self`:
        """
        return "path is %s, rely count is %d" % (self.filePath, self.referencedCount)

    def __cmp__(self,compared):
        """Compare two configutations class according the referencedCount
        
        Arguments:
        - `self`:
        - `compared`:
        """
        if self.filePath and compared.filePath:
            #both the filePath of self and compared object is Not None
            result = cmp(self.referencedCount,compared.referencedCount)
            if result > 0 and self.referencedCount!=65535:
                result = -1
            elif result < 0 and compared.referencedCount!=65535:
                result = 1
        elif not self.filePath and compared.filePath:
            #self's filePath is None, but compared filePath is not None
            result = -1
        elif self.filePath and not compared.filePath:
            #self's filePath is not None, but compared filePath is None
            result = 1 
        else:
            result = cmp(self.referencedCount,compared.referencedCount)

        return result





        
        

