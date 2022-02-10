#!/bin/bash
set -euo pipefail
PWDC="$(pwd -P)"
rm -rf /tmp/PSO2ENPatchCSV.outputCSV
mkdir -p /tmp/PSO2ENPatchCSV.outputCSV
JP="upstream/JP"
EN="upstream/EN"
rsync --recursive --executability --whole-file . /tmp/PSO2ENPatchCSV.outputCSV/WC/ --exclude ".git" --del && cd /tmp/PSO2ENPatchCSV.outputCSV/WC/Files && find .. -name "*.csv" -not -path "../Files/*" -print0|$PWDC/_tools/mp.sh -0 ln -s {} . \; &
git archive --format=tar --prefix=PSO2ENPatchCSV.outputCSV/EN/ $EN | tar xf - -C /tmp && cd /tmp/PSO2ENPatchCSV.outputCSV/EN/Files && find .. -name "*.csv" -not -path "../Files/*" -print0|$PWDC/_tools/mp.sh -0 ln -s {} . \; &
git archive --format=tar --prefix=PSO2ENPatchCSV.outputCSV/JP/ $JP | tar xf - -C /tmp &
buildJP="$(git describe --always --tags $JP)"
buildEN="$(git describe --always --tags $EN)"
buildWC="$(git describe --always --tags)"
TagBranch="$(git describe --always --tags|cut -f 1 -d -|tr [A-Z] [a-z])"
echo '"FILE","ID","JP","EN","WC","JP<->EN","EN<->WC","JP<->WC"'
wait
cd /tmp/PSO2ENPatchCSV.outputCSV/
find JP -name "*.csv" -print0|sort -z|WC/_tools/mp.sh -0 WC/_py/outputCSV.py $TagBranch
exit $?
