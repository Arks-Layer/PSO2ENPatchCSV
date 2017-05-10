#!/bin/bash -x
echo "cmap" > $1.csv
ttx -o - -t cmap $1.ttf|fgrep -e '<!-- ' -e' -->'|cut -f 2 -d \"|awk '{printf("%050s\t%s\n", toupper($0), $0)}'|LC_COLLATE=C sort -k1,1 | cut -f2  > $1.csv
