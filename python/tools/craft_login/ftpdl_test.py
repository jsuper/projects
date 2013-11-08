
from ftpdl import FtpDownloader

import os
from os.path import exists
from ftplib import FTP

save_path = 'c:/tmp/install.exe' 
if exists(save_path):
    os.remove(save_path)

ftp_root = 'Minilink_Craft/MLCraft 2.22/R22A42'

def test_download():
    """
    """
    ftp = FTP('172.16.121.170')
    ftp.login()
    ftp.cwd(ftp_root)
    file_size = ftp.size('install.exe')
    print file_size

    downloader = FtpDownloader(file_size, save_path)
    ftp.retrbinary('RETR install.exe',downloader.write, 1024*1024)
    ftp.quit()
    downloader.close()

test_download()











