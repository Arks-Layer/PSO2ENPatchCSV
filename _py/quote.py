#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import codecs
import csv
import multiprocessing as mp
import os
import sys


def check(i):
	err = os.EX_OK
	with codecs.open(i, encoding="utf-8") as QC:

		try:
			qccsv = list(csv.reader(QC, strict=True))
		except Exception as e:
			print("Error reading {}: {}".format(i, e))
			return os.EX_UNAVAILABLE

		for x, row in enumerate(qccsv):
			for n, col in enumerate(row):
				if n == 0 and "#" not in col:
					print("entry name not valid in file {}, row {}".format(i, x))
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
