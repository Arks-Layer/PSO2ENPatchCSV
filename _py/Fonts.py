#!/usr/bin/env python2
# -*- coding:utf-8 -*-
import codecs
#import fonts.HeiSeiGothic
import fonts.SouGei
import os
import sys


err = os.EX_OK

if len(sys.argv) == 1:
	sys.exit(os.EX_NOINPUT)

glyphs = u""
for i in fonts.SouGei.Charset().glyphs():
	glyphs+=unichr(i)

def checkglyphs(input):
	for l in input:
		for c in l:
			if c not in glyphs:
				return False
	return True

#print(glyphs)
for i in sys.argv[1:]:
	with codecs.open(i, encoding="utf-8") as QC:
		if not checkglyphs(QC):
			if err != 0:
				print("File:{}".format(i))
				err = os.EX_DATAERR

sys.exit(err)
