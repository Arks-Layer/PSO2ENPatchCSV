#!/bin/sh
if [ -f release.sed ]; then
    find . -name "*.csv" -not -path "../Files/*" -not -path "*/.git/*" -print0|_tools/mp.sh -0 sed -i'' -f release.sed
fi
