#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import codecs
import multiprocessing as mp
import os
import sys


def check(i):
	f = open(i, 'rb')
	# read the first 32 bytes
	size = min(32, os.path.getsize(i))
	raw = f.read(size)
	if not raw.startswith(codecs.BOM_UTF8):
		return 0
	else:
		print("UTF-8 file with BOM: {}".format(i))
		return 1


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
