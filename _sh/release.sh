#!/bin/bash
if [ -f release.sed ]; then
    find . -name "*.csv" -not -path "../Files/*" -print0|xargs -0 sed -i'' -f release.sed
fi
