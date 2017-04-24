#!/usr/bin/env python3
import csv
import os
import sys


err = os.EX_OK

if len(sys.argv) == 1:
    sys.exit(os.EX_NOINPUT)

bufout = "000.0%\t0FILE"
for i in sys.argv[1:]:
    w = i.replace("/JP/","/WC/")
    with open(i) as JP:
        JPCSV = list(csv.reader(JP,strict=True))
        WCCSV = list(csv.reader(open(w),strict=True))
        JPlist = dict()
        countt = 0
        for row in JPCSV:
            for n, col in enumerate(row):
                if n == 1:
                    JPlist[countt] = col
                    countt += 1
        countt *= 2
        line = 0
        for row in WCCSV:
            for n, col in enumerate(row):
                if n == 1:
                    if len(JPlist) == line-1:
                        countt += 0
                    elif col == JPlist[line]:
                        countt -= 2
                    elif col[0] == JPlist[line][0]:
                        countt -= 1
                    line += 1

        if len(JPlist) != 0:
            countper = "{:06.1%}".format(countt/(len(JPlist)*2))
            bufout += '\n{0}\t{1}'.format(countper,i.rsplit('/')[-1])


print(bufout)
