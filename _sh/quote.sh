#!/bin/sh
find . -name "*.csv" -not -path "*/.git/*" -print0|_tools/mp.sh -0 _py/quote.py&>/dev/null||find . -name "*.csv" -not -path "*/.git/*" -print0|_tools/mp.sh -0 -n 1 _py/quote.py
