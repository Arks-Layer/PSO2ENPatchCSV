#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import csv
import codecs
import os
import sys

if len(sys.argv) == 2:
	sys.exit(os.EX_NOINPUT)

version = sys.argv[1]

for i in sys.argv[2:]:
	w = i.replace("JP/","WC/")
	e = i.replace("JP/","EN/")
	with codecs.open(i, encoding="utf-8") as JP:
		JPCSV = list(csv.reader(JP,strict=True))
		ENCSV = list(csv.reader(codecs.open(w, encoding="utf-8"),strict=True))
		WCCSV = list(csv.reader(codecs.open(e, encoding="utf-8"),strict=True))
		for x, row in enumerate(JPCSV):
			basename = os.path.splitext(os.path.basename(i))[0]
			#white-space
			print("")
			##  translator-comments
			##. extracted-comments
			print("#. {}".format(version))
			#: refernences...
			print("#: {}:{}".format(basename, row[0]))
			#, flags
			print("#, no-c-format")
			print("#| msgid {}".format(JPCSV[x][1]))
			#msgid
			print("msgid {}".format(ENCSV[x][1]))
			#msgstr
			print("msgstr {}".format(WCCSV[x][1]))
