#!/bin/sh
rm -rf /tmp/PSO2ENPatchCSV.coverage
git archive --format=tar --prefix=PSO2ENPatchCSV.coverage/JP/ origin/JP | tar xf - -C /tmp
rsync -a . /tmp/PSO2ENPatchCSV.coverage/WC --exclude ".git" --del
cd /tmp/PSO2ENPatchCSV.coverage/WC/Files
find .. -name "*.csv" -not -path "../Files/*" -exec ln -s {} . \;
cd /tmp/PSO2ENPatchCSV.coverage/
sh -c "find JP -name "*.csv" -print0|WC/_tools/mp.sh -0  WC/_py/coverage.py" |fgrep --invert-match -e "0FILE" | sed -e 's/\.csv//'| sort --numeric-sort --reverse | awk '{print $2"\t" $1}' | sed -e 's/\t/: /'
