# beaglEd

This code was a Project for SY402: Lab 8.  

Lab Objective:
Write software that will detect changes across the filesystem by hashing all files across your virtual machine. This is accomplished by writing a Python script that will walk through all of the directories and files on your virtual server and hash each individual file, keeping track of the hash values so that subsequent runs can make note of the changes. In essence, you are writing a software package similar to the initial tripwire software.

<h2>Tasking:</h2>

1.) Create a hash.py script that will recursively walk through all files on your file system. You should be able to configure your program to define certain files and/or directories as unhashable so that they will be ignored, /dev is a perfect example, as you do not want to hash this directory. Note: Below is a non-exhaustive list of directories you will probably want to ignore (if your program gets stuck on a directory you will want to consider ignore those as well):

    /dev
    /proc
    /run
    /sys
    /tmp
    /var/lib
    /var/run

A Part 1 solution will be able to walk through the entire file system, printing out the filenames (with their paths), and taking no action other than skipping the unhashable files or directories.
Hint: In-built libraries and functions, such as os.listdir, os.stat, and os.walk can be quite helpful.

2.) Integrate SHA2 (SHA256) so that each file is hashed as it moves through the file system. You are not expected to write SHA2 from scratch, use a python library such as hashlib.
Store the file and hash information so that it will be available for future runs. At a minimum store the following data:

    filename with full path
    hash
    date/time file was observed

3.) The final step, your program should run and update the hash information, upon completion it should print out summary information that includes all new files found, any missing files, and any file that was modified. 

<h2>Deliverables:</h2>

1. Your [hashing script](./hash.py)
2. The file in which you stored all of the [hash data](FieSys_03312021_192512.tar.xz)
3. A file that explains how you stored the data in the hash data file called [README](./README.txt)
