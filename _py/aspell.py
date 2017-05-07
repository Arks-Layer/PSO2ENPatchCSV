#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import csv
import codecs
import os
import sys

if len(sys.argv) == 1:
	sys.exit(os.EX_NOINPUT)

aspellt = [
	("\\u3000", ' '),
	("'s ", ' '),
	('*', ' '),
	('(', ' '),
	(')', ' '),
	('\\', ' '),
	('/', ' '),
	('-', ' '),
	('+', ' '),
	(':', ' '),
	(',', ' '),
	('[', ' '),
	(']', ' '),
	('~', ' '),
	('"', ''),
	(',', ''),
	('$ 0 ', ''),
]

def replacemark(input):
	output = []
	markmode = False
	for char in input:
		if char ==  '<':
			markmode = True
		elif char == '>':
			markmode = False
		if markmode == False:
			output.append(char)
	return "".join(output)

def replacespell(input):
	inputl = input
	for i, o in aspellt:
		outtext = inputl.replace(i, o)
		inputl = outtext
	return outtext

def checkwords(input):
	return replacespell(replacemark(input))

bufout = ""
for i in sys.argv[1:]:
	with codecs.open(i, encoding="utf-8") as aspelldict:
		WCCSV = list(csv.reader(aspelldict,strict=True))
		for row in WCCSV:
			for n, col in enumerate(row):
				if n == 1:
					check = checkwords(col)
					if check != '""':
						bufout += "\n{0}".format(check)


print(bufout)
