#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import codecs
import csv
import multiprocessing as mp
import os
import sys


def check(i):
	err = 0
	try:
		w = i.replace("JP/", "WC/")
		with codecs.open(i, encoding="utf-8") as JP:
			bp = os.path.basename(i)

			try:
				jpcsv = csv.reader(JP, strict=True)
			except Exception as e:
				print("Error reading {}: {}".format(i, e))
				if err == 0:
					err = os.EX_DATAERR
				return

			try:
				wc = codecs.open(w, encoding="utf-8")
				wccsv = csv.reader(wc, strict=True)
			except Exception as e:
				print("Error reading of {}: {}".format(w, e))
				if err == 0:
					err = os.EX_UNAVAILABLE
				return

			while True:
				jid = None
				wid = None
				try:
					wc_ = next(wccsv)
				except StopIteration:
					wc_ = None

				try:
					jp_ = next(jpcsv)
				except StopIteration:
					jp_ = None

				if jp_ is None and wc_ is None:
					break
				elif jp_ == wc_:
					next

				if wc_:
					wid = wc_[0]
					col = wccsv.line_num
				if jp_:
					jid = jp_[0]
					col = jpcsv.line_num

				if wid:
					bid = wid
				elif jid:
					bid = jid

				if jp_ is None or wc_ is None:
					print("File {}:{} have extra line: {}".format(bp, col, bid))
					err = 1
				elif (wc_[0] != jp_[0]):
					print("File {} have mismatch line: {}/{} ".format(bp, jid, wid))
					err = 1

	except Exception as e:
		err = 1
		print("File {} is badly formatted: {}".format(w, e))

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
