#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import codecs
import csv
import os
import sys
import multiprocessing as mp

def check(i):
	err = 0
	try:
		w = i.replace("JP/", "WC/")
		with codecs.open(i, encoding="utf-8") as JP:
			bp = os.path.basename(i)

			try:
				JPCSV = csv.reader(JP, strict=True)
			except Exception as e:
				print("Error reading {}: {}".format(i, e))
				if err == 0:
					err = os.EX_DATAERR
				return

			try:
				WC = codecs.open(w, encoding="utf-8")
				WCCSV = csv.reader(WC, strict=True)
			except Exception as e:
				print("Error reading of {}: {}".format(w, e))
				if err == 0:
					err = os.EX_UNAVAILABLE
				return

			while True:
				jid = None
				wid = None
				try:
					WC_ = next(WCCSV)
				except StopIteration:
					WC_ = None

				try:
					JP_ = next(JPCSV)
				except StopIteration:
					JP_ = None

				if JP_ == None and WC_ == None:
					break
				elif JP_ == WC_:
					next

				if WC_:
					wid = WC_[0]
					col = WCCSV.line_num
				if JP_:
					jid = JP_[0]
					col = JPCSV.line_num

				if wid:
					bid = wid
				elif jid:
					bid = jid

				if JP_ == None or WC_ == None:
					print("File {}:{} have extra line: {}".format(bp, col, wid))
					err = 1
				elif (WC_[0] != JP_[0]):
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
