#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import codecs
import csv
import multiprocessing as mp
import os
import sys


def cutinamount(li):
	extra = 0
	value = None
	for n, word in enumerate(li):
		if n == 0:
			None
		if n == 1:
			try:
				value = int(word)
				extra = 1
			except ValueError:
				value = None
		elif value is None:
			None
		elif not (value is None):
			None
		else:
			print(word)
	return extra


def cutoutcommands(i):
	try:
		i = i[1:-1]
		# most strings do not have commands, skip them
		if i.rstrip() == "/":
			return "\"\""
		elif i[0] != "/":
			return "\"\""
		# by default, most strings do not have a command
		ce = 0
		li = i.split()
		# which one have the last string?
		for n, word in enumerate(li):
			if word[0] == "/" and word != "/":
				ce = n
		if "/ci" in li[ce]:
			ce += cutinamount(li[ce:])
		elif "/mn" in li[ce]:
			ce += 0
		elif "/toge" in li[ce]:
			ce += 0
		elif "/face" in li[ce]:
			ce += 0
		elif "/atime" in li[ce]:
			ce += 0
		elif "/moya" in li[ce]:
			ce += 0
		elif "/start" in li[ce]:
			ce += 0
		elif "/voice11_voice_nav" in li[ce]:
			ce += 0
		elif "/rt_time60" in li[ce]:
			ce += 0
		elif "/ceall" in li[ce]:
			ce += 0
		elif "/ce" in li[ce]:
			ce += 0
		elif "/voice11_sound_voice_magat_qu00" in li[ce]:
			ce += 0
		elif "/voice11_voice_delicious_npcma_0" in li[ce]:
			ce +- 0
		elif "/voice11_voice_delicious_npcha_0" in li[ce]:
			ce += 0
		else:
			print("warning: can not handle {} in {}".format(li[ce], i))
		return "\"" + " ".join(li[0: ce]) + "\""
	except Exception as e:
		print("Error processing string for commands: {}".format(e))
	return None


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
				jstr = None
				wstr = None
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
					wstr = cutoutcommands(wc_[1])
					col = wccsv.line_num
				if jp_:
					jstr = cutoutcommands(jp_[1])
					col = jpcsv.line_num

				if wstr is None:
					print("WC File {} have bad command string at line {}".format(bp, col))
					err = 1
				elif jstr is None:
					print("JP File {} have bad command string at line {}".format(bp, col))
					err = 1
				elif wstr != jstr:
					print("File {} have mismatch commands at line {}: {} vs {}".format(bp, col, jstr, wstr))
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
