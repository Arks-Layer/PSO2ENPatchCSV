#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import csv
import codecs
import os
import sys

if len(sys.argv) <= 2:
	sys.exit(os.EX_NOINPUT)

POFile = "File"
POID = "ID"
POText = "Text"

PInice = [
	('　', "\\u3000"),
]

def PIformat(input):
	inputl = input
	for i, o in PInice:
		outtext = inputl.replace(i, o)
		inputl = outtext
	if outtext is "\\":
		return "\\\\"
	return outtext

def outputPO(input):
	for i in sys.argv[2:]:
		#print(i)
		with codecs.open(i, mode="w+", encoding="utf-8") as f:
			CSV = csv.writer(f)
			basename = os.path.splitext(os.path.basename(i))[0]
			for e in PO:
				#print(e[0])
				if basename == e[0]:
					#print(e[1])
					CSV.writerow(e[1])

PO = []
for inline in codecs.open(sys.argv[1], encoding="utf-8"):
	if inline != "\n":
		if inline.startswith("msgctxt \""):
			POFile = inline.split("\"", 1)[1].split(":", 1)[0]
			POID = inline.split("\"", 1)[1].split(":", 1)[1][:-2]
		if inline.startswith("#| msgid \""):
			POText = inline.split("\"", 1)[1][:-2]
	if inline == "\n":
		PO.append([POFile, [POID, "\"{}\"".format(PIformat(POText))]]);
PO.append([POFile, [POID, "\"{}\"".format(PIformat(POText))]]);
outputPO(PO)

