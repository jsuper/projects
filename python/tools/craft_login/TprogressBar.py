
"""
A progress bar for terminal
"""

class TprogressBar(object):
    """
    """
    _progress_format = '%s [%-50s] %d%%\r'

    def __init__(self, head_str,progress_char='*'):
        """
        
        Arguments:
        - `head_str`:
        """
        self.head_str = head_str
        self.progress_char = progress_char

    def setProgress(self,progress):
        """
        
        Arguments:
        - `self`:
        - `progress`:
        """
        c_progress = int(float(progress)/float(100) * 50)
        progress_bar = self.progress_char * c_progress
        print TprogressBar._progress_format % (self.head_str, progress_bar, progress),



        
