#!/bin/bash -x
echo "cmap" > $1.csv
ttx -o - -t cmap $1.ttf|fgrep -e '<!-- ' -e' -->'|cut -f 2 -d \"  > $1.csv
