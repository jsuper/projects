
from TprogressBar import *
from time import sleep

class FtpDownloader(object):
    """
    """

    def __init__(self,file_size ,local_path, delay=0.006):
        
        self.pb = TprogressBar('Downloading','=')
        self.local_file = open(local_path,'wb')
        self.file_size = file_size
        self.total = 0 
        self.delay = delay
    
    def write(self, data):
        self.total = self.total + len(data)
        self.local_file.write(data)
        progress = int((float(self.total)/float(self.file_size)) * 100 )
        self.pb.setProgress(progress)
        sleep(self.delay)

    def close(self):
        self.local_file.close()

        
        
