#!/bin/sh
find . -name "*.csv" -not -path "./.git/*" -print0|xargs -0 fgrep -e "$2" -l -Z|xargs -0 -r sed -i "s/\"$2\"/\"$1\"/g"