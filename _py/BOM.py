#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import codecs
import os
import sys

err = os.EX_OK

if len(sys.argv) == 1:
	sys.exit(os.EX_NOINPUT)

for i in sys.argv[1:]:
	f = open(i, 'rb')
	# read the first 32 bytes
	size = min(32, os.path.getsize(i))
	raw = f.read(size)
	if not raw.startswith(codecs.BOM_UTF8):
		pass
	else:
		print("UTF-8 file with BOM: {}".format(i), file=sys.stderr)
