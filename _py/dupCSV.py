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
		dupid = []
		for x, row in enumerate(csv.reader(QC, strict=True)):
			header = row[0]
			#print("{}:{}:{}".format(i, x, header))
			if header in dupid:
				print("{}:{} {}".format(i, x, header))
				err = 1
			dupid.append(header)

sys.exit(err)
