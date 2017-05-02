#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import csv
import codecs
import os
import sys


err = os.EX_OK

if len(sys.argv) == 1:
    sys.exit(os.EX_NOINPUT)

for i in sys.argv[1:]:
    with codecs.open(i, encoding="utf-8") as QC:

        try:
            QCCSV = list(csv.reader(QC,strict=True))
        except:
            print("Error reading {0}".format(i))
            sys.exit(os.EX_UNAVAILABLE)
            break;

        for x, row in enumerate(QCCSV):
            for n, col in enumerate(row):
                if n == 0 and not "#" in col:
                     print("entry name not valid in file {}, row {}".format(i, x));
                     err = os.EX_DATAERR
                if n == 1:
                     if not (col.startswith('"') and col.endswith('"')):
                         print("text does not have a quote in file {}, row {}".format(i, x))
                         err = os.EX_DATAERR
                     else:
                         check = col.replace('\\\"', '＂')
                         if '"' in check[1:-1]:
                             print('missing \\\" in file {}, row {}'.format(i, x))
                             print(check[1:-1])
                             err = os.EX_DATAERR

sys.exit(err)
