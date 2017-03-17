#!/bin/sh
rm -rf /tmp/PSO2ENPatchCSV
git archive --format=tar --prefix=PSO2ENPatchCSV/JP/ origin/JP | (cd /tmp && tar xf -)
git archive --format=tar --prefix=PSO2ENPatchCSV/WC/ HEAD | (cd /tmp && tar xf -)
find /tmp/PSO2ENPatchCSV/JP/ -name "*.csv" -print0|xargs -0 python3 check.py
