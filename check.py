#!/usr/bin/env python3
import csv
import sys

for i in sys.argv:
    with open(i, newline='') as JP:
        JPCSV = list(csv.reader(JP))
        WC = open(i.replace("/JP/","/WC/"),newline='')
        WCCSV = list(csv.reader(WC))
        WClist = []
        for row in WCCSV:
            for n, col in enumerate(row):
                if n == 0:
                     WClist.append(col)
                     #print(col)
        #print(WClist)
        for row in JPCSV:
            for n, col in enumerate(row):
                if n == 0:
                     if col not in WClist:
                         print("File {} have extra line: {}".format(i, col))
