#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import codecs
import csv
import os
import sys
import unicodedata

if len(sys.argv) == 2:
	sys.exit(os.EX_NOINPUT)

POnice = [
	("\\\\u3000", '　'),
	("\\u3000", '　'),
	("\\\\\"", "\\\""),
	#("\"\\\"", "\"\\\\\""),
]


def poformat(input):
	inputl = input
	for i, o in POnice:
		outtext = inputl.replace(i, o)
		inputl = outtext
	if outtext == "\\":
		return "\\\\"
	return outtext


def badcheck(en, wc, powcf, poen, powc):
	if en == wc:
		return True
	if unicodedata.normalize('NFKC', en) == unicodedata.normalize('NFKC', wc):
		return True
	if en == powcf:
		return True
	if unicodedata.normalize('NFKC', en) == unicodedata.normalize('NFKC', powcf):
		return True
	if poen == powc:
		return True
	if unicodedata.normalize('NFKC', poen) == unicodedata.normalize('NFKC', powc):
		return True
	return False


ENcheckForce = False
err = 0
if sys.argv[1] == "en":
	ENcheckForce = True
itemlist = ["ui_accessories_text", "ui_charamake_parts"]
for i in sys.argv[2:]:
	w = i.replace("JP/", "WC/")
	e = i.replace("JP/", "EN/")
	with codecs.open(i, encoding="utf-8") as JP:
		ENcheck = ENcheckForce
		JPcheck = False
		JPCSV = list(csv.reader(JP, strict=True))
		ENCSV = list(csv.reader(codecs.open(e, encoding="utf-8"), strict=True))
		WCCSV = list(csv.reader(codecs.open(w, encoding="utf-8"), strict=True))
		basename = os.path.splitext(os.path.basename(i))[0]
		if JPCSV == WCCSV:
			JPcheck = True
		#if ENCSV == WCCSV:
		#	ENcheck = True
		#if ENcheck and JPcheck:
		#	continue
		skip = False
		if basename in itemlist:
			skip = True
		for x, row in enumerate(JPCSV):
			ID = row[0]
			POID = poformat(ID)
			JP = JPCSV[x][1][1:-1]
			POJP = poformat(JP)
			EN = ENCSV[x][1][1:-1]
			POEN = poformat(EN)
			WC = WCCSV[x][1][1:-1]
			POWC = poformat(WC)
			POWCF = POWC.replace("　", " ")
			#white-space
			print("")
			# #  translator-comments
			# #. extracted-comments
			# #: reference…
			print("#: {}:{}".format(basename, POID))
			# #, flag…
			print("#, no-c-format")
			# #| msgctxt previous-context
			print("#| msgctxt \"{}:{}\"".format(basename, POID))
			# #| msgid previous-untranslated-string
			print("#| msgid \"{}\"".format(POJP))
			# msgctxt context
			print("msgctxt \"{}:{}\"".format(basename, ID))
			if JPcheck:
				#msgid untranslated-string
				print("msgid \"{}\"".format(POJP))
				#msgstr translated-string
				print("msgstr \"\"")
			elif ENcheck and JP != WC:
				#msgid untranslated-string
				print("msgid \"{}\"".format(POJP))
				#msgstr translated-string
				print("msgstr \"{}\"".format(POWC))
			elif JP == WC or JP == POWCF:
				#msgid untranslated-string
				print("msgid \"{}\"".format(POEN))
				#msgstr translated-string
				print("msgstr \"\"")
			elif badcheck(EN, WC, POWCF, POEN, POWC):
				#msgid untranslated-string
				print("msgid \"{}\"".format(POEN))
				#msgstr translated-string
				print("msgstr \"\"")
				if not skip:
					print("{}:{} {} \"{}\" =~ \"{}\"".format(basename, x + 1, ID, WC, JP), file=sys.stderr)
					err = 1
			else:
				#msgid untranslated-string
				print("msgid \"{}\"".format(POEN))
				#msgstr translated-string
				print("msgstr \"{}\"".format(POWC))

sys.exit(err)
