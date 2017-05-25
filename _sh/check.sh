#!/bin/sh
rm -rf /tmp/PSO2ENPatchCSV.check
git archive --format=tar --prefix=PSO2ENPatchCSV.check/JP/ upstream/JP | tar xf - -C /tmp
rsync -a . /tmp/PSO2ENPatchCSV.check/WC --exclude ".git" --del
cd /tmp/PSO2ENPatchCSV.check/WC/Files
find .. -name "*.csv" -not -path "../Files/*"  -not -path "*/.git/*" -print0|../../WC/_tools/mp.sh -0 ln -s {} . \;
cd /tmp/PSO2ENPatchCSV.check
find JP -name "*.csv" -print0|WC/_tools/mp.sh -0 WC/_py/check.py
