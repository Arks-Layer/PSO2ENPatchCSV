#!/usr/bin/env python3
import csv
import sys

for i in sys.argv[1:]:
    with open(i) as JP:
        try:
            JPCSV = list(csv.reader(JP,strict=True))
        except:
            print("Error reading {0}".format(i))
            break;
        WC = open(i.replace("/JP/","/WC/"))
        try:
            WCCSV = list(csv.reader(WC,strict=True))
        except:
             print("Error reading WC vresion of {0}".format(i))
             break;
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
