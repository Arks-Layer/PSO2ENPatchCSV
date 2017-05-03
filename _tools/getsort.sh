#!/bin/sh
rm -rf /tmp/PSO2ENPatchCSV.sort
if [ "$#" -ne 1 ]; then
	git archive --format=tar --prefix=PSO2ENPatchCSV.sort/ origin/EN | tar xf - -C /tmp
else
	git archive --format=tar --prefix=PSO2ENPatchCSV.sort/ $1 | tar xf - -C /tmp
fi
cd /tmp/PSO2ENPatchCSV.sort
find . -name "*.csv" -not -path "*/Files/*" -not -path "*/.git/*"|rev|sed 's/\//\t/'|rev|sed 's/\.\///g'|awk -F'\t' ' { t = $1; $1 = $2; $2 = t; printf("%s \"%s\"\n", $1, $2); } '
rm -rf /tmp/PSO2ENPatchCSV.sort
