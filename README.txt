SY402 - Cyber Operations II
Lab 8: Host Integrity

Instructor: Professor Dennis Dias
Creators: Eddy Murphy & Anthony Perry

Usage: $sudo python3 oldFile.csv -OR- $sudo python3

Data Storage Format:
	File Format: FieSys_MMDDYYYY_hhmmss.csv
	CSV Columns: path,hash,time scanned

Python Imports: os, hashlib, dirhash, csv, and time

Hash Type: SHA256

Ignore List: dev, proc, run, sys, tmp, var/lib and var/run

Note: All time formats are MMDDYYYY_hhmmss

Methodology:
Part 1:
1.) Look for log and sys directories, and create them if not present
2.) Get contents of Old File

Part 2:
1.) Use os.walk() to step through each subdirectory of the file system
	a.) Ignore /dev, /proc, /run, /sys, /tmp, /var/lib, and /var/run
2.) Hash the contents of each file 65536 bytes at a time.
3.) Store the path, hash, and access time into a dictionary
4.) Add the dictionary to a overall list of dictionaries
5.) Write contents of this list, into FieSys_<Access Time>.csv
6.) Log all errors into errorFile<Access Time>.csv

Part 3:
1.) Compare New and Old File
2.) Write Changes into Log File

