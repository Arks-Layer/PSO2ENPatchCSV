#!/bin/bash
rm -rf /tmp/PSO2ENPatchCSV.check
git archive --format=tar --prefix=PSO2ENPatchCSV.check/JP/ origin/JP | tar xf - -C /tmp
rsync -a . /tmp/PSO2ENPatchCSV.check/WC --exclude ".git" --del
cd /tmp/PSO2ENPatchCSV.check/WC/Files
find .. -name "*.csv" -not -path "../Files/*" -exec ln -s {} . \;
cd ..
find /tmp/PSO2ENPatchCSV.check/JP/Files -name "*.csv" -print0|xargs -0 python3 check.py&>null||find /tmp/PSO2ENPatchCSV.check/JP/Files -name "*.csv" -print0|xargs -0 -n 1 python3 check.py
