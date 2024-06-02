#!/usr/bin/env python3
# coding=utf8
import os

# Get list of known dupes
dupelist = open("pruned-dupes.txt", "r")
dupes = dupelist.readlines()
dupelist.close()

# Get filelist data
flist = open("filelist.txt", "r")
flines = flist.readlines()
flist.close()

flist = open("filelist.txt", "w")

# Iterate over lines in filelist
for line in flines:
    removed = "no"
    
    for dupe in dupes:
        if (dupe) in line:
            removed = "yes"
            break

    if removed == "yes":
        print("Removed duplicate file {name}"
              .format(name = dupe))
    else:
        flist.write(line)
        
flist.close()
