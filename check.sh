#!/bin/sh -e
rm -rf /tmp/PSO2ENPatchCSV.check
git archive --format=tar --prefix=PSO2ENPatchCSV.check/JP/ origin/JP | tar xf - -C /tmp
rsync -a . /tmp/PSO2ENPatchCSV.check/WC --exclude ".git" --del
cp /tmp/PSO2ENPatchCSV.check/JP/Files/*.csv Files
git diff --color-words --exit-code -- Files
cd /tmp/PSO2ENPatchCSV.check/WC/Files
find .. -name "*.csv" -not -path "../Files/*" -exec ln -sf {} . \;
cd ..
find /tmp/PSO2ENPatchCSV.check/JP/Files -name "*.csv" -print0|xargs -0 python3 check.py&>null||find /tmp/PSO2ENPatchCSV.check/JP/Files -name "*.csv" -print0|xargs -0 -n 1 python3 check.py
