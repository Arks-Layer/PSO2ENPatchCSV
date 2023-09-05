#!/usr/bin/env python3
# coding=utf8
import os

# Get list of empties
empties = os.listdir("Empty")
for file in empties:
    filestats = os.stat(os.path.join("Empty", file))
    filesize = filestats.st_size
    # Not empty, something is up
    if filesize != 0:
        print("Empty/{name} is NOT empty. (File size: {size} bytes)"
              .format(name = file, size = filesize))
        empties.remove(file)
        print("Press enter to continue.")
        input()

# Get filelist data
flist = open("filelist.txt", "r")
flines = flist.readlines()
flist.close()

flist = open("filelist.txt", "w")

# Iterate over lines in filelist
for line in flines:
    empty = "no"
    
    for file in empties:
        text = file.strip(".csv") + ".text"
        
        if ("," + text) in line:
            empty = "yes"
            break

    if empty == "yes":
        print("Removed empty file {name}"
              .format(name = text))
    else:
        flist.write(line)
        
flist.close()

# Get list of dummies
dummies = os.listdir("Dummy")

print("Before proceeding, please check that " +
      "no files in /Dummy are being used.")
print("Press enter to confirm you have made this check, " +
      "or press CTRL + C to cancel.")
input()

# Get filelist data
flist = open("filelist.txt", "r")
flines = flist.readlines()
flist.close()

flist = open("filelist.txt", "w")

# Iterate over lines in filelist
for line in flines:
    dummy = "no"
    
    for file in dummies:
        text = file.strip(".csv") + ".text"
        
        if ("," + text) in line:
            dummy = "yes"
            break

    if dummy == "yes":
        print("Removed dummy file {name}"
              .format(name = text))
    else:
        flist.write(line)
        
flist.close()
