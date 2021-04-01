import os
import hashlib
from dirhash import dirhash
import csv
import time #All time formats are MMDDYYYY_hhmmss
import sys
import getopt

#Global Variables
string = ""
string2 = ""
r2 = []
d2 = []
ignore_list = ["/dev", "/proc", "/run", "/sys", "/tmp", "/var/lib", "/var/run"]
compare = True

opts, args = getopt.getopt(sys.argv[1:], "ho")

def usage():
    print("You need to include a comparison CSV file.")
    print("Usage: python hash.py <comparison.csv>")
    print("For initial run, go: python hash.py -o")
    sys.exit() 

if (len(sys.argv) == 1):
    usage()   
elif (len(sys.argv) == 2) and (sys.argv[-1][-4:] == ".csv"):
    compFile = sys.argv[-1]
elif (len(sys.argv) == 2):
    for o, a in opts: 
        if o == "-o":
            compare = False
        else:
            usage()
else:
    usage()

#os.walk goes through and gets all of the information from the current directory
for root, dirs, files in os.walk("/"):
    
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
newFile = str('FieSys_' + time.strftime("%m%d%Y_%H%M%S") + '.csv')
with open(newFile, 'w') as joe:
    fieldname = ['path', 'hash', 'access']
    writer = csv.DictWriter(joe, fieldnames=fieldname)
    writer.writeheader()
    for data in r2:
        writer.writerow(data)
    for data in d2:
        writer.writerow(data)

#Despite our best efforts, some files are not able to be read due to unicode errors and not able to run $sudo python ...
#We have added these files to this list in order for administrators to track them more closely
f = open("errorFiles"+time.strftime("%m%d%Y_%H%M%S") , 'w')
f.write("The following files were not able to be read:\n" + string)
f.write("\n\nThe following directories were not able to be read:\n" + string2)
f.close()

#This section defines the functions to compare the new file to the comparison (original) file.
class bcol:
    yel = '\033[93m'
    blu = '\033[96m'
    red = '\033[91m'
    noc = '\033[0m'
    bold = '\033[1m'

def check_mod(dir_path, fileone):
    for line in fileone:
        buff = []
        buff = line.split(",")
        if buff[0] == dir_path:
            return True
    return False

def compare_csv(original, compare):
    dir_list = []
    with open(original, 'r') as t1, open(compare, 'r') as t2:
        fileone = t1.readlines()
        filetwo = t2.readlines()

    for line in filetwo:
        buff = []
        buff = line.split(",")
        dir_list.append(buff[0])
        if line not in fileone:
            flag = check_mod(buff[0], fileone)
            if (flag == True): #if it detected there was a modification
                print("{}{}{} modified. Observed at: {}{}{}".format(bcol.yel, buff[0], bcol.noc, bcol.bold, buff[2], bcol.noc))
            if (flag == False): #if it detected there was a new file
                print("{}{}{} added. Observed at: {}{}{}".format(bcol.blu, buff[0], bcol.noc, bcol.bold, buff[2], bcol.noc))
    for line in fileone:
        buff = []
        buff = line.split(",")
        if buff[0] not in dir_list:
            print("{}{}{} removed. Observed at: {}{}{}".format(bcol.red, buff[0], bcol.noc, bcol.bold, time.strftime("%m%d%Y_%H%M%S"), bcol.noc))

#Ensures there is a file to compare, and this isn't the original copy
if compare == True:
    compare_csv(newFile, compFile)

