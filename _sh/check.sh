#!/bin/sh
rm -rf /tmp/PSO2ENPatchCSV.check
git archive --format=tar --prefix=PSO2ENPatchCSV.check/JP/ origin/JP | tar xf - -C /tmp
rsync -a . /tmp/PSO2ENPatchCSV.check/WC --exclude ".git" --del
cd /tmp/PSO2ENPatchCSV.check/WC/Files
find .. -name "*.csv" -not -path "../Files/*" -exec ln -s {} . \;
cd /tmp/PSO2ENPatchCSV.check
find JP -name "*.csv" -print0|xargs -0 python3 WC/_py/check.py&>/dev/null||find JP -name "*.csv" -print0|xargs -0 -n 1 python3 WC/_py/check.py
