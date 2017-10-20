#!/bin/bash
PWDC="$(pwd -P)"
rm -rf /tmp/PSO2ENPatchCSV.GOOD
mkdir -p /tmp/PSO2ENPatchCSV.GOOD
JP="upstream/JP"
EN="upstream/EN"
mkdir /tmp/PSO2ENPatchCSV.GOOD/WC/
rsync --recursive --executability --whole-file Files.TODO/ /tmp/PSO2ENPatchCSV.GOOD/WC/Files/ --del -p || exit
git archive --format=tar --prefix=PSO2ENPatchCSV.GOOD/JP/ $JP | tar xf - -C /tmp &
mkdir -p Files.GOOD
wait
cd /tmp/PSO2ENPatchCSV.GOOD/
find WC/Files -name "*.csv" -print0|sort -z|$PWDC/_tools/mp.sh -0 $PWDC/_py/GOOD.py|fgrep --invert-match -e "0FILE" |sort --numeric-sort --reverse | awk '{print $2"\t" $1}' | sed -e 's/\t/: /'|tee /tmp/PSO2ENPatchCSV.GOOD/GOOD.txt|grep -e '100.0%'|cut -f 1 -d :|xargs -n 1 -I {} find $PWDC -name '{}' -type f|xargs -I '{}' mv '{}' $PWDC/Files.GOOD
#	grep -v -e '000.0%' /tmp/PSO2ENPatchCSV.GOOD/GOOD.txt
