#!/bin/bash
rm -rf /tmp/PSO2ENPatchCSV.coverage
git archive --format=tar --prefix=PSO2ENPatchCSV.coverage/JP/ origin/JP | tar xf - -C /tmp
rsync -a . /tmp/PSO2ENPatchCSV.coverage/WC --exclude ".git" --del
cd /tmp/PSO2ENPatchCSV.coverage/WC/Files
find .. -name "*.csv" -not -path "../Files/*" -exec ln -s {} . \;
cd ..
sh -c "find /tmp/PSO2ENPatchCSV.check/JP/Files -name "*.csv" -print0|xargs -0 python3 coverage.py" |fgrep --invert-match -e "0FILE" | sed -e 's/\.csv//'| sort --numeric-sort --reverse | awk '{print $2"\t" $1}' | sed -e 's/\t/: /'
