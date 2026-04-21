#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import codecs
import csv
import os
import sys

if len(sys.argv) <= 2:
	sys.exit(os.EX_NOINPUT)


def gettext(rows, index, fallback_rows):
	if index >= len(rows):
		return fallback_rows[index][1][1:-1]
	row = rows[index]
	if len(row) <= 1:
		return fallback_rows[index][1][1:-1]
	return row[1][1:-1]


csvout = csv.writer(sys.stdout, quoting=csv.QUOTE_NONNUMERIC)
for i in sys.argv[2:]:
	w = i.replace("JP/", "WC/")
	e = i.replace("JP/", "EN/")
	with codecs.open(i, encoding="utf-8") as JP:
		JPCSV = list(csv.reader(JP, strict=True))
		ENCSV = list(csv.reader(codecs.open(e, encoding="utf-8"), strict=True))
		WCCSV = list(csv.reader(codecs.open(w, encoding="utf-8"), strict=True))
		basename = os.path.splitext(os.path.basename(i))[0]
		for x, row in enumerate(JPCSV):
			JPcheck = False
			ENcheck = False
			WCcheck = False
			ID = row[0]
			JP = row[1][1:-1]
			EN = gettext(ENCSV, x, JPCSV)
			WC = gettext(WCCSV, x, JPCSV)
			if (JP == EN):
				JPcheck = True
			elif EN == WC:
				ENcheck = True
			if JP == WC:
				WCcheck = True
			csvout.writerow([basename, ID, JP, EN, WC, JPcheck, ENcheck, WCcheck])
