#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import json
import os
import sys

err = os.EX_OK

if len(sys.argv) < 2:
    sys.exit(os.EX_NOINPUT)

with open(sys.argv[1]) as f:
    oD = json.load(f)

oJ = {}
for k, vl in oD.items():
    for v in vl:
        if v not in oJ:
            oJ[v] = [k]
        else:
            oJ[v].append(k)

print(json.dumps(oJ, sort_keys=True))

sys.exit(err)
