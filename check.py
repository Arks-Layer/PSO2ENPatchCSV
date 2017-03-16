#!/usr/bin/env python3
import csv
import os
import sys


err = os.EX_OK

if len(sys.argv) == 1:
    sys.exit(os.EX_NOINPUT)

for i in sys.argv[1:]:
    with open(i) as JP:

        try:
            JPCSV = list(csv.reader(JP,strict=True))
        except:
            print("Error reading {0}".format(i))
            sys.exit(os.EX_DATAERR)
            break;

        try:
            WC = open(i.replace("/JP/","/WC/"))
        except:
            print("Error reading WC version of {0}".format(i))
            sys.exit(os.EX_UNAVAILABLE)
            break;
        WCCSV = list(csv.reader(WC,strict=True))
        WClist = []
        for row in WCCSV:
            for n, col in enumerate(row):
                if n == 0:
                     WClist.append(col)
        for row in JPCSV:
            for n, col in enumerate(row):
                if n == 0:
                     if col not in WClist:
                         print("File {} have extra line: {}".format(i, col))
                         err =  1

sys.exit(err)
