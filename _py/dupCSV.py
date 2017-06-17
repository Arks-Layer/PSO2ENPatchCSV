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
		duplist = []
		for x, row in enumerate(QC):
				header = list(csv.reader(row,strict=True))[0]
				if header in duplist:
					print("dup ID in %s:%s".format(i, header))
					err = 1

sys.exit(err)
