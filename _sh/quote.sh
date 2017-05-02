#!/bin/sh
find . -name "*.csv" -not -path "*/.git/*" -print0|xargs -0 _py/quote.py&>/dev/null||find . -name "*.csv" -not -path "*/.git/*" -print0|xargs -0 -n 1 _py/quote.py
