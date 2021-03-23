#os.listdir
#os.stat
#os.walk
import hashlib

#Run through filesystem
def flier(filename_or_directory):
    hashEd = hasher(filename_or_directory)
    time = get time funciton
    return [filename, hashEd, time]

#Use SHA2 (SHA256) so that each file is hashed as it moves through the file system
def hasher(filename_or_directory):
    #hash it
    return #hash

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

#Extra Credit
#Goal: Detect that a file was moved
#Add to your summary section an output that documents 
#   where the file is now, and 
#   where it was, and 
#   the time of the last scan that saw it in the older location.
