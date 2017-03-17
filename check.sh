#!/bin/bash
rm -rf /tmp/PSO2ENPatchCSV
git archive --format=tar --prefix=PSO2ENPatchCSV/JP/ origin/JP | tar xf - -C /tmp
rsync -a . /tmp/PSO2ENPatchCSV/WC --exclude ".git" --del
cd /tmp/PSO2ENPatchCSV/WC/Files
find .. -name "*.csv" -not -path "../Files/*" -exec ln -s {} . \;
cd ..
find /tmp/PSO2ENPatchCSV/JP/Files -name "*.csv" -print0|xargs -0 python3 check.py
