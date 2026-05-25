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
allowed_badcheck = {
	("st_020790", "st_020790_0080#0", "<%me>!", "<%me>っ！"),
	("un_025000", "un_025000_0010#0", "……<%me>", "……<%me>君"),
	("ra_031010", "ra_031010_0140#0", "■■■■■■！　■■■■！", "■■■■■■！\u3000■■■■！"),
	("st_020610", "st_020610_0160#0", "…<%me>.", "……<%me>。"),
	("st_020990", "st_020990_0380#0", "<%me>…!", "<%me>……！"),
	("st_037030", "st_037030_0010#0", "…<%me>.", "……<%me>。"),
	("st_037030_om", "st_037030_0010#0", "…<%me>.", "……<%me>。"),
}


def readcsv(path):
	with codecs.open(path, encoding="utf-8") as handle:
		return list(csv.reader(handle, strict=True))


def gettext(rows, index, fallback_rows):
	if index >= len(rows):
		return fallback_rows[index][1][1:-1]
	row = rows[index]
	if len(row) <= 1:
		return fallback_rows[index][1][1:-1]
	return row[1][1:-1]


for i in sys.argv[2:]:
	w = i.replace("JP/", "WC/")
	e = i.replace("JP/", "EN/")
	ENcheck = ENcheckForce
	JPcheck = False
	basename = os.path.splitext(os.path.basename(i))[0]
	skip = basename in itemlist
	JPCSV = readcsv(i)
	try:
		ENCSV = readcsv(e)
	except FileNotFoundError:
		ENCSV = JPCSV
	except csv.Error:
		if not skip:
			raise
		ENCSV = JPCSV
	try:
		WCCSV = readcsv(w)
	except FileNotFoundError:
		WCCSV = JPCSV
	except csv.Error:
		if not skip:
			raise
		WCCSV = JPCSV
	if JPCSV == WCCSV:
		JPcheck = True
		#if ENCSV == WCCSV:
		#	ENcheck = True
		#if ENcheck and JPcheck:
		#	continue
	for x, row in enumerate(JPCSV):
		ID = row[0]
		POID = poformat(ID)
		JP = JPCSV[x][1][1:-1]
		POJP = poformat(JP)
		EN = gettext(ENCSV, x, JPCSV)
		POEN = poformat(EN)
		WC = gettext(WCCSV, x, JPCSV)
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
			if not skip and (basename, ID, WC, JP) not in allowed_badcheck:
				print("{}:{} {} \"{}\" =~ \"{}\"".format(basename, x + 1, ID, WC, JP), file=sys.stderr)
				err = 1
		else:
			#msgid untranslated-string
			print("msgid \"{}\"".format(POEN))
			#msgstr translated-string
			print("msgstr \"{}\"".format(POWC))

sys.exit(err)
