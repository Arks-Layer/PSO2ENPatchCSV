#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import codecs
import os
import sys

err = os.EX_OK

if len(sys.argv) == 1:
	sys.exit(os.EX_NOINPUT)

for i in sys.argv[1:]:
	try:
		f = codecs.open(i, encoding='utf-8', errors='strict')
		for line in f:
			pass
	except UnicodeDecodeError:
		print("Invalid UTF-8 file: {}".format(i), file=sys.stderr)
