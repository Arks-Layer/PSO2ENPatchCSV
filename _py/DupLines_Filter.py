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
gD = m.dict()
cD = m.dict()
associations = m.dict()
bD = m.list()
kL = m.list()


def check(file):
	with codecs.open(file, encoding="utf-8") as f:
		c = list(csv.reader(f, strict=True))
		for line in c:
			key = "{0}::{1}".format(os.path.basename(file), line[0])
			if key not in associations:
				continue
			if associations[key] in gD and gD[associations[key]] != line[1]:
				if kL[associations[key]] not in bD:
					bD.append(kL[associations[key]])
			elif associations[key] not in gD:
				gD[associations[key]] = line[1]


err = os.EX_OK

if len(sys.argv) < 3:
	sys.exit(os.EX_NOINPUT)

dir = sys.argv[1]
with open(sys.argv[2]) as f:
	cD = json.load(f)

fs = set()
for n, (k, v) in enumerate(cD.items()):
	kL.append(k)
	for i in v:
		fs.add(i.split("::")[0])
		associations[i] = n

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



print(json.dumps({k: v for k, v in cD.items() if k in bD}, sort_keys=True))

sys.exit(err)
