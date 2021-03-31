import os
import hashlib
from dirhash import dirhash
import csv
import time #All time formats are MMDDYYYY_hhmmss

#Global Variables
string = ""
string2 = ""
r2 = []
d2 = []
ignore_list = ["/dev", "/proc", "/run", "/sys", "/tmp", "/var/lib", "/var/run"]

#os.walk goes through and gets all of the information from the specified location
for root, dirs, files in os.walk(os.getcwd()):
    
    #This if condition removes any directories and files within the forbidden root list
    if root in ignore_list:
        dirs[:] = []
        files[:] = []

    #This loops through all the files, hashes them, and stores them into array R2
    #R2 will be written into the CSV file later in the process
    for name in files:
        try:
            f = open(os.path.join(root, name))
            bob = f.read()
            f.close()
            m = hashlib.sha256()
            m.update(bob.encode())
            hshed = m.hexdigest()
            f1 = {}
            f1['path'] = os.path.join(root, name)
            f1['hash'] = hshed
            f1['access'] = time.strftime("%m%d%Y_%H%M%S")
            r2.append(f1)
        except:
            string +=  os.path.join(root, name) + "\n"
    
    #This loops through all the directories, hashes them, then outputs them to d2 
    #D2 will be written to the CSV
    for name in dirs:
        try:
            dir_sha256 = dirhash(os.path.join(root, name), "sha256")
            d1 = {}
            d1['path'] = os.path.join(root, name)
            d1['hash'] = dir_sha256
            d1['access'] = time.strftime("%m%d%Y_%H%M%S")
            d2.append(d1)
        except:
            string2 += root+name+"\n"

#This writes the output of our hashes to the CSV file
with open('FieSys_' + time.strftime("%m%d%Y_%H%M%S") + '.csv', 'w') as joe:
    fieldname = ['path', 'hash', 'access']
    writer = csv.DictWriter(joe, fieldnames=fieldname)
    writer.writeheader()
    for data in r2:
        writer.writerow(data)
    for data in d2:
        writer.writerow(data)

#Despite our best efforts, some files are not able to be read due to unicode errors and the like
#We have added these files to this list in order for administrators to track them more closely
f = open("errorFiles"+time.strftime("%m%d%Y_%H%M%S") , 'w')
f.write("The following files were not able to be read:\n" + string)
f.write("\n\nThe following directories were not able to be read:\n" + string2)
f.close()
