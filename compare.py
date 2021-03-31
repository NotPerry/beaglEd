import os
import time

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

compare_csv("test.csv", "test2.csv")
