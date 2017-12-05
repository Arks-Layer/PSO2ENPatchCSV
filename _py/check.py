#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import codecs
import csv
import os
import sys
import multiprocessing as mp

err = os.EX_OK

if len(sys.argv) == 1:
	sys.exit(os.EX_NOINPUT)

def check(i):
	try:
		w = i.replace("JP/", "WC/")
		with codecs.open(i, encoding="utf-8") as JP:

			try:
				JPCSV = list(csv.reader(JP, strict=True))
			except Exception as e:
				print("Error reading {}: {}".format(i, e))
				if err == 0:
					err = os.EX_DATAERR
				return

			try:
				WC = codecs.open(w, encoding="utf-8")
				WCCSV = list(csv.reader(WC, strict=True))
			except Exception as e:
				print("Error reading of {}: {}".format(w, e))
				if err == 0:
					err = os.EX_UNAVAILABLE
				return

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
	except Exception as e:
		err = 1
		print("File {} is badly formatted: {}".format(w, e))

p = mp.Pool(mp.cpu_count())
p.map(check, sys.argv[1:])
p.close()
p.join()


sys.exit(err)
