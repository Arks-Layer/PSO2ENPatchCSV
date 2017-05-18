#!/bin/sh
rm -rf /tmp/PSO2ENPatchCSV.outputPO
git archive --format=tar --prefix=PSO2ENPatchCSV.outputPO/JP/ upstream/JP | tar xf - -C /tmp
git archive --format=tar --prefix=PSO2ENPatchCSV.outputPO/EN/ upstream/EN | tar xf - -C /tmp
rsync -a . /tmp/PSO2ENPatchCSV.outputPO/WC/ --exclude ".git" --del
build="$(git describe --always)"
cd /tmp/PSO2ENPatchCSV.outputPO/WC/Files
find .. -name "*.csv" -not -path "../Files/*" -exec ln -s {} . \;
cd /tmp/PSO2ENPatchCSV.outputPO/EN/Files
find .. -name "*.csv" -not -path "../Files/*" -exec ln -s {} . \;
cd /tmp/PSO2ENPatchCSV.outputPO/
echo "Content-Type: text/plain; charset=UTF-8"
find JP -name "*.csv" -print0|sort -z|WC/_tools/mp.sh -0 WC/_py/outputPO.py $build
