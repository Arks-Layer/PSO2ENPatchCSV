#!/bin/sh
find . -name "*.csv" -not -path "./.git/*" -print0|xargs -0 fgrep -e "$1" -l -Z|xargs -0 -r sed -i "s/\"$1\"/\"$2\"/g"
