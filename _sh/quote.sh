#!/bin/sh
find . -name "*.csv" -not -path "*/.git/*" -print0|xargs -P 0 -n 1024 -0 _py/quote.py&>/dev/null||find . -name "*.csv" -not -path "*/.git/*" -print0|xargs -P 0 -0 -n 1 _py/quote.py
