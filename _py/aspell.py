#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import codecs
import csv
import os
import sys

if len(sys.argv) == 1:
	sys.exit(os.EX_NOINPUT)

aspellt = [
	("\\\\u3000", '　'),
	("\\u3000", '　'),
	("'s ", ' '),
	('*', ' '),
	('(', ' '),
	(')', ' '),
	('<br>', ' '),
	('\\', ' '),
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
	('※', '. '),
	('０', '0'),
	('１', '1'),
	('２', '2'),
	('３', '3'),
	('４', '4'),
	('５', '5'),
	('６', '6'),
	('７', '7'),
	('８', '8'),
	('９', '9'),
	('†', ""),
	("voice11_sound_voice_magat_qu002", ""),
	("voice11_sound_voice_magat_qu003", ""),
	("voice11_sound_voice_magat_qu004", ""),
]


def replacemark(input):
	output = []
	markmode = False
	for char in input:
		if char == '<':
			markmode = True
		elif markmode is False:
			output.append(char)
		if char == '>':
			markmode = False
	return "".join(output)


def replacespell(input):
	inputl = input
	for i, o in aspellt:
		outtext = inputl.replace(i, o)
		inputl = outtext
	return outtext


def checkwords(input):
	return replacemark(replacespell(input))


for i in sys.argv[1:]:
	bufout = ""
	with codecs.open(i, encoding="utf-8") as aspelldict:
		WCCSV = list(csv.reader(aspelldict, strict=True))
		for row in WCCSV:
			for n, col in enumerate(row):
				if n == 1:
					check = checkwords(col)
					if check != '""':
						bufout += "\n{0}".format(check)
	try:
		print(bufout)
	except BrokenPipeError as e:
		sys.exit(os.EX_IOERR);
