#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from sys import stdin
import unicodedata


def removeCJK(input):
	output = []
	for i in input:
		uc = unicodedata.name(i, "NOPE")
		if ("HIRAGANA" not in uc and "FULLWIDTH" not in uc and "KATAKANA" not in uc and "CJK" not in uc and "IDEOGRAPHIC" not in uc and "CORNER BRACKET" not in uc and "LENTICULAR BRACKET" not in uc):
			#if (uc is not "NOPE"):
			#	print(uc)
			#else:
			#	print(ord(i))
			output.append(i)
	return "".join(output)

for line in stdin:
	output = ""
	#removeCJK(line)
	output = removeCJK(line)
	#if (output != ""):
	print(output, end="")
