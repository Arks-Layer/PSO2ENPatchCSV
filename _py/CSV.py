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
		for x, row in enumerate(QC):
			#print(row)
			try:
				QCrow = list(csv.reader(row,strict=True))
			except:
				#print(row)
				print("Issue in File {}:{}".format(i, x+1))
				err = 1
			#print(QCrow)

sys.exit(err)
