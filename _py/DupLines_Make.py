#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import csv
import codecs
import fnmatch
import json
import multiprocessing as mp
import os
import sys

m = mp.Manager()
gD = m.dict()


def check(file):
	with codecs.open(file, encoding="utf-8") as f:
		c = list(csv.reader(f, strict=True))
		for line in c:
			if line[1] in gD:
				gD[line[1]] += ["{0}::{1}".format(os.path.basename(file), line[0])]
			else:
				gD[line[1]] = ["{0}::{1}".format(os.path.basename(file), line[0])]


err = os.EX_OK

if len(sys.argv) == 1:
	sys.exit(os.EX_NOINPUT)

dir = sys.argv[1]
files = [
	os.path.join(dirpath, f)
	for dirpath, dirnames, files in os.walk(dir)
	for f in fnmatch.filter(files, '*.csv')
]
files.sort()

#p = mp.Pool(mp.cpu_count())
#p.map(check, files)
#p.close()
#p.join()

for i, file in enumerate(files):
	print("{0}/{1}".format(i, len(files)), file=sys.stderr)
	check(file)

print(json.dumps({k: v for k, v in gD.items() if len(v) > 1}, sort_keys=True))

sys.exit(err)
