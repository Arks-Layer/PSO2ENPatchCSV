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
	try:
		w = i.replace("JP/", "WC/")
		with codecs.open(i, encoding="utf-8") as JP:

			try:
				JPCSV = list(csv.reader(JP, strict=True))
			except:
				print("Error reading {0}".format(i))
				if err == 0:
					err = os.EX_DATAERR
				break

			try:
				WC = codecs.open(w, encoding="utf-8")
				WCCSV = list(csv.reader(WC, strict=True))
			except:
				print("Error reading of {0}".format(w))
				if err == 0:
					err = os.EX_UNAVAILABLE
				break
			WClist = []
			JPlist = []
			for row in WCCSV:
				for n, col in enumerate(row):
					if n == 0:
						WClist.append(col)
			for row in JPCSV:
				for n, col in enumerate(row):
					if n == 0:
						if col not in WClist:
							print("File {} have extra line: {}".format(i, col))
							err = 1
			for row in JPCSV:
				for n, col in enumerate(row):
					if n == 0:
						JPlist.append(col)
			for row in WCCSV:
				for n, col in enumerate(row):
					if n == 0:
						if col not in JPlist:
							print("File {} have extra line: {}".format(w, col))
							err = 1
	except:
		err = 1
		print("File {} is badly formatted".format(w))


sys.exit(err)
