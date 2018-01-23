#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import os
import sys

if len(sys.argv) == 1:
	sys.exit(os.EX_NOINPUT)

for i in sys.argv[1:]:
	f = open(i, mode="rb+")
	f.seek(-1, 2)
	char = f.read()
	if ord(char) != 0xa:
		print("Missing EOL in {}'s last line".format(i))
