#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import csv
import codecs
import os
import sys

if len(sys.argv) == 1:
	sys.exit(os.EX_NOINPUT)

bufout = "000.0%\t0FILE"
for i in sys.argv[1:]:
	w = i.replace("JP/", "WC/")
	with codecs.open(i, encoding="utf-8") as JP:
		JPCSV = list(csv.reader(JP, strict=True))
		WCCSV = list(csv.reader(codecs.open(w, encoding="utf-8"), strict=True))
		JPlist = dict()
		countt = 0
		for row in JPCSV:
			for n, col in enumerate(row):
				if n == 1:
					JPlist[countt] = col
					countt += 1
		line = 0
		for row in WCCSV:
			for n, col in enumerate(row):
				if n == 1:
					if len(JPlist) < line:
						countt += 0
					elif col == JPlist[line]:
						countt -= 1
					line += 1

		if len(JPlist) != 0:
			countper = "{:06.1%}".format(countt / (len(JPlist)))
			bufout += '\n{0}\t{1}\t{2}\t{3}'.format(countper, i.rsplit('/')[-1], countt, len(JPlist))

print(bufout)
