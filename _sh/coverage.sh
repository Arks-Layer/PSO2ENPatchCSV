#!/bin/sh
rm -rf /tmp/PSO2ENPatchCSV.coverage
git archive --format=tar --prefix=PSO2ENPatchCSV.coverage/JP/ origin/JP | tar xf - -C /tmp
rsync -a . /tmp/PSO2ENPatchCSV.coverage/WC/ --exclude ".git" --del
cd /tmp/PSO2ENPatchCSV.coverage/WC/Files
find .. -name "*.csv" -not -path "../Files/*" -exec ln -s {} . \;
cd /tmp/PSO2ENPatchCSV.coverage/
find JP -name "*.csv" -print0|WC/_tools/mp.sh -0 WC/_py/coverage.py|fgrep --invert-match -e "0FILE" | sed -e 's/\.csv//'| sort --numeric-sort --reverse | tee /tmp/PSO2ENPatchCSV.coverage/WC.out | awk '{print $2"\t" $1}' | sed -e 's/\t/: /'
awk '{t+=$3; a+=$4} END {printf "%d of %d lines (%3.1f%)\n",t,a,(t*100)/a}' /tmp/PSO2ENPatchCSV.coverage/WC.out
