#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import csv
import codecs
import fnmatch
import multiprocessing as mp
import os
import sys
import json

m = mp.Manager()
rD = m.dict()
cD = dict()
associations = m.dict()


def check(file):
	with codecs.open(file, encoding="utf-8") as f:
		c = list(csv.reader(f, strict=True))
		change = False
		for l in c:
			if l[1] in rD:
				change = True
		if change:
			with codecs.open(file, mode="w+", encoding="utf-8") as o:
				w = csv.writer(o, strict=True)
				for l in c:
					if l[1] in rD:
						l[1] = rD[l[1]][0]
					w.writerow(l)
			#w = csv.writer(f)
			#w.writerows(c)


err = os.EX_OK

if len(sys.argv) < 4:
	sys.exit(os.EX_NOINPUT)

dir = sys.argv[1]
with open(sys.argv[2]) as f:
	sR = json.load(f)
	rD = {k: v for k, v in sR.items() if len(v) == 1}

with open(sys.argv[3]) as f:
	cD = json.load(f)

fs = set()
for n, (k, v) in enumerate(cD.items()):
	for i in v:
		fs.add(i.split("::")[0])

files = [
	os.path.join(dirpath, f)
	for dirpath, dirnames, files in os.walk(dir)
	for f in fnmatch.filter(files, '*.csv')
	if f in fs
]

p = mp.Pool(mp.cpu_count())
p.map(check, files)
p.close()
p.join()
sys.exit(err)
