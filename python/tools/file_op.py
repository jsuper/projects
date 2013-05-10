
#This is the anotation
import os
import sys

def get_first_line_of(file_path):
    """get the first line of the given file
    
    Arguments:
    - `file_path`:
    """
    data_file = open(file_path,'rb')
    header = data_file.readline().strip()
    while not header:
        header = data_file.readline().strip()

    data_file.close()
    return header

def get_last_line_of(file_path):
    """
    Arguments:
    - `file_path`:
    """
    filesize = os.path.getsize(file_path)
    blocksize = 1024
    data_file = open(file_path, 'rb')
    if filesize > blocksize :
        maxseekpoint = (filesize // blocksize)
        data_file.seek(maxseekpoint*blocksize)
    elif filesize :
        maxseekpoint = blocksize % filesize
        data_file.seek(maxseekpoint)    
    lines =  data_file.readlines()
    for line in lines[::-1]:
        line = line.strip()
        if not line:
            pass
        else:
            last_line = line
            break
    
    data_file.close()
    return last_line

if __name__ == "__main__":
    print get_first_line_of(sys.argv[1])
    print get_last_line_of(sys.argv[1])







