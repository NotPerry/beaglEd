import os
import hashlib
from dirhash import dirhash
import csv
import time #All time formats are MMDDYYYY_hhmmss

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

def compare_csv(original, compare, log_file):
    log = open(log_file, "a+")
    dir_list = []
    with open(original, 'r') as pre1, open(compare, 'r') as pre2:
        fileone = pre1.readlines()
        filetwo = pre2.readlines()

    for line in filetwo:
        buff = []
        buff = line.split(",")
        dir_list.append(buff[0])
        if line not in fileone:
            flag = check_mod(buff[0], fileone)
            if (flag == True): #if it detected there was a modification
          #      print("{}{}{} modified. Observed at: {}{}{}".format(bcol.yel, buff[0], bcol.noc, bcol.bold, buff[2], bcol.noc))
                log.write("{} modified. Observed at: {}".format(buff[0],buff[2]))
            if (flag == False): #if it detected there was a new file
          #      print("{}{}{} added. Observed at: {}{}{}".format(bcol.blu, buff[0], bcol.noc, bcol.bold, buff[2], bcol.noc))
                log.write("{} added. Observed at: {}".format(buff[0], buff[2]))
    for line in fileone:
        buff = []
        buff = line.split(",")
        if buff[0] not in dir_list:
          #  print("{}{}{} removed. Observed at: {}{}{}".format(bcol.red, buff[0], bcol.noc, bcol.bold, time.strftime("%m%d%Y_%H%M%S"), bcol.noc))
            log.write("{} removed. Observed at: {}".format(buff[0], time.strftime("%m%d%Y_%H%M%S")))
    fileone.close()
    filetwo.close()
    log.close()

def csv_hash():
    #Global Variables
    string = ""
    string2 = ""
    r2 = []
    d2 = []
    ignore_list = set(["dev", "proc", "run", "sys", "tmp", "var"])
    ignore_in_var = set(["lib", "run"])
    top = '/'
    other_top = 'var'
    
    for root, dirs, files in os.walk(top, topdown=True):
        dirs[:] = [d for d in dirs if d not in ignore_list]
        for name in files:
            BUF_SIZE = 65536  # lets read in 64kb chunks

            sha256 = hashlib.sha256()
            try:
                with open(os.path.join(root,name), 'rb') as f:
                    while True:
                        data = f.read(BUF_SIZE)
                        if not data:
                            break
                        sha256.update(data)
                hshed = "{0}".format(sha256.hexdigest())
                f1 = {}
                f1['path'] = os.path.join(root, name)
                f1['hash'] = hshed
                f1['access'] = time.strftime("%m%d%Y_%H%M%S")
                r2.append(f1)

            except:
                string +=  os.path.join(root, name) + "\n"

    for root, dirs, files in os.walk(other_top, topdown=True):
        dirs[:] = [d for d in dirs if d not in ignore_in_var]
        for name in files:
            print(os.path.join(root,name))
            BUF_SIZE = 65536  # lets read in 64kb chunks

            sha256 = hashlib.sha256()
            try:
                with open(os.path.join(root,name), 'rb') as f:
                    while True:
                        data = f.read(BUF_SIZE)
                        if not data:
                            break
                        sha256.update(data)
                hshed = "{0}".format(sha256.hexdigest())
                f1 = {}
                f1['path'] = os.path.join(root, name)
                f1['hash'] = hshed
                f1['access'] = time.strftime("%m%d%Y_%H%M%S")
                r2.append(f1)

            except:
                string +=  os.path.join(root, name) + "\n"

    #This writes the output of our hashes to the CSV file
    filename = './sys/FieSys_' + time.strftime("%m%d%Y_%H%M%S") + '.csv'
    with open(filename, 'w') as joe:
        fieldname = ['path', 'hash', 'access']
        writer = csv.DictWriter(joe, fieldnames=fieldname)
        writer.writeheader()
        for data in r2:
            writer.writerow(data)

    #We have added these files to this list in order for administrators to track errors in this process
    f = open("./log/errorFile"+time.strftime("%m%d%Y_%H%M%S") , 'w')
    f.write("The following files were not able to be read:\n" + string)
    f.close()

    return filename

def main():
    if not os.path.exists('log'):
        os.makedirs('log')
    if not os.path.exists('sys'):
        os.makedirs('sys')
    old_file = None
    log_file = "./log/changes.log"

    try:
        old_file = sys.argv[1]
        print("file accepted")
    except:
        pass

    if old_file == None:
        print("Scanning files...")
        old_file = csv_hash()   #this is the initial csv file of the system
        print("Completed creation of comparison file")

    while True:
        print("Scanning files...")
        new_file = csv_hash()      #this graps the new csv file to compare to the previous one
        print("Analyzing changes...")
        compare_csv(old_file, new_file, log_file) #compre the two csv files and print out the differences
        old_file = new_file  #after all the differences have been noted, make what was the "new" csv the "old" csv to compare in the next round
        
if __name__ == "__main__":
    main()

