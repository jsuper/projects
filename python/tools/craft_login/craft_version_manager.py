# This is used to install or uninstall craft

FTP_ADDRESS='172.16.121.170' #default ftp address
ROOT_DIR='Minilink_Craft' #Root craft installer directory
DOWNLOAD_DIR='c:/tmp'

import os
from ftplib import FTP
from os.path import exists
from os.path import join

def download_craft_from_ftp (craft_version):
    dist_folder = get_dist_folder(craft_version)   
    local_path = join(DOWNLOAD_DIR,dist_folder)
    path_ = join(DOWNLOAD_DIR,craft_version)
    if not exists(path_):
        os.makedirs(path_)

    ftp = FTP(FTP_ADDRESS)
    ftp.login()
    ftp.cwd(join(ROOT_DIR,dist_folder,craft_version))    
    ftp.retrbinary('RETR install.exe',open(join(path_,'install.exe'),'wb').write)
    ftp.quit()
    

def get_dist_folder(craft_version):
    from re import match
    matcher = match(r'([A-Z])([0-9]{1,2})(.*)',craft_version)
    if matcher:
        release_number =  matcher.group(2)
        return 'MLCraft 2.{0}'.format(release_number)

    

download_craft_from_ftp('R22A40')

