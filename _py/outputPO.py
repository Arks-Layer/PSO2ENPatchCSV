#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import csv
import codecs
import os
import sys

if len(sys.argv) == 1:
	sys.exit(os.EX_NOINPUT)

POnice = [
	("\\\\u3000", '　'),
	("\\u3000", '　'),
	("\\\\\"", "\\\""),
	#("\"\\\"", "\"\\\\\""),
]

def POformat(input):
	inputl = input
	for i, o in POnice:
		outtext = inputl.replace(i, o)
		inputl = outtext
	if outtext is "\\":
		return "\\\\"
	return outtext


for i in sys.argv[1:]:
	w = i.replace("JP/","WC/")
	e = i.replace("JP/","EN/")
	with codecs.open(i, encoding="utf-8") as JP:
		ENcheck = False
		JPcheck = False
		JPCSV = list(csv.reader(JP,strict=True))
		ENCSV = list(csv.reader(codecs.open(e, encoding="utf-8"),strict=True))
		WCCSV = list(csv.reader(codecs.open(w, encoding="utf-8"),strict=True))
		basename = os.path.splitext(os.path.basename(i))[0]
		if JPCSV == WCCSV:
			JPcheck = True
		if ENCSV == WCCSV:
			ENcheck = True
		#if ENcheck and JPcheck:
		#	continue
		for x, row in enumerate(JPCSV):
			ID = row[0]
			POID = POformat(ID)
			JP = JPCSV[x][1][1:-1]
			POJP = POformat(JP)
			EN = ENCSV[x][1][1:-1]
			POEN = POformat(EN)
			WC = WCCSV[x][1][1:-1]
			POWC = POformat(WC)
			#white-space
			print("")
			##  translator-comments
			##. extracted-comments
			##: reference…
			print("#: {}:{}".format(basename, POID))
			##, flag…
			print("#, no-c-format")
			##| msgctxt previous-context
			print("#| msgctxt \"{}:{}\"".format(basename, POID))
			##| msgid previous-untranslated-string
			print("#| msgid \"{}\"".format(POJP))
			#msgctxt context
			print("msgctxt \"{}:{}\"".format(basename, ID))
			if JPcheck:
				#msgid untranslated-string
				print("msgid \"{}\"".format(POJP))
				#msgstr translated-string
				print("msgstr \"\"")
			elif ENcheck:
				#msgid untranslated-string
				print("msgid \"{}\"".format(POJP))
				#msgstr translated-string
				print("msgstr \"{}\"".format(POEN))
			elif EN == WC or JP == WC:
				#msgid untranslated-string
				print("msgid \"{}\"".format(POEN))
				#msgstr translated-string
				print("msgstr \"\"")
			else:
				#msgid untranslated-string
				print("msgid \"{}\"".format(POEN))
				#msgstr translated-string
				print("msgstr \"{}\"".format(POWC))
