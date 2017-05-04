#!/bin/bash
rm -rf /tmp/PSO2ENPatchCSV.Fonts
rsync -a . /tmp/PSO2ENPatchCSV.Fonts --exclude ".git" --del
cd /tmp/PSO2ENPatchCSV.Fonts
./_sh/release.sh
find . -name "*.csv" -not -path "*/Files/*" -not -path "*/.git/*" -print0|./_tools/mp.sh -0 ./_py/Fonts.py
