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
	with codecs.open(i, mode='r', encoding="utf-8") as QC:
		try:
			QCCSV = list(csv.reader(QC, strict=True))
		except:
			print("Error reading {0}".format(i))
			sys.exit(os.EX_UNAVAILABLE)
			break
		output = csv.writer(codecs.open(i, mode='w', encoding="utf-8"))
		for x, row in enumerate(QCCSV):
			for n, col in enumerate(row):
				if n == 0:
					ID = col
				if n == 1:
					TEXT = '"' + col[1:-1].replace('"', '\\"') + '"'
					#print(TEXT)
					output.writerow((ID, TEXT))
sys.exit(err)
