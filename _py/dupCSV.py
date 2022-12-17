#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import codecs
import csv
import multiprocessing as mp
import os
import sys


def check(i):
    err = os.EX_OK
    header = ""  # Initialize header to an empty string
    with codecs.open(i, encoding="utf-8") as QC:
        dupid = []
        for x, row in enumerate(csv.reader(QC, strict=True)):
            if row:  # Only proceed if the row list is non-empty
                header = row[0]
                if header in dupid:
                    print("{}:{} {}".format(i, x, header))
                    err = 1
                dupid.append(header)
            else:
                print("Issue on {}:{}".format(i, x, header))
                err = 1
    return err

if __name__ == '__main__':
	err = os.EX_OK

	if len(sys.argv) == 1:
		sys.exit(os.EX_NOINPUT)

	p = mp.Pool(mp.cpu_count())
	erra = p.map(check, sys.argv[1:])
	p.close()
	p.join()

	err = max(erra)
	sys.exit(err)
