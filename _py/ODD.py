#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import codecs
import csv
import multiprocessing as mp
import os
import sys


def check(i):
	err = 0
	with codecs.open(i, encoding="utf-8") as QC:
		f = list(csv.reader(QC, strict=True))
		for x, row in enumerate(f):
			try:
				if row[0][:4] == "Npc_" and row[1][1] == '[' and row[1][-2] == ']':
					print("Unsafe [] in File {} Line {}: {}".format(i, x + 1, row))
					err = 1
			except Exception as e:
				print("Issue in File {} Line {}: {}".format(i, x + 1, e))
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
