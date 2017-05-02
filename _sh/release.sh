#!/bin/sh
if [ -f release.sed ]; then
    find . -name "*.csv" -not -path "../Files/*" -not -path "*/.git/*" -print0|xargs -P 0 -n 1024 -0 sed -i'' -f release.sed
fi
