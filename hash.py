#os.listdir
#os.stat
#os.walk
from dirhash import dirhash

import hashlib

#Run through filesystem
def flier(filename_or_directory):
    hashEd = hasher(filename_or_directory)
    time = get time funciton
    return #filename, hashEd, time

#Use SHA2 (SHA256) so that each file is hashed as it moves through the file system
def hasher(path):
    dir_sha256 = dirhash(path, "sha256")
    return dir_sha256

#Need:
#   Filename with full path
#   Hash
#   date/time file was observed

def main
    call flier
    write contents to file

#run and update the hash information, upon completion it should print out summary information that includes 
#   all new files found, 
#   any missing files, and 
#   any file that was modified.

def compare():
    import glob
    import os
    file = glob.glob("*.ipynb")
    file.sort(key=os.path.getmtime)
    This will list the most recent file, we could use this to find our most recent baseline to compare our data to

#Extra Credit
#Goal: Detect that a file was moved
#Add to your summary section an output that documents 
#   where the file is now, and 
#   where it was, and 
#   the time of the last scan that saw it in the older location.
