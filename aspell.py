#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import csv
import os
import sys

if len(sys.argv) == 1:
    sys.exit(os.EX_NOINPUT)

aspellt = [
	("\\u3000", ' '),
	('>', '> '),
	("'s ", ' '),
	('*', ' '),
	('(', ' '),
	(')', ' '),
	('/', ' '),
	('/', ' '),
	('-', ' '),
	('+', ' '),
	(':', ' '),
	(',', ' '),
	('[', ' '),
	(']', ' '),
	('~', ' '),
	('"', ''),
]

def replacespell(input):
	inputl = input
	for i, o in aspellt:
		outtext = inputl.replace(i, o)
		inputl = outtext
	return outtext

ranges = [
	{"from": ord(u"\u3300"), "to": ord(u"\u33ff")},         # compatibility ideographs
	{"from": ord(u"\ufe30"), "to": ord(u"\ufe4f")},         # compatibility ideographs
	{"from": ord(u"\uf900"), "to": ord(u"\ufaff")},         # compatibility ideographs
	{"from": ord(u"\U0002F800"), "to": ord(u"\U0002fa1f")}, # compatibility ideographs
	{"from": ord(u"\u30a0"), "to": ord(u"\u30ff")},         # Japanese Kana
	{"from": ord(u"\u2e80"), "to": ord(u"\u2eff")},         # cjk radicals supplement
	{"from": ord(u"\u4e00"), "to": ord(u"\u9fff")},
	{"from": ord(u"\u3400"), "to": ord(u"\u4dbf")},
	{"from": ord(u"\U00020000"), "to": ord(u"\U0002a6df")},
	{"from": ord(u"\U0002a700"), "to": ord(u"\U0002b73f")},
	{"from": ord(u"\U0002b740"), "to": ord(u"\U0002b81f")},
	{"from": ord(u"\U0002b820"), "to": ord(u"\U0002ceaf")}  # included as of Unicode 8.0
]

def is_cjk(char):
	return any([range["from"] <= ord(char) <= range["to"] for range in ranges])

def PSO2check(w):
	#return True
	return w[0] != "/" and w[0] != "<" and w[0] != "$" and "." not in w and "BB" != w[:2] and "SFC" != w[:3] and "GG" != w[:2] and "DK" != w[:2] and "?" not in w and "+" != w[:1] and ">" not in w and "$" not in w and "2" != w[0]

def checkwords(input):
	output = []
	words = replacespell(input)
	for word in words.split(" "):
		anycjk = False
		for char in word:
			if is_cjk(char):
				anycjk = True
		if not anycjk and word and PSO2check(word):
			output.append(word)
	return "\n".join(output)

bufout = ""
for i in sys.argv[1:]:
	with open(i) as aspelldict:
		WCCSV = list(csv.reader(aspelldict,strict=True))
		for row in WCCSV:
			for n, col in enumerate(row):
				if n == 1:
					if len(col) > 4:
							check = checkwords(col)
							if check != "":
								bufout += "\n{0}".format(check)


print(bufout)
