#!/bin/bash
set -euo pipefail
rm -rf /tmp/PSO2ENPatchCSV.check
mkdir -p /tmp/PSO2ENPatchCSV.check
rsync --recursive --executability --whole-file . /tmp/PSO2ENPatchCSV.check/WC --exclude ".git" --del && cd /tmp/PSO2ENPatchCSV.check/WC/Files && find .. -name "*.csv" -not -path "../Files/*" -not -path "*/.git/*" -print0|../../WC/_tools/mp.sh -0 ln -s {} . \; &
git archive --format=tar --prefix=PSO2ENPatchCSV.check/JP/ upstream/JP_Reboot | tar xf - -C /tmp
cd /tmp/PSO2ENPatchCSV.check
wait
find JP -name "*.csv" -print0|WC/_tools/mp.sh --no-keep-order -0 WC/_py/check.py
